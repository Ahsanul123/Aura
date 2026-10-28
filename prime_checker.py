number = int(input("Enter a number: "))

if number < 2:
    print("Not prime")
else:
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            print("Not prime")
            break
    else:
        print("Prime")
