import sys

clg_name = "Modern College of Vashi"
students = {}
id_no = 1
while 1:
    print("[+] {} [+]".format(clg_name))
    print("  1) Add Student \n  2) Delete Student \n  3) Show Students \n  4) Student Info \n  5) Exit")
    choice = int(input("Enter Your choice: "))
    if choice == 1:
        name = str(input("Enter your Name : "))
        age = int(input("Enter your age : "))
        course = str(input("Enter Your Course : "))
        admission_year = int(input("Enter your admission year : "))
        Percentage = float(input("Enter Your Previous Year Percentage :"))
        address = input("Enter your address :")
        contact = int(input("Enter contact details :"))
        students[id_no] = [name,age,course,admission_year,Percentage,address,contact]
        id_no = id_no + 1
    if choice == 2:
        id_no = int(input("Enter account ID : "))
        del students[id_no]
    if choice == 3:
        for i in students:
            print("\n")
            print("[+] Student ID : {}".format(i))
            print("    Student name : {}".format(students[i][0]))
            print("    Student age : {}".format(students[i][1]))
            print("    Student course : {}".format(students[i][2]))
            print("    Student admission year : {}".format(students[i][3]))
            print("    Student percentage : {}".format(students[i][4]))
            print("    Student address : {}" .format(students [i][5]))
            print("    Student contact : {}".format(students[i][6]))
    if choice == 4:
        id = int(input("Enter ID no : "))
        print("\n")
        print("[+] Student ID : {}".format(id))
        print("    Student name : {}".format(students[id][0]))
        print("    Student age : {}".format(students[id][1]))
        print("    Student course : {}".format(students[id][2]))
        print("    Student admission year : {}".format(students[id][3]))
        print("    Student Percentage :  {}".format(students[id][4]))
        print("    Student address : {}".format(students[id][5]))
        print("    Student contact : {}".format(students[id][6]))
    if choice == 5:
        break
    
print("Thanks for using our application")
sys.exit()
        