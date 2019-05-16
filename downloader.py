import requests
import json
from parse import Parser
from University_name import University

class Downloader():
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
        self.Uni = University()

    def get_page(self, url):
        res = requests.get(url, headers = self.headers)
        content = res.content.decode('utf8')
        return content

    def get_name_url(self):
        with open('url_and_name2.json') as f:
            data = json.load(f)
        return data

    def get_name(self, data:list):
        l=[]
        name_list = []
        for i in data:
            name = i.keys()
            l.append(name)
        for i in l:
            for a in i:
                name_list.append(a)
        return name_list

    def get_url(self, data:list):
        l=[]
        url_list = []
        for i in data:
            url = i.values()
            l.append(url)
        for i in l:
            for a in i:
                url_list.append(a)
        return url_list

    def get_url_subject(self, url_list:list):
        other_url_list= []
        for url in url_list:
            other_url = url.replace('jianjie', 'zhuanye')
            other_url_list.append(other_url)
        return other_url_list

