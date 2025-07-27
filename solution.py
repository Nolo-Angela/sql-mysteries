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
#find their interviews
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
print("=============================================================")
#find the killers gym info
"""
get fit gym
membership number starts with 48Z- gold memberhip
car plate- H42W
Jan.19
"""
cursor.execute("SELECT * FROM get_fit_now_check_in WHERE membership_id LIKE ? AND check_in_date LIKE ?", (f"48Z%", "%0109%"),)
check_in = cursor.fetchall()

for check in check_in:
    print(check)

print("=============================================================")
"""
find members
"""
member_info = ()
for check in check_in:
    cursor.execute("SELECT * FROM get_fit_now_member WHERE id LIKE ?", (f"{check[0]}%",))
    member = cursor.fetchall()
    print(member)

connect.close()