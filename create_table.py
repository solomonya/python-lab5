import sqlite3

conn = sqlite3.connect('contact_information.db')
query = (''' CREATE TABLE CONTACT_INFORMATION
            (NAME           TEXT    NOT NULL,
            ADDRESS        CHAR(50) NOT NULL,
            PHONE_NUMBER    INT);''')
conn.execute(query)
conn.close()