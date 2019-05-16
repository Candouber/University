# -*- coding: utf-8 -*-

from handler import Handler
import json

handler = Handler()



name_list = handler.name_list
subject = handler.get_subject()
synopsis = handler.get_synopsis()
tutition = handler.get_tutition()

def get_data(name_list):
    for i in name_list:
        #data = json.dumps({'学校名称':i,'专业':subject.__next__(),'基本资料': synopsis.__next__(),'学费信息': tutition.__next__()}, ensure_ascii=False,separators=(',',':'), indent=4)
        data = []
        d = {'学校名称':i}
        data.append(d)
        d = {'专业':subject.__next__()}
        data.append(d)
        d = {'基本资料':synopsis.__next__()}
        data.append(d)
        d = {'学费信息':tutition.__next__()}
        data.append(d)
        yield data

complete_data = get_data(name_list)
Data = []
# for i in range(len(name_list)-1):
#     Data.append(json.dumps(complete_data.__next__(), ensure_ascii=False, indent=4))
#
# with open('complete_data.json', 'w') as f:
#     f.write(Data)


f =open('complete_data.json', 'a')
f.write('[')
for i in range(len(name_list)-1):
    f.write(json.dumps(complete_data.__next__(), ensure_ascii=False, indent=4))
    f.write(',')
f.write(']')
f.close()


