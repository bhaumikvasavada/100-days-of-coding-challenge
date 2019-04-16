#program to find Armstrong number
num=int(input("Enter a number to check it an armstrong number or not: "))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num," is an armstrong number.")
else:
    print(num," is not an armstrong number.")