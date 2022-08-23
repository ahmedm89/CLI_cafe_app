############### IMPORTS #####################
from menu import *
from insert_into_db import *
from helper import *
from animation import *
import random
import csv
import matplotlib.pyplot as plt




############### PROUDUCTS FUNCTIONS #####################

#start app functiom
def start_app():
    clear_ter()
    intro()
    logo()
    


# this is the view products List Function
def view_products():
    print('PRODUCTS LIST')
    print('-------------')
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    products = results
    
    print(" {:<8} {:<15} {:<15} {:<15}".format('Id', 'Items','Price', 'stock'))
    print(" {:<8} {:<15} {:<15} {:<15}".format('--', '----','-----','-----'))
    for item in products:
        print(" {:<8} {:<15} {:<15} {:<15}".format(item[0],item[1],item[2],item[3]+'%'))
    print('---------------------------------')
    #print(products)
    connection.commit()
# this the data - V function   


def data_v():
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    list1 = []
    list2 = []
    products = results
    for i in products:
        list1.append(i[1])
        list2.append(i[3])

    
    products = list1
    data = list2
       

    # Creating explode data
    explode = (0.1, 0.0, 0.2, 0.3, 0.0, 0.0,0.1, 0.0, 0.2, 0.3, 0.0, 0.0,0.0)
    
    # Creating color parameters
    colors = ( "orange", "cyan", "brown",
            "grey", "indigo", "beige","red", "purple", "olive",
            "yellow", "navy", "deeppink","lightcoral")
    
    # Wedge properties
    wp = { 'linewidth' :2, 'edgecolor' : "black" }
    

    # Creating plot
    fig, ax = plt.subplots(figsize =(10, 7))
    texts, autotexts = ax.pie(data,
                                    
                                    explode = explode,
                                    labels = products,
                                    shadow = True,
                                    colors = colors,
                                    startangle = 90,
                                    wedgeprops = wp,
                                    textprops = dict(color ="black"))
    
    # Adding legend
    ax.legend( products,
            title ="Products",
            loc ="center right",
            bbox_to_anchor =(1, 0, 0.5, 1))
    
    plt.setp(autotexts, size = 8, weight ="bold")
    ax.set_title("Products Stock Availability")
    
    # show plot
    plt.show()
    






# this is the add products function
def add_products():
    # Genertating order Id
    random_number = random.randint(1,1000)
    #user inputs
    Id = random_number
    Items = input('Enter product name: ').upper()
    Price = (int(input('Enter Price: ')))
    stock = 100
    #inserting a new record into database
    sql = "INSERT INTO products (Id, Items, Price, stock) VALUES (%s, %s, %s, %s)"
    val = (Id , Items, Price, stock)
    clear_ter()
    print('---------------------------------')
    cursor.execute(sql,val)
    connection.commit()
    
# this is the Delete products Function
def delete_products(input):
    print('Delete PRODUCTS')
    print('-------------')
    sql = "DELETE FROM products WHERE Id = %s"
    val = (input,)
    cursor.execute(sql, val)  
    connection.commit()   
    print('---------------------------------')
    

# this is the update options
def product_update_options():
    # options list
    options_list = ['Change product Name','Change product Price','Change product Id','Update stock']
    print('Update Optons')
    print('-------------')
    for indx, option in enumerate(options_list):
        indx += 1
        print(f'{indx}. { option}')
        

            
