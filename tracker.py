#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists

'''

from category import Category
import sys

from transactions import Transactions

transactions = Transactions('tracker.db')
category = Category('tracker.db')


# here is the menu for the tracker app

menu = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. Clear table
12. print this menu
13. summarize transactions by most expensive
'''




def process_choice(choice):

    if choice=='0':
        return
    elif choice=='1':
        cats = category.select_all()
        print_categories(cats)
    elif choice=='2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice=='3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid,cat)
    # Made By Fritz Duverglas
    elif choice =='4': #show transactions
        print_transactions(transactions.select_all())
    #Made by John Lervandal
    elif choice == '5':
        print("Add A Transaction To The Database!")
        amount = float(input("Please Input The Cost Of The Transaction: "))
        name = input("Please Input The Name of Category: ")
        date = input("Please Input The Date (yyyymmdd) This Item Was Bought: ")
        description = input("Please Input The Description of the Item: ")

        dicter = {'amount':amount, 'category':name, 'date': date, 'description':description}
        add = transactions.add(dicter)
        print("We Successfully Add Transction", add, "To The Database")

    #Made by John Lervandal
    elif choice == '6':
        deletion = int(input("Please Input The Number Of The Transaction You're Deleting: "))
        transactions.delete(deletion)
        print("We Have Sucessfully Deleted The Transaction From The Database")

    # elif choice == '7':  # summarize transactions by date

    elif choice == '8':  # summarize transactions by month
        # Made by Matthew Caplovitz
        mon = transactions.month_sort()
        print_transactions(mon)
    elif choice == '9':  # summarize transactions by year
        # Made by Matthew Caplovitz
        year = transactions.year_sort()
        print_transactions(year)
    # elif choice == '10':  # summarize transactions by category

    # elif choice == '11':  # Clear table

    elif choice == '12':  # print this menu  
        print(menu)
    elif choice == '13': #summarize by the top
        print_transactions(transactions.amount_sort())
    else:
         print("choice",choice,"not yet implemented")

    choice = input("> ")
    return(choice)


def toplevel():
    ''' handle the user's choice '''

    ''' read the command args and process them'''
    print(menu)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('bye')

#
# here are some helper functions
#

def print_transactions(items):
    ''' print the transactions '''
    if len(items)==0:
        print('no items to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-30s"%('item #','amount','category','date','description'))
    print('-'*50)
    counter = 1
    for item in items:
        lis = [x for x in list(item.values())]
        lis.insert(0, transactions.select_rowid(item))
        values = tuple(lis)
        counter += 1
        print("%-10s %-10s %-10s %-10s %-30s"%values)

def print_category(cat):
    print("%-3d %-10s %-30s"%(cat['rowid'],cat['name'],cat['desc']))

def print_categories(cats):
    print("%-3s %-10s %-30s"%("id","name","description"))
    print('-'*45)
    for cat in cats:
        print_category(cat)


# here is the main call!

toplevel()

