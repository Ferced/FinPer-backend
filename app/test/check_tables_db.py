#!/usr/bin/env python3
import sqlite3
def tables_in_sqlite_db(conn):
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [
        v[0] for v in cursor.fetchall()
        if v[0] != "sqlite_sequence"
    ]
    cursor.close()
    return tables
def print_content_from_table(conn,table_name):

	cursor = conn.execute('select * from '+table_name)
	names = list(map(lambda x: x[0], cursor.description))
	print (names)
	print (cursor.fetchall())
# Open database
conn = sqlite3.connect('../main/finper_main.db')

# List tables
tables = tables_in_sqlite_db(conn)

# Your code goes here!
# Example:
print(tables) # prints ['commands', 'packages']


print_content_from_table(conn,"credit_cards_details")