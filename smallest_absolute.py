# Question: Find two numbers that have the smallest absolute difference.
numbers = [4, 9, 6, 1]

numbers.sort()

min_diff = float('inf')

for i in range(len(numbers) - 1):
    diff = numbers[i + 1] - numbers[i]

    if diff < min_diff:
        min_diff = diff
        result = [numbers[i], numbers[i + 1]]

print(result)

