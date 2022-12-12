class Facility:
    def addFacility():
        global fac_num
        fac_num= int(input ('''
Facilities Menu:
1 - Display Facilities list
2 - Add Facility
3 - Back to the Main Menu
        '''))
        

    def displayFacilities():
        with open ('facilities.txt', 'r') as f: 
            f_contents = f.read()
            print(f_contents)

    def writeListOffacilitiesToFile():
        with open ('facilities.txt', 'a') as f:
            txt = input('Enter Facility name: ')
            txt = '\n' + txt  
            f.write(txt)

Facility.addFacility()

if fac_num == 1:
    Facility.displayFacilities()
if fac_num == 2:
    Facility.writeListOffacilitiesToFile()
