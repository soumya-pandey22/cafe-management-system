"""
SHOULD PRINT THIS:
Welcome to our restaurant. Here's the menu:
Pizza: Rs40
Pasta: Rs50
Burger: Rs60
Salad: Rs70
Coffee: Rs80
Enter your first item you want to order = Pasta
Order of Pasta has been added.
Do you want to order anything else? Yes
Enter your second item you want to order = Coffee
Order of Coffee has been added.
The total price to pay is 130
"""

menu_1 = {}
menu_2 = {}
menu_3 = {}
menu_4 = {}
menu_5 = {}
print("Welcome to our restaurant. Here's the menu:")

menu_1["Pizza"] = 'Rs.40'
print(menu_1)
menu_2["Pasta"] = 'Rs.50'
print(menu_2)
menu_3["Burger"] = 'Rs.60'
print(menu_3)
menu_4["Salad"] = 'Rs.70'
print(menu_4)
menu_5["Coffee"] = 'Rs.80'
print(menu_5)

total = 0

Order = str(input("Enter your first item you want to order = "))

if Order == "Pizza" :
    print("Order of Pizza has been added.")
    total = total + 40
elif Order == "Pasta" :
    print("Order of Pasta has been added.")
    total = total + 50
elif Order == "Burger" :
    print("Order of Burger has been added.")
    total = total + 60
elif Order == "Salad" :
    print("Order of Salad has been added.")
    total = total + 70
else :
    print("Order of Coffee has been added.")
    total = total + 80

another_order = input("Do you want to order anything else?")

if another_order == "Yes" :
    order2 = str(input("Enter your second item you want to order = "))
#print("order2")
    if order2 == "Pizza":
        print("Order of Pizza has been added.")
        total = total + 40
    elif order2 == "Pasta":
        print("Order of Pasta has been added.")
        total = total + 50
    elif order2 == "Burger":
        print("Order of Burger has been added.")
        total = total + 60
    elif order2 == "Salad":
        print("Order of Salad has been added.")
        total = total + 70
    else :
        print("Order of Coffee has been added.")
        total = total + 80

print("The total price to pay is", total)