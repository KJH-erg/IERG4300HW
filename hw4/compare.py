import filecmp
lst = ['4','8','16','32','64']
import os
lst = os.listdir('./result_train')
for i in lst:
    print(filecmp.cmp('./result_train/'+i, 'result_train_2/'+i))