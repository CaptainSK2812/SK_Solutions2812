# def alphabet_sum(text):
#     total_sum = 0
#     for char in text:
#         if char.isalpha():  
#             char_lower = char.lower()
#             value = ord(char_lower) - ord('a') + 1 
#             total_sum += value
#     return total_sum
# input_string = input("Enter a string: ")
# result = alphabet_sum(input_string)
# print(f"The sum of alphabet values in '{input_string}' is: {result}")

# A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26
# total_sum=0
# aa=str(input("Enter your name: "))
# bb=list(aa)
# print(bb.reverse(True))
# def fac(user):
#     if user == 0 or user==1:
#         return 1
#     else:
#         return user*fac(user-1)
# print(fac(user =int(input("enter number:"))))
# s = [1, 12, 3, 4, 5, 6]
# s.sort()
# print(s)

# def daya(old_balance="0",new_balance="0"):
#         old_balance=int(input("old_balance: "))
#         new_balance=int(input("new_balance: "))
#         print(old_balance+new_balance ) 
# daya()
# total_sum=0
# for i in range(1,11):
#     print(total_sum)
#     total_sum+=i
        
# class human:
#     def __init__(self,name,age=0):
#         self.name=name
#         self.age=age

#     def walk(self):
#         print(f"{self.name} is walkig")
# c=human("sujan")
# d=human("amruth")
# d.walk()
# human.walk(d)

# class college:
#     def __init__(self,name=0,id=0):
#         self.name=name
#         self.id=id
#     def students(self):
#         print(f"hi, i am {self.name} my roll number is {self.id}")
# s=college("sujan",41)
# college.students(s)

# class calculator:
#     def __init__(self,number1="error",number2="error"):
#         self.number=number1+number2
#         print(self.number)
# a=calculator(input("values: "),input("valuess: "))

# for i in range(1,20):
#     for j in range(1,11):
#         print(f"{i}x{j}={i*j}")

# class Database:
#     def __init__(self):
#         self.storage={}
#     def write(self,key,value):
#         self.storage[key]=value
#     def read(self,key):
#         if key in self.storage:
#             print(self.storage[key])
#         else:
#          print("DB item not available")
# db=Database()
# db.write("sub","100k")
# db.read("sub")

# class calculator:
#     def add(a=0,b=0):
#         print(a+b)
#     def sub(a=0,b=0):
#         print(a-b)
#     def mul(a=0,b=0):
#         print(a*b)
#     def div(a=0,b=0):
#         print(a/b)
# a=input("value a: ") 
# b=input("value b: ")
# calculator.add(a,b)

# class user:
#     def __init__(self,username,password):
#         self.username=username
#         self.password=password
# u=user("sujan",123)
# print(u.username)

# def inputt(a=0,b=0):
#     a=input("va")
#     b=input("va")
# inputt()

# class Animal:
#     def make_sound(self,a):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Bark")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow")

# animals = [Dog(), Cat()]
# for animal in animals:
#     animal.make_sound()



# class ATM:
#     def __init__(self, balance):
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"Deposited {amount}. New balance: {self.__balance}")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.__balance}")
#         else:
#             print("Insufficient balance")
# atm = ATM(1000)
# atm.deposit(500)
# atm.withdraw(300)
# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password  # Private attribute
#     def get_username(self):
#         return self.username
#     def check_password(self, password):
#         return password == self.__password
# user = User("dev_karnataka", "pass1234")
# print(user.get_username())  # Access allowed
# print(user.check_password("wrong_pass"))  # Returns False
# print(user.check_password("pass1234"))  # Returns True



# class Car:
#     def start_engine(self):
#         print("Engine started")
#     def accelerate(self):
#         print("Car accelerating")
#     def brake(self):
#         print("Car stopping")



# car = Car()
# car.start_engine()  # Abstracts complex internal workings
# car.accelerate()
# car.brake()3



# class calculator:
#     def __init__(self,a=0,b=0):
#         a=input("value: ")
#         self.a=a
#         b=input("value: ")
#         self.b=b
#         print(f"{self.a+self.b}")
# calculator()



