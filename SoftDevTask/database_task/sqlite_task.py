import sqlite3

db = sqlite3.connect("contact.db")
cursor = db.cursor()
sql = """
    CREATE TABLE IF NOT EXISTS contacts (
    contact_id integer PRIMARY KEY,
    first_name text,
    last_name text,
    email text,
    phone text);
    """
cursor.execute(sql)
db.commit()

sql = """
    INSERT INTO contacts (first_name, last_name, email, phone)
    VAlUES ('Boris', 'Johnson', 'bj@number10.com', '12345678');
    """
cursor.execute(sql)
db.commit()

sql = "Select * from contacts"
cursor.execute(sql)
print(cursor.fetchall())

