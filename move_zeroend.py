number=[0,5,0,8,3,0,7]
result=[]
count=0
for i in number:
    if i == 0:
        count +=1
    else:
        result.append(i)
for i in range(count):
    result.append(0)
print(result)

    
        
    
