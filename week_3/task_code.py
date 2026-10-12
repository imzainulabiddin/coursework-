class Employee:
    def __init__(self, active, months_employed, rating,
                 disciplinary_action, attendance):
        self.active = active
        self.months_employed = months_employed
        self.rating = rating
        self.disciplinary_action = disciplinary_action
        self.attendance = attendance

def eligibility(employee):
    if employee.active:
        if employee.months_employed >= 12:
            if employee.rating >= 4:
                if not employee.disciplinary_action:
                    if employee.attendance >= 90:
                        return True

    return False

normal_employee = Employee(True, 24, 4.5, False, 95)
boundary_employee = Employee(True, 12, 4, False, 90)
failed_employee = Employee(True, 11, 3, True, 85)

print(eligibility(normal_employee))
print(eligibility(boundary_employee))
print(eligibility(failed_employee))