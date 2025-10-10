class Employee:
    def __init__(self, name, salary_month, worked_days, bonus_percent=0):
        self._name = name
        self._salary_month = salary_month
        self._worked_days = worked_days
        self._bonus_percent = bonus_percent

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_salary(self):
        return self._salary_month

    def set_salary(self, salary):
        self._salary_month = salary

    def get_worked_days(self):
        return self._worked_days

    def set_worked_days(self, days):
        self._worked_days = days

    def get_bonus_percent(self):
        return self._bonus_percent

    def set_bonus_percent(self, percent):
        self._bonus_percent = percent

    def calculate_monthly_salary(self):
        return (self._salary_month / 30) * self._worked_days

    def calculate_bonus(self):
        return (self._salary_month / 100) * self._bonus_percent
