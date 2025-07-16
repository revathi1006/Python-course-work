#8.Dictionary
#1.1.Syntax of a Dictionary
dict = {'Key1':'val1','key2':'val2','key3':'val3'}
print(dict) #{'Key1': 'val1', 'key2': 'val2', 'key3': 'val3'}

#1.2.Dictionary
dict1 = {"name":"Durgam Revathi","age":"22","course":"CSE"}
print(dict1) #{'name': 'Durgam Revathi', 'age': '22', 'course': 'CSE'}

#2.Dictionary Operations
#2.1.Accessing Values
dict2 = {'name': 'Durgam Revathi', 'age': '22', 'course': 'CSE'}
print(dict2["name"]) #Durgam Revathi
print(dict2.get("age")) #22

#dict(key),dict.get(key)
dict2 = {'name': 'Durgam Revathi', 'age': '22', 'course': 'CSE'}
salary = dict2.get("salary")
print(salary) #None
city = dict2.get("city","unknown")
print(city) #unknown

#2.2.Adding and updating Item
dict3 = {'name': 'Durgam Revathi', 'age': '22', 'course': 'CSE'}
dict3['age'] = 24 #updating
dict3['city'] = 'Mancherial' #adding
print(dict3) #{'name': 'Durgam Revathi', 'age': 24, 'course': 'CSE', 'city': 'Mancherial'}
dict3.setdefault("year","unknown")
print(dict3) #{'name': 'Durgam Revathi', 'course': 'CSE', 'year': 'unknown'}

#2.3.Removing item from a Dictionary
#2.3.1.Using pop(key)
age = dict3.pop("age")
print(age) #{'name': 'Durgam Revathi', 'age': 24, 'course': 'CSE', 'city': 'Mancherial'}
print(dict3) #{'name': 'Durgam Revathi', 'course': 'CSE', 'city': 'Mancherial'}
city = dict3.pop("city")
print(city) #{'name': 'Durgam Revathi', 'course': 'CSE', 'city': 'Mancherial'}
print(dict3) #{'name': 'Durgam Revathi', 'course': 'CSE'}

#2.3.2.del
del dict3["name"]
print(dict3) #{'course': 'CSE'}

#2.3.3.popitem
dict4 = {'name': 'Durgam Revathi', 'age': 24, 'course': 'CSE', 'city': 'Mancherial'}
dict4.popitem()
print(dict4) #{'name': 'Durgam Revathi', 'age': 24, 'course': 'CSE'}
dict4.popitem()
print(dict4) #{'name': 'Durgam Revathi', 'age': 24}

#2.3.4.clear
dict4.clear()
print(dict4) #{}

#3.Dictionary Built-in Methods
#3.1.dict.keys()
dict5 = {'name': 'Durgam Revathi', 'age': 24, 'course': 'CSE', 'city': 'Mancherial'}
print(dict5.keys()) #dict_keys(['name', 'age', 'course', 'city'])
print(dict5.values()) #dict_values(['Durgam Revathi', 24, 'CSE', 'Mancherial'])
print(dict5.items()) #dict_items([('name', 'Durgam Revathi'), ('age', 24), ('course', 'CSE'), ('city', 'Mancherial')])

#4.Built-in Function For Dictionaries
#4.1.len,sorted,max,min
dict6 = {1:'a',2:'b',3:'c',4:'d'}
print(len(dict6)) #3
print(sorted(dict6)) #['Key1', 'key2', 'key3']
print(max(dict6)) #key3
print(min(dict6)) #key1

#5.Nested Dictionaries
dict7 = { "Revathi":{'age': 24, 'course': 'CSE', 'city': 'Mancherial', 'year': 4},"Sony":{'age': 19, 'course': 'IT', 'city': 'Jannaram', 'year': 2}}
print(dict7["Revathi"]["city"]) #Mancherial
print(dict7["Sony"]["age"]) #19

