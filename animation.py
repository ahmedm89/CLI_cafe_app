############### IMPORTS #####################
from winsound import PlaySound
import os
from helper import *




# APP LOGO
def logo():
    logo = """
     __  __         _            _____        _   
    |  \/  |       | |          |  __ \      | |  
    | \  / |  ___  | | __ __ _  | |__) |___  | |_ 
    | |\/| | / _ \ | |/ // _` | |  ___// _ \ | __|
    | |  | || (_) ||   <| (_| | | |   | (_) || |_ 
    |_|  |_| \___/ |_|\_\\__,_|  |_|    \___/  \__|

                                        
                    

        """
    print(logo)
    audio_file = os.path.dirname('COFFEE_APP') + 'intro-transition2.wav'
    PlaySound(audio_file,False)
    timer(1)
    os.system('cls')
    
def logo_end():
    logo = """
     __  __         _            _____        _   
    |  \/  |       | |          |  __ \      | |  
    | \  / |  ___  | | __ __ _  | |__) |___  | |_ 
    | |\/| | / _ \ | |/ // _` | |  ___// _ \ | __|
    | |  | || (_) ||   <| (_| | | |   | (_) || |_ 
    |_|  |_| \___/ |_|\_\\__,_|  |_|    \___/  \__|

                                        
                    

        """
    print(logo)
    timer(2)
    os.system('cls')
    
    
    
    
    
    

# This is the intro Function
def intro():
    sub_logo_m = """"
                 __  __ 
                |  \/  |
                | \  / |
                | |\/| |
                | |  | |
                |_|  |_|
                        

    """
    print(sub_logo_m)
    timer(0.5)
    sub_logo_o = """
    
                 ___  
                / _ \ 
               | (_) |
                \___/ 
    """
    print(sub_logo_o)
    timer(0.5)
    sub_logo_K = """
    
                 _    
                | |   
                | | __
                | |/ /
                |   < 
                |_|\_\  
                
    """
    print(sub_logo_K)
    timer(0.5)
    sub_logo_a = """
    
                 __ _ 
                / _` |
               | (_| |
                \__,_|  
                
    """
    print(sub_logo_a)
    timer(0.5)
    sub_logo_p = """
    
                 _ __  
                | '_ \ 
                | |_) |
                | .__/ 
                | |    
                |_|    
                
    """
    print(sub_logo_p)
    timer(0.5)
    sub_logo_o2 = """
    
                 ___  
                / _ \ 
               | (_) |
                \___/ 
            
                
    """
    print(sub_logo_o2)
    timer(0.5)
    sub_logo_t = """
    
                 _   
                | |  
                | |_ 
                | __|
                | |_ 
                \__| 
            
                
    """
    print(sub_logo_t)
    timer(0.5)
    

    
    
    
############# loading products menu screen ########################
def loading_products_menu_screen():
    frame1 = """"           
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓟ Ⓡ Ⓞ Ⓓ Ⓤ Ⓒ Ⓣ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ
    """
    print(frame1)
    timer(0.3)
    
    frame2 = """"           
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓟ Ⓡ Ⓞ Ⓓ Ⓤ Ⓒ Ⓣ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ  .
    """
    print(frame2)
    timer(0.3)
    
    frame3 = """"          
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓟ Ⓡ Ⓞ Ⓓ Ⓤ Ⓒ Ⓣ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ  .  .
    """
    print(frame3)
    timer(0.3)
    
    frame4 = """"           
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓟ Ⓡ Ⓞ Ⓓ Ⓤ Ⓒ Ⓣ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ  .  .  .
    """
    print(frame4)
    timer(0.3)
    
    
    
############# loading couriers menu screen ########################
def loading_couriers_menu_screen():
    frame1 = """"           
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓒ Ⓞ Ⓤ Ⓡ Ⓘ Ⓔ Ⓡ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ
    """
    print(frame1)
    timer(0.3)
    
    frame2 = """"           
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓒ Ⓞ Ⓤ Ⓡ Ⓘ Ⓔ Ⓡ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ  .                                        
    """
    print(frame2)
    timer(0.3)
    
    frame3 = """" 
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓒ Ⓞ Ⓤ Ⓡ Ⓘ Ⓔ Ⓡ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ  .  .                                         
    """
    print(frame3)
    timer(0.3)
    
    frame4 = """"             
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓒ Ⓞ Ⓤ Ⓡ Ⓘ Ⓔ Ⓡ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ  .  .  .                                 
    """
    print(frame4)
    timer(0.3)
    