# def add(x,y):
#     return x+y
# def subtract(x,y):
#     return x - y
# def multiply(x,y):
#     return x*y
# def divide(x,y):
#     return x/y
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
# while True:
#     choice=input("Enter the your choice: ")
#     if choice in ('1','2','3','4'):
#         try:
#             a=float(input("Enter the value of a: "))
#             b=float(input("Enter the value of b: "))
#         except ValueError:
#             print("please enter valid numbers...!")
#             continue
#         if choice=='1':
#             print(a,'+',b,'=',sum(a,b))
#         elif choice=='2':
#             print(a,'-',b,'=',subtract(a,b))
#         elif choice=='3':
#             print(a,'*',b,'=',multiply(a,b))
#         elif choice=='4':
#             print(a,'/',b,'=',divide(a,b))
#         next_cal=input("if you want to continue your calculation.(yes/no):  ").lower()
#         if next_cal=='no':
#             break
#         else:
#             print(choice=input("Enter the your choice: "))



# class friends:
#     def friend(self):
#         print(f"you are friend is {self}")
# class sujan(friends):
#     def friend(self):
#         print(f"{friends}you are friend is {self}")
# class daya(sujan):
#     def friend(self):
#         print(f"you are friend is {self}")
# class ayush(daya):
#     def friend(self):
#         print(f"you are friend is {self}")
# A=friends.friend("ayush")
# B=ayush.friend("Poorna")



# def ayush(a):
#     return "Your friend is sujan and daya"
# def daya(a):
#     return "your friend is ayush"
# def sujan(a):
#     return "You are my friend"
# print("1.ayush")
# print("2.daya")
# print("3.sujan")
# while True:
#     a=input("enter your choice: ")
#     if a=='1':
#         print(ayush(a))
#     elif a=='2':
#         print(daya(a))
#     elif a=='3':
#         print(sujan(a))
#     else:
#         break



# class MathOperations:
#     def add(self, a, b, c=0):
#         print(a + b + c)  
# math = MathOperations()
# math.add(5, 10)  
# math.add(5, 10, 15)



# class calculator:
#     def add(self,a,b,c=0):
#         print(a+b+c)
# c=calculator()
# c.add(2,4,5)



# class calculator:
#     def add(self,a=0,b=0):
#         self.a=a
#         self.b=b
#         return a+b
# c=calculator()
# print(c.add(a=input("vale:"),b=input("vale:")))



# def sujan():
#     print("i love you kusuma")
# def kusuma():
#     print("i love you sujan")
# def suku():
#     print("both are in love")
# choice=str(input("Name: "))
# while True:
#      if choice in ('sujan','kusuma','suku'):
#             if choice=='sujan':
#                 sujan()
#             elif choice=='kusuma':
#                 kusuma()
#             elif choice=='suku':
#                 suku()
#             else :
#                 print("not valid")
#                 break



# def leap_year(year):
#     year=int(input("enter the year: "))
#     if (year%4==0 and year%100!=0)or(year%400==0):
#         return True
#     else:
#         return False
# print(leap_year(year=""))



# class Account:
#     def __init__(self,id,holder_name):
#         self.id=id
#         self.holder_name=holder_name
#         self._balance=0  

#     def check_balance(self):
#         print(f'Balnce: {self._balance}')

#     def deposit(self, amount):
#         self._balance+=amount
#         print(f"Deposit successful. Updated Balance: {self._balance}")

#     def withdraw(self,amount):
#         if self._balance>=amount:
#             self._balance-=amount
#             print(f"Deposit successful. Updated Balance: {self._balance}")
#         else:
#             print("not enough")

# class savingsAccount(Account):
#     def calculate_interest(self):
#         interest_rate=0.04
#         interest=self._balance*interest_rate
#         print(f"interest rate: {interest}")


# class currentAccount(Account):
#     def withdraw(self, amount):
#         overlimit=1000
#         if self._balance+overlimit>=amount:
#             self._balance-=amount
#             print(f"Deposit successful. Updated Balance: {self._balance}")
#         else:
#             print("limit over")

# class bank:
#     def __init__(self,name,city):
#         self.name=name
#         self.city=city
#         self.__accounts={}
#     def create_account(self,id,holder_name,type):
#         if type=='savings':
#             new_account=savingsAccount(id,holder_name)
#         elif type=='current':
#             new_account=currentAccount(id,holder_name)
#         self.__accounts[id]=new_account
#         print("Account creation succesful")
#         return new_account
#     def get_account(self,id):
#         if id not in self.__accounts:
#             print("account not found")
#             return None
#         else:
#             account=self.__accounts[id]
#             print(f"\n ID {account.id}\n holder name: {account.holder_name}")
#             return account
    
# svl=bank("karnataka bank","sullia")
# a1=svl.create_account("1","sujan","savings")
# a2=svl.create_account("2","kushi","current")
# a1.deposit(1000)
# a2.deposit(10)
# a1.withdraw(2000)
# a2.withdraw(20)
# a1.calculate_interest()


