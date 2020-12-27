'''
Created on 22 nov. 2019

@author: Aaron
'''
import os
import platform
import sys

def sysInfo():

    user=os.getlogin()
    a=os.name
    b=str(platform.system())
    c=str(platform.release())
    d=platform.machine()
    e=platform.node()
    print("a log file with info about the system has been created on the desktop.")
    
    if(b=="Darwin"):
        sys.stdout=open(f"/Users/{user}/Desktop/sysInfo.txt","w") # redirects all prints from here and will create the file if it does not exists.
        print(f"OS name: {a}",f"System: {b}",f"System version: {c}",f"Architecture: {d}",f"System name: {e}",sep='\n')
        sys.stdout.close() #everything shown through prints will be saved in the file until we close it.
        

    elif(b=="Windows"):
        sys.stdout=open(f"c:/users/{user}/Desktop/sysInfo.txt","w") 
        print(f"OS name: {a}",f"System: {b}",f"System version: {c}",f"Architecture: {d}",f"System name: {e}",sep='\n')
        sys.stdout.close() 
        
        
    else:
        sys.stdout=open(f"/home/{user}/Desktop/sysInfo.txt","w")
        print(f"OS name: {a}",f"System: {b}",f"System version: {c}",f"Architecture: {d}",f"System name: {e}",sep='\n')
        sys.stdout.close() 

    
sysInfo()