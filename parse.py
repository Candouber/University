import re
from lxml import etree

class Parser():

    def synopsis(self, con):             #获取简介信息
        pattern_t = r'class="t">(.*?)</span>'
        pattern_c = r'class="c">(.*?)</div>'
        k_list = re.findall(pattern_t, con, re.S)
        v_list = re.findall(pattern_c, con, re.S)
        synopsis_dict = dict(zip(k_list, v_list))
        return synopsis_dict

    def subject(self, con):              #获取专业信息
        pattern_k = r'<h3>(.*?)</h3>'
        pattern_v = r'<li><a.*?.html">(.*?)</a>'
        pattern_v2 = r'<li style="color.*?20px;">(.*?)</li>'
        # k_list = re.findall(pattern_k, con, re.S)
        v_list = re.findall(pattern_v, con, re.S)
        v2_list = re.findall(pattern_v2, con, re.S)
        v_list = v_list+v2_list
        # subject_dict = dict(zip(k_list, v_list))
        return v_list

    def tutition(self, con):#获取学费信息
        content = con
        data = []
        html = etree.HTML(content)
        Data = html.xpath('//*[@id="schoolPage"]/div[2]/div[1]/div[9]/text()')
        for d in Data:  #去除空格
            d = d.strip()
            data.append(d)
        return data