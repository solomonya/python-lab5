import sqlite3

def insert_contact(name, address, phone_number):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("INSERT INTO CONTACT_INFORMATION (NAME,ADDRESS,PHONE_NUMBER) \
VALUES (?,?,?)", (name,address,phone_number))
    conn.commit()
    conn.close()

def delete_contact_by_name(name):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("DELETE from CONTACT_INFORMATION where name = ?",(name,))
    conn.close()

def edit_address_by_name(name, address):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("UPDATE CONTACT_INFORMATION set ADDRESS = ? where NAME = ?", (name, address))
    conn.commit()
    conn.close()

def edit_phone_number_by_name(name, phone_number):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("UPDATE CONTACT_INFORMATION set ADDRESS = ? where NAME = ?", (name, phone_number))
    conn.close()

def retrieve_contacts():
    results = []
    conn = sqlite3.connect('contact_information.db')
    cursor = conn.execute("SELECT name, address, phone_number from CONTACT_INFORMATION")
    # Contact records are tuples and need to be converted into an array
    for row in cursor:
        results.append(list(row))
    return results