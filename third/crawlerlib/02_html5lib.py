# https://github.com/html5lib/html5lib-python
# pip install html5lib

from urllib.request import urlopen
import html5lib

with urlopen("http://example.com/") as f:
    document = html5lib.parse(f, transport_encoding=f.info().get_content_charset())