# class Student:
#     def __init__(self,name,rollnumber):
#         self.name=name
#         self.rollnumber=rollnumber
#         self.__marks={}
#     def get_marks(self):
#         return self.__marks
#     def add_marks(self,subjects,marks):
#         self.__marks[subjects]=marks
#     def calculateaverage(self):
#         total=0
#         for  mark in self.__marks.values():
#             total=0
#         average=total/len(self.__marks)
#         return average
#     def is_passed(self):
#         has_passed=all(mark<35 for mark in self.__marks.values())
#         if has_passed:
#             print("{self.name} has passed")
#         else:
#             print("{self.name} has passed")
#     def calculategrade(self):
#         print("Grade: ",end="")
#         per=self.calculateaverage*100
#         if per>=90:
#             print("A")
#         elif per>=85:
#             print("B")
#         else:
#             print("C")

# class Reportcard:
#     @staticmethod
#     def generate(student: Student):
#         student_marks=student.get_marks()
#         print(f"Name: {student.name}\t Roll no. {student.rollnumber}")
#         print("------marks-----")
#         for subject, marks in student_marks.items():
#             print(f"{subject}-{marks}")
#         print("-----------")
#         print(f"average:{student.calculateaverage}")
#         student.is_passed
#         student.calculategrade

# a=Student("sujan",1)
# a.add_marks("maths",95)
# a.add_marks("science",35)
# Reportcard.generate(a)



# a=input("enter your name: ")
# s=0
# while s<=35:
#     print(a)
#     s+=1


# def sum_all(*numbers):
#     total = 0
#     for num in numbers:  # 'numbers' is a tuple here
#         total += num
#     return total

# print(sum_all(1, 2, 3, 4,34,5,6,7,7))  # Output: 10
# print(sum_all(10, 20))       # Output: 30



# x=0
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()



# x=0
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# x=5
# for i in range(x,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# x=5
# for i in range(x,0,-1):
#     for j in range(i):
#         print(j+1,end=" ")
#     print()
 

# x=5
# for i in range(x,0,-1):
#     for j in range(1,i+1):
#         for k in range(j-1):
#             print("*",end=" ")
# print()



# for i in range(1,6):
#     for j in range(1,6):
#         print(" ",end="")
#     for k in range(0,i):
#         print('*',end=" ")
#     for m in range(i,0,-1):
#         print("*",end=" ")
#     print()


# a=int(input("a : "))
# b=int(input("b : "))

# try:
#     print(a/b)
# except Exception as e:
#     print(f"not possible: {e}")
# finally:
#     print(" program error")

# try:
#     boy=input("your lover name: ")
#     if boy.lower()!="ayush" or boy.lower()!="kruthi":
#         raise Exception("you can enter ayush or kruthi only")
# except Exception as e:
#     print(f"error:{e}")
# if boy=="kruthi":
#     print(f"{boy} is ready to marry ayush")
# elif boy=="ayush":
#     print(f"{boy} is ready to marry kruthi ")
# else:
#     print("you can enter ayush or kruthi only")



# class friends: 
#     def __init__(self, name=0, id=0):
#         self.name = name
#         self.id = id
#     def sujan(self):
#         print(f"sujan:{self.name}")
# u = friends("sujan", "8") 
# print(f"Name: {u.name}, ID: {u.id}")



# a="i love you moti"
# x=0
# while x<=10:
#     print(a)
#     x+=1


# numdiff={}
# target=input("target; ")
# for i,num in enumerate(nums):
#     c=target+num
#     if c in numdiff:
#         return [numdiff[c],i]
#     numdiff[num]=i
# return []



# import wikipedia
# print(wikipedia.summary("Virat Kohli"))



# import qrcode
# img = qrcode.make("engineering in kannada")
# img.save("karnataka.png")

# import qrcode
# img=qrcode.make("I love you kusuma")
# img.save("kusuma.png")

# list=[1,2,34,5]
# a=sorted(list)
# print(a[-2])


# num=list(input("enter the numbers: ").split())
# print(num)


# Write a Python program to print "Hello, World!"
# print("hello, world!")


# Write a program to add two numbers and print the result.
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# print(a+b)


# Take name input from the user and greet them.
# name=str(input("enter your name: "))
# print(f"i love you {name}")


# Write a program to calculate the square of a number.
# c=int(input("enter number: "))
# print(c*c)
# for i in range(1,11):
#     print(i*i)


# Write a program to check if a number is even or odd.
# d=int(input("enter number: "))
# if d%2==0:
#     print(f"{d} is even number")
# else:
#     print(f"{d} is odd number")


