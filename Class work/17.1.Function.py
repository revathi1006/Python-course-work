
'''#1.Postional Agr
def function_name(arg1,agr2,agr3):
    #block of code
#function_name(val1,val2,val3) different argments and different value
#function_name(arg1,agr2,agr3)
#function_name(val3,val2,val1)

def student_details(name,rollno,marks,grade,course):
    print('Name:',name)
    print('Rollno:',rollno)
    print('Marks:',marks)
    print('Grade:',grade)
    print('Course:',course)
name = input("Name:")
rollno = int(input("Rollno:"))
marks = int(input("Marks:"))
grade = input("Grade:")
student_course = input("Course:")
student_details(name,rollno,marks,grade,student_course)
student_details('Revathi',78,100,'A','Python')
output:
Name:Sony
Rollno:32
Marks:90
Grade:A
Course:Java
Name: Sony
Rollno: 32
Marks: 90
Grade: A
Course: Java
Name: Revathi
Rollno: 78
Marks: 100
Grade: A
Course: Python
---------------------------------------------------------------------------------------

#2.Keyword Arg

def function_name(agr1,agr2,agr3):
    #Block Of Code
function_name(agr1='Val1',agr2='Val2',agr3='Val3')
function_name(agr3='Val3',agr2='Val2',agr1='Val1')

def student_details(name,rollno,marks,grade,course):
    print('Name:',name)
    print('Rollno:',rollno)
    print('Marks:',marks)
    print('Grade:',grade)
    print('Course:',course)
name = input("Name:")
rollno = int(input("Rollno:"))
marks = int(input("Marks:"))
grade = input("Grade:")
student_course = input("Course:")
student_detailslno=(rollno=rollno,name=name,marks=marks,course=student_course,grade=grade)
student_detailslno=(name=name,rollno=rollno,marks=marks,course=student_course,grade=grade)

output:
Name:aravind
Rollno:12
Marks:56
Grade:C
Course:Python
Name: aravind
Rollno: 12
Marks: 56
Grade: C
Course: Python
Name: aravind
Rollno: 12
Marks: 56
Grade: C
Course: Python

---------------------------------------------------------------------------------------------------
3.Default Arg

def function_name(arg1,arg2,arg3='val3'):
    #Block Of Code
function_name(val1,val2)
function_name(val3,val1)
function_name(arg1,agr2,arg3)

def student_details(name,rollno,marks=0,grade='F',course='python'):
    print('Name:',name)
    print('Rollno:',rollno)
    print('Marks:',marks)
    print('Grade:',grade)
    print('Course:',course)
name = input("Name:")
rollno = int(input("Rollno:"))
marks = int(input("Marks:"))
grade = input("Grade:")
course = input("Course:")
student_details(name,rollno)
student_details(name,rollno,marks)
student_details(name,rollno,marks,grade)
student_details(name,rollno,marks,grade,course)
output:
Name:Revathi
Rollno:56
Marks:78
Grade:B
Course:CSE
Name: Revathi
Rollno: 56
Marks: 0
Grade: F
Course: python
Name: Revathi
Rollno: 56
Marks: 78
Grade: F
Course: python
Name: Revathi
Rollno: 56
Marks: 78
Grade: B
Course: python
Name: Revathi
Rollno: 56
Marks: 78
Grade: B
Course: CSE

-------------------------------------------------------------------------------------------
Variable Lenght

def function_name(*agr):=>(tuple)
    #block of code

function_name(val1,val2,val3,val4)
function_name(val3,val1)
function_name(agr1,agr2,agr3)
function_name(agr1)


def names(*stdnames):
    print("\nName of students")
    for i in stdnames:
        print(f"**{i.upper()}**")

names('Revathi','sony','Aravind')
names('Revathi','sony','Aravind','nihitha','Ranjith','Vaish')
names('Aravind','nihitha','Ranjith','Vaish')
names('Revathi','sony','Aravind','vaish')

Name of students
**REVATHI**
**SONY**
**ARAVIND**

Name of students
**REVATHI**
**SONY**
**ARAVIND**
**NIHITHA**
**RANJITH**
**VAISH**

Name of students
**ARAVIND**
**NIHITHA**
**RANJITH**
**VAISH**

Name of students
**REVATHI**
**SONY**
**ARAVIND**
**VAISH**

-----------------------------------------------------------------------------------------------------


def function_name(**agr):=>(dict)
    #block of code

function_name(agr1='val1')
function_name(agr2='val1',agr1='val2',agr3='val3')
function_name(agr1='val2',agr3='val3')
function_name(agr2='val1',agr1='val2',agr3='val3',agr4='val4')



def display_products(**product):
    print("\nProducts and Prices: ")
    for i in product:
        print(f'{i}: ${product[i]}')

display_products(laptop=60000,phone=35000,watch=15000,fridge=200000)
display_products(fashwash=600,perfume=2000,eyeliner=1500,powder=2500)
display_products(carrot=25,tomato=30,beetroot=40,apple=50)

Products and Prices:
laptop: $60000
phone: $35000
watch: $15000
fridge: $200000

Products and Prices:
fashwash: $600
perfume: $2000
eyeliner: $1500
powder: $2500

Products and Prices:
carrot: $25
tomato: $30
beetroot: $40
apple: $50

-----------------------------------------------------------------------------------------------'''