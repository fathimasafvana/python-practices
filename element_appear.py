numbers=[10,7,4,8,4,9,7,7,10,1,7,1]
count={}
max_count=0
for i in numbers:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i in count:
    if count[i] >1 :
        max_count +=1
print(max_count)
