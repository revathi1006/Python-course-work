#1.Positive or Negative
a = int(input("Enter The number:"))
if a > 0:
    print("Postive")
else:
    print("Negative")  

#2.Even or odd
num = int(input("Enter the number:"))
if num%2==0:
    print("Even")
else:
    print("odd")    

#3.Divisible by 5
n = int(input("Enter The Number:"))

if n % 5 == 0:
    print("The Number is divisible")
else:
    print("The Number is Not divisible")    

#4.Divisible by 3 and 7
n1 = int(input("Enter the number:"))
if n1 % 3 == 0  and n1 % 7 == 0:
    print("The Number is divisible by both 3 and 7")
else:
    print("The Number is  not divisible by both 3 and 7 ")

#5.Check for Leap year
year = int(input("Enter The Number:")) 
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap year")
else:
    print("Not Leap Year")   

#6.Check pass or Fail(Passing marks = 35)
marks =int(input("Enter The Marks Details:"))
if marks >= 35:
    print("Pass")
else:
    print("Fail")       

#7.Check if number is 3-digit
number1 = int(input("Enter The Number:"))
if 100 <= number1 <= 999:
    print("it's Three-digit Number") 
else:
    print("it's not a Three-digit Number")    

#8.Check if Character is vowel
char = input("Enetr The Character:")
if char in ['a','e','i','o','u']:
    print("Vowel")
else:
    print("Not a Vowel")     

#9.Check Greatest of two numbers
a = int(input("Enter The Number1:"))
b = int(input("Enter The number2:"))
if a > b:
    print("The Greatest number is",a)
elif b > a :
    print("The Greatest number is",b)    
else:
    print("Both numbers are equal ")    

#10.Check Smallest of two number
c = int(input("Enter The Number1:"))
d = int(input("Enter The Number2:"))
if c < d:
    print("The Smallest Number",c)
elif d < c:
    print("The Smallest Number",d)
else:
    print("Both Number are equal")        

#11.Check if Number is Zero
a = int(input("Enter The Number:"))
if a == 0:
    print("The Number is Zero")  

#12.Check if Number is Multiple of 10
a = int(input("Enter The number:"))
if a % 10 == 0:
    print("Multiple of 10") 

#13.Check ig age is Eligible to vote(18+)
age = int(input("Enter The age eligible to Vote:"))
if age >=18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")    

#14.Check if Number is Between 1 and 100
num = int(input("Enter The Number:"))
if 1 <= num <= 100:
    print("The Number is between 1 and 100.")
else:
    print("The Number is not between 1 and 100.") 

#15.Check if number is square of another
number = int(input("Enter The Number"))
root = int(number ** 0.5)
if root ** root == number:
    print(f"{number} is the square of {root}.")
else:
    print(f"{num} is not a perfect square")    

#16.Check if two string are equal
a = input("Enter The String1:")
b = input("Enter The String2:")
if a == b:
    print("String are equal")
else:
    print("String are Not equal")

#17.Check if a  number is prime 
n = int(input("Enter The Prime Number:"))
if n <= 1:
    if n % 2 != 0 and  n % 3 != 0 and  n % 4 != 0 and  n % 5 != 0 and  n % 6 != 0 and  n % 7 != 0:
        print("prime")
else:
    print("Not prime")       

#18.Check if Number is Postive and even
n1 = int(input("Enter The Number: "))
if n1 > 0 and n1%2==0:
    print("Postive and even number")    

#19.Check if Character is UpperCase
n2 = input("Enter The Character:")
if n2.isupper():
    print("Uppercase letter")    
else:
    print("Not an Uppercase letter")    

#20.Check if temperature is hot
tem = int(input("Enter The Temperature"))
if tem >30:
    print("Temperature cool")
else:
    print("Temperature hot")    

"---------------------------------------------------------------------------------------------------------------"
#21.Check if a number is 4-digit even number
n3 = int(input("Enter The Number:"))
if 1000 <= n3 <= 9999 and n3 % 2 == 0:
    print("It's Four-digit even number")
else:
    print("It's not a Four-digit even number")    

#22.Check if a Character is a consonant  
char = input("Enter The Character:").lower()
if char.isalpha() and char not in["a","e","i","o","u"]:
    print("Consonant")
else:
    print("not Consonant") 
#22.1.
char = input("Enter The Character:")
if char in["a","e","i","o","u"]:
    print("vowel")
else:
    print("Consonant")  

#23.Check if a number is divisible by 2 or 3 but not both
a = int(input("Enter The First Number:"))
b = int(input("Enter The second Number:"))
if a % 2 == 0 and b % 3 == 0:
    print("Divisible by both 2 and 3") 
else:
    print("Divisible by 2 only")     
#23.1.Check if a number is divisible by 2 or 3 but not both
a = int(input("Enter The First Number:"))
if a % 2 == 0 and a % 3 == 0:
    print("Divisible by both 2 and 3") 
elif a % 2 == 0:
    print("Divisible by only 2")
elif a % 3 == 0:
    print("Divisible by only 3")        
else:
    print("Not Divisible by 2 and 3") 

#24.Check if a number is negative and odd
b = int(input("Enter The Number:"))
if a < 0 and a % 2 != 0:
    print("negative and odd number")
else:
    print(" not negative and odd number")    
#24.1
if b < 0 and b % 2 != 0:
    print("negative and odd number")
elif b < 0:
    print("negative number")
elif b % 2 != 0:
    print("odd number")    
else:
    print(" not negative and odd number")  

#25.Check if a string start with a vowel
c = input("Enter The string:")
if c[0] in['a','e','i','o','u']:
    print("start with a vowel")  

c = input("Enter The string:")
if c[0].lower() in['a','e','i','o','u']:
    print("start with a vowel") 
else:
    print("Does not start with a vowel") 

#26.Check if Three sides from a valid triangle
a = int(input("First triangle:"))
b = int(input("Second triangle:"))
c = int(input("Third triangle"))
if a + b > c and a + c > b and b + c > a:
    print("valid triangle")
else:
    print("Not valid triangle")    

#27.Find The greatest among three number
a = int(input("Enter The number1:"))
b = int(input("Enter The number2:"))
c = int(input("Enter The number3:"))
if a >=b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c
print(f"{greatest} is the greatest number ")    


#29.Check if a year is a century year and leap year
year = int(input("Enter the year:"))
if year % 100 == 0 and year % 400 == 0:
    print(f"{year} is centure year and a leap year")
else:
    print(f"{year} is a centure year and not a leap year") 

#30.check if character is a digit
char = input("Enter the character:")
if char.isdigit():
    print(f"'{char}'is a digit")
else:
    print(f"'{char}'is not a digit")