from dataclasses import dataclass


# I've done this version on OOP bases this is more optimized and easy to read and understand version.

@dataclass
class Employee:
    active: bool
    months_employed: int
    rating: float
    disciplinary_action: bool
    attendance: float

    def is_eligible(self):
        return (
            self.active and
            self.months_employed >= 12 and
            self.rating >= 4 and
            not self.disciplinary_action and
            self.attendance >= 90
        )

# --- Testing ---
normal_employee = Employee(True, 24, 4.5, False, 95)
boundary_employee = Employee(True, 12, 4, False, 90)
failed_employee = Employee(True, 11, 3, True, 85)

print(normal_employee.is_eligible())   # True
print(boundary_employee.is_eligible()) # True
print(failed_employee.is_eligible())   # False
