print("Menu of restaurant")
menu = {
    "Nepali": 'Koda ko roti',
    "Nepali": 'Makkai ko roti',
    'Chinese1': "Chaumin",
    'Chinese2': "Noodles",
    "English1":'Burgur',
    "English2": 'Pizza',
}
for key in menu:
   print(key,menu[key],sep=" : ")
customer_order ={}
current_choice= None
while current_choice != "0":
    if current_choice in menu:
        order = menu[current_choice]
        if current_choice in customer_order:
         print("Removing order from list")
         del customer_order[current_choice]
        else:
            print("Adding item to order")
            customer_order[current_choice]=order
            print("Customer order is: ")
            print(customer_order)
    current_choice=input(">Enter your order: ")