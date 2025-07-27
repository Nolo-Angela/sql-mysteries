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
cursor.execute("SELECT MAX(address_number) FROM person WHERE address_street_name='Franklin Ave'")  
first_witness = cursor.fetchall()[0]

for witness in first_witness:
    print(witness)

cursor.execute("SELECT * FROM person WHERE address_street_name='Franklin Ave' AND address_number =?", (first_witness))
witness_1 = cursor.fetchall()

print(witness_1)


connect.close()