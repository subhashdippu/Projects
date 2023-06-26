number = int(input('Enter the number: '))
for i in range(1, number+1):
    if number%i == 0:
        print(i)
 
# ---------------------------------------
 
number = int(input('Enter the number: '))
factors = []
for i in range(1, number+1):
    if number%i == 0:
        factors.append(i)
print('The factors of the number', number, 'are:')
print(factors)