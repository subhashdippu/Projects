numbers = [12, 55, 40, 23, 10, 67, 0, -5]
maximum = numbers[0]
for i in numbers[1:]:
    if i > maximum:
        maximum = i
print(maximum)


# Method 2

numbers = [12, 55, 40, 23, 10, 67, 0, -5]
maximum = max(numbers)
print(maximum)