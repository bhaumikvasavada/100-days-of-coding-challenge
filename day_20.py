#Factorial of a given number.....
num = int(input("Enter a number to find its factorial: "))
factorial=1

if num < 0:
    print("SORRY..!! Factorial is not possible for the number less than 1")
elif num==0:
    print("factorial of 0 is 1 itself")
else:
    for i in range (1,num+1):
        factorial = factorial * i
        print("Factorial of ",num," is ",factorial)