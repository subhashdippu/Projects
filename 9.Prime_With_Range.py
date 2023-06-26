for num in range(2000, 2500):
    for i in range(2, num):
        if num%i == 0:
            print("This is not prime", num)
    else:
        print("This is Prime", num)