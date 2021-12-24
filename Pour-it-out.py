# Pour it out 
# https://brilliant.org/daily-problems/pour-it-out-14/

import time

'''
rules:
0. we can start with 2 milliliters in the 90-milliliter container
1. fill the 75-milliliter container when it's empty,
2. pour from the 75-milliliter container into the 90-milliliter container,
3. empty the 90-milliliter container when it's full, and
4. pour whatever is left in the 75-milliliter container into the 90-milliliter container just emptied.
'''

def main():

    smallSize = 75
    bigSize = 90
    small = 75  # fill small when empty
    big = 4  # initial quantity
    wanted = 32
       
    print(f"start (wanted: {wanted}, initial in big: {big})")
    print(f"\tsmall: {small}/{smallSize}\n\tbig: {big}/{bigSize}")

    step = 1
    while small != wanted and big != wanted:
        small = smallSize # fill when empty 
        
        spaceInBig = bigSize - big
        if small <= spaceInBig:         
            print(f"{step}. pour small into big")     
            big = big + small                   
        else:            
            print( f"{step}. pour small into big until full, empty big and pour the rest")  
            big = small - spaceInBig       
        
        step += 1 
        time.sleep(3)

        print(f"\tsmall: {small}/{smallSize}\n\tbig: {big}/{bigSize}")

    print("end")

main()