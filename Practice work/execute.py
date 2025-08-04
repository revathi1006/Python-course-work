'''# Sum of Digits of a Number (Using while loop)

# Input
n = int(input("Enter an integer: "))

# Initialize sum
sum_of_digits = 0

# Make a copy of n to work on
temp = abs(n)  # Handle negative numbers as well

# While loop to extract digits
while temp > 0:
    digit = temp % 10       # Get the last digit
    sum_of_digits += digit  # Add digit to sum
    temp //= 10             # Remove last digit

# Output
print("Sum of digits:", sum_of_digits)'''


n = int(input("Enter the Number: "))
c = 0
for i in range(2,n//2):
    if n%i==0:
        c=1
        break
if c==0:
    print("prime number")  
else:
    print("not a prime number")     

m = int(input("Enter a Number:"))

for i in range(1,11):
    print(f"{m} * {i} = {m*i}")