#functions 
def avg():#function definition
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    average = (num1 + num2) / 2
    print(average)
avg() #function call
print("this is the end of functions.py")


#built-in functions
print(abs(-7.25))  # Absolute value
print(pow(3, 4))   # Power function
print(max(5, 10))  # Maximum value
print(min(5, 10))  # Minimum value
print(round(7.65)) # Rounding off
print(round(7.45)) # Rounding off
print(len("Hello, World!"))  # Length of string
print(len([1, 2, 3, 4, 5]))   # Length of list
print(type(42))            # Type of integer
print(type(3.14))          # Type of float


#function with arguments
def greet(name): #function definition with parameter
    print(f"Hello, {name}!")
greet("sahana")