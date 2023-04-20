with open ('../small/small_relation') as f:
    data = f.read()
p1=0
p2=0
k1= '699'
k2= '896'
lst1 = []
lst2 = []
for i in data.split('\n'):
    try:
        t1, t2 = i.split(' ')
        if t1 == k1 :
            print('wow')
        lst1.append(t1)
        if t2 == k2:
            lst2.append(t1)
    except:
        print('error')
        print(i)
# print(lst1)
print(lst2)
lst3 = [value for value in lst1 if value in lst2]
# print(len(set(lst3)))