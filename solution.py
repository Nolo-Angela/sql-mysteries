import sqlite3

#Jan 15 2018 SQL City

# Connect to the SQLite database
connect = sqlite3.connect("sql-murder-mystery.db")
cursor = connect.cursor() #create cursor

# Query the list of tables
cursor.execute("SELECT * FROM crime_scene_report WHERE city = 'SQL City' AND date=20180115")
clues = cursor.fetchall()

for clue in clues:
    print(clue)

print("=========================================================")

#find last house on Northwestern Dr
# and name containing Annabel that lives on Frankline Ave
cursor.execute("SELECT MAX(address_number) FROM person WHERE address_street_name='Northwestern Dr'")  
first_witness = cursor.fetchall()[0]

# for witness in first_witness:
#     print(witness)

cursor.execute("SELECT * FROM person WHERE address_number =?", (first_witness))
witness_1 = cursor.fetchone()
print(witness_1)
print("=============================================================")

cursor.execute("SELECT * FROM person WHERE address_street_name='Franklin Ave' AND name LIKE ?", (f"Annabel%",))
second_witness = cursor.fetchall()

for s in second_witness:
    print(s)

print("=============================================================")
cursor.execute("SELECT * FROM interview WHERE  person_id=14887 OR person_id = 16371")
#cursor.execute("SELECT * FROM interview WHERE person_id=16371")
interviews = cursor.fetchall()

for int in interviews:
    print(int)

connect.close()