# Write a program to find the largest of two numbers.
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# if a>b:
#     print(a)
# else:
#     print(b)


# Write a program to swap two variables.
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# a,b=b,a
# print(a,b)


# Write a program to get the length of a string.
# a=str(input("enter a name: ")) 
# print(len(a))


# Write a program to reverse a string.
# a=str(input("enter a name: ")) 
# print(a[::-1])


# Write a program to check if a string is a palindrome.
# a=str(input("enter a name: "))
# if a==a[::-1]:
#     print(f"{a} is a palindrome")
# else:
#     print(f"{a} is not a palindrome")


# Write a program to print numbers from 1 to 10 using a loop.
# for i in range(1,11):
#     print(i)


# Write a program to find the sum of the first n natural numbers.
# n=int(input("Value of n: "))
# total_sum=0
# for i in range(1,1+n):
#     total_sum=total_sum+i
# print(total_sum)

# def sumcal(total_sum=0):
#     n=int(input("Value of n: "))
#     for i in range(1,1+n):
#         total_sum+=i
#     print(total_sum)
# sumcal()


# Write a program to calculate the factorial of a number.
# def fact(n=0):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(n=int(input("Value of n: "))))


# Write a program to print the multiplication table of a given number.5
# n=int(input("Value of n: "))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")


# Write a program to count the number of vowels in a string.
# a=str(input("enter a name: "))
# vowels="AEIOUaeiou"
# count=0
# for char in a :
#     if char in vowels:
#         count+=1
# print(f"number of vowels in {a} is {count}") 


# Write a program to print all even numbers between 1 and 100.
# for i in range(1,101):
#     if i%2==0:
#         print(i)


# Write a program to check if a number is prime.
# n=int(input("enter number: "))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print(f"{n} is not a prime number")
#             break
#     else:
#         print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")


# Write a function that returns the square of a number.
# def square(num=0):
#     num=int(input("enter number: "))
#     print(num*num)
# square()


# Write a function that takes two numbers and returns the greater one.
# def greater(a=0,b=0):
#     a=int(input("enter a: "))
#     b=int(input("enter b: "))
#     if a>b:
#         print(a)
#     else:
#         print(b)
# greater()


# Write a program to find the largest number in a list.
# def largest_list(list=0):
#     list=[1,2,3,4,5,6,7,8]
#     print(max(list))
# largest_list()


# Write a program to calculate the average of numbers in a list.
# def calculate_average(numbers=0):
#     numbers=[10,20,30,40,50,60]
#     if len(numbers)==0:
#         return 0
#     total=sum(numbers)
#     average=total/len(numbers)
#     print(average)
# calculate_average()


# Write a program to remove duplicates from a list.
# lists=[1,2,3,4,4,4,5,6,7,8,9]
# a=set(lists)
# print(a)


# Write a program to sort a list in ascending order.
# lists=[1,2,3,4,7,4,5,6,7,8,9]
# a=sorted(lists)
# print(a[::-1])
# b=set(a)
# print(b)


# Write a program to find the sum of digits of a number.
# num=int(input("enter a number: "))
# total_sum=0
# while num>0:
#     last=num%10
#     total_sum+=last
#     num=num//10
# print(total_sum)


# Write a program to generate the Fibonacci series up to n terms.
# def fibonacci(n):
#     a, b = 0, 1
#     series = []
#     for i in range(n):
#         series.append(a)
#         a, b = b, a + b 
#     return series
# n = int(input("Enter the number of terms: "))
# print("Fibonacci series up to", n, "terms:", fibonacci(n))


# Write a program that prints the first n even numbers.
# for i in range(1,100):
#     if i%2==0:
#         print(i)


# Write a program that converts Celsius to Fahrenheit.
# def celsius_to_fahrenheit(n):
#     n=int(input("enter celsius: "))
#     fahrenheit=(n*9/5)+32
#     print(fahrenheit)
# celsius_to_fahrenheit(n=0)


# Write a program that converts Fahrenheit to Celsius.
# def fahrenheit_to_celsius(n):
#     n=int(input("enter fahrenheit: "))
#     celsius=(n-32)*5/9
#     print(celsius)
# fahrenheit_to_celsius(n=0)


# Write a program that checks if a string contains only digits.
# def check_digits(s):
#     s=str(input("enter string: "))
#     if s.isdigit():
#         print(f"{s} contains only digits")
#     else:
#         print(f"{s} does not contain only digits")
# check_digits(s="")


