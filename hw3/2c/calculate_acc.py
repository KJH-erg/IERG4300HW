
with open('./result2',"r") as f:
    data = f.read().split('\n')[0:-1]
total = 0
correct = 0
max_acc = []
for j in data:
    s = j.split()
    # print(s[3])
    # print(s[6])
    # print(s[12])
    correct += int(s[9])
    total += int(s[6])
    max_acc.append(float(s[12]))
    print(s[2]+s[3]+' '+ s[6]+' '+s[9]+ ' '+s[12])
print(correct)
print(total)
print('average accuracy is '+ str(float(correct)/total))
    