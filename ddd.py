students = []

def add_student():
    
    n = int(input("Enter the no of students: "))
    
   
    for i in range(n):
        print(f"\nEnter the student details {i+1}")
        
        roll = input("Roll number: ")
        name = input("Name: ")
        marks = input("Marks: ")
        
        
        students.append([roll, name, marks])

def display_student():
    if not students:
        print("No record found.\n")
        return
    print("\nStudent records:")
    for student in students:
        print(f"Roll no:{student[0]},Name:{student[1]},Marks:{student[2]}")


def search_student():
    roll=int(input("Enter the roll no :"))
    for student in students:
        if student[0]==roll:
            print(f"Found:{student}")
            return
    print("Student not found.\n")
   
def update_marks():
    roll=int(input("Enter the roll no :"))
    for student in students:
        if student[0]==roll:
            new_marks=input("Enter the new marks :")
            student[2]=new_marks
            print("Marks updated successfully.\n")
            return
    print("Student not found.\n")
    
def delete_student():
    roll=int(input("Enter the roll no :"))
    for student in students:
        if student[0]==roll:
            students.remove(student)
            print("Student removed")
            return
    print("Student not found.\n")
 
def find_topper():
     if not students:
         print("NO record found.\n")
         return
     topper=max(students,key=lambda x:x[2])   
     print(f"Topper is {topper[1]} with marks {topper[2]}\n")
        
def class_average():
    if not students:
        print("No record found.\n")
        return
    total_marks=sum(int(student[2]) for student in students)
    average=total_marks/len(students)
    print(f"Class average marks: {average}\n")
    
def sort_by_marks():
    if not students:
        print("No record found.\n")
        return
    sorted_students=sorted(students,key=lambda x:x[2],reverse=True)
    print("Students sorted by marks:")
    for student in sorted_students:
        print(f"Roll no:{student[0]},Name:{student[1]},Marks:{student[2]}") 
        
while True:
    print("1. Add student")
    print("2. Display students")
    print("3. Search student")  
    print("4. Update marks")
    print("5. Delete student")
    print("6. Find topper")
    print("7. Class average")
    print("8. Sort by marks")
    print("9. Exit")
    
    choice=input("Enter your choice: ")
    if choice=='1':
        add_student()
    elif choice=='2':
        display_student()
    elif choice=='3':
        search_student()
    elif choice=='4':
        update_marks()
    elif choice=='5':
        delete_student()
    elif choice=='6':
        find_topper()
    elif choice=='7':
        class_average()
    elif choice=='8':
        sort_by_marks()
    elif choice=='9':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.\n")