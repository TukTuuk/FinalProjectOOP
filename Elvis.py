class laboratry: 
    def addLabToFile():
        newLabtxt= laboratry.formatLabInfo()
        f= open("laboratories.txt", "a")
        f.write(newLabtxt)
        f.close

    
    def writeListOfLabsToFile():
        pass

    
    def displayLabsList():
        f=open("laboratories.txt", "r")
        for line in f:
            print(line.replace("_","\t"))

    def formatLabInfo():
        newLab= laboratry.enterLaboratoryInfo()
        labTxt= "\n{}_{}"
        newLabTxt=(labTxt.format(newLab[0],newLab[1]))
        return newLabTxt

    def enterLaboratoryInfo():
        newLabNb=input("Enter Laboratory facility:\n")
        newLabCost=input("Enter Laboratory cost:\n")
        newlab= newLabNb, newLabCost
        return newlab
    
    
    def readLaboratoriesFile():
        f = open('laboratories.txt')
        for line in f:
            print(line.replace("_","\t"))
        
print("Laboratories Menu:")
menu= int(input("\n 1- Display laboratories list \n 2- Add laboratory \n 3- Back to the Main Menu\n"))
while menu:
    match menu:
        case 1:
            laboratry.displayLabsList()
            print('Back to the previous Menu')
            menu= int(input("\n 1- Display laboratories list \n 2- Add laboratory \n 3- Back to the Main Menu\n"))
        case 2:
            laboratry.addLabToFile()
            print('Back to the previous Menu')
            menu= int(input("\n 1- Display laboratories list \n 2- Add laboratory \n 3- Back to the Main Menu\n"))
        case 3:
            menu=int(input("Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop: \n 1 - Doctors \n2 - Facilities \n3 - Laboratories \n4 - Patients"))
        case _:
            print("Error")
            break
