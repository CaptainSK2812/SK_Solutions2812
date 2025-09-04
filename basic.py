# 1.Write a Python program to print "Hello, World!" to the screen.
print("Hello, World!")

# 2.Write a program that takes two numbers as input and prints their sum.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("The sum is:", num1 + num2)

# 3.Write a program to subtract the second number from the first number and display the result.
print("The difference is:", num1 - num2)

# 4.Write a Python program that multiplies two numbers entered by the user.
print("The product is:", num1 * num2)

# 5.Write a program to divide one number by another and print the quotient.
print("The quotient is:", num1 / num2)

# 6.Write a program to find the remainder when one number is divided by another.
print("The remainder is:", num1 % num2)

# 7.Write a Python program to swap the values of two variables.
a,b = num2, num1
print("After swapping:")
print("First number:", a)
print("Second number:", b)

# 8.Write a program to convert a distance in kilometers to miles.
kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * 0.621371
print("Distance in miles:", miles)

# 9.Write a Python program to convert temperature from Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)


# 10.Write a program that checks whether a given number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")