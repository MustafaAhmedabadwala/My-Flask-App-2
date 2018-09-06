#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute("DROP TABLE user;")
conn.commit()
print ("TABLE dropped :", conn.total_changes)

conn.close()
