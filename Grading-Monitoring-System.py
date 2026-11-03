students = []


def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return None


def calculate_average(grades):
    if len(grades) == 0:
        return 0

    total = 0

    for grade in grades:
        total = total + grade["grade"]

    return total / len(grades)


def register_student():
    print("      REGISTER STUDENT      ")

    while True:
        student_id = input("Student ID (02-2627-000000): ")

        if len(student_id) == 14:
            if (student_id[0:2].isdigit() and
                    student_id[2] == "-" and
                    student_id[3:7].isdigit() and
                    student_id[7] == "-" and
                    student_id[8:14].isdigit()):

                duplicate_id = False

                for student in students:
                    if student["id"] == student_id:
                        duplicate_id = True
                        break

                if duplicate_id:
                    print("Student ID already registered.")
                else:
                    break

        else:
            print("Invalid Student ID!")
            print("Format: 02-2627-000000")

    while True:
        last_name = input("Last Name: ").strip()

        if last_name.replace(" ", "").isalpha():
            break
        else:
            print("Name must contain letters only.")

    while True:
        first_name = input("First Name: ").strip()

        if first_name.replace(" ", "").isalpha():
            break
        else:
            print("Name must contain letters only.")

    while True:
        middle_name = input("Middle Name: ").strip()

        if middle_name == "":
            break

        if middle_name.lower() == "n/a":
            middle_name = ""
            break

        if middle_name.replace(" ", "").isalpha():
            break
        else:
            print("Name must contain letters only.")

    if middle_name.lower() == "n/a":
        middle_name = ""

    name = last_name + ", " + first_name

    if middle_name != "":
        name = name + ", " + middle_name

    duplicate_name = False

    for student in students:
        old_name = student["name"].replace(" ", "").lower()
        new_name = name.replace(" ", "").lower()

        if old_name == new_name:
            duplicate_name = True
            break

    if duplicate_name:
        print("Student name already registered.")
        return

    while True:
        password = input("Password (8-16 characters): ")

        if len(password) >= 8 and len(password) <= 16:
            break

        print("Password must be 8 to 16 characters.")

    student = {
        "id": student_id,
        "name": name,
        "password": password,
        "grades": []
    }

    students.append(student)

    print("Student registered successfully!")


def record_grade():
    print("      RECORD GRADES      ")

    if len(students) == 0:
        print("No registered students.")
        return

    print("\nREGISTERED STUDENTS")
    print("-" * 55)
    print("No.".ljust(6), "Student ID".ljust(18), "Name")
    print("-" * 55)

    number = 1

    for student in students:
        print(
            str(number).ljust(6),
            student["id"].ljust(18),
            student["name"]
        )
        number = number + 1

    print("-" * 55)
    print("0. EXIT")

    while True:
        choice = input("Choose student: ")

        if choice == "0":
            return

        if choice.isdigit():
            choice = int(choice)

            if choice >= 1 and choice <= len(students):
                student = students[choice - 1]
                break

        print("Invalid choice.")

    subjects = [
        "Math",
        "Science",
        "English",
        "Filipino",
        "Araling Panlipunan",
        "MAPEH",
        "Edukasyon sa Pagkakatao (EsP)",
        "Technical Livelihood Education (TLE)"
    ]

    while True:
        print("SUBJECTS")

        number = 1

        for subject in subjects:
            print(number, ".", subject)
            number = number + 1

        print("9. BACK")

        choice = input("Choose subject: ")

        if choice == "9":
            return

        if choice.isdigit():
            choice = int(choice)

            if choice >= 1 and choice <= 8:

                subject = subjects[choice - 1]

                already_recorded = False

                for grade in student["grades"]:
                    if grade["subject"] == subject:
                        already_recorded = True
                        break

                if already_recorded:
                    print("Grade for", subject, "is already recorded.")

                else:
                    while True:
                        grade = input(subject + " grade: ")

                        if grade.isdigit():
                            grade = int(grade)

                            if grade >= 0 and grade <= 100:
                                student["grades"].append({
                                    "subject": subject,
                                    "grade": grade
                                })

                                print("Grade recorded successfully.")
                                break
                            else:
                                print("Grade must be from 0 to 100.")
                        else:
                            print("Please enter a number.")

            else:
                print("Invalid choice.")

        else:
            print("Invalid choice.")


