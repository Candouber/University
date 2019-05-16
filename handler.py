
from downloader import Downloader
from parse import Parser


data = Downloader().get_name_url()


url_list = Downloader().get_url(data)
other_url_list = Downloader().get_url_subject(url_list)

sysnopsis_list = []
tutitioin_list = []
subject_list = []

class Handler():

    def __init__(self):
        self.name_list = Downloader().get_name(data)

    def get_page(self):
        for url in url_list:
            content = Downloader().get_page(url)
            yield content

    def get_sub_page(self):
        for url in other_url_list:
            content = Downloader().get_page(url)
            yield content

    def get_synopsis(self):
        content = self.get_page()
        for con in content:
            yield (Parser().synopsis(con))


    def get_subject(self):
        content = self.get_sub_page()
        for con in content:
            yield (Parser().subject(con))


    def get_tutition(self):
        content = self.get_page()
        for con in content:
            yield (Parser().tutition(con))






handler = Handler()


