from employee import Employee

class Manager(Employee):
    bonus_amount = 500

    def __init__(self, name, salary_month, worked_days, bonus_percent=0, subordinates=0):
        super().__init__(name, salary_month, worked_days, bonus_percent)
        self._subordinates = subordinates

    def get_subordinates(self):
        return self._subordinates

    def set_subordinates(self, count):
        self._subordinates = count

    def report(self):
        return f"Manager {self._name} manages {self._subordinates} employees."

    def calculate_bonus(self):
        base_bonus = super().calculate_bonus()
        extra = self._subordinates * Manager.bonus_amount
        return base_bonus + extra
