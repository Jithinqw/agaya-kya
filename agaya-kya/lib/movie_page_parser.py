'''Main class for parsing movies pages from book my show'''

try:
    import re
    import urllib
    from urllib.error import URLError, HTTPError
    from book_my_show_parser import parser
except ImportError as err:
    raise err

class movie_parser():

    def __init__(self):
        self.name = 'movie parser'
        self.url  = 'https://in.bookmyshow.com/'
        self.user_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'
        }

    def santitizer(self, movie_name):
        if movie_name is None:
            return False
        else:
