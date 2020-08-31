import requests
from bs4 import BeautifulSoup
import os
import fleep

from magic import magic


def down(name, tag):
    a = tag.select('a')
    if a:
        url = a[0].get('href')
        down_res = requests.get(url=url)
        mime = magic.from_buffer(down_res.content[0:2048], mime=True)
        # for element in fleep.data:
        #     if element['mime'] == mime:
        #         print('{} - {}'.format(mime, element['extension']))
        #         break
        extension = 'mp3'
        if mime == 'audio/ogg':
            extension = 'oga'
        with open('{}.{}'.format(name, extension), 'wb') as f:
            f.write(down_res.content)


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    url = 'https://github.com/shimohq/chinese-programmer-wrong-pronunciation/blob/master/README.md'
    resp = requests.get(url=url, headers=headers)

    if resp.ok:
        soup = BeautifulSoup(resp.text, 'html.parser')
        readme = soup.select('#readme')[0]
        need_table = readme.select('table')[0]
        rows = need_table.select('tr')
        for r in rows[1:]:
            columns = r.select('td')
            down(os.path.join(r'C:\Users\Administrator\Desktop\发音\英音', columns[0].text), columns[1])
            down(os.path.join(r'C:\Users\Administrator\Desktop\发音\美音', columns[0].text), columns[2])


if __name__ == '__main__':
    main()
