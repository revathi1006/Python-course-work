'''n = input()
full = len(n) 
length = len(n)//2
ind = 0
while ind<=length:
    if n[ind] !=n[full]:
        print("Not palindrome")
        break
    ind += 1
    full =- 1
else:
    print("palindrome")   '''


products={ 
    "apple":30,
    "banana":10,
    "Orange":20,
    "Milk":50,
    "Bread":25,
    "Eggs":60,
    "Rice":40,
    "Tea":35,
    "Salt":40
    }
#Bill generation
AddtoCart={}
while True:
    #Display Menu
    print('Available product'.center(40,'='))
    for i,key in enumerate(products):
        print(f'{(i+1)}. {key.ljust(10," ")}: ${products[key]}')
    #Taking a product name
    product= input("Enter the Product name(Done-Exit):").title()

    #Exit -Bill generation Logic
    if product == 'Done':
        if AddtoCart:
            totalbill = 0
            for i in AddtoCart:
                print(f'{i.ljust(10," ")}: {AddtoCart[i]} *{products[i]}')
                totalbill = totalbill+AddtoCart[i]*products[i]
            print(f"Total Bill:{totalbill}")
        else:
            print('Thanks')
        break
    #Adding Product to the cart
    if product in products:
        qua=int(input("enter the quantity:"))
        print(f'{product} is add to the cart')

        AddtoCart[product]=qua
    else:
        print(f"{product} is not found")
