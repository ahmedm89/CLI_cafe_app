############### IMPORTS #####################

import time
import os


#clear function
def clear_ter():
    os.system('cls||clear')

#  timer function
def timer(t):
    s = time.sleep(t)
    c = os.system('cls')
    return s ,c

    
# invalid input funcion
def invalid_input():
    clear_ter()
    print('INVALID INPUT: Returning To Main Menu...')
    timer(3)
    clear_ter()
    
    