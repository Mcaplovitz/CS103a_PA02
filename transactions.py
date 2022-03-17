'''
transactions.py is a Object Relational Mapping to the transactions table

The ORM will work map SQL rows with the schema
    (item#,amount,category,date,description)
to Python Dictionaries.

This app will store the data in a SQLite database ~/tracker.db

'''
import sqlite3

def to_tra_dict(tra_tuple):
    ''' tra is a transaction tuple (item#, amount, category, date, description)'''
    tra = {'itemnum':tra_tuple[0], 'amount':tra_tuple[1], 'category':tra_tuple[2],'date':tra_tuple[3], 'description':tra_tuple[4]}
    return tra

def to_tra_dict_list(tra_tuples):
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [to_tra_dict(tra) for tra in tra_tuples]

class Transactions():
    ''' Transactions represents a table of transactions'''

    def __init__(self,dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (itemnum int, amount float, category text, date text, description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT itemnum,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tra_dict_list(tuples)

    def select_one(self,itemNums):
        ''' return a transaction with a specified rowid '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT itemnum,* from transactions where itemnum=(?)",(itemNums))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tra_dict(tuples[0])


    def add(self,item):
        ''' add a transaction to the transaction table.
            this returns the item number of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['itemnum'],item['amount'],item['category'],item['date'],item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def update(self,itemNum,item):
        ''' updates a transaction to the transactions table.
            this returns the number of the updated element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''UPDATE transactions
                        SET itemnum=(?), amount=(?), category=(?), date=(?), description=(?)
                        WHERE itemnum=(?);
        ''',(item['itemnum'],item['amount'],item['category'],item['dat'],item['description'],itemNum))
        con.commit()
        con.close()

    def delete(self,itemNum):
        ''' delete a transaction to the transactions table.
            this returns the item number of the deleted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE itemnum=(?);
        ''',(itemNum,))
        con.commit()
        con.close()
    
