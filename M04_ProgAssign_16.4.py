"""
------------------------------------------------------------------------------------------------------------------------------------

 Program Name: Book Things To Do 16.4 - books.db Creation

 GitHub Filepath: jlanier7/M04_SDEV220/M04_ProgAssign_16.4.py

 Author: Josh Lanier 

 SDEV 220

 11/19/22

 Program Purpose: To create a SQLite Database called 'books.db', create a Table in it called 'books', and then insert some records into the table.
  
1. Imports

    - sqlite3 as sq

2. Constants and variables:   

    INITIALIZED:

    - booksdb   (Connection object)     the connection object that creates the 'books.db' file
    - booksQuery(Cursor object)         the cursor object that query methods can be called against for 'books.db'

    IN-LINE:

    - response  (string)                response from user input for whether to delete old table, if it is yes, table is deleted
    - ins       (string)                in function 'insert()': the string portion minus the values for the query in the line beneath it
    - rows      (Cursor object method)  executes the fetchall() method for the booksQuery Cursor object to print in the next line
    
3. Inputs

    - user determines if they would like to delete the table: yes deletes table, no passes and program will produce error because table is 
            already created
            
4. Computations (pseudocode)

    import labraries

    connect to and create new database 'books.db'
    create cursor object to query database 'books.db'

    user input for whether table 'books' is to deleted
        if yes delete table

    create new table 'books' in database 'books.db'

    define function 'insert()' to abstract insertion of records into table
        define variable to hold string for first part of query
        execute INSERT query for values passed to it by function paramters
        if 'conf' parameter is True, print insertion confirmation message

    insert multiple records into table 'books'

    execute select all from books query 
    execute method to gather results
    print results

    commit changes to database

    close Cursor object
    close database connection

5. Outputs   

    - if user elected to delete table, confirmation message is printed
    - table creation confirmation message
    - if function insert() parameter 'conf' is set to True, insertion confirmation message is printed
    - print results from <line 88> select all from 'books' table query
    

------------------------------------------------------------------------------------------------------------------------------------
"""
# importing libraries

import sqlite3 as sq

# initializing variables

booksdb = sq.connect('books.db')
booksQuery = booksdb.cursor()

# table creation

#       error will raise if creation of new table is attempted without deleting already existing 'books' table
#       giving user the option to delete table allows to bypass that for this application
response = input("TABLE books already exists, would you like to delete the table 'books', so you can create it again? (yes or no) ")
if response.lower() == 'yes':
    booksQuery.execute('DROP TABLE IF EXISTS books')
    print('TABLE books dropped')

booksQuery.execute('''CREATE TABLE books
(title VARCHAR (100),
author VARCHAR (50),
year INT,
CONSTRAINT compositekey PRIMARY KEY (title, author))
''')
print('TABLE books created')

# table record insertion

def insert(title, author, year, conf=False):
    '''Inserts values for title, author, and year into Database book, with optional paramater 'conf' which will print confirmation message
    if set to True, default is false.'''
    ins = 'INSERT INTO books (title, author, year) VALUES (?, ?, ?)'
    booksQuery.execute(ins, (title, author, year))
    if conf == True:
        print(f'Inserted values for title={title}, author={author}, year={year}')
    else:
        pass
    # in future, would probably put connection.commit() at the end of this function
        
insert('The Weirdstone of Brisingamen','Alan Garner','1960', conf=True)
insert('Perdido Street Station','China Miéville','2000', conf=True)
insert('Thud!','Terry Pratchett','2005', conf=True)
insert('The Spellman Files','Lisa Lutz','2007', conf=True)
insert('Small Gods','Terry Pratchett','1992', conf=True) 

# table query to grab all values

booksQuery.execute('SELECT * FROM books')
rows = booksQuery.fetchall()
print('The records queried from TABLE books are: ', rows)

# commit changes to database

booksdb.commit()

# closing cursor object and connection

booksQuery.close()
booksdb.close()