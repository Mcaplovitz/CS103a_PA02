'''
transactions.py is a Object Relational Mapping to the transactions table

The ORM will work map SQL rows with the schema
    (amount,category,date,description)
to Python Dictionaries.

This app will store the data in a SQLite database ~/tracker.db

'''
import sqlite3

def to_tra_dict(tra_tuple):
    ''' tra is a transaction tuple (amount, category, date, description)'''
    if len(tra_tuple) == 5:
        return {'amount':tra_tuple[1], 'category':tra_tuple[2],'date':tra_tuple[3], 'description':tra_tuple[4]}
    else:
        return {'amount':tra_tuple[0], 'category':tra_tuple[1],'date':tra_tuple[2], 'description':tra_tuple[3]}

def to_tra_dict_list(tra_tuples):
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [to_tra_dict(tra) for tra in tra_tuples]

class Transactions():
    ''' Transactions represents a table of transactions'''

    def __init__(self,dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (amount float, category text, date text, description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tra_dict_list(tuples)

    def select_one(self,rowid):
        ''' return a transaction with a specified rowid '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        # print(itemNums)
        cur.execute("SELECT rowid,* from transactions where rowid=(?)",(rowid,))
        tuples = cur.fetchall()
        # print(tuples[0])
        con.commit()
        con.close()
        return to_tra_dict(tuples[0])
    
    def select_rowid(self, item):
        ''' return a transaction with a specified rowid '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        # print(itemNums)
        cur.execute("SELECT rowid from transactions where amount=(?) and category=(?) and date=(?) and description=(?)",(item['amount'],item['category'],item['date'],item['description']))
        id = cur.fetchone()
        con.commit()
        con.close()
        return id[0]


    def add(self,item):
        ''' add a transaction to the transaction table.
            this returns the item number of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'],item['category'],item['date'],item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def update(self,rowid,item):
        ''' updates a transaction to the transactions table.
            this returns the number of the updated element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''UPDATE transactions
                        SET amount=(?), category=(?), date=(?), description=(?)
                        WHERE rowid=(?);
        ''',(item['amount'],item['category'],item['date'],item['description'],rowid))
        con.commit()
        con.close()

    def delete(self,rowid):
        ''' delete a transaction to the transactions table.
            this returns the item number of the deleted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE rowid=(?);
        ''',(rowid,))
        con.commit()
        con.close()
    
    def month_sort(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * FROM transactions ORDER BY substring(date,0)")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tra_dict(tuples)
    
    def year_sort(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * FROM transactions ORDER BY date[2:3]")
        
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tra_dict(tuples)

    def amount_sort(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * FROM transactions ORDER BY amount")
        
        tuples = cur.fetchall()
        con.commit()
        con.close() 
        return tuples