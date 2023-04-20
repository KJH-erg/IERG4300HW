with open ('medium_result') as f:
    data = f.read()
lst2 = []
for i in data.split('\n'):
    tmp = i.split(':')[0]
    lst2.append(tmp)

print(len(set(lst2)))
del lst2
with open ('../medium/medium_relation') as f:
    data = f.read()
lst1 = []
for i in data.split('\n')[0:-1]:
    lst1.append(i.split(' ')[1])
print(len(set(lst1)))
print(set(lst2)-set(lst1))