############# loading Orders menu screen ########################
def loading_orders_menu_screen():
    frame1 = """"    
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓞ Ⓡ Ⓓ Ⓔ Ⓡ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ
    """
    print(frame1)
    timer(0.3)
    
    frame2 = """"          
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓞ Ⓡ Ⓓ Ⓔ Ⓡ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ  .
                                                    
                                         
    """
    print(frame2)
    timer(0.3)
    
    frame3 = """" 
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓞ Ⓡ Ⓓ Ⓔ Ⓡ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ  .  .                                     
    """
    print(frame3)
    timer(0.3)
    
    frame4 = """" 
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓞ Ⓡ Ⓓ Ⓔ Ⓡ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ  .  .  .                                    
    """
    print(frame4)
    timer(0.3)
    
############# loading customers menu screen ########################
def loading_customers_menu_screen():
    frame1 = """"                                                                                   
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓒ Ⓤ Ⓢ Ⓣ Ⓞ Ⓜ Ⓔ Ⓡ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ      
    """
    print(frame1)
    timer(0.3)
    
    frame2 = """"          
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓒ Ⓤ Ⓢ Ⓣ Ⓞ Ⓜ Ⓔ Ⓡ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ  .
                                         
    """
    print(frame2)
    timer(0.3)
    
    frame3 = """" 
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓒ Ⓤ Ⓢ Ⓣ Ⓞ Ⓜ Ⓔ Ⓡ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ  .  .   
                                                    
                                         
    """
    print(frame3)
    timer(0.3)
    
    frame4 = """" 
Ⓛ Ⓞ Ⓓ Ⓘ Ⓝ Ⓖ

Ⓒ Ⓤ Ⓢ Ⓣ Ⓞ Ⓜ Ⓔ Ⓡ Ⓢ

Ⓜ Ⓔ Ⓝ Ⓤ  .  .  .
                                                    
                                         
    """
    print(frame4)
    timer(0.3)

    
# this the updating animation function  
def updating_an():
    print('ＵＰＤＡＴＩＮＧ .')
    timer(0.3)
    print('ＵＰＤＡＴＩＮＧ . .')
    timer(0.3)
    print('ＵＰＤＡＴＩＮＧ . . .')
    timer(0.3)
    print('ＵＰＤＡＴＩＮＧ . . . .')
    timer(0.3)
    
def returning_to_main():
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＭＡＩＮ ＭＥＮＵ .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＭＡＩＮ ＭＥＮＵ . .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＭＡＩＮ ＭＥＮＵ . . .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＭＡＩＮ ＭＥＮＵ . . . .')
    timer(0.3)
    
def returning_to_prodducts_menu():
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＰＲＯＤＵＣＴＳ ＭＥＮＵ .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＰＲＯＤＵＣＴＳ ＭＥＮＵ . .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＰＲＯＤＵＣＴＳ ＭＥＮＵ . . .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＰＲＯＤＵＣＴＳ ＭＥＮＵ . . . .')
    timer(0.3)
    
def returning_to_couriers_menu():
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＣＯＵＲＩＥＲＳ ＭＥＮＵ .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＣＯＵＲＩＥＲＳ ＭＥＮＵ . .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＣＯＵＲＩＥＲＳ ＭＥＮＵ . . .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＣＯＵＲＩＥＲＳ ＭＥＮＵ . . . .')
    timer(0.3)
    
def returning_to_orders_menu():
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＯＲＤＥＲＳ ＭＥＮＵ .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＯＲＤＥＲＳ ＭＥＮＵ . .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＯＲＤＥＲＳ ＭＥＮＵ . . .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＯＲＤＥＲＳ ＭＥＮＵ . . . .')
    timer(0.3)
    
def returning_to_customers_menu():
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＣＯＵＳＴＯＭＥＲＳ ＭＥＮＵ .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＣＯＵＳＴＯＭＥＲＳ ＭＥＮＵ . .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＣＯＵＳＴＯＭＥＲＳ ＭＥＮＵ . . .')
    timer(0.3)
    print('ＲＥＴＵＲＮＩＮＧ ＴＯ ＴＨＥ ＣＯＵＳＴＯＭＥＲＳ ＭＥＮＵ . . . .')
    timer(0.3)
    

#updating_an()
#loading_customers_menu_screen()
#loading_products_menu_screen()

