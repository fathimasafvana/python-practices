s=input("Enter a string:")
k=input("Enter the  letter:")
index=[]
for i in range(len(s)):
    if k in s[i]:
        index=i
print(index)


