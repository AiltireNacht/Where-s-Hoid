import time
import os

def Intro():

    print(''' _    _  _   _  ____  ____  ____ / ___    _   _  _____  ____  ____   ___ 
( \/\/ )( )_( )( ___)(  _ \( ___) / __)  ( )_( )(  _  )(_  _)(  _ \ (__ )
 )    (  ) _ (  )__)  )   / )__)  \__ \   ) _ (  )(_)(  _)(_  )(_) ) (_/ 
(__/\__)(_) (_)(____)(_)\_)(____) (___/  (_) (_)(_____)(____)(____/  (_) ''')

    def Order(order):
        #This defines what Order the RPG character plays as, defining what abilities are given and what ideals the player must play by
        ordr = " " 
        while ordr[0] != "w" and ordr[0] != "l" and ordr[0] != "t":
            ordr = input("\n\nYou are a member of the Knights Radiant.\nFrom what Order do you hail (Truthwatcher, Lightweaver, Windrunner)? ")
            ordr = ordr.lower()

            if ordr[0] == "w":
                order = "Windrunner"
            elif ordr[0] == "l":
                order = "Lightweaver"
            elif ordr[0] == "t":
                order = "Truthwatcher"
            else:
                print("\n\nInvalid Order Name. Please choose one of the three options.")
            
        return order
    
    def Name(n):
        

        
        
        if n == "Windrunner":
            Order_Name = "Kaladin"
        elif n == "Lightweaver":
            Order_Name = "Shallan"
        else:
            Order_Name = "Renarin"
            
        nme = input("\nWhat is your name, Radiant? (Press enter to keep default name '" + Order_Name + "')")

        if nme == "": 
            name = Order_Name
        else:
            name = nme
        return name
        
     #Make it so order is one of the three options without having to repeat Order function
    n = Order("order")
    name = Name(n)
    print("\n Welcome to Roshar, " + name, "of the Order of", n + "s")


    

Intro()
