# student_result.py

def get_student_data():
    """Responsibility 1: Gathering Input from User"""
    name = input("Enter student name: ")
    
    marks_input = input("Enter student marks separated by spaces (e.g., 45 60 70 50): ")
    marks = [int(m) for m in marks_input.split()]
    
    return name, marks

def calculate_total(marks):
    """Responsibility 2: Calculation Logic"""
    return sum(marks)

def calculate_average(marks):
    """Responsibility 2: Calculation Logic"""
    if not marks:
        return 0
    return sum(marks) / len(marks)

def determine_status(average):
    """Responsibility 3: Decision Logic"""
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

def display_student_result(name, total, average, status):
    """Responsibility 4: Presentation/Output Logic"""
    print("\n----- Student Report -----")
    print(f"Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Average: {average:.2f}")
    print(f"Final Status: {status}")
    print("--------------------------\n")

def main():

    student_name, student_marks = get_student_data()
    

    total = calculate_total(student_marks)
    avg = calculate_average(student_marks)
    

    status = determine_status(avg)
    

    display_student_result(student_name, total, avg, status)

if __name__ == "__main__":
    main()