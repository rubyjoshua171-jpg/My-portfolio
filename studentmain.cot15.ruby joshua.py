studentList = [] 
def printMenu():
  print("************************")
  print("Welcome to Student Marks")
  print("************************")
  print("1. Add new student")
  print("2. Add student marks")
  print("3. List students")
  print("4. Display marks per subject")
  print("5. Display marks")
  print("6. Display student Grand Total")
  print("7. Display SRC Members")
  print("0. Close")

def addStudent():
  name = input("Enter student name: ")
  surname = input("Enter student surname: ")
  grade = int(input("Enter student grade: "))
  age = int(input("Enter student age: "))
  src_input = input("SRC Member? y/n: ")

  is_src = src_input.strip().lower() in ["y", "yes"]

  student = Senior(name, surname, grade, age, is_src)
  studentList.append(student)
  print(f"Student {name} {surname} added successfully!")


def displayStudents():
  if not studentList:
    print("No students in the system yet.")
    return
  print("\n--- Student List ---")
  for i, student in enumerate(studentList, 1):
    print(f"{i}. {student.get_name()} {student.get_surname()}")


def displaySubjects(student_name):
  for student in studentList:
    if student.get_name().lower() == student_name.lower():
      subjects = student.get_subjects()
      if subjects:
        print(f"\nSubjects for {student.get_name()}:")
        for i, subject in enumerate(subjects, 1):
          print(f"{i}. {subject}")
        return subjects
      else:
        print(f"{student.get_name()} has no subjects yet.")
        return []
  print("Student not found.")
  return []


def addMarks(student_name, subject):
  for student in studentList:
    if student.get_name().lower() == student_name.lower():
      print(f"Enter 4 marks for {subject}:")
      marks = []
      for i in range(4):
        try:
          mark = float(input(f"Mark {i+1}: "))
          marks.append(mark)
        except ValueError:
          print("Invalid mark entered. Please try again.")
          return
      student.add_marks_to_subject(subject, marks)
      print(f"Marks added for {student.get_name()} in {subject}.")
      return
  print("Student not found.")


def main():
  while True:  
    printMenu()
    try:
      choice = int(input("What would you like to do? "))
      if choice == 1:
        addStudent()

      elif choice == 2:
        displayStudents()
        if studentList:
          student_name = input("Enter the students name: ")
          subjects = displaySubjects(student_name)
          if subjects:
            subject = input("Enter subject name: ")
          else:
            subject = input("Enter a new subject name: ")
          addMarks(student_name, subject)

      elif choice == 3:
        displayStudents()

      elif choice == 4:
        displayStudents()
        if studentList:
          student_name = input("Enter the students name: ")
          subjects = displaySubjects(student_name)
          if subjects:
            subject = input("Enter subject: ")
            for student in studentList:
              if student.get_name().lower() == student_name.lower():
                avg = student.avgPerSubject(subject)
                print(f"Average for {subject}: {avg:.2f}")
                break

      elif choice == 5:
        displayStudents()
        if studentList:
          student_name = input("Enter the students name: ")
          for student in studentList:
            if student.get_name().lower() == student_name.lower():
              subjects = student.get_subjects()
              print(f"\n--- Marks for {student.get_name()} {student.get_surname()} ---")
              if subjects:
                for subject in subjects:
                  avg = student.avgPerSubject(subject)
                  marks = ", ".join(str(m) for m in student.get_marks()[subject])
                  print(f"{subject}: {marks} (Avg: {avg:.2f})")
              else:
                print("This student has no marks yet.")
              break

      elif choice == 6:
        displayStudents()
        if studentList:
          student_name = input("Enter the students name: ")
          for student in studentList:
            if student.get_name().lower() == student_name.lower():
              total = student.grandTotal()
              print(f"Grand Total average for {student.get_name()}: {total:.2f}")
              break

      elif choice == 7:
        print("\n--- SRC Members ---")
        src_found = False
        for student in studentList:
          if student.get_is_src():
            print(f"{student.get_name()} {student.get_surname()}")
            src_found = True
        if not src_found:
          print("The name you entered is not in the scr plese try again...")

      elif choice == 0:
        print("Goodbye! Have a nice day!!!!")
        break

      else:
        print("Invalid selection, please try again , enter a number given above.")

    except ValueError:
      print("PLEASE Enter a valid input for what is ask above, your input is invalid")
if __name__ == "__main__":
  main()
