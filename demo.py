def addhar_update():
    add_num =  int(input("enter Adhar number "))
    name = input("enter yor name ")
    b_date =  int(input("enter your birth date "))
    add= input("enter your address")
    m_num =  int(input("enter your mobile number "))
    email = (input("enter your email"))

    print("your information saved sucessfully")

    print("please verify your information")
    print("address := " , add_num)
    print("name := " , )


def Tea_recommender():
    # welcome 
    print("hello sir welcome to the Mumbai || which is world famous for the vada-pav ")
    # get the name 
    name = input("what is your good name sir")
    # greeting the with name 
    print("hello" , name , "welcome to the mumbai")
    # get the buget 
    vada_pav_buget = int(input("What is Your Buget for the vada-pav"))
    if vada_pav_buget >= 500 :
        print("Dear" , name , "Go To The Taj restaurant ")
    elif vada_pav_buget  >= 300 and vada_pav_buget  < 500 :
        print("Dear" , name , "Go To The Jw Maritoo restaurant")
    elif vada_pav_buget  >= 100 and vada_pav_buget  < 300 :
        print("Dear" , name , "Go To The udipi restaurant")
    elif vada_pav_buget  >= 20 and vada_pav_buget  < 100 :
        print("Dear" , name , "Go To The any thela or Tapri")
    else :
        print("Dear" , name , "You Need At Least 20Rs Buget ")

def laptop_recomender():
    
    print("welcome to our store || which  is the famous for the laptops and  mobiles ")
    name =  input(("Enter your good name here := "))
    print("good morning " , name )
    choise =  int(input("For See Laptops Enter 1 and For See mobiles Enter 2 "))
    if choise == 1 :
        print("here are some laptops ")
        buget =  int(input("Enter your Buget For Laptop B/W 30,000 to 2,00000"))
        if buget > 150000 :
            print("here a some good laptops in this buget")
            print("HP VICTUS ")
            print("Apple MAC Book Pro ")
        elif buget >= 100000 and buget < 150000 :
            print("here a some good laptops in this buget")
            print("Dell pro")
            print("Apple MAC Book")
        elif buget >=  30000 and buget < 100000 :
            print("here a some good laptops in this buget")
            print("HP fjri ")
            print("lenevo ")
        else :
            print("there are no laptop availble in this buget")
    elif choise   == 2  :
         print("here are some Mobiles ")
         buget =  int(input("Enter your Buget For Laptop B/W 30,000 to 2,00000"))
         if buget > 150000 :
             print("here a some good mobiles in this buget")
             print("s24 ultra")
             print("Applei phone 14 ")
         elif buget >= 100000 and buget < 150000 :
             print("here a some good mobiles in this buget")
             print("s23 ultra")
             print("Apple iphone 13 ")
         elif buget >=  30000 and buget < 100000 :
             print("here a some good mobile in this buget")
             print("realme narzo 20 pro ")
             print("i phone 6 ")
         else :
             print("thNere are no mobiles availble in this buget")
    else : 
         print("you not choise write option ")

def head_tail_game():
    
    import random 
    print("Hello sir Welcome to Head and Tails Game")
    user_Choise =  input("Enter Your CHoise Head Or Tails")
    user_Choise.title()
    print("You Chose ",  user_Choise.title() )

    if random.choice('ht') == 'h' :
        result = 'head' 
    else :
        result = 'tail'

    print("Result Is " , result) 

    if user_Choise.lower() == result.lower() :
        print("You Win")
    else :
        print("You Lose")





def dise_game():
    #welcome the user 
    print("Hello , Welcome To The Dise Roll Game ")
    #Enter Your Prediction 
    user_input = int(input("Enter The Number B/W 1-6 For Dise Roll "))
    print("You Chose "  , user_input)
    #dise roll 

    import random
    result =  random.randrange(1,6)
    print("Result IS " , result )

    #result
    if user_input == result :
        print("You win ")
    else :
        print("You Lose")



def double_dise_game():
    #welcome the user 
    print("Hello , Welcome To The Dise Roll Game ")
    #Enter Your Prediction 
    user_input1 = int(input("Enter The Number B/W 1-6 For First Dise Roll "))
    print("You Chose For First Dise "  , user_input1) 
    user_input2 = int(input("Enter The Number B/W 1-6 For Second Dise Roll "))
    print("You Chose For Second Dise "  , user_input2) 
    #dise roll 

    import random
    result_FirstDise =  random.randrange(1,6)
    print("Result  For First Dise " , result_FirstDise )
    result_SecondDise =  random.randrange(1,6)
    print("Result For Second Dise  " , result_SecondDise )
    #result
    result = result_FirstDise + result_SecondDise
    if user_input1 + user_input2  == result :
        print("You win ")
    else :
        print("You Lose")

