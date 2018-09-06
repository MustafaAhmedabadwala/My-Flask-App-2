import sqlite3
import hashlib
email='user@user.com'
password1='12345'
password = hashlib.md5(password1.encode())
password = (password.hexdigest())
conn = sqlite3.connect('test.db')
cursor = conn.execute("SELECT email,password from user WHERE email=(?) AND password=(?)",(email,password,))
for row in cursor:
   if(row[0]==email):
      return render_template("result.html")
   else:
      return render_template("login.html")
conn.close()
