"""print("Hello world!")
num1=input("Enter first number: ")
num2=input("Enter second number: ")
num1=int(num1)
num2=int(num2) 
sum=num1+num2
print("The sum of", num1, "and", num2, "is", sum)
"""

# Program from book
while True:
    line = input('> ')
    if line == 'done':
        break   
    print(line)
print('Done!')