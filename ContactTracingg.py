
Person1 = {"FullName": "Bebs Reyes", 
            "Age": "19", 
            "Gender":"Female",
            "Number": "09283623123",
            "Email": "beverly@gmail.com",
            "Address": "Jalajala"}
Person2 = {"FullName": "Jay Park", 
            "Age": "20",
            "Gender":"Male","Number": "09123985458",
            "Email": "jaypark@gmail.com",
            "Address": "Seoul"}
Person3 = {"FullName": "Niki Rodriguez", 
            "Age": "17", 
            "Gender":"Male",
            "Number": "09096937644",
            "Email": "nikirodriguez@gmail.com",
            "Address": "Tokyo"}
Person4 = {"FullName": "Jake Marcus",
            "Age": "19", 
            "Gender":"Male",
            "Number": "09845321473",
            "Email": "jakemarcus@gmail.com",
            "Address": "Makati"}
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


    elif Options == 2:
        search = input("ENTER THE NAME YOU WANT TO SEARCH: ")
        for i in range(len(i)):

            name = input("What is the name? ")
for i in range(len(infos)):
    user = infos[i]
    if user["Fullname"] == name:
        print("Satrue")
        print(user)

#viewall
for i in range(len(infos)):
    print(infos[i])
        
        
