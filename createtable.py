#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE user
         (firstname         TEXT    	NOT NULL,
         lastname            INT     	NOT NULL,
         email      		CHAR(50),
         password        	REAL);''')
print("Table created successfully");

conn.close()