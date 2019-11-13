import time
import os

def Intro():
    print(''' _    _  _   _  ____  ____  ____ / ___    _   _  _____  ____  ____   ___ 
( \/\/ )( )_( )( ___)(  _ \( ___) / __)  ( )_( )(  _  )(_  _)(  _ \ (__ )
 )    (  ) _ (  )__)  )   / )__)  \__ \   ) _ (  )(_)(  _)(_  )(_) ) (_/ 
(__/\__)(_) (_)(____)(_)\_)(____) (___/  (_) (_)(_____)(____)(____/  (_) ''')
    time.sleep(2)
    def Order():
        ordr = input("\n\nYou are a member of the Knights Radiant.\nFrom what Order do you hail (Truthwatcher, Lightweaver, Windrunner)? ").lower().strip()
        order = ordr
        return order
    time.sleep(2)
    def Name():
        n = Order()
        
        if n[0] == "w":
            Order_Name = "Kaladin"
        elif n[0] == "l":
            Order_Name = "Shallan"
        elif n[0] == "t":
            Order_Name = "Renarin"
        else:
            print("Invalid Order Name. Please choose one of the three choices.")
            Name()
        nme = input("What is your name, Radiant? (Press enter to keep default name '" + Order_Name + "')")
        name = nme
        return name
    
    name = Name()
    print(name, order)


    

Intro()
