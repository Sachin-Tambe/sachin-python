def welcome_user():
    print("Welcome to the King Of Cafe !")
def show_menu():
    menu = {
        1 :("Coffie", 300),
        2 :('Tea', 200),
        3 :('Milk', 100),
        4 :('Juice', 150),
        5 :('Burger', 250),
        6 :('Pizza', 350),
        7 :('Sandwich', 200),
        8 :('Pasta', 300),
        9 :('Noodles', 250),
        10 :('French Fries', 150),
        11 :('Chicken', 250),
        12 :('Fish', 300),
        13 :('Rice', 150),
        14 :('Biryani', 250)
    }
    print("Menu")
    for key , value in menu.items():
        item_price , item_value = value
        print(f"{key}:{item_price} - {item_value}")
    chooise = int(input("Please Enter Your Choise As Per Dish Number "))
    if chooise in menu.keys():
        item_price , item_value = menu[chooise]
        print(f"Good Choise sir , You choice := {menu[chooise]}")
        quantity = int(input("The No Of Quantity You Want Sir ?"))
        total_price = item_value * quantity
        print(total_price)

show_menu()