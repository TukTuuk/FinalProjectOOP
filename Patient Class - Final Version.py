#-----Patient Class-----        


# #Main
class Patient:

        def __init__(pat, id, name, disease, gender, age):
                pat.id = id
                pat.name = name
                pat.disease = disease
                pat.gender = gender
                pat.age = age
        
        
        def __str__(pat):
                return f"{pat.id}\t{pat.name}\t{pat.disease}\t\t{pat.gender}\t\t{pat.age}"        
        

        def readPatientsFile():
                f = open("patients.txt", "r")

                labelto = (f.readline().split("_"))
                pankajto = (f.readline().split("_"))
                janinato = (f.readline().split("_"))
                alonato = (f.readline().split("_"))
                ravito = (f.readline().split("_"))

                pankaj = Patient(pankajto[0], pankajto[1], pankajto[2], pankajto[3], pankajto[4])
                janina = Patient(janinato[0], janinato[1], janinato[2], janinato[3], janinato[4])
                alona = Patient(alonato[0], alonato[1], alonato[2], alonato[3], alonato[4])
                ravi = Patient(ravito[0], ravito[1], ravito[2], ravito[3], ravito[4])
                patients = (pankaj, janina, alona, ravi)

                return patients

        # readfiles = readPatientsFile()
        # print(readfiles.read())

        def displayPatientsInfo():
                f = open("patients.txt")

                print(f.readline().split("_"))
                print(f.readline().split("_"))
                print(f.readline().split("_"))
                print(f.readline().split("_"))
                print(f.readline().split("_"))
        # displayPatientsInfo()

        # #1 - Display patient list

        def displayPatientsList():        
                f=open("patients.txt", "r")
                for line in f:
                        print(line.replace("_","\t"))
        # displayPatientsList()

        #2 - Search for patient by ID

        def searchPatientById():
                patients = Patient.readPatientsFile()
                searchId = input("Enter Patient id: \n")
                match = None
                for num in patients:
                        if num.id == searchId:
                                match = True
                                print("ID\t", end=''), print("Name\t", end=''), print("Disease\t\t", end=''), print("Gender\t\t", end=''), print("Age")
                                print(num)
                                break
                        else:
                                match = False

                if match == False:
                        print("Can't find the Patient with the same id on the system")
        # searchPatientById()

        #3 - Add patient

        def enterPatientInfo():
                patientId = input("Enter Patient id: \n")
                patientName = input("Enter Patient name: \n")
                patientDisease = input("Enter Patient disease: \n")
                patientGender = input("Enter Patient gender: \n")
                patientAge = int(input("Enter Patient age: \n"))

                newPatient = (patientId, patientName, patientDisease, patientGender, patientAge)
                return newPatient
        # enterPatientinfo()

        #4 - Edit patient info

        def editPatientInfo():
                patients = Patient.readPatientsFile()
                editPat = input("Please enter the id of the Patient that you want to edit their information: \n")
                match = None
        
                for info in patients:
                        if info.id == editPat:
                                match = True
                                info.name = input("Enter new Name: \n")
                                info.disease = input("Enter new disease: \n")
                                info.gender = input("Enter new gender: \n")
                                info.age = int(input("Enter new age: \n"))

                                break
                        else:
                                match = False
                        
                if match == False:
                        print("Can't find the patient with the same id on the system")
                        
        # editPatientInfo()

        def formatPatientInfo():
                newText = Patient.enterPatientInfo()
                patText = "\n{}_{}_{}_{}_{}"
                modpatText = (patText.format(newText[0], newText[1], newText[2], newText[3], newText[4]))
                
                return modpatText

        def addPatientToFile():
                modpatText = Patient.formatPatientInfo()
                f = open("patients.txt", "a")

                f.write(modpatText)
                f.close


        def writeListOfPatientsToFile():
                pass



# -----Display Menu for Patient Class-----

print("Welcome to the Alberta Hostpital (AH) Management System \nSelect from the following options, or select 0 to stop:")
menu = int(input("1 - Doctors \n2 - Facilities \n3 - Laboratories \n4 - Patients \n"))

match menu:
        case 4:
                patMenu = int(input("\n Patients Menu: \n1 - Display patients list \n2 - Search for patient by ID \n3 - Add patient \n4 - Edit patient info \n5 - Back to the Main Menu \n"))
                while True:
                        if patMenu == 1:
                                Patient.displayPatientsList()
                                print("Back to previous Menu")
                                patMenu = int(input("\n Patients Menu: \n1 - Display patients list \n2 - Search for patient by ID \n3 - Add patient \n4 - Edit patient info \n5 - Back to the Main Menu \n"))

                        elif patMenu == 2:
                                Patient.searchPatientById()
                                print("Back to previous Menu")
                                patMenu = int(input("\n Patients Menu: \n1 - Display patients list \n2 - Search for patient by ID \n3 - Add patient \n4 - Edit patient info \n5 - Back to the Main Menu \n"))

                        elif patMenu == 3:
                                Patient.addPatientToFile()
                                print("Back to previous Menu")
                                patMenu = int(input("\n Patients Menu: \n1 - Display patients list \n2 - Search for patient by ID \n3 - Add patient \n4 - Edit patient info \n5 - Back to the Main Menu \n"))

                        elif patMenu == 4:
                                Patient.editPatientInfo()
                                print("Back to previous Menu")
                                patMenu = int(input("\n Patients Menu: \n1 - Display patients list \n2 - Search for patient by ID \n3 - Add patient \n4 - Edit patient info \n5 - Back to the Main Menu \n"))

                        elif patMenu == 5:
                                print("Back to previous Menu")
                                patMenu = int(input("\n Patients Menu: \n1 - Display patients list \n2 - Search for patient by ID \n3 - Add patient \n4 - Edit patient info \n5 - Back to the Main Menu \n"))

                        else:
                                print("Invalid input")
                                break        









        