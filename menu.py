print("Welcome to the Alberta hospital (AH) Management system")

print("Select from the following options, or select 0 to stop:")

#Menu

mainMenu = input("1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients")

#if for which meanu
def displayMenu():
mainMenu = input("1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients")
    if mainMenu == 1:
        #doctors code here
    elif mainMenu == 2:
        #facilities code here
    elif mainMenu == 3:
        #laboratories code here
    elif mainMenu == 4:
        #patients code here
    elif mainMenu == 0:
        print("Thank you for using AH Management system")
    else:
        print("Error please enter a number between 0-4")
    
    