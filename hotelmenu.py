# define the menu of restro
menu = {
    'Pizza': 40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Cofee':80,

}
#Greet
print("Welcome to python restro!!!")
print("Pizza : Rs40\nPasta : Rs50\nBurger : Rs60\nSalad : Rs70\nCofee : Rs80")

order_total = 0

item_1 = input("Enter the name of item you want to order! =")
if item_1 in menu:        #membership operator is used
    order_total += menu[item_1]
    print(f"Your item{item_1} has been added in your order")

else:
    print(f"Ordered item{item_1} not available yet")

another_order = input("DO you want to add another item ?(Yes/No):")
if another_order == "Yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item{item_2}has been added to order")
    else:
        print(f"Ordered item{item_2}is not available!")

another_order = input("DO you want to add another item ?(Yes/No):")
if another_order == "Yes":
     item_3 = input("Enter the name of Third item =")
     if item_3 in menu:
         order_total += menu[item_3]
         print(f"Item{item_3}has been added to order")
     else:
         print(f"Ordered item{item_2}is not available!")
    
    
print(f"Your total amount of items to pay is{order_total}")            
