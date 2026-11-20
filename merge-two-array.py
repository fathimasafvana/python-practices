#  Merge two arrays into a single sorted array

a = list(map(int, input("Enter a elements: ").split()))
b = list(map(int, input("Enter b elements: ").split()))
for i in b:
    a.append(i)

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)