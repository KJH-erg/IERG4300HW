with open ('train_img','r') as f:
    img = f.read().split('\n')[0:-1]
with open ('train_label','r') as f:
    label = f.read().split('\n')[0:-1]
with open('train_combined','w') as f:
    for i,j in zip(img,label):
        f.write(i+','+j+'\n')