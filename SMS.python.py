students = []     
while True:
    print("\n" + "="*40)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("="*40)
    print("1 → Add New Student")
    print("2 → View All Students")
    print("3 → Search Student by Name")
    print("4 → Exit")

    try:
        choice = int(input("\nEnter your choice (1-4): "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 1:
        print("\n--- Add New Student ---")
        name = input("Enter student name     : ").strip().title()
        roll = input("Enter roll number      : ").strip()
        class_name = input("Enter class (ex: 10A) : ").strip().upper()
        phone = input("Enter phone number     : ").strip()

        # Create student dictionary
        student = {
            "name": name,
            "roll": roll,
            "class": class_name,
            "phone": phone
        }

        students.append(student)
        print(f"\nStudent '{name}' added successfully!")

    elif choice == 2:
        if not students:
            print("\nNo students found!")
        else:
            print("\n--- All Students ---")
            print("-"*50)
            print(f"{'Sr':<4} {'Roll':<10} {'Name':<20} {'Class':<8} {'Phone':<15}")
            print("-"*50)
            for i, s in enumerate(students, 1):
                print(f"{i:<4} {s['roll']:<10} {s['name']:<20} {s['class']:<8} {s['phone']:<15}")
            print("-"*50)

    elif choice == 3:
        if not students:
            print("\nNo students to search!")
        else:
            search_name = input("\nEnter name to search: ").strip().title()
            found = False
            print("\nSearch Results:")
            print("-"*50)
            for s in students:
                if search_name in s["name"]:
                    print(f"Name : {s['name']}")
                    print(f"Roll : {s['roll']}")
                    print(f"Class: {s['class']}")
                    print(f"Phone: {s['phone']}")
                    print("-"*50)
                    found = True
            if not found:
                print("No student found with that name!")

    elif choice == 4:
        print("\nThank you! bye.")
        break

    else:
        print("Invalid choice! Please select 1 to 4.")