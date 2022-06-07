# After you write all your classes, use this file to call them all together and run your program
from classes.budget import Budget 
from classes.budget_category import Bugdet_Category

jons_budget = Budget("Jon's Budget")
looping_var = True

# print(school.staff)
# print(school.students)


while looping_var:

    mode = input("\nWhat would you like to do?\nOptions:\n1. Update monthly income\n2. Create new transactions\n3. View monthly costs\n4. View expense distributions\n5. View budget details\n6. Quit\n>>") 

    if mode == '1':
        jons_budget.update_income()

    elif mode == '2':
        jons_budget.add_transaction()
        jons_budget.save_transaction()

    elif mode == '3':
        for item in jons_budget.transaction_list:
            print(item)
        print(f'Total spent: ${jons_budget.amount_spent()}')

    elif mode == '4':
        print(jons_budget.transaction_list) 
    
    elif mode == '5':
        print(jons_budget) 

    elif mode == '6':
        looping_var = False

    else:
        pass 