for i in range(1, 5):  # First Way
    for j in range(1, 5):
        if j<=i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# for i in range(1, 6): # Second Way
#     print('*' * i)

# i = 1
# while i<=5:
#     print('*' * i)
#     i += 1


          # Mirror right tringle
# for i in range(1, 6):
#     print(' '*(5-i) + '*'*i)

# i = 1
# while i<=5:
#     print(' '*(5-i) + '*'*i)
#     i += 1