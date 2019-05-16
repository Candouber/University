import requests
import re
import json


class University():

    def html(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
        name_url = 'http://www.gaokaopai.com/daxue-0-0-0-1-0-0-0--p-'
        name_url_list = [name_url+str(i)+'.html' for i in range(1,162)]
        for url in name_url_list:
            res = requests.get(url, headers = headers)
            con = res.content.decode('utf8')
            yield con

    def parse(self, content):
        pattern_url_name = r'<h3><a.*?="(.*?)</a>'
        url_and_name = re.findall(pattern_url_name, content)
        return url_and_name

    def Item(self, Data):
        list = []
        for i in Data:
            Data = i.split('">')
            list.append(Data)
        d = {
            name:url for url, name in list
        }
        return d

    def save(self, data):
        with open('url_and_name2.json', 'a') as f:
            f.write(data)
            f.write('\n')

    def excute(self):           #将大学名和地址写到文件中
        data = []
        content = self.html()
        for i in content:
            data.append(self.parse(i))
        self.save(self.Item(data))
        print('done')


# json_list = []
# Uni = University()
# content = Uni.html()
# for i in content:
#     data = Uni.parse(i)
#     json_list.append(Uni.Item(data))
#     s = json.dumps(json_list, ensure_ascii=False, indent=4)
# Uni.save(s)
# print('done')


