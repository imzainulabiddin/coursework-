# salary_calculator.py

def gross_salary(basic, allow=0.0, bonus=0.0):
    return basic + allow + bonus

def net_salary(gross, deduct=0.0):
    return gross - deduct

def get_positive(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val >= 0:
                return val
            print("Amount cannot be negative. Enter 0 or more.")
        except ValueError:
            print("Invalid input! Numbers only.")

def display_summary(name, gross, deduct, net):
    print(f"\n--- Monthly Salary Summary ---\n"
          f"Employee Name : {name}\n"
          f"Gross Salary  : {gross:.2f}\n"
          f"Deductions    : {deduct:.2f}\n"
          f"Net Salary    : {net:.2f}")

def main():
    print("---- Employee Salary Calculator ----")
    
    name = ""
    while not name:
        name = input("Enter employee name: ").strip()
        if not name: print("Name cannot be empty.")

    basic = get_positive("Enter basic salary: ")
    allow = get_positive("Enter allowances (0 if none): ")
    bonus = get_positive("Enter bonus (0 if none): ")
    
    gross = gross_salary(basic, allow, bonus)
    
    while True:
        deduct = get_positive("Enter deductions (0 if none): ")
        if deduct <= gross:
            break
        print(f"Deductions cannot exceed gross salary ({gross:.2f}). Try again.")
        
    display_summary(name, gross, deduct, net_salary(gross, deduct))

if __name__ == "__main__":
    main()