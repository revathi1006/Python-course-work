#19.List Compersion
l = []
for i in range(5):
    l.append(i)
ul=[i for i in range(5)]
print(l,ul)
#[0, 1, 2, 3, 4] [0, 1, 2, 3, 4]
#2.even
even = []
n=20
for i in range(1,n+1):
    if i%2==0:
        even.append(i)
ueven = [ i for i in range(1,n+1) if i%2==0]
print(ueven,even)
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20] [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#3.Even and Odd
l = [1,2,3,4,5,6,7,8,9,10]
res = []
for i in l:
    if i%2==0:
        res.append("Even")
    else:
        res.append("Odd")
ures = ["Even" if i%2==0 else "Odd" for i in l]
print(res,ures)
#['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even'] ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']

#4.Sum
l=[[1,2],[3,4],[5,6],[7,8]]
res = []
for i in l:
    res.append(sum(i))

ures = [sum(i) for i in l]
print(res,ures)
#[3, 7, 11, 15] [3, 7, 11, 15]

#5.
l=[1,2,3,4,5,6]
res =[]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        res.append((l[i],l[j]))

ures=((l[i],l[j]) for i in range(len(l)-1) for j in range(i+1,len(l)))
print(res,ures)
#[(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6)]

s=set()
for i in range(1,11):
    s.add(i)
us={i for i in range(1,11)}
print(s,us)
#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

d={}
for i in range(1,10):
    d[i]=i*i
ud={i:i*i for i in range(1,10)}
print(s,us)
#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

t=tuple(i for i in range(1,10))
print(t)
#(1, 2, 3, 4, 5, 6, 7, 8, 9)
