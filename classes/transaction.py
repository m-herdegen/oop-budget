import csv 

class Transaction:

    id_num = 0

    def __init__(self, name, cost, category):
        self.name = name 
        self.cost = cost 
        self.category = category 


    def __str__(self):
        return f"*-*-*-*-*\nName: {self.name}\nCost: {self.cost}\nCategory: {self.category}\n*-*-*-*-*"

    @classmethod
    def increment_id_num(cls):
        cls.id_num += 0

    def get_cost(self):
        return int(self.cost)