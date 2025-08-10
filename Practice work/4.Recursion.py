#Recursion
#1 To N
'''
def number(n):
    if n == 0:
        return
    number(n-1)
    print(n)
number(5)
1
2
3
4
5
# N To !
def number(n):
    if n == 0:
        return 
    print(n)
    number(n-1)

number(4)
4
3
2
1'''