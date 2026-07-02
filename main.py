# Student Result Management 

student = {}

while True:
        print("""
    1. Add student details
    2. View total students in the list
    3. Check students marks 
    4. Result ~ Passed or Not
    5. Exit """)
        
        choice= int(input("Enter your choice : "))


    # Add student details
        if choice ==1:
            name = input("Enter student name: ")
            mark = int(input("Enter student marks: "))
            student[name] = mark # Anshul : 80
            with open("students_list.txt", "a") as f:
                f.write(f"{name}: {mark} \n")
            print(f"{name} added successfully! ")
        
        elif choice ==2:
            # View total students in the list
            if student:
                for name, mark in student.items():
                    print(f"{name} : {mark}")
            else:
                print("No data!")
            
        
        elif choice ==3:
            # Check students marks
            name = input("Enter Student Name: ")
            if name in student:
                print(f"{name} : {student[name]}")
            else:
                print("Student not found! ")
        
        elif choice ==4:
            # Result ~ Passed or Not
            name = input("Enter student name: ")
            if name in student:
                if student[name] >= 40:
                    print("PASS")
                else:
                    print("FAIL") 
            else:
                print("Student not found! ")
        
        elif choice ==5:
            # Exit...
            print("Exit...")
            break

        else:
            print("Invalid Choice!")
    
        




     
    