'''
test_transactions runs unit and integration tests on the transactions module
(amount,category,date,description)

'''

import pytest
from transactions import Transactions, to_tra_dict

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transactions(dbfile)
    yield db


@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    tra1 = {'amount':20, 'category': 'food', 'date': '20220314', 'description': 'groceries'}
    tra2 = {'amount':30, 'category': 'food', 'date': '20220214', 'description': 'groceries'}
    tra3 = {'amount':40, 'category': 'food', 'date': '20220114', 'description': 'groceries'}
    id1=empty_db.add(tra1)
    id2=empty_db.add(tra2)
    id3=empty_db.add(tra3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.fixture
def med_db(small_db):
    ''' create a database with 10 more elements than small_db'''
    rowids=[]
    # add 10 categories
    for i in range(1, 11):
        s = str(i)
        tra ={'amount': 20 * i, 
            'category': 'food' + s,
            'date':'20220314',
            'description':'i love food '+s
            }
        rowid = small_db.add(tra)
        rowids.append(rowid)

    yield small_db

    # remove those 10 categories
    for j in range(10):
        small_db.delete(rowids[j])



@pytest.mark.simple
def test_to_tra_dict():
    ''' teting the to_tra_dict function '''
    a = to_tra_dict((20,'food','20220314', 'i love food'))
    assert a['amount']==20
    assert a['category']=='food'
    assert a['date'] == '20220314'
    assert a['description'] == 'i love food'
    assert len(a.keys())==4


@pytest.mark.add
def test_tra_add(med_db):
    ''' add a transaction to db, then select it, then compare it'''
    tra ={  'amount': 20,
            'category': 'food',
            'date':'20220314',
            'description':'i love food'
            }
    tras0 = med_db.select_all()
    rowid = med_db.add(tra)
    tras1 = med_db.select_all()
    assert len(tras1) == len(tras0) + 1
    tra1 = med_db.select_one(rowid)
    assert tra1['amount']==tra['amount']
    assert tra1['category']==tra['category']
    assert tra1['date']==tra['date']
    assert tra1['description']==tra['description']


@pytest.mark.delete
def test_tra_delete(med_db):
    ''' add a transaction to db, delete it, and see that the size changes'''
    # first we get the initial table
    tras0 = med_db.select_all()

    # then we add this transaction to the table and get the new list of rows
    tra0 ={  'amount': 20,
            'category': 'food',
            'date':'20220314',
            'description':'i love food'
            }
    rowid = med_db.add(tra0)
    tras1 = med_db.select_all()

    # now we delete the transaction and again get the new list of rows
    med_db.delete(rowid)
    tras2 = med_db.select_all()

    assert len(tras0) == len(tras2)
    assert len(tras2) == len(tras1)-1

@pytest.mark.update
def test_tra_update(med_db):
    ''' add a transaction to db, updates it, and see that it changes'''

    # then we add this transaction to the table and get the new list of rows
    tra0 ={ 'amount': 20,
            'category': 'food',
            'date':'20220314',
            'description':'i love food'
            }
    rowid = med_db.add(tra0)

    # now we update the transaction
    tra1 ={ 'amount': 30,
            'category': 'food',
            'date':'20220214',
            'description':'i love food a lot'
            }
    med_db.update(rowid,tra1)

    # now we retrieve the transaction and check that it has changed
    tra2 = med_db.select_one(rowid)
    assert tra1['amount']==tra2['amount']
    assert tra1['category']==tra2['category']
    assert tra1['date']==tra2['date']
    assert tra1['description']==tra2['description']

@pytest.mark.datesort
def test_date_sort(med_db):
    ''' add a transaction to db, updates it, and see that it changes'''

    # then we add this transaction to the table and get the new list of rows
    tra0 ={ 'amount': 20,
            'category': 'food',
            'date':'20210314',
            'description':'i love food'
            }
    rowid1 = med_db.add(tra0)
    tra1 ={ 'amount': 20,
            'category': 'food',
            'date':'20200314',
            'description':'i love food'
            }
    rowid2 = med_db.add(tra1)
    
    # now we retrieve the transaction and check that it has changed
    test_dict = med_db.date_sort()
    assert tra1['amount']==test_dict[0]["amount"]
    assert tra1['category']==test_dict[0]["category"]
    assert tra1['date']==test_dict[0]["date"]
    assert tra1['description']==test_dict[0]["description"]

@pytest.mark.amountsort
def test_amount_sort(med_db):
    ''' add a transaction to db, updates it, and see that it changes'''

    # then we add this transaction to the table and get the new list of rows
    tra0 ={ 'amount': 201,
            'category': 'food',
            'date':'20210314',
            'description':'i love food'
            }
    rowid1 = med_db.add(tra0)
    tra1 ={ 'amount': 202,
            'category': 'food',
            'date':'20200314',
            'description':'i love food'
            }
    rowid2 = med_db.add(tra1)
    
    # now we retrieve the transaction and check that it has changed
    test_dict = med_db.amount_sort()
    assert tra1['amount']==test_dict[0]["amount"]
    assert tra1['category']==test_dict[0]["category"]
    assert tra1['date']==test_dict[0]["date"]
    assert tra1['description']==test_dict[0]["description"]

    assert tra0['amount']==test_dict[1]["amount"]
    assert tra0['category']==test_dict[1]["category"]
    assert tra0['date']==test_dict[1]["date"]
    assert tra0['description']==test_dict[1]["description"]