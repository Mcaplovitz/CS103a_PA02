'''
test_transactions runs unit and integration tests on the transactions module
(item#,amount,category,date,description)

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
    tra1 = {'itemnum':1,'amount':20, 'category': 'food', 'date': '3/14/2022', 'description': 'groceries'}
    tra2 = {'itemnum':2,'amount':30, 'category': 'food', 'date': '2/14/2022', 'description': 'groceries'}
    tra3 = {'itemnum':3,'amount':40, 'category': 'food', 'date': '1/14/2022', 'description': 'groceries'}
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
        tra ={'itemnum': i,
            'amount': 20 * i, 
            'category': 'food' + s,
            'date':'3/14/2022',
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
    ''' teting the to_cat_dict function '''
    a = to_tra_dict((1,20,'food','3/14/2022', 'i love food'))
    assert a['itemnum']==1
    assert a['amount']==20
    assert a['category']=='food'
    assert a['date'] == '3/14/2022'
    assert a['description'] == 'i love food'
    assert len(a.keys())==5


@pytest.mark.add
def test_tra_add(med_db):
    ''' add a category to db, the select it, then delete it'''

    tra ={'itemnum': 1,
            'amount': 20,
            'category': 'food',
            'date':'3/14/2022',
            'description':'i love food '
            }
    tras0 = med_db.select_all()
    rowid = med_db.add(tra)
    print(rowid)
    tras1 = med_db.select_all()
    assert len(tras1) == len(tras0) + 1
    tra1 = med_db.select_one(rowid)
    assert tra1['itemnum']==tras0['itemnum']
    assert tra1['amount']==tras0['amount']
    assert tra1['category']==tras0['category']
    assert tra1['date']==tras0['date']
    assert tra1['description']==tras0['description']


# @pytest.mark.delete
# def test_delete(med_db):
#     ''' add a category to db, delete it, and see that the size changes'''
#     # first we get the initial table
#     cats0 = med_db.select_all()

#     # then we add this category to the table and get the new list of rows
#     cat0 = {'name':'testing_add',
#             'desc':'see if it works',
#             }
#     rowid = med_db.add(cat0)
#     cats1 = med_db.select_all()

#     # now we delete the category and again get the new list of rows
#     med_db.delete(rowid)
#     cats2 = med_db.select_all()

#     assert len(cats0)==len(cats2)
#     assert len(cats2) == len(cats1)-1

# @pytest.mark.update
# def test_update(med_db):
#     ''' add a category to db, updates it, and see that it changes'''

#     # then we add this category to the table and get the new list of rows
#     cat0 = {'name':'testing_add',
#             'desc':'see if it works',
#             }
#     rowid = med_db.add(cat0)

#     # now we upate the category
#     cat1 = {'name':'new cat','desc':'new desc'}
#     med_db.update(rowid,cat1)

#     # now we retrieve the category and check that it has changed
#     cat2 = med_db.select_one(rowid)
#     assert cat2['name']==cat1['name']
#     assert cat2['desc']==cat1['desc']
