with open ('tmp2.txt') as f:
    data = f.read()
tmp_dict = {}
for i in data.split('\n')[0:-1]:
    key = i.split(':')[0]
    lst = tmp_dict.get(key,[])
    if len(lst) !=3:
        lst.append(i)
    tmp_dict[key] = lst

with open("b_tt.txt",'w') as f:
    for k,v in tmp_dict.items():
        for i in v:
            f.write(i+'\n')