print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

Informations = []
Person1 = {"FullName": "Bebs Reyes", 
            "Age": "19", 
            "Gender":"Female",
            "Number": "09123456789",
            "Address": "Jalajala"}
Person2 = {"FullName": "Jay Park", 
            "Age": "20",
            "Gender":"Male","Number": "09876543210",
            "Address": "Seoul"}
Person3 = {"FullName": "Niki Rodriguez", 
            "Age": "17", 
            "Gender":"Male",
            "Number": "09096937644",
            "Address": "Tokyo"}
Person4 = {"FullName": "Jake Marcus",
            "Age": "19", 
            "Gender":"Male",
            "Number": "09845321473",
            "Address": "Makati"}

Informations.append(Person1)
Informations.append(Person2)
Informations.append(Person3)
Informations.append(Person4)
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


menu()
Options = int(input("\t\nSELECT AN OPTION (Choose from 1-4): "))


while True:
    if Options == 1:
        print("\t\t\t>>>>> PLEASE ENTER YOUR PERSONAL DATA <<<<<")
        Name = (input("\n\tPLEASE ENTER YOUR FULL NAME:      "))
        Age = int(input("\tPLEASE ENTER YOUR AGE:            "))
        Gender = (input("\tPLEASE ENTER YOUR GENDER(F/M):     "))
        PhoneNumber = (int(input("\tPLEASE ENTER YOUR NUMBER:         ")))
        CityAddress = (input("\tPLEASE ENTER YOU CITY ADDRESS:    "))
        print("\t>>>>> INFORMATIONS ARE SAVED! <<<<<")
        person = {"Name": Name, "A": Age, "G": Gender, "Add": CityAddress, "Num": PhoneNumber}
        print("\tThese are the informations: \n\t", person)
        

    elif Options == 2:
        search = input("ENTER THE NAME YOU WANT TO SEARCH: ")
        for i in range(len(Informations)):
            person = Informations[i]
            if person['FullName'] == search:
                print("\t\t\t\n>>>>> RESULTS <<<<<")
                print(person)

    elif Options == 3:   
        for i in range(len(Informations)):
            print("\n\t\t\t\t>>>>> THESE ARE THE INFORMATIONS <<<<<")
            print(Informations[i])

    elif Options == 4:
        exit = input("\tDO YOU WANT TO EXIT THE PROGRAM? (YES / NO): ")
        if exit == "NO":
           menu()
        else:
            print("\n\t\t>>>>> THANK YOU FOR USING THIS PROGRAM! <<<<<")
            break
    menu()
    Options = int(input("\t\nSELECT AN OPTION (Choose from 1-4): "))

        
        
