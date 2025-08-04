# First half
for i in range(1, 5):
    print((str(i) + ' * ') * (i - 1) + str(i))

# Second half
for i in range(3, 0, -1):
    print((str(i) + ' * ') * (i - 1) + str(i))



size = 7  # Pattern size (must be odd)

for row in range(size):
    for col in range(size):
        if row == col or row + col == size - 1:
            print('.', end=' ')
        else:
            print('*', end=' ')
    print()

size = 7  # Must be odd
mid = size // 2  # Middle index

for row in range(size):
    for col in range(size):
        if col == mid:
            print('.', end=' ')
        elif row == mid:
            print('.', end=' ')
        elif col < abs(mid - row) or col >= size - abs(mid - row):
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()


for i in range(4): # Outer loop runs 3 times
    for j in range(2): # Inner loop runs 2 times for each

        print(f"i={i}, j={j}")



# Print odd numbers only
n = int(input("Enter a Number:"))
for num in range(n,n+1):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")