# this is the Update products Function
def update_products():
    print('Update PROUDCTS')
    print('-------------')
    view_products()
    print()
    user_input = input('Please product Id: ')
    re = "SELECT * FROM products WHERE Id = %s"
    val = (user_input,)
    cursor.execute(re, val)
    connection.commit();
    product = cursor.fetchall()
    #print(product)
    clear_ter()
    #print order
    print(" {:<8} {:<15} {:<15} {:<15}".format('Id', 'Items','Price', 'stock'))
    print(" {:<8} {:<15} {:<15} {:<15}".format('--', '----','-----','-----'))
    for key in product:
        print(" {:<8} {:<15} {:<15}".format(key[0],key[1],key[2],key[3]+'%'))
    print()
    #update options list 
    product_update_options()
    print()
    #prompt options
    user_option = input('What would you like do do? ')
    # change product Name 
    if user_option == '1':
        user_in = input('Enter New value: ')

        sql = " UPDATE  products SET Items = %s  WHERE Id = %s"
        value = (user_in, val)
        cursor.execute(sql,value)
        connection.commit();
    # Change product price
    elif user_option == '2':
        user_in =  int(input('Enter Price: '))
        sql = " UPDATE  products SET Price = %s  WHERE Id = %s"
        value = (user_in, val)
        cursor.execute(sql,value)
        connection.commit();
    # Change product Id ** random
    elif user_option == '3':
        random_id = random.randint(1,1000)
        sql = " UPDATE  products SET Id = %s  WHERE Id = %s"
        value = (random_id, val)
        cursor.execute(sql,value)
        connection.commit();
        #update stock
    elif user_option == '4':
        user_in = input('Enter new stock value')
        sql = " UPDATE  products SET stock = %s  WHERE Id = %s"
        value = (user_in, val)
        cursor.execute(sql,value)
        connection.commit();
    print('---------------------------------')

# This is the Exit the app Function
def exit_app():
    time.sleep(1)
    os.system('cls||clear')

    
# this is the shutdown function
def shutdown():
    clear_ter()
    timer(1)
    print('Saving...')
    timer(1)
    print('Exiting...')
    timer(2)
    exit_app()

############### COURIERS FUNCTIONS #####################
    
# this is the view products List Function
def view_couriers():
    print('COURIERS LIST')
    print('-------------')
    cursor.execute("SELECT * FROM couriers")
    results = cursor.fetchall()
    couriers = results
    print(" {:<8} {:<17} ".format('Id', 'Service'))
    print(" {:<8} {:<17} ".format('--', '-------'))
    for item in couriers:
        print(" {:<8} {:<17} ".format(item[0],item[1]))
    print('-------------------------')
    
   
    
# this is the add couriers function
def add_couriers(): 
    print('ADD COURIERS ')
    print('-------------')
    # Genertating order Id
    random_number = random.randint(1,1000)
    #user inputs
    Id = random_number
    name = input('Enter Courier name: ').upper()
    #inserting a new record into database
    sql = "INSERT INTO couriers (Id, Servicee) VALUES (%s, %s)"
    val = (Id , name)
    clear_ter()
    print('---------------------------------')
    cursor.execute(sql,val)
    connection.commit();
    

    
# check for duplicate ** NOT IN USE **
def check_dublicates(user_input):
    global product_list
    for item in product_list:
        if item == user_input:
            return item
        else:
            break
    
    
# this is the Delete products Function
def delete_couriers(input):
    print('Delete COURIERS')
    print('-------------')
    sql = "DELETE FROM couriers WHERE Id = %s"
    val = (input,)
    cursor.execute(sql, val)  
    connection.commit()
    print('-------------------------')
    


# this is the update options
def couriers_update_options():
    # options list
    options_list = ['Change Courier Name','Change Courier Id']
    print('Update Optons')
    print('-------------')
    for indx, option in enumerate(options_list):
        indx += 1
        print(f'{indx}. { option}')


# this is the Update COURIERS Function
def update_couriers():
    print('Update COURIERS')
    print('-------------')
    view_couriers()
    print()
    user_input = input('Please couriers Id: ')
    
    re = "SELECT * FROM couriers WHERE Id = %s"
    val = (user_input,)
    cursor.execute(re, val)
    connection.commit();
    couriers = cursor.fetchall()
    #print(courier)
    clear_ter()
    #print order
    print(" {:<8} {:<15} ".format('Id', 'Name'))
    print(" {:<8} {:<15} ".format('--', '----'))
    for key in couriers:
        print(" {:<8} {:<15} ".format(key[0],key[1]))
    print()
    #update options list 
    couriers_update_options()
    print()
    #prompt options
    user_option = input('What would you like do do? ')
    # change courier Name 
    if user_option == '1':
        user_in = input('Enter New value: ')
        sql = " UPDATE  couriers SET Servicee = %s  WHERE Id = %s"
        value = (user_in, val)
        cursor.execute(sql,value)
        connection.commit();
    # Change courier's ID
    elif user_option == '2':
        random_id = random.randint(1,1000)
        sql = " UPDATE  couriers SET Id = %s  WHERE Id = %s"
        value = (random_id, val)
        cursor.execute(sql,value)
        connection.commit();
                             
    print('---------------------------------')
        
