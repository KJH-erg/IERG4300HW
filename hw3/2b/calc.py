lst = ['1','2','seed1','seed2']
# lst = ["12_1"]
for i in lst:
    print './'+str(i)+'/'+str(i)+'_result2'
    try:
        with open('./'+str(i)+'/'+str(i)+'_result2',"r") as f:
            data = f.read().split('\n')[0:-1]
        print('ads')
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