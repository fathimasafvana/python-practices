# Second Question: Reverse the last k elements of an array
list = [1, 2, 3, 4, 5, 6]
k = 3
# out=[1, 2, 3, 6, 5, 4]
a = list[:k]
b = list[k:][:: -1]
for i in b:
    a.append(i)
print(a)
  
   

  

