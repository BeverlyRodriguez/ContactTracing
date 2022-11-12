print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

Person1 = {"\nFullName": "Bebs Reyes", 
            "\nAge": "19", 
            "\nGender":"Female",
            "\nNumber": "09283623123",
            "\nEmail": "beverly@gmail.com",
            "\nAddress": "Jalajala"}
Person2 = {"\nFullName": "Jay Park", 
            "\nAge": "20",
            "\nGender":"Male","Number": "09123985458",
            "\nEmail": "jaypark@gmail.com",
            "\nAddress": "Seoul"}
Person3 = {"\nFullName": "Niki Rodriguez", 
            "\nAge": "17", 
            "\nGender":"Male",
            "\nNumber": "09096937644",
            "\nEmail": "nikirodriguez@gmail.com",
            "\nAddress": "Tokyo"}
Person4 = {"\nFullName": "Jake Marcus",
            "\nAge": "19", 
            "\nGender":"Male",
            "\nNumber": "09845321473",
            "\nEmail": "jakemarcus@gmail.com",
            "\nAddress": "Makati"}
Informations = []



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
Options = int(input("\t\nSELECT AN OPTION (Choose from 1-3): "))

while True:
    if Options == 1:
        print("\t\t\t>>>>> PLEASE ENTER YOUR PERSONAL DATA <<<<<")
        Name = (input("\n\tPLEASE ENTER YOUR FULL NAME:     "))
        Age = int(input("\tPLEASE ENTER YOUR AGE:            "))
        Gender = (input("\tPLEASE ENTER YOUR GENDER:         "))
        PhoneNumber = (int(input("\tPLEASE ENTER YOUR NUMBER:         ")))
        CityAddress = (input("\tPLEASE ENTER YOU CITY ADDRESS:    "))
        print("\t>>>>> INFORMATIONS ARE SAVED! <<<<<")
        person = {"Fullname": Name, "Age": Age, "Gender": Gender, "Address": CityAddress, "Number": PhoneNumber}

        Informations.append(Person1)
        Informations.append(Person2)
        Informations.append(Person3)
        Informations.append(Person4)

    elif Options == 2:
        search = input("ENTER THE NAME YOU WANT TO SEARCH: ")
        for i in range(len(Informations)):
            person = Informations[i]
            if person["Fullname"] == Name:
                print()
                print(person)

    elif Options == 4:   
        for i in range(len(Informations)):
            print(Informations[i])
    menu()
    Options = int(input("\t\nSELECT AN OPTION (Choose from 1-4): "))
        
        
