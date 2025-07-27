#1.print Number from 1 to N (using for loop)
n = int(input("Enter a Number: "))
for n in range(1,n+1):
    print(n)
#output:Enter a Number: 5
'''1
2
3
4
5'''

#2.Print even Number from 1 to N (Using for loop)
a = int(input("Enter the number:"))
for a in range(2,a+1,2):
        print(a) 
#Enter the number:10
'''2
4
6
8
10'''
#3.Sum of number from 1 to n(using for loop)
a = int(input("Enter the number:"))
sum = 0
for i in range(1,a+1):
    sum = sum + i
print(sum)    
#output:Enter the number:5 --15

#4.print odd numbers from 1 to n (using for loop)
a = int(input("Enter the number:"))
for a in range(1,a+1,2):
        print(a) 
#output:Enter the number:4
'''1
3'''

#5.find factories of a number
n = int(input("Enter a number:"))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(f"{n}! = {fact}")  
#output:Enter a number:5 -- 5! = 120  

#6. print multiplication table of n
n = int(input("Enter a Number:"))   
for i in range(1,10):
      print(f"{n} * {i} = {n * i}")

#7.Check prime number using for loop
n = int(input("Enter a number:"))
for i in range(n,n+1):
    if n % i == 0:
        print("prime number")

     
