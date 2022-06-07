from classes.budget_category import Bugdet_Category
from classes.transaction import Transaction
import csv
# from classes.transaction import Transaction

class Budget:
    def __init__(self, name):
        self.name = name
        self.income = 5400
        self.transaction_dict = {}
        self.transaction_list = []
        self.all_transactions()
        

    def __str__(self):
        return f"Name: {self.name}\nMonthly income: {self.income}\nAmount spent: {self.amount_spent()}"
    
    def update_income(self):
        income = input("please enter your monthly income: ")
        self.income = income 

    def all_transactions(self):
        self.transaction_list = []
        file_name = './data/transactions.csv'
        
        with open(file_name, newline='') as transaction_file:
            reader = csv.DictReader(transaction_file)

            for row in reader:
                self.transaction_list.append(Transaction(row['name'], row['cost'], row['category'] ))

                # if self.name in self.transaction_dict.keys():
                #     self.transaction_dict[self.name].append([{'name': row['name'], 'cost':row['cost'], 'category': row['category']}])
                # else:
                #     self.transaction_dict[self.name]=([{'name': row['name'], 'cost':row['cost'], 'category': row['category']}])

        transaction_file.close()
        return self.transaction_list

    def add_transaction(self):
        name = input("please enter a transaction name: ")
        cost = input("please enter the cost: ")
        category = input("please enter a transaction category: ")

        self.transaction_list.append(Transaction(name, cost, category))
        self.transaction_dict={'name': name, 'cost':cost, 'category': category}
        return self.transaction_dict
        

    def save_transaction(self):
        file_name = './data/transactions.csv'
        fields = ['name','cost','category']

        with open(file_name, 'a', newline='') as transaction_file:
            writer = csv.DictWriter(transaction_file, fieldnames=fields)
            writer.writerow(self.transaction_dict)
    
    # def remove_transaction(self, name):
    #     for i,item in enumerate(self.transaction_list):
    #         if name == item['name']:
    #             self.transaction_list.pop(i)

    def amount_spent(self):
        sum = 0
        updated_list = self.all_transactions()
        for item in updated_list:
            sum += item.get_cost()
        print(sum)
        return sum

    
