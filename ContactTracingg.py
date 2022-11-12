
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


while True:
    if Options == 1:
        print("PLEASE ENTER YOUR PERSONAL DATA:")
        Name = (input("PLEASE ENTER YOUR FIRST NAME: "))
        Age = int(input("PLEASE ENTER YOUR AGE: "))
        Gender = (input("PLEASE ENTER YOUR GENDER: "))
        Number = (int(input("PLEASE ENTER YOUR NUMBER: ")))
        CityAddress = (input("PLEASE ENTER YOU CITY ADDRESS: "))

    elif Options == 2:
        search = input("ENTER THE NAME YOU WANT TO SEARCH: ")
        print("RESULTS:")
        for i in range(len(Name)):
        
