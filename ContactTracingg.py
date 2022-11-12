
Name = {}
Age = {}
Gender = {}
Number = {}
Email = {}
CityAddress = {}

def menu():
    print("""
            >>>>> WELCOME TO RODRIGUEZ`S PROGRAM <<<<<
                 _________________________________
                ||          MENU OPTIONS          ||
                ||________________________________||  
                ||                                ||
                ||        1. ADD AN ITEM          ||
                ||        2. SEARCH INFORMATION   ||   
                ||        3. VIEW INFORMATION     ||
                ||        4. EXIT                 ||
                ||________________________________||
        """)
def end():
    print(">>>>> THANK YOU FOR USING THIS PROGRAM! <<<<<")

    Options = int(input("\t\nSELECT AN OPTION (Choose from 1-3): "))
    while Options != 4:
     if Options == 1:
        print("PLEASE ENTER YOUR PERSONAL DATA:")
        Name.append(input("Enter your first name: "))
        Age.append(int(input("Enter your last name: ")))
        Gender.append(input("Enter your address: "))
        Number.append(int(input("Enter your phone number: ")))
        CityAddress.append(input("Enter your phone number: "))
