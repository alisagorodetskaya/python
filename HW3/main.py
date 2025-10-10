from employee import Employee
from manager import Manager

if __name__ == "__main__":
    e1 = Employee("Ivan", 30000, 28, 10)
    e2 = Employee("Olena", 25000, 26, 5)
    m1 = Manager("Maria", 40000, 30, 15, 5)
    m2 = Manager("Petro", 45000, 29, 10, 8)

    employees = [e1, e2, m1, m2]

    for emp in employees:
        print(f"Name: {emp.get_name()}")
        print(f"Monthly salary: {emp.calculate_monthly_salary():.2f} UAH")
        print(f"Bonus: {emp.calculate_bonus():.2f} UAH")
        if isinstance(emp, Manager):
            print(emp.report())
        print("-" * 50)
