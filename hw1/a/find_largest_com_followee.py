with open ('medium_result.txt') as f:
    data = f.read()
tmp_dict={}
lines = data.split('\n')
for line in lines[0:-1]:
    try:
        data,count = line.split('},')
        count = count.strip()
        count = int(count)
        key,_ = (data.split(':'))
        best_pair,val = tmp_dict.get(key,(None,0))
        saved_count = val
        if count > saved_count:
            tmp_dict[key] = (line,count)
    except:

        print(line)
with open('a.txt',"w") as f:
    for k,v in tmp_dict.items():
        f.write(v[0]+'\n')


