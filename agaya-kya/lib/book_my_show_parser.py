"""Parses the book my show website"""
try:
    import urllib.request
    import re
    from urllib.error import URLError, HTTPError
except ImportError as err:
    raise err


class parser:
    def __init__(self):
        self.name = "BookMyShow parser"
        self.url = "https://in.bookmyshow.com/"
        self.NOW_SHOWING = '{"event":"productClick","ecommerce":{"currencyCode":"INR","click":{"actionField":{"list":"Filter Impression:category\\\/now showing"},"products":\[{"name":"(.*?)","id":"(.*?)","category":"(.*?)","variant":"(.*?)","position":(.*?),"dimension13":"(.*?)"}\]}}}'
        self.COMING_SOON = '{"event":"productClick","ecommerce":{"currencyCode":"INR","click":{"actionField":{"list":"category\\\/coming soon"},"products":{"name":"(.*?)","id":"(.*?)","category":"(.*?)","variant":"(.*?)","position":(.*?),"dimension13":"(.*?)"}}}}'
        self.user_agent = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
            "Accept-Encoding": "none",
            "Accept-Language": "en-US,en;q=0.8",
            "Connection": "keep-alive",
        }

    def get_html(self, city_name):
        if city_name is None:
            return False
        else:
            try:
                request = urllib.request.Request(
                    self.url + city_name.lower() + "/movies",
                    headers={"User-Agent": "Magic Browser"},
                )
                read_html = urllib.request.urlopen(request).read()
                santitized_html = (read_html).decode("utf-8")
                return santitized_html
            except HTTPError as e:
                return "%s" % e
            except URLError as err:
                return "%s" % err

    def get_coming_soon(self, html):
        if html is None:
            return False
        else:
            return re.findall(self.COMING_SOON, html)

    def get_now_showing(self, html):
        if html is None:
            return False
        else:
            print(re.findall(self.NOW_SHOWING, html))
            return re.findall(self.NOW_SHOWING, html)
