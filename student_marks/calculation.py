def calculateTotal(marks):
    return sum(marks)


def calculateAverage(marks):
    return calculateTotal(marks) / len(marks)


def calculateGrade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"