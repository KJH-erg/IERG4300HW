import re

with open ('fin.txt') as f:
    data = f.read()
tmp_dict = {}
for i in data.split('\n')[0:-1]:
    key = i.split(':')[0]
    lst = tmp_dict.get(key,[])
    print(i)
    val = (i.split("},")[1].strip())
    print(val)
    val = float(val)
    t = {}
    t["line"] = i
    t["val"] = val
    lst.append(t)
    tmp_dict[key] = lst

with open("e_fin2.txt",'w') as f:
    for k,v in tmp_dict.items():
        fin = sorted(v, key=lambda x: x['val'], reverse=True)[0:3]
        for i in fin:
            f.write(i['line']+'\n')