def update_grade():
    print("       UPDATE GRADE")

    while True:
        if len(students) == 0:
            print("No registered students.")
            return

        print("     REGISTERED STUDENTS     ")
        print("-" * 60)
        print("No.".ljust(6), "Student ID".ljust(20), "Name")
        print("-" * 60)

        number = 1

        for student in students:
            print(
                str(number).ljust(6),
                student["id"].ljust(20),
                student["name"]
            )
            number = number + 1

        print("-" * 60)
        print("0. BACK")

        choice = input("Choose student: ")

        if choice == "0":
            return

        if choice.isdigit():
            choice = int(choice)

            if choice >= 1 and choice <= len(students):
                student = students[choice - 1]
            else:
                print("Invalid choice.")
                continue
        else:
            print("Invalid choice.")
            continue

        while True:
            if len(student["grades"]) == 0:
                print("No grades recorded.")
                break

            print("-" * 55)
            print("No.".ljust(6), "Subject".ljust(40), "Grade")
            print("-" * 55)

            for i in range(len(student["grades"])):
                print(
                    str(i + 1).ljust(6),
                    student["grades"][i]["subject"].ljust(40),
                    str(student["grades"][i]["grade"])
                )

            print("-" * 55)

            choice = input("Choose grade number: ")
            print("0. BACK")

            if choice == "0":
                break

            if choice.isdigit():
                choice = int(choice)

                if choice >= 1 and choice <= len(student["grades"]):
                    while True:
                        new_grade = input("Enter new grade: ")

                        if new_grade.isdigit():
                            new_grade = int(new_grade)

                            if new_grade >= 0 and new_grade <= 100:
                                student["grades"][choice - 1]["grade"] = new_grade

                                print("Grade updated successfully!")

                                if new_grade < 75:
                                    print("Status: Failed")
                                else:
                                    print("Status: Passed")

                                break
                            else:
                                print("Grade must be from 0 to 100.")
                        else:
                            print("Please enter a number.")
                else:
                    print("Invalid grade number.")
            else:
                print("Invalid choice.")


def view_grades():
    print("\n" + "-" * 120)

    print(
        f"{'Name':<28}"
        f"{'Math':<10}"
        f"{'English':<10}"
        f"{'Science':<10}"
        f"{'Filipino':<10}"
        f"{'AP':<10}"
        f"{'MAPEH':<10}"
        f"{'EsP':<10}"
        f"{'TLE':<10}"
        f"{'Average':<10}"
    )

    print("-" * 120)

    subjects = [
        "Math", "English", "Science", "Filipino",
        "Araling Panlipunan", "MAPEH",
        "Edukasyon sa Pagkakatao (EsP)",
        "Technical Livelihood Education (TLE)"
    ]

    for student in students:
        row = f"{student['name']:<28}"
        total = 0
        count = 0

        for subject in subjects:
            subject_total = 0
            subject_count = 0

            for grade in student["grades"]:
                if grade["subject"] == subject:
                    subject_total = subject_total + grade["grade"]
                    subject_count = subject_count + 1

            if subject_count > 0:
                subject_average = subject_total / subject_count
                row = row + f"{round(subject_average, 2):<10}"
                total = total + subject_total
                count = count + subject_count
            else:
                row = row + f"{'-':<10}"

        if count > 0:
            average = total / count
            row = row + f"{round(average, 2):<10}"
        else:
            row = row + f"{'No grades':<10}"

        print(row)

    print("-" * 120)


def view_student_grades(student):
    print("      MY GRADES      ")

    print("Student ID:", student["id"])
    print("Student Name:", student["name"])

    if len(student["grades"]) == 0:
        print("No grades recorded.")
        return

    print("-----------------------------------------------")
    print("| Subject                                  | Grade |")
    print("-----------------------------------------------")

    total = 0

    for grade in student["grades"]:
        print(
            "|",
            grade["subject"].ljust(40),
            "|",
            str(grade["grade"]).ljust(5),
            "|"
        )

        total = total + grade["grade"]

    print("-----------------------------------------------")

    average = total / len(student["grades"])

    print("Average:", round(average, 2))

    if average < 75:
        print("Status: Failed")
    else:
        print("Status: Passed")


def teacher_menu():
    while True:
        print("      TEACHER MENU       ")
        print("1. Register Student")
        print("2. Record Grade")
        print("3. Update Grade")
        print("4. View Student Grades")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            record_grade()

        elif choice == "3":
            update_grade()

        elif choice == "4":
            view_grades()

        elif choice == "5":
            print("Logging out...")
            break

        else:
            print("Invalid choice!")


def student_menu(student):
    while True:
        print("      STUDENT MENU       ")
        print("1. View Grades")
        print("2. Logout")

        choice = input("Choose: ")

        if choice == "1":
            view_student_grades(student)


        elif choice == "2":
            print("Logging out...")
            break

        else:
            print("Invalid choice!")


def teacher_login():
    print("      TEACHER LOGIN        ")

    username = input("Username: ")
    password = input("Password: ")

    if username.lower() == "admin" and password == "1234":
        print("Login successful!")
        teacher_menu()

    else:
        print("Wrong username or password!")


def student_login():
    print("      STUDENT LOGIN        ")

    student_id = input("Student ID: ")
    password = input("Password: ")

    student = find_student(student_id)

    if student == None:
        print("Student not found!")

    elif password == student["password"]:
        print("Login successful!")
        print("Welcome,", student["name"])
        student_menu(student)

    else:
        print("Wrong password!")


def login():
    while True:
        print("      GRADING MONITORING SYSTEM        ")
        print("1. Teacher Login")
        print("2. Student Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            teacher_login()

        elif choice == "2":
            student_login()

        elif choice == "3":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice!")


login()