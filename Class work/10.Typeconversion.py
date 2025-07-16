#10.Type Conversion (Type Casting)
#1.Converting from int
a = 5
print(float(a)) #5.0
print(str(a)) #5
print(complex(a)) #(5+0j)
print(bool(a)) #True
#print(list(a)) #Error
#print(set(a)) #Error
#print(tuple(a)) #Error
#print(dict(a)) #Error

#2.Converting from float
f = 4.6
print(int(f)) #4
print(str(f)) #4.6
print(bool(f)) #True
print(complex(f)) #(4.6+0j)
#print(list(f)) #Error
#print(tuple(f)) #Eorro
#print(set(f)) #Error
#print(dict(f)) #Error

#3.Converting from str
s = "Revathi"
#print(int(s)) #Error
#print(float(s)) #Error
#print(complex(s)) #Error
print(list(s))
print(bool(s)) #True
print(tuple(s)) #('R', 'e', 'v', 'a', 't', 'h', 'i')
print(set(s)) #{'i', 'e', 'v', 'a', 'R', 'h', 't'}
#print(dict(s)) #Error

#4.Converting from list
l = [1,2,3,4,5,6]
#print(int(l)) #Error
#print(float(l)) #Error
print(bool(l)) #True
print(tuple(l)) #(1, 2, 3, 4, 5, 6)
print(set(l)) #{1, 2, 3, 4, 5, 6}
#print(dict(l)) #Error
print(str(l)) #[1, 2, 3, 4, 5, 6]

#5.Converting from tuple
t = (1,2,3,4,5,6,7)
#print(int(t)) #Error
#print(float(t)) #Error
print(str(t)) #(1, 2, 3, 4, 5, 6, 7)
print(list(t)) #[1, 2, 3, 4, 5, 6, 7]
print(set(t)) #{1, 2, 3, 4, 5, 6, 7}
#print(dict(t)) #Error
print(bool(t)) #True

#6.Converting from set
s = {10,20,30,40,50}
#print(int(s)) #Error
#print(float(s)) #Error
print(bool(s)) #True
print(str(s)) #{50, 20, 40, 10, 30}
print(list(s)) #[50, 20, 40, 10, 30]
print(tuple(s)) #(50, 20, 40, 10, 30)
#print(dict(s))

#7.Converting from dict
d = {1:11,2:22,3:33}
#print(int(d))
#print(float(d))
print(str(d)) #{1: 11, 2: 22, 3: 33}
print(bool(d)) #True 
print(list(d)) #[1, 2, 3]
print(set(d)) #{1, 2, 3}
print(tuple(d)) #(1, 2, 3)

#8.Converting from bool
b = False
print(int(b)) #0
print(float(b)) #0.0
print(str(b)) #False
print(complex(b)) #0j
#print(list(b))
#print(tuple(b))
#print(set(b))
#print(dict(b))