def multiplication_tabel():
    print("hello  , Welcome Sir")
    multiplication_tabel = int(input("Enter a Number To print The Tabel "))
    for i in range(1 , 11) :
        print(multiplication_tabel  , 'X' , i  , '=' , multiplication_tabel* i )

def cude_of_number():
    print("hello  , Welcome Sir")
    input_num  = int(input("Enter a Number To print The factorial  "))
    result = 1 
    for i in range(1 ,  input_num+1  ) :
        result = result * i 
    print('factorial of the ' , input_num , 'is' ,  result)
    result = 1  




import random 
import string
def password_creater():
    import random 
    import string
    name = random.choices('0123456789', k=3)
    #print(name)
    capitals = random.choices(string.ascii_uppercase , k=1)
    #print(capitals)
    lower = random.choices(string.ascii_lowercase , k=6)
    #print(lower)
    special_char = random.choices(string.punctuation , k=2) 
    #print(special_char)
    password = (name + capitals + lower + special_char)
    random.shuffle(password)
    passw ="".join(password) 

    print(passw)

def password_generator():    
    user_password = input("Enter a Password")
    is_smalCase = False 
    is_uppercase = False 
    is_special = False 
    is_number  = False 
    special = string.punctuation
    if len(user_password) >= 12 :
        is_smalCase = any(char.isupper() for char in user_password)
        print(is_smalCase)
        is_uppercase = any(char.islower() for char in user_password)
        print(is_uppercase)
        is_number = any(char.isdigit() for char in user_password)
        print(is_number)
        is_special = any(char in special for char in user_password)
        print(is_special)

    else :
        print('Password Length Must Be Greater Than 12')


    if is_smalCase and is_uppercase and is_special and is_number :
        print("Pasword Meet Requirement")
    else :
        print("password is incorrect")
        print("You can use Following password " ,password_creater() )
        


def fabinoci():
    
    number =  int(input("Enter a Number To Find The Fabinoci "))

    f_num = 0 
    l_num = 1 
    result = 0 

    for i in range(number)  :
        print(f_num)
        result = f_num + l_num
        f_num = l_num 
        l_num = result 

def factorial():
    print("hello  , Welcome Sir")
    input_num  = int(input("Enter a Number To print The factorial  "))
    result = 1 
    for i in range(1 ,  input_num+1  ) :
        result = result * i 
    print('factorial of the ' , input_num , 'is' ,  result)
    result = 1  




import time 
def coundown():
    minites = int(input("enter a number of minites "))
    seconds = int(input("enter a number of seconds "))
    total_second =  minites * 60 + seconds 
    for i in range (total_second , 0 ,-1)  :
        minis = i // 60 
        secs = i % 60 
        timer_display = '{:02d}:{:02d}'.format(minis , secs)
        print(timer_display , end='\r')
        time.sleep(1)

    print("time up")
    

import tkinter as tk

window = tk.Tk()  # Create a Tkinter window
window.title("Sachin Python Project")
window.geometry('1000x1000')
tk.Label(window, text="Python Project List", font=('Calisto MT', 30, 'bold')).place(x=390, y=100)
tk.Label(window, text="Made By Sachin Tambe", font=('Calisto MT', 15, 'bold')).place(x=450, y=160)


tk.Button(window,text="Addhar_Update",font=('Calisto MT',15),command=addhar_update).place(x=100,y=200,height=100,width=200)
tk.Button(window,text="Tea_recommender",font=('Calisto MT',15),command=Tea_recommender).place(x=425,y=200,height=100,width=200)
tk.Button(window,text="laptop_recomender",font=('Calisto MT',15),command=laptop_recomender).place(x=750,y=200,height=100,width=200)

tk.Button(window,text="head_tail_game",font=('Calisto MT',15),command=head_tail_game).place(x=100,y=350,height=100,width=200)
tk.Button(window,text="dise_game",font=('Calisto MT',15),command=dise_game).place(x=425,y=350,height=100,width=200)
tk.Button(window,text="double_dise_game",font=('Calisto MT',15),command=double_dise_game).place(x=750,y=350,height=100,width=200)

tk.Button(window,text="multiplication_tabel",font=('Calisto MT',15),command=multiplication_tabel).place(x=100,y=500,height=100,width=200)
tk.Button(window,text="cude_of_number",font=('Calisto MT',15),command=cude_of_number).place(x=425,y=500,height=100,width=200)
tk.Button(window,text="password_generator",font=('Calisto MT',15),command=password_generator).place(x=750,y=500,height=100,width=200)

tk.Button(window,text="fabinoci",font=('Calisto MT',15),command=fabinoci).place(x=100,y=650,height=100,width=200)
tk.Button(window,text="factorial",font=('Calisto MT',15),command=factorial).place(x=425,y=650,height=100,width=200)
tk.Button(window,text="coundown",font=('Calisto MT',15),command=coundown).place(x=750,y=650,height=100,width=200)
window.mainloop()  # Enter the Tkinter event loop
