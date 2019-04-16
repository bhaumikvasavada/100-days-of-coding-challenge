import random

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!.?,-()'
length = int(input("Enter the length of your password: "))
no_pass = int(input("Enter the number of passwords you want: "))
for p in range(no_pass):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    print(password)
