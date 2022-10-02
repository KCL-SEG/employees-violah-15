"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, pay, time, have_bonus, bonus_quant, bonus_value):
        self.name = name
        self.contract = contract
        self.pay = pay
        self.time = time
        self.have_bonus = have_bonus
        self.bonus_quant = bonus_quant
        self.bonus_value = bonus_value
        self.commission_type = True

    def get_pay(self):
        if self.contract:
            total_pay = self.pay
        else:
            total_pay = self.pay * self.time

        if self.have_bonus:
            total_pay += self.bonus_quant * self.bonus_value

        return total_pay

    def __str__(self):
        if self.contract:
            description = f'{self.name} works on a monthly salary of {self.pay}'
        else:
            description = f'{self.name} works on a contract of {self.time} hours at {self.pay}/hour'

        if self.have_bonus:
            if self.commission_type:
                description += f' and receives a commission for {self.bonus_quant} contract(s) at {self.bonus_value}/contract'
            else:
                description += f' and receives a bonus commission of {self.bonus_value}'

        description += f'.  Their total pay is {self.get_pay()}.'
        return description

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', True, 4000, 1, False, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, 25, 100, False, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, 3000, 1, True, 4, 200)
renee.commission_type = True
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', False, 25, 150, True, 3, 220)
jan.commission_type = True
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, 2000, 1, True, 1, 1500)
robbie.commission_type = False
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', False, 30, 120, True, 1, 600)
ariel.commission_type = False