# get a random courier         
def random_couries():
    cursor.execute("SELECT Servicee FROM couriers")
    results = cursor.fetchall()
    couriers = results
    connection.commit();
    cl = []
    for i in couriers:
        cl.append(i)
    random_courier = random.choice(cl)
    cl.clear()
    return random_courier
        
###################### ORDERS #####################

#view orders
def view_orders():
    clear_ter()
    cursor.execute("SELECT * FROM orders")
    results = cursor.fetchall()
    orders = results
    clear_ter()
    # lable
    print("{:<6} {:<12} {:<12} {:<12}   {:<30} {:<25} {:<25} {:<8}  {:<13}  {:<13} ".format('Id','First Name', 'Last Name','Phone Number','Email','Address','cart','total','Couriers','Status'))
    #under line lable
    print("{:<6} {:<12} {:<12} {:<12}   {:<30} {:<25} {:<25} {:<8}  {:<13}  {:<13} ".format('--','----------', '---------','------------','-----',  '-------','-----','-----','--------','------'))
    # print orders in table formate
    for order in orders:
        print("{:<6} {:<12} {:<12} {:<12}   {:<30} {:<25} {:<25} {:<8}  {:<13}  {:<13} ".format(order[0],order[1],order[2],order[3],order[4],order[5],order[6],order[7],order[8],order[9]))
    connection.commit();   

# view an order
def view_an_order(u_i):
    clear_ter()
    re = "SELECT * FROM orders WHERE Id = %s"
    val = (u_i,)
    cursor.execute(re, val)
    connection.commit();
    orders = cursor.fetchall()
    for order in orders:
        print('* Order Id     : '+str(order[0]))
        print('* First Name   : '+str(order[1]))
        print('* Last Name    : '+str(order[2]))
        print('* Phone Number : '+str(order[3]))
        print('* Email        : '+str(order[4]))
        print('* Address      : '+str(order[5]))
        print('* Cart         : '+str(order[6]))
        print('* Total        : '+str(order[7]))
        print('* Couriers     : '+str(order[8]))
        print('* Status       : '+str(order[9]))
              
