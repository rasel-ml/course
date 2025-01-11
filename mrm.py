def loadDatabase():
    global students
    try:
        with open("database.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()  # Remove any leading/trailing whitespace
                if not line:  # Skip empty lines
                    continue
                info = line.split(",")
                if len(info) != 3:  # Check if line has exactly 3 parts (id, name, dept)
                    with open("error_log.txt", "a") as error:
                        error.write(f"Invalid line: {line}\n")  # Log the invalid line
                    continue
                student = {'id': info[0], 'name': info[1], 'dept': info[2]}
                students.append(student)
    except FileNotFoundError:
        with open("database.txt", "w") as file:
            pass  # This creates the file, but doesn't add any students.
            
def updateDatabase():
    with open("database.txt", "w") as file:
        for student in students:
            file.write(f"{student['id']},{student['name']},{student['dept']}\n")

def Main():
    print("Welcome to the Student Information System. Please choose an option from the menu below.")
    while (True):
        print("\nMain menu:\n──────────\n1. Add a New Student\n2. View All Students\n3. Search for a Student\n4. Edit a Student Profile\n5. Delete a Student Profile\n6. Exit")
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            addStudent()
        elif choice == "2":
            viewStudent()
        elif choice == "3":
            searchStudent()
        elif choice == "4":
            editStudent()
        elif choice == "5":
            deleteStudent()
        elif choice == "6":
            print("\nThank you for using the system. Have a great day!")
            break
        else:
            print("\nInvalid choice. Please input a valid option.\n")

def addStudent(): # Function for adding student in database
    print("\nPlease enter a new Student ID. Ensure the ID is within 20 characters and does not contain spaces or special characters. Type 'X' to cancel.")
    while (True): # Infinte loop for taking student id if they doest meet given criteria
        id = input("Student Id : ").strip() # Input with strip function for removing extra space
        if (id == "X"):
            return
        elif (id == ""): # Validating if wether input is empty or not
            print("\nThe ID field can't be empty. Please try again.")
            continue # loop continue beacause input is empty
        elif (len(id) >= 20): # Validating if input is over length or not
            print("\nThe ID field can't exceed 20 characters. Please try again.")
            continue # Loop continue becuase id is over length
        elif (id.isalnum() == False):
            print("\nThe ID must not contain space or special charecters. Please try again.")
            continue
        for student in students: # For loop for checking if input already in database or not
            if (student['id'] == id):
                print("A Student with the same ID already exists.")
                return # Function termination because student already in database
        break # Break infinite loop because all criteria is met
    print("\nPlease enter the student's name. The name must be between 3 to 50 characters. Type 'X' to cancel.")
    while (True):
        name = input("Student Name : ").strip()
        if (name == "X"):
            return
        elif (name == ""):
            print("The name field can't be empty. Please try again.")
            continue
        elif ((len(name)<3) or (len(name) > 50)):
            print("The name must be between 3 to 50 characters. Please try again.")
            continue
        elif (name.isdecimal() == True):
            print("The name can not be a numeric value. Please try again.")
            continue
        name = name.title()  # Capitalize the first letter of each word
        break
    print("\nPlease enter the department name. The name must not exceed 50 characters. Type 'X' to cancel.")
    while (True):
        dept = input("Department Name : ").strip()
        if (dept == "X"):
            return
        elif (dept == ""):
            print("Field can't be empty. Please enter a valid department.")
            continue
        elif (len(dept) > 50):
            print("Department name can't exceed 30 characters. Please try again.")
            continue
        dept = dept.title()  # Capitalize the first letter of each word
        break
    students.append({'id': id, 'name': name, 'dept': dept})
    updateDatabase()
    print("\nStudent information has been added successfully.\n")

def viewStudent():
    if (len(students) == 0):
        print("\nNo student information available.\n")
        return
    temp = sorted(students, key = lambda x:x["id"])
    a=[10]
    b=[12]
    c=[15]
    for i in students:
        a.append(len(i["id"]))
        b.append(len(i["name"]))
        c.append(len(i["dept"]))
    print("┌─" + "─" * max(a) + "─┬─" + "─" * max(b) + "─┬─" + "─" * max(c) + "─┐")
    print("│ " + "Student ID".center(max(a)) + " │ " + "Student Name".center(max(b)) + " │ " + "Department Name".center(max(c)) + " │")
    print("├─" + "─" * max(a) + "─┼─" + "─" * max(b) + "─┼─" + "─" * max(c) + "─┤")
    for student in temp:
        print("│ " + student["id"].center(max(a)) + " │ " + student["name"].ljust(max(b)) + " │ " + student["dept"].ljust(max(c)) + " │")
    print("└─" + "─" * max(a) + "─┴─" + "─" * max(b) + "─┴─" + "─" * max(c) + "─┘\n")

def searchStudent():
    search = input("\nEnter your queary to search: ").strip()
    temp = []
    n=1
    for student in students:
        if (search == student["id"]) or (search.lower() in student["name"].lower()) or (search.lower() in student["dept"].lower()):
            temp.append({'id': student["id"], 'name': student["name"], 'dept': student["dept"]})
    if len(temp) == 0:
        print(f"\nNo match found for {search}.\n")
    else:
        if len(temp)==1:
            print("\n1 match found for "+search+".\n"+"─"*(19+len(search)))
        else:
            print("\n"+str(len(temp))+" match's found for "+search+".\n"+"─"*(len(temp)+19+len(search)))
        for i in temp:
            if len(temp)>1:
                print(n,"\n──")
            print("Student ID      :", i["id"])
            print("Student Name    :", i["name"])
            print("Department Name :", i["dept"], "\n")
            n+=1
    return
    
def editStudent():
    id = input("\nEnter a valid student ID number: ").strip()
    for student in students:
        if student["id"] == id:
            print("\nWhat do you want to edit?\n1. ID number\n2. Name\n3. Department\n")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                while (True):
                    new_id = input("Enter correct student ID : ").strip()
                    if (new_id == "X"):
                        return
                    elif (new_id == ""):
                        print("\nThe ID field can't be empty. Please try again.")
                        continue
                    elif (len(new_id) >= 20):
                        print("\nThe ID field can't exceed 20 characters. Please try again.")
                        continue
                    elif (new_id.isalnum() == False):
                        print("\nThe ID must not contain space or special charecters. Please try again.")
                        continue
                    break
                student["id"] = new_id
                updateDatabase()
                print("\nStudent information updated successfully!\n")
            elif choice == "2":
                while (True):
                    new_name = input("Enter correct name : ").strip()
                    if (new_name == "X"):
                        return
                    elif (new_name == ""):
                        print("The name field can't be empty. Please try again.")
                        continue
                    elif ((len(new_name)<3) or (len(new_name) > 50)):
                        print("The name must be between 3 to 50 characters. Please try again.")
                        continue
                    elif (new_name.isdecimal() == True):
                        print("The name can not be a numeric value. Please try again.")
                        continue
                    new_name = new_name.title()
                    break
                student["name"] = new_name
                updateDatabase()
                print("\nStudent information updated successfully!\n")
            elif choice == "3":
                while (True):
                    new_dept = input("Enter correct department name : ").strip()
                    if (new_dept == "X"):
                        return
                    elif (new_dept == ""):
                        print("Field can't be empty. Please enter a valid department.")
                        continue
                    elif (len(new_dept) > 50):
                        print("Department name can't exceed 50 characters. Please try again.")
                        continue
                    new_dept = new_dept.title()  # Capitalize the first letter of each word
                    break
                    student["dept"] = new_dept
                    updateDatabase()
                    print("\nStudent information updated successfully!\n")
                    
            else:
                print("\nInvalid choice. Please try again.\n")
            return
    print(f"\nNo student found with the ID: {id}.\n")
    return

def deleteStudent():
    print(r'To delete a student profile please enter the student ID. To delete multiple, type desired student IDs one after another followed by a comma(,). Type "ALL" to completely delete the whole database. Type "X" to cancel.')
    while(True):
        ids = input("\nEnter a valid Student Id number: ").strip()
        del_list = ids.split(",")
        deleted=[]
        other=[]
        if not ids:
            print("You have to input atleast one ID.")
            continue
        elif ids == "X":
            return 
        elif ("ALL" in del_list):
            confirm = input("Are you sure you want to delete all student profiles? (yes/no): ").strip().lower()
            if confirm == "yes":
                students.clear()
                print("All student profiles deleted successfully.")
                updateDatabase()
                return  # Save to the file
            print("Deletion process cancelled.")
            return
        for i in del_list:
            found = False
            for student in students:
                if (student["id"] == i.strip()):
                    students.remove(student)
                    deleted.append(i.strip())
                    found = True
                    break
            if not found:
                other.append(i.strip())
        if (len(deleted)==1):
            print("\nStudent with ID number",deleted[0],"deleted successfully.\n")
        if (len(deleted)>1):
            print("\nStudent with ID number",",".join(deleted[:-1]),"and",deleted[-1],"deleted successfully.\n")
        if (len(other)==1):
            print("No student found with the ID number",other[0],".\n")
        if (len(other)>1):
            print("No student found with the ID number",",".join(other[:-1]),"and",other[-1],".\n")
        updateDatabase()
        break
        return
        
students = [] 
loadDatabase()
Main()