import re
p = re.compile(".*6482$")
with open ('sim_score.txt') as f:
    data = f.read()
lst2 = []
for i in data.split('\n'):
    tmp = i.split(':')[0]
    if re.search(p,tmp):
        lst2.append(i)
            
with open("b_fin.txt",'w') as f:
    for i in lst2:
        f.write(i+'\n')
