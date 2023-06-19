import sqlite3
import os
os.system('clear') # clear the terminal 

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

readSqliteTable()
