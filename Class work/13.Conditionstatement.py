#13.Condition Statements
#1.if,else statements
hr,mins = list(map(int,input("Enter the HH:MM:").split(":")))
if hr>=0 and hr<=24 and mins>=0 and mins<=60:
    if hr>=0 and hr<4:
        print("It's high time. Time to sleep")
    if hr>=4 and hr<=12:
        print("Good morning. Have a nice day")
    if hr>=12 and hr<16:
        print("Good Atfernoon. Have a Great lunch")
    if hr>=16 and hr<20:
        print("Good evening. Have some snacks")
    if hr>=20 and hr<24:
        print("Good Night. sweet Dreams")
else:
    print("Enter the proper input, your input is invalid")

#2.Bus Seats Avaliable
seats = {
    'L1':True,
    'L2':False,
    'L3':True,
    'U1':False,
    'U2':True,
    'U3':True

}
seatno = input("Enter the seat no to check its avaliability:").upper()
if seatno in seats:
    if seats[seatno]:
        print("Already Booked.Try with other number")
    else:
        print("seat is avaliable. Hurry up")
else:
    print("Enter the correct seat number")  

#3. 
data = {
    'watch':{'discount':10,'brands':['titan','fastrack']}

}   
print(data.keys) 
pro = input("Enter the cat:")
if pro in data:
    print(f'{data[pro] ["discount"]} % discount is going on for this brands : {data[pro]["brands"]}')
else:
    print(f"product is out of stock. please check with our other products: {data}")

               
#4.
Movies = {
    'salar':{'kids':True},
    'Rajarani':{'kids':True},
    'Arjunreddy':{'kids':False}
}
print('welcome to hotstar'.center(30,'='))
Movie = input("Enter the Movie:").title()
if Movie in Movies:
    if Movies[Movie]['kids']:
        print(f"Good selection. you can watch with your family\n{Movies}.....")
    else:
        print(f"Adult Movie. kids are not allowed.\n{Movie}......")
else:
    print(f"{Movie} is not available")            


#5.
data={
    'INDIA':('passport'),
    'NEPAL':('passport'),
    'USA':('passport','visa'),
    'CANADA':('passport','visa'),
    'ENGLAND':('passport','visa')
}
from_place = input("Enter the place from where you want to go:")
to_place = input("Enter the placeyou want to go: ").upper()
if to_place in data:
    if len(data[to_place])==1:
        print(f"Great. you only need passport to visit {to_place}")
    else:
        print(f"Great. you only need passport and visa to visit {to_place}")    
else:
    print("Data is not available")        


seats= {
    "U1":{'price':1029,'booking_status':False},
    "U2":{'price':1029,'booking_status':True},
    "U3":{'price':1029,'booking_status':True}

}
for i in seats:
    if seats[i]['booking_status']:
        print(f'***{i}***')
    else:
        print(f'{i}-{seats[i]["price"]}')
seatno = input("Enter the seat no:").upper()
if seatno in seats:
    if seats[seatno]['booking_status']:
        print(f"{seatno} is already booked. Go for other one!!")
    else:
        name = input("Enter the name:").title()
        age=int(input("Enter The age:"))
        gender = input("Enter The gender(F or M):").upper()
        if age<=5:
            print(f'Hello {name} your seat booked sucessfully with free of cost')
        elif age < 15:
            print(f'Hello {name} you seat booked sucessfully wth 50 % disscount\nTotal price={seats[seatno]["price"]*0.5}')
        else:
            print(f'Hello {name} you seat is booked suceccfull.pay the amount-{seats[i]["price"]}')      
else:
    print("Enter the seat no properly ")     



#Prime Number
n = int(input("Enter the Number: "))
c = 0
for i in range(2,n//2+1):
    if n%i==0:
        c=1
        break
if c==0:
    print("prime number")  
else:
    print("not a prime number")      


n = int(input("Enter the Number: "))
isprime = False
for i in range(2,n//2):
    if n%i==0:
        prime=True
        break
if isprime:
    print("prime number")  
else:
    print("not a prime number") 


#Fobanacci series
n = int(input("Enter the number:"))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print("f{n}! = {fact}")    


n = int(input("Enter the number:"))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)    


moves = 34
winningpoint=int(input("Enter the winning point: "))
while moves>0:
    if moves==winningpoint:
        print("Congrats!!!You Won the game")
        break
    print(f"{moves} are left. you have chance to win the game")
    moves-=1
else:
    print("game Over. Try again")   


l = (1,2,3,4)
index = 0
while index<len(l):
    print(l(index))
    index+=1


n=1
while n<7:
    print(n**2)
    n+=1

#sum of 
n = int(input())
s = 0
while n > 0:
    s+=(n%10)
    n//=10
print(s)    

n = int(input())
temp=n
rev=0
while n>0:
    rev = rev*10+(n%10)
    n//=10
if rev==temp:
    print("Palindrome")
else:
    print("Not palindrome")    

n=input()
if n==n[::-1]:
    print(True)
else:
    print(False)    

n = input()
full = len(n) 
length = len(n)//2
ind = 0
while ind<=length:
    if n[ind] !=n[full]:
        print("Not palindrome")
        break
    ind += 1
    full =- 1
else:
    print("palindrome")        