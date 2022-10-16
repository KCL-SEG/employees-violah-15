"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, commission):
        self.name = name
        self.commission = commission

    def get_pay(self):
        total_pay = self.salary_calculation() + (self.commission.commission_payment if self.commission else 0)
        return total_pay

    def __str__(self):
        full_description = self.description() + (self.commission.description if self.commission else "") + f".  Their total pay is {self.get_pay()}."
        return full_description

class SalaryEmployee(Employee):
    def __init__(self, name, monthly_salary, commission=0):
        super().__init__(name, commission)
        self.monthly_salary = monthly_salary

    def salary_calculation(self):
        return self.monthly_salary

    def description(self):
        description = f'{self.name} works on a monthly salary of {self.monthly_salary}'
        return description

class HourlyEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_salary, commission=0):
        super().__init__(name, commission)
        self.hours_worked = hours_worked
        self.hourly_salary = hourly_salary

    def salary_calculation(self):
        return self.hours_worked * self.hourly_salary

    def description(self):
        description = f'{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_salary}/hour'
        return description

class BonusCommission:
    def __init__(self, bonus):
        self.description = f' and receives a bonus commission of {bonus}'
        self.commission_payment = bonus

class ContractCommission:
    def __init__(self, contract_number, pay_per_contract):
        self.description = f' and receives a commission for {contract_number} contract(s) at {pay_per_contract}/contract'
        self.commission_payment = contract_number * pay_per_contract


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee', 3000, ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan', 150, 25, ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie', 2000, BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel', 120, 30, BonusCommission(600))
