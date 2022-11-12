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
            ||           MENU OPTIONS         ||
            ||________________________________||  
            ||                                ||
            ||         1. ADD AN ITEM         ||
            ||         2. SEARCH              ||
            ||         3. EXIT                ||
            ||________________________________||
    """)

def end():
    print(">>>>> THANK YOU FOR USING THIS PROGRAM! <<<<<")

Name = {}
Age = {}
Gender = {}
Number = {}
Email = {}
CityAddress = {}



menu()
Options = int(input("\t\nSELECT AN OPTION (Choose from 1-3): "))

while option != 4:
    if option == 1:
        print("PLEASE ENTER YOUR PERSONAL DATA:")
        Name(input("Enter your first name: "))


    elif option == 3:
        exit = input("DO YOU WANT TO EXIT THE PROGRAM? (YES / NO)")
        if exit == "YES":
            break
        print()
        break
    menu()
    option = int(input("\t\nSELECT AN OPTION (Choose from 1-10): "))