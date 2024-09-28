#adds an expense to the 'expenses' list in main() function by using a dictionary
#Takes parameters and adds them to a dictionary in the 'expenses' list defined in the main() function
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    

#Outputs out each expense and its corresponding amount
#Takes 'expenses' as a perameter and iterates over it outputting out each expense and its corresponding amount
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
    
#Outputs the sum of all expenses
#Lambda function uses expense as an unknown and searches for 'amount' in whatever is specified in th map function )expenses)
#Map function makes this ^ happen for as many iterations as there are expenses and stores values in a list (each amount in expenses is stored in a list)
#Sum function adds up the values in the list
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
    
#Outputs total expense of specific category
#Takes 'expenses' list and category as perameters 
#Lambda function uses expense as an unknown and searches for 'category' in whatever is specified by the filter function (expenses)
#Filter function makes this ^ happen for as many iterations as there are expenses and creates a True/False list according to the condition of the logic statement 
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    


def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break

main()
