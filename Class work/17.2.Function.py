#1.Local Scope
'''
def student():
    name = "Revathi"
    print(name)
student()
output:Revathi'''

#2.Global scope
'''
name = "Revathi"
def student():
    print(name)
student()
print(name)
output:
Revathi
Revathi'''

#3.Global keyword 
'''
name = "Revathi"
def student():
    global name
    name = "Durgam"
student()
print(name)
output:Durgam
'''
#4.Enclosing Scope
''''
def student():
    course = "python"
    def student():
        nonlocal course
        course = "Java"
    student()
    print(course)
student()
#output:
Java'''

