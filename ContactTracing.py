print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")


#Write a python program for contact tracing:
# Display a menu of options
# Allow user to select item in the menu.
# Ask personal data for contact tracing. Use dictionary to store the info
# Search, ask full name then display the record



def menu(): 
    print("""
        >>>>> WELCOME TO RODRIGUEZ`S PROGRAM <<<<<
             _________________________________
            |           MENU OPTIONS          |
            |_________________________________|  
            |                                 |
            |         1. ADD AN ITEM          |
            |         2. SEARCH               |
            |         3. EXIT                 |
            |_________________________________|
    """)

def end():
    print(">>>>> THANK YOU FOR USING THIS PROGRAM! <<<<<")

FullName = []
Nickname = []
Gender = []
Age = []
CityAddress = []
CivilStatus = []
Birthdate = []

menu()
option = int(input("\t\nSELECT AN OPTION (Choose from 1-3): "))

while option != 4:
    if option == 1:
        num = int(input("\tPlease enter the number you want to add: "))
        Array.append(num)
        print("\tThank you!!The element has been added.")
        print(f"\tTHIS IS NOW THE NEW ARRAY!! = {Array}")
       
    elif option == 2:
        insert = int(input("Please enter the number you want to insert: "))
        insert_idx = int(input(f"Enter the index you want to insert {insert}: "))
        Array.insert(insert_idx, insert)
        print("\tThank you!! The element has been inserted.")
        print(f"\tTHIS IS NOW THE NEW ARRAY!! = {Array}")
          
    elif option == 10:
        end()
        break
    menu()
    option = int(input("\t\nSELECT AN OPTION (Choose from 1-10): "))