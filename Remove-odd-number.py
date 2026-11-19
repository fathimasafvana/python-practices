# Remove elements that appear an odd number of times

arr = []

n = int(input("Enter length: "))

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

d = {}

for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

a = []

for i in d:
    if d[i] % 2 == 0:
        a.append(i)

print(a)
print(d)
