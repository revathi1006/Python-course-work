#15.patterns
#Nested Loops
for i in range(5):
    print(i,end=" ") #1 2 3 4 5

n = int(input("Enter The size:"))
for row in range(n):
    for col in range(n):
        print('*',end='')
    print()    
'''output
Enter The size:8
********
********
********
********
********
********
********
********'''
n = int(input("Enter The size:"))
for row in range(n):
    for col in range(n):
        print(row,end='')
    print()  
'''Enter The size:5
00000
11111
22222
33333
44444'''
n = int(input("Enter The size:"))
for row in range(n):
    for col in range(n):
        print(col,end='')
    print()  

'''Enter The size:7
0123456
0123456
0123456
0123456
0123456
0123456
0123456'''
n = int(input("Enter The size:"))
for row in range(n):
    for col in range(row+1):
        print("*",end='')
    print()  

'''Enter The size:8
*
**
***
****
*****
******
*******
********'''

n = int(input("Enter The size:"))
for row in range(n):
    for col in range(n-row):
        print("*",end='')
    print()  

'''Enter The size:6
******
*****
****
***
**
*'''
n = int(input("Enter The size:"))
for row in range(n):
    for spc in range(n-row-1):
        print(' ',end='')
    for col in range(row+1):
        print("*",end='')
    print()  

'''Enter The size:9
        *
       **
      ***
     ****
    *****
   ******
  *******
 ********
*********'''
n = int(input("Enter The size:"))
for row in range(n):
    for spc in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print("*",end='')
    print() 

'''Enter The size:9
*********
  ********
    *******
      ******
        *****
          ****
            ***
              **
                *'''
n = int(input("Enter The size:"))
for row in range(n):
    if row<=n//2:
        for col in range(row+1):
            print('*',end=' ')
    else:
        for col1 in range(n-row):
            print('*',end=' ')        
    print()  

'''Enter The size:10
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * *
* * *
* *
*'''
n = int(input("Enter The size:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()       

'''Enter The size:10
* * * * * * * * * *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
* * * * * * * * * * '''     

n = int(input("Enter The size:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()  


'''Enter The size:12
* * * * * * * * * * * *
*                     *
*                     *
*                     *
*                     *
*                     *
* * * * * * * * * * * *
*                     *
*                     *
*                     *
*                     *
* * * * * * * * * * * *'''

n = int(input("Enter The size:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==n//2 or col==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()  

'''Enter The size:12
* * * * * * * * * * * *
*           *         *
*           *         *
*           *         *
*           *         *
*           *         *
* * * * * * * * * * * *
*           *         *
*           *         *
*           *         *
*           *         *
* * * * * * * * * * * *'''


n = int(input("Enter The size:"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col+row== n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()  

'''Enter The size:12
* * * * * * * * * * * *
                    *
                  *
                *
              *
            *
          *
        *
      *
    *
  *
* * * * * * * * * * * *'''

n = int(input("Enter The size:"))
for row in range(n):
    for col in range(n):
        if row==col or col+row== n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()  

'''Enter The size:14
*                         *
  *                     *
    *                 *
      *             *
        *         *
          *     *
            * *
            * *
          *     *
        *         *
      *             *
    *                 *
  *                     *
*                         *'''