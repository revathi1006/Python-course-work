#3.Python
#1.Add Two Numbers
'''
def add_number(a,b):
    return a + b
num1,num2= map(int, input("Enter two Number:").split())
sum = add_number(num1,num2)
print("The sum is:",sum)
#Enter two Number:2 4
#The sum is: 6

#2. Square a Number
def square_number(a):
    return a**2
a = int(input("Enter a Number:"))
square=square_number(a)
print("The square is:",square)
#Enter a Number:4
#The square is: 16

#3.Area of a Circle
def area_of_circle(radius):
    pi = 3.14
    return pi * radius * radius
r = float(input("Enter radius:"))
area = area_of_circle(r)
print("Area of circle is :",area)
#Enter a Number:3
#The square is: 9
#4. Greet the User
def greet_user(name):
    return name
a = input("Enter your name:")
b = greet_user(a)
print("Hello,",b)
#Enter your name:Alice
#Hello, Alice

#5.Convert Celsius to Fahrenheit
def celsius_Fahrenheit(c):
    return (c*9/5)+32
celsius = float(input("Enter temperature in Celsius:"))
Fahrenheit=celsius_Fahrenheit(celsius)
print("Temperature in Fahrenheit:",Fahrenheit)
#Enter temperature in Celsius:37
#Temperature in Fahrenheit: 98.6

#6. Multiply Three Numbers
def Three_numbers(a,b,c):
    return a * b * c
number = input("Enter Three numbers:")
a,b,c = map(int,number.split())
mulity = Three_numbers(a,b,c)
print("Product:",mulity)
#Enter Three numbers:2 3 4
#Product: 24

#7.Calculate Simple Interest
def Calculate_Simple_Interest(a,b,c):
    return (a*b*c)/100
a = float(input("Enter the principal: "))
b = float(input("Enter Rate of time:"))
c = float(input("Enter the time period (in year):"))
Simple_Interest=Calculate_Simple_Interest(a,b,c)
print("Simple Interest is:",Simple_Interest)
#Enter the principal: 1000
#Enter Rate of time:5
#Enter the time period (in year):2
#Simple Interest is: 100.0

#8. Find Length of a String
def length_string(s):
    return len(s)
string = input("Enter a string:")
length = length_string(string)
print("Length of string is:",length)
#Enter a string:hello
#Length of string is: 5

#9.Append to a List

def append_to_list(lst, element):
    lst.append(element)
    return lst
input_list = input("Enter list elements separated by space: ")
lst = list(map(int, input_list.split()))
element = int(input("Enter element to append: "))
updated_list = append_to_list(lst, element)
print("Updated list:", updated_list)
#Enter list elements separated by space: 1 2 3
#Enter element to append: 4
#Updated list: [1, 2, 3, 4]

#10.Double Each Element in a List
def Double_element(lst):
    return [x * 2 for x in lst]
input_lst = input("Enter list Eements:")
list = list(map(int,input_lst.split()))
element = Double_element(list)
print("Doubled list:",element)
#Enter list Eements:1 2 3
#Doubled list: [2, 4, 6]

#11. Sort a List
def sort_list(n):
    return sorted(n)
input_lst = input("Enter list elements:")
list = list(map(int,input_lst.split()))
sorted = sort_list(list)
print("Sorted list:",sorted)
#Enter list elements:4 2 5 1
#Sorted list: [1, 2, 4, 5]

#12.Clear a List Inside Function
def clear_list(lst):
    lst.clear()
    return lst
input_list =input("Enter list elements:")
list = list(map(int,input_list.split()))
cleared = clear_list(list)
print("Cleared list:",cleared)
#Enter list elements:1 2 3
#Cleared list: []

#13. Update Dictionary Value
def update_dict_value(d, key, new_value):
    if key in d:
        d[key] = new_value
    else:
        print(f"Key '{key}' not found in dictionary.")
    return d
dict_input = input("Enter dictionary: ")
d = eval(dict_input) 
key = input("Enter key to update: ")
new_value = eval(input("Enter new value: ")) 
updated_dict = update_dict_value(d, key, new_value)
print("Updated dictionary:", updated_dict)

#14. Remove Element from List by Value
def remove_list(lst,value):
    if value in lst:
        lst.remove(value)
    else:
        print(f"Element{value} is not found in the list")
    return lst
input_list = input("Enter list elements:")
lst = list(map(int,input_list.split()))
value = int(input("Enter element to remove:"))
update = remove_list(lst,value)
print("Updated list:",update)
#Enter list elements:1 2 3 4
#Enter element to remove:4
#Updated list: [1, 2, 3]

#15.Add Key to Dictionary
#16.Factorial of a Number
def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact
num = int(input("Enter a number:"))
print("Factorial is:",factorial(num))
#Enter a number:5
#Factorial is: 120

#17.Fibonacci Number (Nth Term)
def fibonacci(n):
    a,b = 0,1
    if n == 1:
        return a
    elif n == 2:
        return b
    for _ in range(2, n):
        a, b = b, a + b
    return b
n = int(input("Enter nth term number:"))
print("Fibonacci number is:",fibonacci(n))  

#18. Sum of First N Natural Numbers
def sum_of_naturalnum(n):
    total = n * (n+1)//2
    return total
num = int(input("Enter a number:"))
result = sum_of_naturalnum(num)
print("sum is:",result)
#Enter a number:10
#sum is: 55 

#19.20. Reverse a String Using
def reverse_string(s):
    return s[::-1]
text = input("Enter a string:")
reverse_s = reverse_string(text)
print("Reversed string is:",reverse_s)

#Enter a string:hello
#Reversed string is: olleh   

#25.Maximum of Three Numbers Using max()
def max_three(a,b,c):
    return max(a,b,c)
num1,num2,num3 =map(int,input("Enter three number:").split())
number = max_three(num1,num2,num3)
print("Maximum:",number)

#Enter three number:2 3 5
#Maximum: 5 

#26. Sort a List Using sorted()
def sort_number(n):
    return sorted(n)
lst = list(map(int,input("Enter list element:").split()))
element = sort_number(lst)
print("sorted list:",element)

#Enter list element:3 1 4
#sorted list: [1, 3, 4]

#27. Sum of Elements Using sum()
def sum_element(n):
    return sum(n)
lst = list(map(int,input("Enter list elements:").split()))
element = sum_element(lst)
print("sum of list is:",element)

#Enter list elements:4 5 6
#sum of list is: 15

#28. Find Data Type Using type()
def find_data_type(value):
    return type(value)
value = int(input("Enter any value: "))
print("Data type is:", find_data_type(value))

#Enter any value: 2
#Data type is: <class 'int'>

#29. Print Even Numbers up to N
def even_number(n):
    for i in range(0,n+1,2):
        print(i,end=" ")
even = int(input("Enter a number:"))
print("Even numbers:",end=" ")
num = even_number(even)

#Enter a number:10
#Even numbers: 0 2 4 6 8 10  


#30. Return List of Squares
def list_squares(n):
    return [x**2 for x in n]
lst = list(map(int,input("Enter list elements:").split()))
elements = list_squares(lst)
print("Squared list",elements)

#Enter list elements:1 2 3
#Squared list [1, 4, 9] 

#31. Check if Number is Prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True
num = int(input("Enter a number:"))
print("Is prime:",is_prime(num))
#Enter a number:7
#Is prime: True  

#32. Count Vowels in a String
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

text = input("Enter a string: ")
vowel_count = count_vowels(text)
print("Number of vowels:", vowel_count)
#Enter a string: EDUCATION
#Number of vowels: 5'''