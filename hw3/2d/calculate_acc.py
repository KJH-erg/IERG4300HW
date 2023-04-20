lst = ['12_1','12_2','12_3','15_1','15_2','15_3','20_1','20_2',"20_3"]
# lst = ["12_1"]
for i in lst:
    # print './'+str(i)+'_fin'
    try:
        with open('./'+str(i)+'_fin',"r") as f:
            data = f.read().split('\n')[0:-1]
        total = 0
        correct = 0
        max_acc = []
        for j in data:
            s = j.split()
            correct += int(s[9])
            total += int(s[6])
            max_acc.append(float(s[12]))
        print(i)
        print(correct)
        print(total)
        print('average accuracy is '+ str(float(correct)/total))
    except:
        pass
        