with open('result','r') as f:
    data = f.read().split('\n')
t= 0
c=0
for i in data[0:-1]:
    s=(i.split())
    print(s[6])
