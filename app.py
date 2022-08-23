############### IMPORTS #####################
from animation import *
from menu import *
from functions import *
from helper import *





################ FUNCTIONALITY ##############


#start app
start_app()

### Main Menu ###
main_loop = 1
while main_loop == 1:
    print(main_menu)
    user_input = input('Enter Choice: ').upper()
    # Exting app
    if user_input == 'P':
        main_menu_sub_loop = 1
        while main_menu_sub_loop == 1:
            user_in = input('ARE YOU SURE YOU WANT TO LEAVE [Y : N] ').upper()
            if user_in  == 'Y':
                shutdown()
                main_menu_sub_loop = 0
                main_loop = 0
                # return to main menu
            elif user_in == 'N':
                  main_menu_sub_loop = 0
                  main_loop = 1
                  clear_ter()
                  returning_to_main()
                
            else:
                print('Invalid Choice')
                main_menu_sub_loop = 1 
        
     ## products menu ##
    elif user_input == 'M':
        clear_ter()
        loading_products_menu_screen()
        new_loop = 1
        while new_loop == 1:
                clear_ter()
                print(products_menu)
                user_input = input('Enter Choice: ').upper()
                
                # View Products List
                sub_loop = 1
                while sub_loop == 1:
                    if user_input == 'A':
                        clear_ter()
                        #print(product_list)
                        view_products()
                        print()
                        #Question
                        sub_loop1 = 1
                        while sub_loop1:
                            user_input = input('Press [V] for stock data-v or press [R] To Return to Products Menu: ').upper()
                            #Data -v
                            if user_input == 'V':
                                sub_loop1 =1
                                sub_loop = 0
                                new_loop = 0
                                clear_ter() 
                                data_v()
                            elif user_input == 'R':
                                #Return to Products menu
                                sub_loop1 = 0
                                sub_loop = 0
                                new_loop = 1
                                clear_ter()
                                returning_to_prodducts_menu()
                                
                            else:
                                print('Invalid Input')
                                sub_loop1 = 1
                        
                    #Add Products
                    elif user_input == 'B':
                            clear_ter()
                            view_products()
                           # user_input = input('Enter Value You Would Like to [Add]: ').upper()
                            timer(3)
                            clear_ter()
                            add_products()
                            clear_ter()
                            updating_an()
                            view_products()
                            #Question
                            sub_loop2 = 1
                            while sub_loop2 == 1:
                                user_in = input('Press [A] To Add another [R] To Return to Products Menu: ').upper()
                                if user_in == 'A':
                                    #user_input = input('Enter Value: ').upper()
                                    clear_ter()
                                    add_products()
                                    updating_an()
                                    clear_ter()
                                    view_products()
                                    sub_loop2 = 1
                                #Return to Products menu
                                elif user_in == 'R':
                                    sub_loop2 = 0
                                    sub_loop = 0
                                    new_loop = 1
                                    clear_ter()
                                    returning_to_prodducts_menu()
                                    
                                else:
                                    print('Invalid Input')
                                    sub_loop2 = 1
                        
                    #UPDATE PRODUCTS
                    elif user_input == 'C':
                        clear_ter()
                        #view_products()
                        #original_val = input('Enter Original Value You would Like to [Update]: ').upper()
                        #new_val = input('Enter new Value: ').upper()
                        update_products()
                        clear_ter()
                        updating_an()
                        view_products()
                        #Question
                        sub_loop3 = 1
                        while sub_loop3 == 1:
                                user_in = input('Press [E] To Edit another [R] To Return to Products Menu: ').upper()
                                if user_in == 'E':
                                    #original_val = input('Enter Original Value You would Like to [Update]: ').upper()
                                    #new_val = input('Enter new Value: ').upper()
                                    clear_ter()
                                    update_products()
                                    updating_an()
                                    view_products()
                                    sub_loop3 = 1
                                #Return to Products menu
                                elif user_in == 'R':
                                    sub_loop3 = 0
                                    sub_loop = 0
                                    new_loop = 1
                                    clear_ter()
                                    returning_to_prodducts_menu()
                                    
                                else:
                                    print('Invalid Input')
                                    sub_loop3 = 1
                        
                    #DELETE PRODUCTS
                    elif user_input == 'D':
                        clear_ter()
                        view_products()
                        user_input = input('Enter Value You Would Like to [Delete]: ').upper()
                        delete_products(user_input)
                        clear_ter()
                        updating_an()
                        view_products()
                        #Question
                        sub_loop4 = 1
                        while sub_loop4 == 1:
                                user_in = input('Press [D] To Delete another [R] to Return To Products Menu: ').upper()
                                if user_in == 'D':
                                    clear_ter()
                                    view_products()
                                    user_input = input('Enter Value You Would Like to [Delete]: ').upper()
                                    delete_products(user_input)
                                    clear_ter()
                                    updating_an()
                                    sub_loop4 = 1
                                #Return to Products menu
                                elif user_in == 'R':
                                    sub_loop4 = 0
                                    sub_loop = 0
                                    new_loop = 1
                                    clear_ter()
                                    returning_to_prodducts_menu()
                                    sub_loop4 = 0
                    
                    #Return to Main menu
                    elif user_input == 'E':
                        clear_ter()
                        returning_to_main()
                        
                        sub_loop = 0
                        new_loop = 0
                    else:
                        print('Invalid Input')
                        sub_loop = 0
                        main_loop = 1
                        clear_ter()
                        returning_to_main()
          ##################### END ##############################
    
    ## couriers menu ##
    elif user_input == 'O':
        clear_ter()
        loading_couriers_menu_screen()
        new_loop2 = 1
        while new_loop2 == 1:
                clear_ter()
                print(couriers_menu)
                user_input = input('Enter Choice: ').upper()
                # View couriers List
                sub_loop = 1
                while sub_loop == 1:
                    if user_input == 'A':
                        clear_ter()
                        view_couriers()
                        print()
                        #Question
                        sub_loop1 = 1
                        while sub_loop1 == 1:
                            user_input = input('Press [R] To Return to Couriers Menu: ').upper()
                            #Return to couriers menu
                            if user_input == 'R':
                                sub_loop1 = 0
                                sub_loop = 0
                                new_loop2 = 1
                                clear_ter()
                                returning_to_couriers_menu()
                            else:
                                print('Invalid Input')
                                sub_loop1 = 1
                        
                    #Add couriers
                    elif user_input == 'B':
                            clear_ter()
                            view_couriers()

                            add_couriers()
                            clear_ter()
                            updating_an()
                            view_couriers()
                            #Question
                            sub_loop2 = 1
                            while sub_loop2 == 1:
                                user_in = input('Press [A] To Add another [R] To Return to Couriers Menu: ').upper()
                                if user_in == 'A':
                                   
                                    clear_ter()
                                    updating_an()
                                    add_couriers()
                                    sub_loop2 = 1
                                #Return to Couriers menu
                                elif user_in == 'R':
                                    sub_loop2 = 0
                                    sub_loop = 0
                                    new_loop2 = 1
                                    clear_ter()
                                    returning_to_couriers_menu()
                                else:
                                    print('Invalid Input')
                                    sub_loop2 = 1
                        
                    #UPDATE COURIERS
                    elif user_input == 'C':
                        clear_ter()
                        update_couriers()
                        clear_ter()
                        updating_an()
                        clear_ter()
                        view_couriers()
                        #Question
                        sub_loop3 = 1
                        while sub_loop3 == 1:
                                user_in = input('Press [E] To Edit another [R] to Return To Couriers Menu: ').upper()
                                if user_in == 'E':
                                    update_couriers()
                                    updating_an()
                                    clear_ter()
                                    view_couriers()
                                    sub_loop3 = 1
                                #Return to Couriers menu
                                elif user_in == 'R':
                                    sub_loop3 = 0
                                    sub_loop = 0
                                    new_loop2 = 1
                                    clear_ter()
                                    returning_to_couriers_menu()
                                else:
                                    print('Invalid Input')
                                    sub_loop3 = 1
                        
                    #DELETE COURIERS
                    elif user_input == 'D':
                        clear_ter()
                        view_couriers()
                        user_input = input('Enter Id of courier You Would Like To [Delete]: ').upper()
                        delete_couriers(user_input)
                        clear_ter()
                        updating_an()
                        view_couriers()
                        #Question
                        sub_loop4 = 1
                        while sub_loop4 == 1:
                                user_in = input('Press [D] To Delete another [R] To Return to Couriers Menu: ').upper()
                                if user_in == 'D':
                                    clear_ter()
                                    view_couriers()
                                    user_input = input('Enter Value You Would Like to [Delete]: ').upper()
                                    updating_an()
                                    delete_couriers(user_input)
                                    clear_ter()
                                    view_couriers()
                                    sub_loop4 = 1
                                #Return to Couriers menu
                                elif user_in == 'R':
                                    sub_loop4 = 0
                                    sub_loop = 0
                                    new_loop2 = 1
                                    clear_ter()
                                    returning_to_couriers_menu()
                                else:
                                    print('Invalid Input')
                                    sub_loop4 = 1
                    
                    #Return to Main menu
                    elif user_input == 'E':
                        clear_ter()
                        returning_to_main()
                        sub_loop = 0
                        new_loop2 = 0
                        main_loop = 1
                    else:
                        print('Invalid Input')
                        sub_loop = 0
                        main_loop = 1
                        clear_ter()
                        print('INVALID INPUT!!! Returning to the main menu?...')
                        timer(2)
                        returning_to_main()
            ##################### END ##############################
    ## Orders menu ##
    elif user_input == 'K':
        clear_ter()
        loading_orders_menu_screen()
        new_loop3 = 1
        while new_loop3 == 1:
                clear_ter()
                print(orders_menu)
                user_input = input('Enter Choice: ').upper()
                # View orders List
                sub_loop = 1
                while sub_loop == 1:
                    if user_input == 'A':
                        clear_ter()
                        view_orders()
                        print()
                        #Question
                        sub_loop1 = 1
                        while sub_loop1 == 1:
                            print()
                            user_input = input('Press [A] to View an Order Press [E] To Export Orders Or [R] To Return to Orders Menu: ').upper()
                            #veiw an order
                            if user_input == 'A':
                                clear_ter()
                                view_orders()
                                sub_loop1 = 1
                                sub_loop = 0
                                new_loop3 = 0
                                print()
                                u_i = input('Please Enter Order Id: ')
                                view_an_order(u_i)
                                # export orders
                            elif user_input == 'E':
                                clear_ter()
                                view_orders()
                                sub_loop1 = 1
                                sub_loop = 0
                                new_loop3 = 0
                                print()
                                export_orders()
                            elif user_input == 'R':
                                sub_loop1 = 0
                                sub_loop = 0
                                new_loop3 = 1
                                clear_ter()
            
                                returning_to_orders_menu()
                            else:
                                print('Invalid Input')
                                sub_loop1 = 1     
                    #Add orders
                    elif user_input == 'B':
                            clear_ter()
                            view_orders()
                            timer(3)
                            add_order()
                            clear_ter()
                            updating_an()
                            view_orders()
                            #Question
                            sub_loop2 = 1
                            while sub_loop2 == 1:
                                print()
                                user_in = input('Press [A] To Add another [R] To Return to Orders Menu: ').upper()
                                if user_in == 'A':
                                    clear_ter()
                                    view_orders()
                                    timer(3)
                                    add_order()
                                    clear_ter()
                                    updating_an()
                                    view_orders()
                                    sub_loop2 = 1
                                #Return to Orders menu
                                elif user_in == 'R':
                                    sub_loop2 = 0
                                    sub_loop = 0
                                    new_loop3 = 1
                                    clear_ter()
                                    returning_to_orders_menu()
                                else:
                                    print('Invalid Input')
                                    sub_loop2 = 1
                        
                    #UPDATE Orders
                    elif user_input == 'C':
                        clear_ter()
                        #view_orders()
                        update_order()
                        clear_ter()
                        updating_an()
                        view_orders()
                        #Question
                        sub_loop3 = 1
                        while sub_loop3 == 1:
                                print()
                                user_in = input('Press [E] To Edit another [R] to Return To Orders Menu: ').upper()
                                print()
                                if user_in == 'E':
                                    clear_ter()
                                    #view_orders()
                                    update_order()
                                    clear_ter()
                                    updating_an()
                                    view_orders()
                                    print()
                                    sub_loop3 = 1
                                #Return to Orders menu
                                elif user_in == 'R':
                                    sub_loop3 = 0
                                    sub_loop = 0
                                    new_loop3 = 1
                                    clear_ter()
                                    returning_to_orders_menu()
                                else:
                                    print('Invalid Input')
                                    sub_loop3 = 1
                        
                    #DELETE Orders
                    elif user_input == 'D':
                        clear_ter()
                        view_orders()
                        print()
                        user_input = input('Enter the Order Id You Would Like To [Delete]: ')
                        delete_order(str(user_input))
                        clear_ter()
                        updating_an()
                        view_orders()
                        #Question
                        sub_loop4 = 1
                        while sub_loop4 == 1:
                                print()
                                user_in = input('Press [D] To Delete another [R] To Return to Orders Menu: ').upper()
                                print()
                                if user_in == 'D':
                                    del_val = input('Enter the Order Id You Would Like To [Delete]: ')
                                    print()
                                    clear_ter()
                                    delete_order(int(del_val))
                                    updating_an()
                                    view_orders()
                                    print()
                                    sub_loop4 = 1
                                #Return to orders menu
                                elif user_in == 'R':
                                    sub_loop4 = 0
                                    sub_loop = 0
                                    new_loop3 = 1
                                    clear_ter()
                                    returning_to_orders_menu()
                                else:
                                    print('Invalid Input')
                                    sub_loop4 = 1
                    
                    #Return to Main menu
                    elif user_input == 'E':
                        clear_ter()
                        returning_to_main()
                        sub_loop = 0
                        new_loop3 = 0
                        main_loop = 1
                    else:
                        print('Invalid Input')
                        sub_loop = 0
                        main_loop = 1
                        clear_ter()
                        returning_to_main()
           ##################### END ##############################
    
    ###### customer's menu starts ######
    elif user_input == 'A':
        clear_ter()
        #loading_customers_menu_screen()
        new_loop4 = 1
        while new_loop4 == 1:
                clear_ter()
                print(customers_menu)
                user_input = input('Enter Choice: ').upper()
                # View customer List
                sub_loop = 1
                while sub_loop == 1:
                    if user_input == 'A':
                        clear_ter()
                        view_customers()
                        print()
                        #Question
                        sub_loop1 = 1
                        while sub_loop1 == 1:
                            print()
                            user_input = input('Press [A] to View customer Press [E] To Export customers Or [R] To Return to customers Menu: ').upper()
                            #Return to customer  menu
                            if user_input == 'A':
                                clear_ter()
                                view_customers()
                                sub_loop1 = 1
                                sub_loop = 0
                                new_loop4 = 0
                                print()
                                u_i = input('Please Enter customer Id: ')
                                view_a_customer(u_i)
                            # export orders
                            elif user_input == 'E':
                                clear_ter()
                                view_customers()
                                sub_loop1 = 1
                                sub_loop = 0
                                new_loop3 = 0
                                print()
                                export_customers()
                            elif user_input == 'R':
                                sub_loop1 = 0
                                sub_loop = 0
                                new_loop4 = 1
                                clear_ter()
            
                                returning_to_customers_menu()
                            else:
                                print('Invalid Input')
                                sub_loop1 = 1     
                    #Add customer
                    elif user_input == 'B':
                            clear_ter()
                            view_customers()
                            timer(3)
                            add_customer()
                            clear_ter()
                            updating_an()
                            view_customers()
                            #Question
                            sub_loop2 = 1
                            while sub_loop2 == 1:
                                print()
                                user_in = input('Press [A] To Add another [R] To Return to customer Menu: ').upper()
                                if user_in == 'A':
                                    clear_ter()
                                    view_customers()
                                    timer(3)
                                    add_customer()
                                    clear_ter()
                                    updating_an()
                                    view_customers()
                                    sub_loop2 = 1
                                #Return to customer menu
                                elif user_in == 'R':
                                    sub_loop2 = 0
                                    sub_loop = 0
                                    new_loop4 = 1
                                    clear_ter()
                                    returning_to_customers_menu()
                                else:
                                    print('Invalid Input')
                                    sub_loop2 = 1
                        
                    #UPDATE customer
                    elif user_input == 'C':
                        clear_ter()
                        #view_orders()
                        update_customers()
                        clear_ter()
                        updating_an()
                        view_customers()
                        #Question
                        sub_loop3 = 1
                        while sub_loop3 == 1:
                                print()
                                user_in = input('Press [E] To Edit another [R] to Return To customer Menu: ').upper()
                                print()
                                if user_in == 'E':
                                    clear_ter()
                                    #view_customers()
                                    update_customers()
                                    clear_ter()
                                    updating_an()
                                    view_customers()
                                    print()
                                    sub_loop3 = 1
                                #Return to customer menu
                                elif user_in == 'R':
                                    sub_loop3 = 0
                                    sub_loop = 0
                                    new_loop4 = 1
                                    clear_ter()
                                    returning_to_customers_menu()
                                else:
                                    print('Invalid Input')
                                    sub_loop3 = 1
                        
                    #DELETE customer
                    elif user_input == 'D':
                        clear_ter()
                        view_customers()
                        print()
                        user_input = input('Enter the customer Id You Would Like To [Delete]: ')
                        delete_customer(str(user_input))
                        clear_ter()
                        updating_an()
                        view_customers()
                        #Question
                        sub_loop4 = 1
                        while sub_loop4 == 1:
                                print()
                                user_in = input('Press [D] To Delete another [R] To Return customer Menu: ').upper()
                                print()
                                if user_in == 'D':
                                    del_val = input('Enter the customer Id You Would Like To [Delete]: ')
                                    print()
                                    clear_ter()
                                    delete_customer(int(del_val))
                                    updating_an()
                                    view_customers()
                                    print()
                                    sub_loop4 = 1
                                #Return to customer menu
                                elif user_in == 'R':
                                    sub_loop4 = 0
                                    sub_loop = 0
                                    new_loop4 = 1
                                    clear_ter()
                                    returning_to_customers_menu()
                                else:
                                    print('Invalid Input')
                                    sub_loop4 = 1
                    
                    #Return to Main menu
                    elif user_input == 'E':
                        clear_ter()
                        returning_to_main()
                        sub_loop = 0
                        new_loop4 = 0
                        main_loop = 1
                    else:
                        print('Invalid Input')
                        sub_loop = 0
                        main_loop = 1
                        clear_ter()
                        returning_to_main()      
           
    else:
        print('Invalid Input')
        main_loop  = 1
        clear_ter()
        returning_to_main()
                    
            
        
    

    






































                


                

            
    

    
                

        

        


    
    

    


