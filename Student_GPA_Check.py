# Andrew Tillotson
# File Name = Student_GPA_Check
# Decription: This app checks students names and GPAs. It will show if the student makes Deans list or Honors.
# https://github.com/Dewey20123/Module-2-Lab---Case-Study-if...else-and-while/blob/main/Student_GPA_Check.py
while True:
    last_name = input("Enter your students last name(or ZZZ to quit)")
    if last_name.upper() == 'ZZZ':
        print("Exiting student record processing.")
        break
    first_name = input("Enter your students first name ")
    try:
        gpa = float(input("Enter your students GPA "))
    except ValueError:
        print("Invaild GPA. Please enter a numeric value")
        continue
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Deans List.")

    elif gpa >= 3.25:
        print(f"{first_name}{last_name} has made the Honors Roll.")
    else:
        print(f"{first_name}{last_name} does not qualify for the Deans List or Honor Roll.")