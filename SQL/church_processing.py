import sqlite3
import os
import sys
import pandas as pd

os.system('clear') # clear the terminal 

def do_SQL_table_count(table_name):
    sqliteConnection = None

    try:
        sqliteConnection = sqlite3.connect('mp_test.db', timeout=20)
        cursor = sqliteConnection.cursor()

        sqlite_select_query = f"SELECT count(*) from {table_name};"  # Use the table_name parameter
        cursor.execute(sqlite_select_query)
        totalRows = cursor.fetchone()[0]  # Extract the count value from the fetched row
        cursor.close()

        return totalRows  # Return the number of rows
    except sqlite3.OperationalError as error:
        return error

    except sqlite3.Error as error:
        return error

    finally:
        if sqliteConnection:
            sqliteConnection.close()

# Get count of a table
# result = do_SQL_table_count("ward_info")

# if isinstance(result, int):
#     print("Total rows:", result)
# else:
#     print("Error:", result)

# ------------
def getAllRows_demo():
    print()
    try:
        connection = sqlite3.connect('mp_test.db')
        cursor = connection.cursor()

        sqlite_select_query = """SELECT 
            Id, Preferred_Name, Unit, Address, Age, Baptism_Date, Birth_Country, Birthday, Birthplace, Callings, Confirmation_Date, Endowment_Date, 
            Endowment_Status, Gender, Has_Children, Individual_E_mail, Individual_Phone, Is_Convert, Is_Divorced, Is_Endowed, Is_Married, 
            Is_Returned_Missionary, Is_Sealed_to_Current_Spouse, Is_Single, Is_Widowed, Maiden_Name, Marriage_Date, Marriage_Status, Mission_Country, 
            Mission_Language, Move_In_Date, Ordination_Date, Priesthood, Priesthood_office, Sealing_to_Spouse, Spouse_Name, Temple_Recommend_Expiration_Date, 
            Temple_Recommend_Status, Temple_Recommend_Type, Unit_Abbreviation
            from ward_info"""

        cursor.execute(sqlite_select_query)
        df = pd.DataFrame(cursor.fetchall(), columns = [ \
            'Id', 'Preferred_Name', 'Unit', 'Address', 'Age', 'Baptism_Date', 'Birth_Country', 'Birthday', 'Birthplace', 'Callings', 'Confirmation_Date', 'Endowment_Date', \
                'Endowment_Status', 'Gender', 'Has_Children', 'Individual_E_mail', 'Individual_Phone', 'Is_Convert', 'Is_Divorced', 'Is_Endowed', 'Is_Married', \
            'Is_Returned_Missionary', 'Is_Sealed_to_Current_Spouse', 'Is_Single', 'Is_Widowed', 'Maiden_Name', 'Marriage_Date', 'Marriage_Status', 'Mission_Country', \
            'Mission_Language', 'Move_In_Date', 'Ordination_Date', 'Priesthood', 'Priesthood_office', 'Sealing_to_Spouse', 'Spouse_Name', 'Temple_Recommend_Expiration_Date', \
            'Temple_Recommend_Status', 'Temple_Recommend_Type', 'Unit_Abbreviation'])
        cursor.close()
        return df
    except sqlite3.OperationalError as error:
        return error
    except sqlite3.Error as error:
        return error
    finally:
        if connection:
            connection.close()

# Get all rows of a table
my_df = getAllRows_demo()
if isinstance(my_df, pd.DataFrame):
    # print(my_df)
    # print(my_df.Mission_Country.unique())

    filtered_df = my_df[my_df['Age'] > 60].sort_values('Age')
    print(filtered_df)


else:
    print("Error:", my_df)


def insertRow_old(fname, lname, street, city):
    try:
        connection = sqlite3.connect('mp_test.db')
        cursor = connection.cursor()
 
        sqlite_insert_query = """INSERT INTO address
                          (fname, lname, street, city) 
                           VALUES 
                          (?,?,?,?)"""

        data_tuble = (fname, lname, street, city)
        count = cursor.execute(sqlite_insert_query,data_tuble)
        connection.commit()
        print("Record inserted successfully into 'address' table ", cursor.rowcount)

        cursor.close()
    except sqlite3.OperationalError as error:
        print("Failed to connect to SQLite:", error)
        print()

    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if connection:
            connection.close()
            # print("The Sqlite connection is closed")

def insertRow(table_name, column_names, columns_placeholder, *args):
    try:
        connection = sqlite3.connect('mp_test.db')
        cursor = connection.cursor()

        sqlite_insert_query = f"INSERT INTO {table_name} {column_names} VALUES {columns_placeholder}"

        data_tuple = args  # Use *args to dynamically reference additional function arguments

        count = cursor.execute(sqlite_insert_query, data_tuple)
        connection.commit()
        print(cursor.rowcount, "record inserted successfully into '{}' table".format(table_name))

        cursor.close()
    except sqlite3.OperationalError as error:
        print("Failed to connect to SQLite:", error)
        print()
    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if connection:
            connection.close()

def insertMultipleRecords(recordList):
    try:
        connection = sqlite3.connect('mp_test.db')
        cursor = connection.cursor()
 
        sqlite_insert_query = """INSERT INTO address
                          (fname, lname, street, city) 
                           VALUES 
                          (?,?,?,?)"""

        count = cursor.executemany(sqlite_insert_query,recordList)
        connection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into 'address' table")
    
        cursor.close()
    except sqlite3.OperationalError as error:
        print("Failed to connect to SQLite:", error)
        print()

    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if connection:
            connection.close()
            # print("The Sqlite connection is closed")

# insertRow_old('John','Baker','25 Nowhere Ave SE','Calgary')

# recordsToInsert = [('Ann','Dalen','56 Somewhere Ave SE','Okotoks'),
#                    ('Lee','Draden','422 Main Street','High River'),
#                    ('Phil','Elway','8738 112nd Ave','Edmonton')]

# insertMultipleRecords(recordsToInsert)

def getAllRows():
    try:
        connection = sqlite3.connect('mp_test.db')
        cursor = connection.cursor()

        sqlite_select_query = """SELECT * from address"""
        cursor.execute(sqlite_select_query)
        df = pd.DataFrame(cursor.fetchall(), columns = ['fname', 'lname', 'street', 'city'])
        print (df)

        cursor.close()
    except sqlite3.OperationalError as error:
        print("Failed to connect to SQLite:", error)
        print()

    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if connection:
            connection.close()
            # print("The Sqlite connection is closed")

# getAllRows()

# table_name = 'employees'
# column_names = '(fname, lname, age, address, salary)'
# columns_placeholder = '(?,?,?,?,?)'
# insertRow(table_name, column_names, columns_placeholder,'Cam','Fowler',49,'874 Windy Street',97500)

# ----
# check SQLite version
# Connect to an in-memory database
# conn = sqlite3.connect(':memory:')
# cursor = conn.cursor()

# # Execute a query to retrieve the SQLite version
# cursor.execute('SELECT sqlite_version();')
# version = cursor.fetchone()[0]

# # Print the SQLite version
# print("SQLite version:", version)

# # Close the connection
# conn.close()
# ----
