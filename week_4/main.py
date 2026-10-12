from validation import validateMark
from calculation import calculateAverage, calculateGrade ,calculateTotal
from display import displayResult

def main():
    name = input("Enter student name: ")
    marks = []

    for i in range(3):
        mark = float(input(f"Enter marks for subject {i + 1}: "))

        while not validateMark(mark):
            print("Invalid marks. Enter 0-100.")
            mark = float(input(f"Enter marks for subject {i + 1}: "))

        marks.append(mark)

    total   = calculateTotal(marks)
    average = calculateAverage(marks)
    grade   = calculateGrade(average)

    displayResult(name, total, average, grade)
    
if __name__ == "__main__":
    main()