# Write a program that finds the second largest number in a list.
# lists=[1,2,3,4,5,6,7,8,9]
# lists.sort()
# print(lists[-2])


# Write a program that finds the index of a specific element in a list.
# lists=[10,20,30,40,50,60]
# element=int(input("enter element: "))
# if element in lists:
#     index=lists.index(element)
#     print(f"index of {element} is {index}")
# else:
#     print(f"{element} not found in the list")


# Write a program to check if a number is a perfect square
# import math
# def is_perfect_square(n=0):
#     n=int(input("enter number: "))
#     sqrt_n=math.isqrt(n)
#     if sqrt_n*sqrt_n==n:
#         print(f"{n} is a perfect square")
#     else:
#         print(f"{n} is not a perfect square")
# is_perfect_square()


# Write a program to remove all whitespaces from a string
# def remove_whitespaces(s):
#     s = str(input("enter string: "))
#     s = s.replace(" ", "")
#     print(s)
# remove_whitespaces()


# Write a program that reverses the words in a sentence.
# a=str(input("enter a name: "))
# print(a[::-1])



# Write a program to create a list of all the odd numbers between 1 and 50.
# a=[]
# for i in range(1,51):
#     if i%2!=0:
#         a.append(i)
# print(a)



# Write a program that converts a string to lowercase.
# a=str(input("enter a name: "))
# print(a.lower())
# Write a program that converts a string to uppercase.
# print(a.upper())



# Write a program that counts the number of digits in a given number.
# def count_digits_loop(n):
#     if n==0:
#         return 1 
#     count=0
#     while n>0:
#         n//=10
#         count+=1
#     return count

# print(f"The number of digits is: {count_digits_loop(n=int(input("enter number: ")))}")


# Write a program that finds the common elements between two lists.
# a=[1,2,3,4,5]
# b=[4,5,6,7,8]
# common_elements=[c for c in a if c in b]
# print(f"Common elements between {a} and {b} are: {common_elements}")

# a=[1,2,3,4,5,6]
# b=[2,3,4,5,6,7,8,9]
# common1=set(a)
# common2=set(b)
# print(common1&common2)


# Write a program that removes all elements from a list that are less than a certain value.
# a=[1,2,3,4,5,6,7,8,9]
# value=int(input("enter value: "))
# filtered_list=[i for i in a if i<value]
# print(f"List after removing elements less than {value}: {filtered_list}")


# Write a program that calculates the area of a circle given its radius.
# import math
# def area_of_circle(radius=0):
#     radius=float(input("enter radius: "))
#     area=math.pi*radius*radius
#     print(f"Area of circle with radius {radius} is: {area}")
# area_of_circle()


# Write a program to calculate the area of a rectangle.
# import math
# def area_of_rectangle(l=0,b=0):
#     l=float(input("enter length: "))
#     b=float(input("enter breadth: "))
#     area=l*b
#     print(f"Area of rectangle with length {l} and breadth {b} is: {area}")
# area_of_rectangle()


# Write a program to calculate the perimeter of a rectangle.
# import math
# def perimeter_of_rectangle(l=0,b=0):
#     l=float(input("enter length: "))
#     b=float(input("enter breadth: "))
#     perimeter=2*(l+b)
#     print(f"Perimeter of rectangle with length {l} and breadth {b} is: {perimeter}")
# perimeter_of_rectangle()


# Write a program that checks whether a given number is a palindrome.
# def is_palindrome(n=0):
#     n=str(input("enter number: "))
#     if n==n[::-1]:
#         print(f"{n} is a palindrome")
#     else:
#         print(f"{n} is not a palindrome")



# Write a program to check if two strings are anagrams.

# Write a program to sum the squares of the first n positive integers.

# Write a program that finds the smallest number in a list.

# Write a program to find the length of a string without using len().

# Write a program to print the multiplication table in reverse order.

# Write a program to calculate the sum of the even numbers in a list.

# Write a program that replaces all spaces in a string with underscores.

# Write a program to find the difference between the largest and smallest number in a list.

# Write a program that accepts a string and returns the number of occurrences of each letter in the string.

# Write a program to check if a list is sorted.

# Write a program to generate all possible permutations of a string.

# Write a program that finds the intersection of two lists.

# Write a program that generates a random number between 1 and 100.

# Write a program that counts how many times a substring appears in a string.

# Write a program to concatenate two lists.

# Write a program that prints the factors of a number.


# n=input("Enter numbers or characters: ")
# if n.isdigit():
#     print(f"{n} it is digit")
# else:
#     print(f"{n} it is contains both digit and characters")
