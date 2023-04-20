#[0:-1] for neglecting the last empty line
for n in [4,8,16,32,64]:
    with open ('result_train/train_'+str(n),'r') as f:
        img = f.read().split('\n')[0:-1]
    with open ('result_train/train_label','r') as f:
        label = f.read().split('\n')[0:-1]
    with open('result_train/train_combined_'+str(n),'w') as f:
        for i,j in zip(img,label):
            f.write(i+','+j+'\n')
    with open ('result_train/test_'+str(n),'r') as f:
        img = f.read().split('\n')[0:-1]
    with open ('result_train/test_label','r') as f:
        label = f.read().split('\n')[0:-1]
    with open('result_train/test_combined_'+str(n),'w') as f:
        for i,j in zip(img,label):
            f.write(i+','+j+'\n')