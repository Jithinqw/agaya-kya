'''Main class for parsing movies pages from book my show'''

try:
    import re
    import urllib.request
    from urllib.error import URLError, HTTPError
    from book_my_show_parser import parser
except ImportError as err:
    raise err

class movie_parser():

    def __init__(self):
        self.name = 'movie page parser'
        self.url  = 'https://in.bookmyshow.com/'
        self.city_name = None
        self.user_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'
        }

    def santitizer(self, city_name, movie_name):
        if movie_name and movie_name is None:
            return False
        else:
            self.city_name = city_name
            api_name = movie_name.lower().replace(' ', '-')
            demo = parser()
            demo1 = demo.get_now_showing(demo.get_html(city_name))
            for movie in demo1:
                if (movie[0].lower()).__contains__(api_name):
                    return movie
    
    def get_movie_html(self, movie_spec):
        if movie_spec is None:
            return False
        else:
            try:
                request = urllib.request.Request(self.url+self.city_name.lower()+'/movies/'+movie_spec[0].lower()+'/'+movie_spec[1]+'/')
                read_html = urllib.request.urlopen(request).read()
                santitized_html = (read_html).decode('utf-8')
                file = open('test.txt','w')
                file.write(santitized_html)
                return santitized_html
            except Exception as err:
                return "%s"%err

snake = movie_parser()
print(snake.get_movie_html(snake.santitizer('trivandrum', 'june')))