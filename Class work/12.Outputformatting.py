#12.Outputformatting
#1.Printing Text
print("Hello world") #Hello world

#1.1.Printing multiple items
name = "Revathi"
age = 23
print("name:", name, "age:", age) #name: Revathi age: 23

#1.2.Using sep to change the separator
print("2002","05","10", sep = "-") #2002-05-10

#1.3.Using end to Control Line Endings
print("Hello",end= " ")
print("Word!") #Hello Word!

#1.4.Printing special Characters
#new line(\n):
print("Name\nRevathi")
#Name
#Revathi

#1.5.tab(\t)
print("age:\t24") #age:    24

#Ouput Formatting
#2.Using Commas(simple Print Method)
Name = "Revathi"
age = 23
score = 79.1
print("Name:", name, "age:", age, "score:", score) #Name: Revathi age: 23 score: 79.1

#3.Using Modulo Operatord(%Formatting)
Name = "Navya" #String 
age = 22 #int
score = 84.57 #Float
print("Name: %s | Age: %d | Score: %.2f" % (name,age,score)) #Name: Revathi | Age: 22 | Score: 84.57

#4.Using f - string(Formatted String Literals)
name = "Sony"
age = 20
score = 75.63
print(f"Name: {name} | Age: {age} | Score: {score:.2f}") #Name: Sony | Age: 20 | Score: 75.63

#5.Using str.format() Methods
name = "Anusha"
age = 24
score = 89.456
print("Name : {} | Age : {} | Score: {:.1f}".format(name,age,score)) #Name : Anusha | Age : 24 | Score: 89.5
