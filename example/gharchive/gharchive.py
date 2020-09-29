# File for querying GH Archive
import argparse
import pandas as pd
from pandas.io.json import json_normalize
import logging
import coloredlogs
import requests
import datetime
import os
import glob
import gzip
import shutil
import sqlite3
import multiprocessing as mp
import time

conn = sqlite3.connect('github.db')
TABLE_NAME = 'github'
TMP_DIR = "tmp"

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

BASE_URL = "http://data.gharchive.org/%s-%d.json.gz"


def format_dataframe(df):
    # Normalize the columns
    actor = json_normalize(df.actor.tolist()).add_prefix('actor.')
    org = json_normalize(df.org.fillna(-1).apply(lambda x: {}
                                                 if x == -1 else x).tolist()).add_prefix('org.')
    payload = json_normalize(df.payload.tolist()).add_prefix('payload.')
    repo = json_normalize(df.repo.tolist()).add_prefix('repo.')

    df = pd.concat([df.drop(['actor', 'org', 'repo'], axis=1),
                    actor,
                    org,
                    repo], axis=1)

    for column in df.columns:
        df[column] = df[column].astype('str')

    return df


def load_data(filename):
    logger.info("Loading File: %s" % filename)
    df = pd.read_json(filename, lines=True)
    return format_dataframe(df)


def download_file(url, dir):
    local_filename = dir + "/" + url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
        f.close()

    return local_filename


def file_download(url):
    logger.info("Download URL: %s" % url)
    gz_file = download_file(url, TMP_DIR)
    try:
        with gzip.open(gz_file) as gz:
            json_str = gzip.decompress(gz.read()).decode('utf-8')
    except OSError:
        with gzip.open(gz_file) as gz:    # Try opening the file as a regular file
            json_str = gz.read().decode('utf-8')

    df = pd.read_json(json_str, lines=True)
    df = format_dataframe(df)
    os.remove(gz_file)
    return df

def load_files_for_date_range(start_date, end_date, use_mt, num_threads):
    if os.path.exists(TMP_DIR):
        files = glob.glob(TMP_DIR + "/*")
        for f in files:
            os.remove(f)
        os.rmdir(TMP_DIR)
    os.mkdir(TMP_DIR)

    date = start_date
    while date <= end_date:
        suffix = date.strftime("%Y-%m-%d")
        logger.info("Downloading files for date: %s" % suffix)
        if use_mt:
            with mp.Pool(num_threads) as p:
                logger.info("Parallelized Download")
                dfs = p.map(file_download, [
                            (BASE_URL % (suffix, hour)) for hour in range(0, 24)])
                p.close()
                p.join()
        else:
            logger.info("Single Threaded Download")
            dfs = [file_download((BASE_URL % (suffix, hour))) for hour in range(0, 24)]

        # Merge all the df's
        logger.info("Merging Dataframes")
        joined_df = pd.concat(dfs)
        logger.info("Writing to SQL")
        joined_df.to_sql(TABLE_NAME, conn, if_exists='append')

        date = date + datetime.timedelta(days=1)
        logger.info("Sleeping for 1 second")
        time.sleep(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-filename", help="Filename to load")
    parser.add_argument("-start_date", help="Start Date")
    parser.add_argument("-end_date", help="End Date")
    parser.add_argument("-use_mt", help="Use multithreading", default=False)
    parser.add_argument("-num_threads", help="Number of threads to launch", default=4)
    args = parser.parse_args()

    if (args.filename):
        logger.info("Loading Single File")
        load_data(args.filename)
    else:
        if args.start_date is None:
            logger.error("Start Date not specified")
            return

        start_date = pd.to_datetime(args.start_date)
        end_date = args.end_date
        if end_date is None:
            end_date = pd.to_datetime(datetime.date.today())
        else:
            end_date = pd.to_datetime(end_date)

        load_files_for_date_range(start_date, end_date, args.use_mt, args.num_threads)


if __name__ == "__main__":
    main()
