import sqlite3

#Connect to SQLite
connection=sqlite3.connect("student.db")

#Creating a cursor to insert record and creating table

cursor=connection.cursor()

# CREATING A TABLE

table_info="""
Create table STUDENT(NAME VARCHAR(25),
CLASS VARCHAR(25),
SECTION VARCHAR(25));
"""

cursor.execute(table_info)

# INSERTING RECORDS

cursor.execute('''Insert Into STUDENT values ('Soham','Data Science','MDS')''')
cursor.execute('''Insert Into STUDENT values ('Jayagna','Statistics','Btech')''')
cursor.execute('''Insert Into STUDENT values ('Priya','Data Science','MDS')''')
cursor.execute('''Insert Into STUDENT values ('Naman','Data Science','MDS')''')
cursor.execute('''Insert Into STUDENT values ('Utkarsh','Computer Science','MCS')''')
cursor.execute('''Insert Into STUDENT values ('Jayagna','ML','Btech')''')
cursor.execute('''Insert Into STUDENT values ('Soham','ML','MDS')''')
cursor.execute('''Insert Into STUDENT values ('Varun','Computer Science','MDS')''')
cursor.execute('''Insert Into STUDENT values ('Soham','Big Data','MDS')''')
cursor.execute('''Insert Into STUDENT values ('Priya','Big Data','MDS')''')
cursor.execute('''Insert Into STUDENT values ('Priya','ML','MDS')''')
cursor.execute('''Insert Into STUDENT values ('Sahil','Data Science','MDS')''')
cursor.execute('''Insert Into STUDENT values ('Naman','ML','MDS')''')
#DISPLAYING

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)
connection.commit()
connection.close()