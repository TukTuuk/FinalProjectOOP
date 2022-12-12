print("Welcome to the Alberta hospital (AH) Management system")

print("Select from the following options, or select 0 to stop:")

#if for which meanu
def displayMenu():
    mainMenu = int(input("1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients\n"))
    if mainMenu == 1:
            #doctors code here
            #Creation of Class
            class Doctor:
                def __init__(doc, id, name, specialization, workingTime, qualifications, roomNB):
                    doc.id = id
                    doc.name = name
                    doc.specialization = specialization
                    doc.workingTime = workingTime
                    doc.qualifications = qualifications
                    doc.roomNB = roomNB
                    
                def __str__(doc):
                    return f"{doc.id}\t{doc.name}\t{doc.specialization}\t\t{doc.workingTime}\t\t{doc.qualifications}\t\t{doc.roomNB}\t"
                
                def readDoctorsFile():
                    
                    f = open('doctors.txt')
                    
                    headerList = (f.readline().split("_")) #header line not an object
                    godyList = (f.readline().split("_"))
                    vikramList = (f.readline().split("_"))
                    amyList = (f.readline().split("_"))
                    davidList = (f.readline().split("_"))
                    rossList = (f.readline().split("_"))
                    mikeList = (f.readline().split("_"))
                    
                    gody = Doctor(godyList[0],godyList[1],godyList[2],godyList[3],godyList[4],godyList[5])
                    vikram = Doctor(vikramList[0],vikramList[1],vikramList[2],vikramList[3],vikramList[4],vikramList[5])
                    amy = Doctor(amyList[0],amyList[1],amyList[2],amyList[3],amyList[4],amyList[5])
                    david = Doctor(davidList[0],davidList[1],davidList[2],davidList[3],davidList[4],davidList[5])
                    ross = Doctor(rossList[0],rossList[1],rossList[2],rossList[3],rossList[4],rossList[5])
                    mike = Doctor(mikeList[0],mikeList[1],mikeList[2],mikeList[3],mikeList[4],mikeList[5])
                    
                    doctors = (gody, vikram, amy, david, ross, mike)
                    
                    return doctors

                def displayDoctorsInfo():
                    
                    f = open('doctors.txt')
                    
                    print(f.readline().split("_"))
                    print(f.readline().split("_"))
                    print(f.readline().split("_"))
                    print(f.readline().split("_"))
                    print(f.readline().split("_"))
                    print(f.readline().split("_"))
                    print(f.readline().split("_"))
                    
                def displayDoctorsList(): # make doctors table
                    
                    f = open('doctors.txt')
                    
                    header = (f.readline().split("_"))
                    gody = (f.readline().split("_"))
                    vikram = (f.readline().split("_"))
                    amy = (f.readline().split("_"))
                    david = (f.readline().split("_"))
                    ross = (f.readline().split("_"))
                    mike = (f.readline().split("_"))
                    
                    print(header[0],'\t',header[1],'\t\t',header[2],'\t',header[3],'\t',header[4],'\t\t',header[5])
                    print(gody[0],'\t',gody[1],'\t',gody[2],'\t\t',gody[3],'\t',gody[4],'\t\t',gody[5])
                    print(vikram[0],'\t',vikram[1],'\t',vikram[2],'\t',vikram[3],'\t',vikram[4],'\t\t',vikram[5])
                    print(amy[0],'\t',amy[1],'\t',amy[2],'\t',amy[3],'\t',amy[4],'\t\t\t',amy[5])
                    print(david[0],'\t',david[1],'\t',david[2],'\t\t',david[3],'\t',david[4],'\t\t',david[5])
                    print(ross[0],'\t',ross[1],'\t',ross[2],'\t',ross[3],'\t',ross[4],'\t\t\t',ross[5])
                    print(mike[0],'\t',mike[1],'\t',mike[2],'\t\t',mike[3],'\t',mike[4],'\t\t\t',mike[5])
                    
                def searchDoctorByName(): ####### THIS IS WHAT YOU WERE WORKING ON AND ITS BEING STUPID #######
                    
                    doctors = Doctor.readDoctorsFile() #creates list
                    
                    search = input('What is the doctor name:\n')
                    
                    match = None
                    
                    for obj in doctors:
                        if obj.name == search:
                            match = True
                            print("Id\t","Name\t\t","Speciality\t","Timing\t\t","Qualifications\t\t","Room Number\n")
                            print(obj)
                            break
                        else:
                            match = False
                        
                    if match == False:
                        print("Can't find the doctor with the same name on the system")
                    
                def searchDoctorById():
                    
                    doctors = Doctor.readDoctorsFile() #creates list
                    
                    search = input('What is the doctor Id:\n')
                    
                    match = None
                    
                    for obj in doctors:
                        if obj.id == search:
                            match = True
                            print("Id\t","Name\t\t","Speciality\t","Timing\t\t","Qualifications\t\t","Room Number\n")
                            print(obj)
                            break
                        else:
                            match = False
                        
                    if match == False:
                        print("Can't find the doctor with the same  on the system")
                        
                def enterDoctorInfo():
                    
                    newDocId = int(input("Enter the doctor's ID:\n"))
                    newDocName = str(input("Enther the doctor's name:\n"))
                    newDocSpeciality = str(input("Enter the doctor's speciality:\n"))
                    newDocTiming = str(input("Enter the doctor's timing (e.g., 7am=10pm):\n"))
                    newDocQualification = str(input("Enter the doctor's qualification:\n"))
                    newDocRoomNB = int(input("Enter the doctor's room number:\n"))
                    
                    newDoc = (newDocId, newDocName, newDocSpeciality, newDocTiming, newDocQualification, newDocRoomNB)
                    
                    return newDoc
                
                def formatDrInfo(): #formats all of doctor objects into formatted string (underscores inbetween )
                
                    newDoc = Doctor.enterDoctorInfo()
                
                    docTxt = "{}_{}_{}_{}_{}_{}"
                    
                    newDocTxt = (docTxt.format(newDoc[0],newDoc[1],newDoc[2],newDoc[3],newDoc[4],newDoc[5]))
                    
                    return newDocTxt
                
                def addDrToFile():
                    
                    newDocTxt = Doctor.formatDrInfo()
                    
                    f = open('doctors.txt', "a")
                    
                    f.write(newDocTxt)
                    
                    f.close()
                    
                    f = open('doctors.txt')
                    
                    print(f.readlines)
                        
                def writeListOfDoctorsToFile():
                    pass
                    
                def editDoctorInfo():
                    
                    doctors = Doctor.readDoctorsFile() #creates list
                    
                    editDoc = input("Please enter the id of the doctor that you want to edit their information:\n\n")
                    
                    match = None
                    
                    for obj in doctors:
                        if obj.id == editDoc:
                            match = True
                            obj.name = input("Enter new Name:\n\n")
                            obj.specialization = input("Enter new Specilist in:\n\n")
                            obj.workingTime = input("Enter new Timing:\n\n")
                            obj.qualifications = input("Enter new Qualification:\n\n")
                            obj.roomNB = input("Enter new Room number:\n\n")
                            Doctor.formatDrInfo()
                            Doctor.addDrToFile()
                            break
                        else:
                            match = False
                        
                    if match == False:
                        print("Can't find the doctor with the same ID on the system")
                    
            #MAIN PROGRAM 

            print('Doctors Menu:')

            menu = int(input('1 - Display Doctors List\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the main menu\n'))

            while menu >= 1 and menu <=6 :
                
                if menu == 1:
                    Doctor.displayDoctorsList()
                    print('Back to the previous Menu')
                    menu = int(input('1 - Display Doctors List\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the main menu\n'))
                
                elif menu == 2:
                    Doctor.searchDoctorById()
                    print('Back to previous Menu')
                    menu = int(input('1 - Display Doctors List\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the main menu\n'))
                
                elif menu == 3:
                    Doctor.searchDoctorByName()
                    print('Back to previous Menu')
                    menu = int(input('1 - Display Doctors List\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the main menu\n'))
                
                elif menu == 4:
                    Doctor.addDrToFile()
                    print('Back to previous Menu')
                    menu = int(input('1 - Display Doctors List\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the main menu\n'))  
                    
                elif menu == 5:
                    Doctor.editDoctorInfo()
                    print("Back to previous Menu")  
                    menu = int(input('1 - Display Doctors List\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the main menu\n')) 
                    
                elif menu == 6:
                    #go back to management file
                    print("Back to previous Menu")  
                    displayMenu()
                
                else:
                    print('Error')
                    break

    elif mainMenu == 2:
            #facilities code here

                    #This program is an assignment from the course CPRG216G. 
            #The program aims at helping Alberta Hospital (AH) (a new healthcare provider in Alberta) to create a management system which is customized to meet their unique operational needs.
            #In this group project, 4 different classes will be created. While the program below is just a part of it as an individual work. 
            #In this individual assignment, Class #2: Facility will be deployed.
            #There are three methods in this class, which mainly uses the function of reading and writing the txt.file provided by the course. 
            #Apart from the functions mention-aboved. A loop and if-else statement are also used to run the program. 
            #Date 12 Dec 2022

            #Create lass #2: Facility
            class Facility:
            # adding the first method, which gives instructions for adding and writing the facility name to the file   
                def addFacility():
                    with open ('facilities.txt', 'r') as f: 
                        global fac_num
                        fac_num=int(input(
            '''Facilities Menu:
            1 - Display Facilities list
            2 - Add Facility
            3 - Back to the Main Menu
                    '''))
                    
            # second method, enable the class to display the list of facilities
                def displayFacilities():
                    with open ('facilities.txt', 'r') as f: 
                        for x in f.read().split('\n'):
                            print (x + '\n')
                        print('Back to the prevoius Menu')

            # third method, enable the class to write the facilities list to the corresponding txt.file
                def writeListOffacilitiesToFile():
                    with open ('facilities.txt', 'a') as f:
                        txt = input('Enter Facility name:\n')
                        txt = '\n' + txt  
                        f.write(txt)
                        print('\nBack to the prevoius Menu')

            # An loop function is created for proceeding the program
            while True:
                Facility.addFacility()
                if fac_num == 1:
                    Facility.displayFacilities()
                if fac_num == 2:
                    Facility.writeListOffacilitiesToFile()
                if fac_num == 3:
                    displayMenu()

    #Program ends

    elif mainMenu == 3:
            #laboratories code here
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
                    displayMenu()

