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
        break

#Program ends