# num = int(input("Enter the no: "))
# factorial = 1
# i = 1
# while i <=num:
#     factorial *= i
#     i = i+1
# print(factorial)

number = int(input("Enter a number: "))
def fact(value):
    if value == 1:
        return 1
    else:
        return value * fact(value-1)
print(fact(number))