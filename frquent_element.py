numbers = [10,7,4,8,9,4,7,7,10,1,7,1]
count={}
max_count=0
for i in numbers:
    if i in count:
        count[i]+=1
    else:
        count[i] = 1
    if count [i] > max_count:
        max_count=count[i]
        num=i
print(num)



    