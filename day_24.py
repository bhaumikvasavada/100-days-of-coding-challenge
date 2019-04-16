#program to convert celcius to farenhit

print("a. Celcius")
print("b. Farenhit")

choice=input("Enter your choice: ")
def temp(choice):
    return{

        'a':( float(input("Enter a temprature in celcius: "))*1.8)+32,
            
        'b':(float(input("Enter a temprature in farenhit: ")) - 32) / 1.8
            
}[choice]

print(temp(input('enter a or b: ')))
