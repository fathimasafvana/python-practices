numbers=[5,8,3,9,2,10]
smallest = numbers[0]
largest = numbers[0]
for nums in numbers:
    if nums < smallest:
        smallest = nums
    elif nums > largest:
        largest = nums
difference=largest - smallest
print(difference)


