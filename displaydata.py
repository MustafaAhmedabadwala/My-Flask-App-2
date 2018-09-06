#!/usr/bin/python

import sqlite3
from passlib.hash import sha256_crypt
conn = sqlite3.connect('test.db')
cursor = conn.execute('SELECT * FROM user')
results = cursor.fetchall()
print(results)
conn.close()
