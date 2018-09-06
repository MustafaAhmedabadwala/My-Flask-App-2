#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute("DELETE from user where email='abcd02@admin.com';")
conn.commit()
print ("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT * from user")
for row in cursor:
   print ("First Name = ", row[0])
   print ("Last name = ", row[1])
   print ("Email = ", row[2])
   print ("password = ", row[3], "\n")

print ("Operation done successfully");
conn.close()
