print('1-100之间的全部质数')
count=0
for i in range(1,101):
    for s in range(2,i):
        if i%s == 0:break
        if i==s+1:
            print(i)


        
        
    