#export orders
def export_orders():
    # Export data into CSV file
    clear_ter()
    print ("Exporting data into CSV............")
    cursor.execute("SELECT * FROM orders")
    results = cursor.fetchall()
    with open("orders_data.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)
       
        csv_writer.writerows(results)
    dirpath = os.getcwd() + "/orders_data.csv"
    print ("Data exported Successfully into {}".format(dirpath))

              
# add order function
def add_order():
    clear_ter()
    prompt_user = input('Press[N] for New Customer or press[E] for An Existing: ').upper()
    clear_ter()
    ## New customer ##
    if prompt_user == 'N':
        # Genertating order Id
        random_number = random.randint(1,10000)
        Id = random_number
        first_name = input('Enter first name: ')
        clear_ter()
        last_name = input('Enter last name: ')
        clear_ter()
        phone_number = input('Enter phone number: ')
        clear_ter()
        email = input('Enter Email : ')
        clear_ter()
        address = input('enter adderss: ')
        clear_ter()
        # products
        view_products()
        input_list = list(map(str,input('please Enter the product Id you would like to add:  ').split()))
        #CART
        string = ' '.join([str(item) for item in input_list])
        cart = string
        clear_ter()
        # updating TOTAL
        cursor.execute("SELECT * FROM products")
        results = cursor.fetchall()
        connection.commit()
        products = results;
        t = 0
        for p in products:
            for i in input_list:
                if int(i) == p[0]:
                    t += p[2]
                    #updating stock
                    s = 0
                    s += int(p[3]) 
                    s -= 1
                    s = str(s)
                    sql = " UPDATE  products SET stock = %s  WHERE Id = %s"
                    value = (s ,p[0])
                    cursor.execute(sql,value)
                    connection.commit();
        # Total
        t = float(t)
        total = f'£{t}0' 
        # Adding COURIERS 
        couriers = random_couries()
        # Adding STATUS
        Status = 'Pending'
        clear_ter()
        # adding Object ** order
        sql = "INSERT INTO orders (Id, First_name, Last_name,Phone_number, Email, ad, cart, total, Couriers,st) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
        val = (Id , first_name, last_name,phone_number, email, address, cart, total, couriers, Status)
        cursor.execute(sql,val)
        connection.commit();
    ## Existing customer ##   
    elif prompt_user == 'E': 
        clear_ter()   
        view_customers()
        print()
        user_input = input('Please Enter Order Id: ')
        re = "SELECT * FROM customers WHERE Id = %s"
        val = (user_input,)
        cursor.execute(re, val)
        connection.commit();
        customers = cursor.fetchall()
        for customer in customers:
            Id = customer[0]
            first_name = customer[1]
            last_name = customer[2]
            phone_number = customer[3]
            email = customer[4]
            address = customer[5]
        clear_ter()
        view_products()
        input_list = list(map(str,input('please Enter the product Id you would like to add:  ').split()))
        #CART
        string = ' '.join([str(item) for item in input_list])
        cart = string
        clear_ter()
        # updating TOTAL
        cursor.execute("SELECT * FROM products")
        results = cursor.fetchall()
        connection.commit()
        products = results;
        t = 0
        for p in products:
            for i in input_list:
                if int(i) == p[0]:
                    t += p[2]
                    #updating stock
                    s = 0
                    s += int(p[3]) 
                    s -= 1
                    s = str(s)
                    sql = " UPDATE  products SET stock = %s  WHERE Id = %s"
                    value = (s ,p[0])
                    cursor.execute(sql,value)
                    connection.commit();
        # Total
        t = float(t)
        total = f'£{t}0' 
        # Adding COURIERS 
        couriers = random_couries()
        # Adding STATUS
        Status = 'Pending'
        clear_ter()
        # adding Object ** order
        sql = "INSERT INTO orders (Id, First_name, Last_name,Phone_number, Email, ad, cart, total, Couriers,st) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
        val = (Id , first_name, last_name,phone_number, email, address, cart, total, couriers, Status)
        cursor.execute(sql,val)
        connection.commit();
            

        
# update order function
def update_order():
    view_orders()
    print()
    user_input = input('Please Enter Order Id: ')
    re = "SELECT * FROM orders WHERE Id = %s"
    val = (user_input,)
    cursor.execute(re, val)
    connection.commit();
    orders = cursor.fetchall()
    clear_ter()
    
    print("{:<6} {:<12} {:<12} {:<12}   {:<30} {:<25} {:<25} {:<8}  {:<13}  {:<13} ".format('Id','First Name', 'Last Name','Phone Number','Email','Address','cart','total','Couriers','Status'))
    #under line lable
    print("{:<6} {:<12} {:<12} {:<12}   {:<30} {:<25} {:<25} {:<8}  {:<13}  {:<13} ".format('--','----------', '---------','------------','-----',  '-------','-----','-----','--------','------'))
    for order in orders:
        print("{:<6} {:<12} {:<12} {:<12}   {:<30} {:<25} {:<25} {:<8}  {:<13}  {:<13} ".format(order[0],order[1],order[2],order[3],order[4],order[5],order[6],order[7],order[8],order[9]))
        print()
    
    #update options list funciton 
    update_options()
    print()
    #prompt options
    user_option = input('What would you like do do? ')
    #First Name 
    if user_option == '1':
        user_in = input('Enter New value: ')
        sql = " UPDATE  orders SET First_name = %s  WHERE Id = %s"
        value = (user_in, val)
        cursor.execute(sql,value)
        connection.commit();
    #Last Name
    elif user_option == '2':
        user_in = input('Enter New value: ')
        sql = " UPDATE  orders SET Last_name = %s  WHERE Id = %s"
        value = (user_in, val)
        cursor.execute(sql,value)
        connection.commit();
    #Phone Number
    elif user_option == '3':
        user_in = input('Enter New value: ')
        sql = " UPDATE  orders SET Phone_number = %s  WHERE Id = %s"
        value = (user_in, val)
        cursor.execute(sql,value)
        connection.commit();
    #Email
    elif user_option == '4':
        user_in = input('Enter New value: ')
        sql = " UPDATE  orders SET Email = %s  WHERE Id = %s"
        value = (user_in, val)
        cursor.execute(sql,value)
        connection.commit();
    #Address
    elif user_option == '5':
        user_in = input('Enter New value: ')
        sql = " UPDATE  orders SET ad = %s  WHERE Id = %s"
        value = (user_in, val)
        cursor.execute(sql,value)
        connection.commit();
    #Couries
    elif user_option == '6':
        #Generating a Courier
        
        print('choosing another courier')
        timer(3)
        sql = " UPDATE  orders SET Couriers = %s  WHERE Id = %s"
        r = random_couries()
        value = (r,val)
        cursor.execute(sql,value)
        connection.commit();         
    #status
    elif user_option == '7':
        clear_ter()
        print('Status Optons')
        print('-------------')
        print()
        order_status = ['Pending', 'preparing','Dispatched']
        for indx, option in enumerate(order_status):
            indx += 1
            print(f'{indx}. { option}')
        print()   
        user_in = input('Enter Status: ')
        #status options
        if user_in == '1':
            sql = " UPDATE  orders SET st = %s  WHERE Id = %s"
            user_in = order_status[0]
            value = (user_in, val)
            cursor.execute(sql,value)
            connection.commit();
            
        elif user_in == '2':
            sql = " UPDATE  orders SET st = %s  WHERE Id = %s"
            user_in = order_status[1]
            value = (user_in, val)
            cursor.execute(sql,value)
            connection.commit();
            
        elif user_in == '3':
            sql = " UPDATE  orders SET st = %s  WHERE Id = %s"
            user_in = order_status[2]
            value = (user_in, val)
            cursor.execute(sql,value)
            connection.commit();                         
            
# the update options list function     
def update_options():
    # options list
    options_list = ['First Name','Last Name','Phone Number','Email', 'Address' , 'Couriers', 'status']
    print('Update Optons')
    print('-------------')
    for indx, option in enumerate(options_list):
        indx += 1
        print(f'{indx}. { option}')
                    
                        
# #this is the delete order funtion
def delete_order(input):
    sql = "DELETE FROM orders WHERE Id = %s"
    val = (input,)
    cursor.execute(sql, val)  
    connection.commit()
        

###################### customers #####################

# This is the view customer Function
def view_customers():
    clear_ter()
    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
    customers = results
    clear_ter()
    #lable
    print("{:<6} {:<12} {:<12} {:<12}   {:<30} {:<25}  ".format('Id','First Name', 'Last Name','Phone Number','Email','Address'))
    #under line lable
    print("{:<6} {:<12} {:<12} {:<12}   {:<30} {:<25}  ".format('--','----------', '---------','------------','-----',  '-------'))
    #print customers in a table formate
    for customer in customers:
         print("{:<6} {:<12} {:<12} {:<12}   {:<30} {:<25}  ".format(customer[0],customer[1],customer[2],customer[3],customer[4],customer[5]))
    connection.commit()
    
#this is the  view a customer functon
def view_a_customer(u_i):
    clear_ter()
    re = "SELECT * FROM customers WHERE Id = %s"
    val = (u_i,)
    cursor.execute(re, val)
    connection.commit();
    customers = cursor.fetchall()
    for customer in customers:
        print('* Customer Id     : '+str(customer[0]))
        print('* First Name      : '+str(customer[1]))
        print('* Last Name       : '+str(customer[2]))
        print('* Phone Number    : '+str(customer[3]))
        print('* Email           : '+str(customer[4]))
        print('* Address         : '+str(customer[5]))
        
# export customers
def export_customers():
    ## Export data into CSV file
    clear_ter()
    print ("Exporting data into CSV............")
    
    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
    with open("customers_data.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        
        csv_writer.writerows(results)
    dirpath = os.getcwd() + "/customers_data.csv"
    print ("Data exported Successfully into {}".format(dirpath))
      
#this is the add customer function
def add_customer():
    clear_ter()
    # Genertating order Id
    random_number = random.randint(1,10000)
    Id = random_number
    first_name = input('Enter first name: ')
    clear_ter()
    last_name = input('Enter last name: ')
    clear_ter()
    phone_number = input('Enter phone number: ')
    clear_ter()
    email = input('Enter Email : ')
    clear_ter()
    address = input('enter adderss: ')
    clear_ter()
    # adding Object ** customer
    sql = "INSERT INTO customers (Id, First_name, Last_name,Phone_number, Email, ad) VALUES (%s, %s,%s, %s,%s, %s)"
    val = (Id , first_name, last_name,phone_number, email, address)
    cursor.execute(sql,val)
    connection.commit();
    
#this is the update options list function * for customers   
def update_customers_options():
    # options list
    options_list = ['First Name','Last Name','Phone Number','Email','Address']
    print('Update Optons')
    print('-------------')
    for indx, option in enumerate(options_list):
        indx += 1
        print(f'{indx}. { option}') 
           
# this is the update customer function
def update_customers():
    view_customers()
    print()
    user_input = input('Please Enter Customer Id: ')
    re = "SELECT * FROM customers WHERE Id = %s"
    val = (user_input,)
    cursor.execute(re, val)
    connection.commit();
    customers = cursor.fetchall()
    clear_ter()
    # lable ** name fields
    print("{:<6} {:<12} {:<12} {:<12}   {:<30} {:<25}  ".format('Id','First Name', 'Last Name','Phone Number','Email','Address'))
    #under line lable
    print("{:<6} {:<12} {:<12} {:<12}   {:<30} {:<25}  ".format('--','----------', '---------','------------','-----',  '-------'))
    #print customers in a table formate
    for customer in customers:
         print("{:<6} {:<12} {:<12} {:<12}   {:<30} {:<25}  ".format(customer[0],customer[1],customer[2],customer[3],customer[4],customer[5]))
    #update options list funciton ** for customers
    update_customers_options()
    print()
    user_option = input('What would you like do do? ')
    #First Name 
    if user_option == '1':
        user_in = input('Enter New value: ')
        sql = " UPDATE  customers SET First_name = %s  WHERE Id = %s"
        value = (user_in, val)
        cursor.execute(sql,value)
        connection.commit();
    #Last Name
    elif user_option == '2':
        user_in = input('Enter New value: ')
        sql = " UPDATE  customers SET Last_name = %s  WHERE Id = %s"
        value = (user_in, val)
        cursor.execute(sql,value)
        connection.commit();
    #Phone Number
    elif user_option == '3':
        user_in = input('Enter New value: ')
        sql = " UPDATE  customers SET Phone_number = %s  WHERE Id = %s"
        value = (user_in, val)
        cursor.execute(sql,value)
        connection.commit();
    #Email
    elif user_option == '4':
        user_in = input('Enter New value: ')
        sql = " UPDATE  customers SET Email = %s  WHERE Id = %s"
        value = (user_in, val)
        cursor.execute(sql,value)
        connection.commit();
    #Address
    elif user_option == '5':
        user_in = input('Enter New value: ')
        sql = " UPDATE  customers SET ad = %s  WHERE Id = %s"
        value = (user_in, val)
        cursor.execute(sql,value)
        connection.commit();

# #this is the delete customer funtion
def delete_customer(input):
    sql = "DELETE FROM customers WHERE Id = %s"
    val = (input,)
    cursor.execute(sql, val)  
    connection.commit()