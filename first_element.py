number=[1,7,8,5,7,8,3,2,5,7]
for i in range(len(number)):
   if number[i] in number[i+1:]:
      print (number[i])
      break
