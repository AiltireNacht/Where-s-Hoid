import time
import os

def Intro():
    print(''' _    _  _   _  ____  ____  ____ / ___    _   _  _____  ____  ____   ___ 
( \/\/ )( )_( )( ___)(  _ \( ___) / __)  ( )_( )(  _  )(_  _)(  _ \ (__ )
 )    (  ) _ (  )__)  )   / )__)  \__ \   ) _ (  )(_)(  _)(_  )(_) ) (_/ 
(__/\__)(_) (_)(____)(_)\_)(____) (___/  (_) (_)(_____)(____)(____/  (_) ''')
    time.sleep(2)
    order = input("\n\nYou are a member of the Knights Radiant.\nFrom what Order do you hail (Truthwatcher, Lightweaver, Windrunner)? ")
    time.sleep(2)
    name = input("What is your name, Radiant? ")


Intro()
