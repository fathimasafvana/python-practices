s =int (input("Enter a length:"))
d={}
for i in range(s):
    k=input("Enter the key:")
    v=input("Enter the value:")
    d.update({k:v})
print(d)