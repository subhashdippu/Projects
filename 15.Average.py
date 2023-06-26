def get_average(numbers):
    summation = 0
    for i in numbers:
        summation += i
    average = summation/len(numbers)
    return average
 
ages = [12, 33, 50, 23, 40, 14]
avg = get_average(ages)
print(avg)

# Method 2

def get_average(numbers):
    summation = sum(numbers)
    average = summation/len(numbers)
    return average
 
ages = [1, 2, 3, 4]
avg = get_average(ages)
print(avg)