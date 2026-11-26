inp=[8,12,20,40]
# out=[8,28,40,80]

a=[]
count=0
for i in inp:
    count =+ i
    a.append(i)
print(a)
lis = [1, 2, 3, 4, 5, 6]
k = 3

result = []

for i in range(len(lis) - k):
    result.append(lis[i])

for i in range(len(lis) - 1, len(lis) - k - 1, -1):
    result.append(lis[i])

print(result)