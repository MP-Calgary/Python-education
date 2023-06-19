import sqlite3
import os
import sys
import pandas as pd

os.system('clear') # clear the terminal 

# Add the folder to the system path containing the path to where package tabulate exists
# sys.path.insert(0, '/opt/homebrew/lib/python3.11/site-packages')

def readSqliteTable():
    sqliteConnection = None

    try:
        sqliteConnection = sqlite3.connect('acs-1-year-2015.sqlite', timeout=20)
        cursor = sqliteConnection.cursor()

        # sqlite_select_query = """SELECT count(*) from places;"""
        sqlite_select_query = "SELECT count(*) from states;"
        # sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        totalRows = cursor.fetchone()
        print("Total rows are:  ", totalRows)
        cursor.close()

    except sqlite3.OperationalError as error:
        print("Failed to connect to SQLite:", error)
        print()

    except sqlite3.Error as error:
        print("Failed to read data from SQLite table:", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")

# readSqliteTable()

def getAllRows():
    print()
    try:
        connection = sqlite3.connect('acs-1-year-2015.sqlite')
        cursor = connection.cursor()

        sqlite_select_query = """SELECT * from states"""
        cursor.execute(sqlite_select_query)
        df = pd.DataFrame(cursor.fetchall(), columns = ['year', 'name', 'geo_id', 'total_population', 'white', 'black', 'hispanic', 'asian', 'american_indian', \
            'pacific_islander', 'other_race', 'median_age', 'total_households', 'owner_occupied_homes_median_value', 'per_capita_income', \
            'median_household_income', 'below_poverty_line', 'foreign_born_population', 'state'])
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

getAllRows()