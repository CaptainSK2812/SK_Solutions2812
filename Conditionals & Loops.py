# 1.Write a program that takes three numbers and prints the largest one.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>=b and a>=c:
    print(f"{a} is the largest number")
elif b>=a and b>=c:
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")



# 2.Write a Python program to check whether a given year is a leap year.
a=int(input("Enter a year: "))
if (a%4==0 and a%100!=0) or (a%400==0):
    print(f"{a} is a leap year")
else:
    print(f"{a} is not a leap year")


# 3.Write a program that checks whether a number is positive, negative, or zero.
a=int(input("Enter a number: "))
if a>0:
    print(f"{a} is a positive number")
elif a<0:
    print(f"{a} is a negative number")
else:
    print(f"{a} is zero")


# 4.Write a Python program to print numbers from 1 to 100 using a loop.
for i in range(1,100):
    print(i,end=" ")


# 5.Write a program to print all even numbers from 1 to 50.
for i in range(1,50):
    if i%2==0:
        print(i,end=" ")



# 6.Write a program that prints the multiplication table of a given number.
for i in range(1,4):
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}')


# 7.Write a Python program to calculate the factorial of a given number.
a=int(input("Enter a number: "))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(f"The factorial of {a} is {fact}")


# 8.Write a program that checks whether a given number is a prime number.
a=int(input("Enter a number: "))
is_prime=True
for i in range(2,a):
    if a%i==0:
        is_prime=False
        break
if is_prime:
    print(f"{a} is a prime number")
else:
    print(f"{a} is not a prime number")


# 9.Write a program to generate the Fibonacci sequence up to n terms.
n=int(input("Enter number of terms: "))
a,b=0,1
count=0
if n<=0:
    print("Please enter a positive integer")
elif n==1:
    print("Fibonacci sequence upto",n,":")
    print(a)
else:
    print("Fibonacci sequence:")
    while count<n:
        print(a,end=' ')
        c=a+b
        a=b
        b=c
        count+=1


# 10.Write a Python program to calculate the sum of all numbers in a given range.
n=int(input("value of n: "))
t=0
for i in range(1,n+1):
    t+=i
print(t)
