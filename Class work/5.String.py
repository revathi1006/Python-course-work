#1.Defining string
str1 = 'Python'
str2 = "Programming"
str3 = '''Python programming language'''
print(str1) #Python
print(str2) #Programming
print(str3) #Python programming language

#2.Operations On String
#2.1.Concatenation
str1 = "Durgam"
str2 = "Revathi"
result = str1 + " " + str2
print(result) #Durgam Revathi

#2.2.Repetition
print("Revathi! " * 4) #Revathi! Revathi! Revathi! Revathi! 

#2.3.Indexing
text = "Revathi"
print(text[0]) #R
print(text[4]) #t
print(text[-2]) #h

#2.4.Slicing
text = "Durgam"
print(text[0:2]) #Du
print(text[0:6]) #Durgam
print(text[1:5]) #urga
print(text[:4]) #Durg
print(text[3:]) #gam
print(text[-5]) #u
print(text[-6:]) #Durgam
print(text[:-4]) #Du

#2.4.1Slicing
string ="RevathiRamyaNavya"
print(string[-5:]) #Navya
print(string[-10:-5]) #Ramya
print(string[-17:-10]) #Revathi
print(string[::-1]) #ayvaNaymaRihtaveR
print(string[-1:-6:-1]) #ayvaN
print(string[-6:-11:-1]) #aymaR

#2.5.Membership
print('Dur' in text) #True
print('rev' not in text) #True

#3.Built-in String Function
#3.1.len()
text = "Revathi"
print(len(text)) #7

#3.2.Max() and min()
print(max(text)) #v
print(min(text)) #R

#3.3.sorted()
print(sorted("Python")) #['P', 'h', 'n', 'o', 't', 'y']
 
#3.4.chr() and ord()
print(ord('A')) #65
print(ord('R')) #82
print(chr(78)) #N
print(chr(89)) #Y

#4.String Methods
#4.1.Uppercase
text = "hello"
print(text.upper()) #HELLO

#4.2.Lowercase
text = "HELLO"
print(text.lower()) #hello

#4.3.Capitalize
text1 = "python program"
print(text1.capitalize()) #Python program

#4.4.Title
print(text1.title()) #Python Program

#4.5.Swapcase
print(text1.swapcase()) #PYTHON PROGRAM

#5.Alignment & Formatting
#5.1.Center width
text2 = "python"
print(text2.center(20, "*")) #*******python*******

#5.2.Left-aligns
text3 = "python"
print(text3.ljust(25,"*")) #python*******************


#5.3.Right-align
text4 = "python"
print(text4.rjust(10,"*")) #****python

#5.4.Pads the string with zero on the left
text5 = "40"
print(text5.zfill(6)) #000040

#6.Search & Find Methods
#6.1.Index Of First Occurrence
text6 = "python"
print(text6.find("p")) #0
print(text6.find("h")) #3

#6.2.Last Occurrence
text7="Hello"
print(text7.rfind("l")) #3
print(text7.rfind("o")) #4

#6.3.find error not found
S = "hello"
print(S.index("e")) #1

#6.4.rfind 
print(S.rindex("o")) #4

#6.5.count
text8 = "durgam revathi"
print(text8.count("a")) #2
print(text8.count("r")) #2

#7.String Testing Methods(Boolean Result)
#7.1String Startswith
s = "python programming"
print(s.startswith("py")) #True
print(s.startswith("ra")) #False

#7.2.String Endswith
print(s.endswith("ing")) #True
print(s.endswith("on")) #False

#7.3.String isalpha
s1 = "Python"
print(s1.isalpha()) #True
s2 ="Python2"
print(s2.isalpha()) #False

#7.4.String isalnum
s3 = "Python123"
print(s3.isalnum()) #True

#7.5.String islower
s4 = "python"
print(s4.islower()) #True

#7.6.String isupper
s5 = "PYTHON"
print(s5.isupper()) #True

#7.7.String isspace
s6 = " "
print(s6.isspace()) #True
s7 = "Hello      "
print(s7.isspace()) #False

#7.8.String
s8 = "Hello"
print(s8.istitle()) #True
s9 = "hello"
print(s9.istitle()) #False

#7.9.String isidentifier
s10 = "var1"
print(s10.isidentifier()) #True
s11 = "2rev"
print(s11.isidentifier()) #False

#7.10.String isdecimal
s12 = "123"
s13 = "23.5"
print(s12.isdecimal()) #True
print(s13.isdecimal()) #False

#7.11.String isdigit
s14 = "25"
s15 = "①"
print(s14.isdigit()) #True
print(s15.isdigit()) #True

#7.12.String isnumeric
s16 = "⑤"
s17 = "¾"
s18 = "123"
print(s16.isnumeric()) #True
print(s17.isnumeric()) #True
print(s18.isnumeric()) #True

#8.Replace & Modify Methods
#8.1.replace(old,new)
l = "Python Programming Language"
result = l.replace("Python","Java") #Java Programming Language
print(result)

#8.2.translate(table)
l1 = "abc"
print(l1.translate(str.maketrans("a","x"))) #xbc

#8.3.maketrans
l2 = "python"
print(l2.maketrans("aon","%#$")) #{97: 37, 111: 35, 110: 36}

#9Splitting & Joining Methods
#9.1.splitting
l3 = "a,b,c,d"
print(l3.split(",")) #['a', 'b', 'c', 'd']

#9.2.rsplit
l4 = "a,b,c,d"
print(l4.rsplit(",", 1)) #['a,b,c', 'd']

#9.3.splitlines
l5 = "Python\nProgram"
print(l5.splitlines()) #['Python', 'Program']

#9.4.join
l6 = ["Python","Program"]
s = " ".join(l6)
print(s) #Python Program

#9.5.partition
l7 = "python@programm"
print(l7.partition("@")) #('python', '@', 'programm')

#9.6.rpartition
l8 = "python-program"
print(l8.rpartition("-")) #('python', '-', 'program')

#10.Whitespace & trimming Methods
#10.1.strip
a = "python"
print(a.strip()) #python

#10.2.lstrip
a1 = "-------python"
print(a1.lstrip("-")) #python

#10.3.rstrip
a2 = "python      "
print(a2.rstrip(" ")) #python

#11.Encoding & Decoding Methods
#11.1.Encoding
a3 = "Python"
print(a3.encode("utf-8")) #b'Python'

#11.2.Decoding
a4 = b"Python"
print(a4.decode("utf-8")) #Python

