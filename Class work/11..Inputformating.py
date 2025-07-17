#1.String input
name = input("Enter your full name: ")
print(name) #Enter your full name: Durgam Revathi = Durgam Revathi

#2.Integer input
quality = int(input("Enter the number of items: "))
print(quality) #Enter the number of items: 6 = 6

#3.Float input
price = float(input("Enter the product price: "))
print(price) #Enter the product price: 24.5 = 24.5

#4.Input as List(Space-separated)
names = input("Enter employee names (space-separated): ").split()
print(names) #Enter employee names (space-separated): Revathi Navya Sony = ['Revathi', 'Navya', 'Sony']

#5.Input as List(Comma-separated)
tags = input("Enter tags (comma-separated): ").split(',')
print(tags) #Enter tags (comma-separated): sale,discount,new = ['sale', 'discount', 'new']

#6.List of Integerse'
marks = list(map(int,input("Enter marks: ").split()))
print(marks) #Enter marks: 23 45 76 89 = [23, 45, 76, 89]

#7.List of floats
weights = list(map(float,input("Enter weights:").split()))
print(weights) #Enter weights:356.876 =[356.876]

#8.Tuple Input
dimensions = tuple(map(int,input("Enter length, width,height: ").split()))
print(dimensions) #Enter length, width,height: 30 40 50 = (30, 40, 50)

#9.Set Input
selected_ids = set(map(int,input("Enter selected images IDs: ").split()))
print(selected_ids) #Enter selected images IDs: 101 102 103 104 = {104, 101, 102, 103}

#10.Dictionary Input using eval()
profile = eval(input("Enter user profilr as a dictionary: "))
print(profile) #Enter user profilr as a dictionary: {'name':'Revathi','age':23,'city':'Mancherial'} ={'name': 'Revathi', 'age': 23, 'city': 'Mancherial'}

#11.Multiple Input with Unpacking
username,password = input("Enter username and password: ").split() #Enter username and password: revathi revathi123
print("username:",username) #username: revathi
print("password:",password) #password: revathi123