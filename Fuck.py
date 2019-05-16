import requests
import json
import re
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
sysnopsis_list = []
tutitioin_list = []
subject_list = []


#下载器
def down_page(url):
    res = requests.get(url, headers=headers)
    content = res.content.decode('utf8')
    return content


def down_name_url():
    with open('url_and_name2.json') as f:
        data = json.load(f)
    return data


def down_name(data: list):
    l = []
    name_list = []
    for i in data:
        name = i.keys()
        l.append(name)
    for i in l:
        for a in i:
            name_list.append(a)
    return name_list


def down_url(data: list):
    l = []
    url_list = []
    for i in data:
        url = i.values()
        l.append(url)
    for i in l:
        for a in i:
            url_list.append(a)
    return url_list


def down_url_subject(url_list: list):
    other_url_list = []
    for url in url_list:
        other_url = url.replace('jianjie', 'zhuanye')
        other_url_list.append(other_url)
    return other_url_list


#解析器

def synopsis(con):             #获取简介信息
    pattern_t = r'class="t">(.*?)</span>'
    pattern_c = r'class="c">(.*?)</div>'
    k_list = re.findall(pattern_t, con, re.S)
    v_list = re.findall(pattern_c, con, re.S)
    synopsis_dict = dict(zip(k_list, v_list))
    return synopsis_dict

def subject(con):              #获取专业信息
    pattern_k = r'<h3>(.*?)</h3>'
    pattern_v = r'<li><a.*?.html">(.*?)</a>'
    pattern_v2 = r'<li style="color.*?20px;">(.*?)</li>'
    k_list = re.findall(pattern_k, con, re.S)
    v_list = re.findall(pattern_v, con, re.S)
    v2_list = re.findall(pattern_v2, con, re.S)
    v_list = v_list+v2_list
    subject_dict = dict(zip(k_list, v_list))
    return subject_dict

def tutition(con):
    content = con
    html = etree.HTML(content)
    data = html.xpath('//*[@id="schoolPage"]/div[2]/div[1]/div[9]/text()')
    return data

#处理器--获取页面的生成器
def get_page():
    for url in url_list:
        content = down_page(url)
        yield content

def get_sub_page():
    for url in other_url_list:
        try:
            content = down_page(url)
        finally:
            yield content


#处理器--获取数据

def get_synopsis():
    content = get_page()
    for con in content:
        #sysnopsis_list.append(synopsis(con))
        yield synopsis(con)

def get_subject():
    content = get_sub_page()
    for con in content:
        #subject_list.append(subject(con))
        yield subject(con)

def get_tutition():
    content = get_page()
    for con in content:
        #tutitioin_list.append(tutition(con))
        yield tutition(con)

# if __name__ == '__main__':
#     #各个必要数据初始化
#     data = down_name_url()
#     name_list = down_name(data)
#     url_list = down_url(data)
#     other_url_list = down_url_subject(url_list)
#
#
#     print(get_subject())
#     print(get_tutition())
#     print(get_synopsis())

data = down_name_url()
name_list = down_name(data)
url_list = down_url(data)
other_url_list = down_url_subject(url_list)

s = get_synopsis()
t = get_tutition()
sub = get_subject()

for i in range(10):
    print(s.__next__())
    print(t.__next__())
    print(sub.__next__())



