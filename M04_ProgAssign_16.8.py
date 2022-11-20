"""
------------------------------------------------------------------------------------------------------------------------------------

 Program Name: Book Things To Do 16.8 - books.db 'title' query with SQLAlchemy

 GitHub Filepath: jlanier7/M04_SDEV220/M04_ProgAssign_16.8.py

 Author: Josh Lanier 

 SDEV 220

 11/19/22

 Program Purpose: To query table 'books' in SQLite database 'books.db' to return the title column in alphabetical order.
  
1. Imports

    - sqlalchemy as sa

2. Constants and variables:   

    INITIALIZED:

    - engine        (engine object)       sqlalchemy engine object, which facilitates connection to the database, and connection
                                          pooling
    - conn          (connection object)   sqlalchemy connection object, through which queries are executed
    
    IN-LINE:

    - metadate      (MetaData object)     sqlalchemy MetaData object for 'books' table
    - books         (Table object)        sqlalchemy Table object, creating and populating a table object for querying against
    - query         (not sure)            holds a query to run through the execute() function
    - queryResult   (CursorResult object) contains the result of the executed query
    - result        (list)                list of the data returned from the query results

3. Inputs

    none

4. Computations (pseudocode)

    import library

    create connection to database

    transfer existing table into program

    construct query FROM books SELECT title

    execute query

    gather data from query

    iterate and print data

5. Outputs   

    - iterated list of values in title column
    

------------------------------------------------------------------------------------------------------------------------------------
"""
# importing libraries

import sqlalchemy as sa

# initializing variables

# establishing connection to database and creating engine

engine = sa.create_engine('sqlite:///books.db')
conn = engine.connect()

# creating Table object with table 'books'

metadata = sa.MetaData()
books = sa.Table('books', metadata, autoload=True, autoload_with=engine)

# constructing query for column 'title'

query = sa.select([books.columns.title])

# executing query 

queryResult = conn.execute(query)
# also works as queryResult = conn.execute('SELECT title FROM books ')

# fetching data from query 

result = queryResult.fetchall()

# printing data from the query

print('The values in the title column are:')
for value in result:
    print(value)
