
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

    Options = int(input("\t\nSELECT AN OPTION (Choose from 1-3): "))
    while Options != 4:
     if Options == 1:
        print("PLEASE ENTER YOUR PERSONAL DATA:")
