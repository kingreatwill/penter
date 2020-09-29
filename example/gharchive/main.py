from crawler import Crawler
from logutils import get_logger
from dbmanager import DBManager, DBType

from model_converter import *

logger = get_logger(__name__)

def main():
    crawler = Crawler()
    db = DBManager(DBType.SQLITE, 'github.db')

    rate_limit = crawler.get_rate_limit()
    logger.info("Rate Limit: %s Remaining: %s", rate_limit.limit, rate_limit.remaining)
    # repos = crawler.fetch_repositories_with_stars_in_range(10000, 100000)
    # logger.info(repos)
    repos = crawler.fetch_repositories_with_stars_in_range(100000, 200000)
    logger.info(repos)

    # Test the DB
    for repo in repos:
        db_repo = convert_api_repo_to_db(repo)
        db.session.add(db_repo)

    db.session.commit()

if __name__ == "__main__":
    main()