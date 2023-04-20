import psycopg2, csv

conn = psycopg2.connect(
    host='localhost',
    dbname='Phonebook',
    user='postgres',
    password='20112004erkow',
    port = '6566'
)

def add_entry(name, phone):
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()

def search_entry(name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (name,))
    rows = cur.fetchall()
    cur.close()
    return rows

def delete_entry(pattern):
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", ('%'+pattern+'%', '%'+pattern+'%'))
    conn.commit()
    cur.close()

def display_entries():
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    cur.close()
    for row in rows:
        print(row)

def update_user(name, phone):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name = %s OR phone = %s", (name, phone))
    user = cur.fetchone()
    if user == None:
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    else:
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
    conn.commit()
    cur.close()

def upload_csv(filename):
    cur = conn.cursor()
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # Skip the header row
        for row in reader:
            name = row[0]
            phone = row[1]
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()

while True:
    print("Phonebook Program")
    print("1. Add Entry")
    print("2. Search Entry")
    print("3. Display Entries")
    print("4. Update Entry")
    print("5. Upload CSV File")
    print("6. Quit")
    print("7. Delete Entry")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_entry(name, phone)
    elif choice == '2':
        name = input("Enter name to search: ")
        rows = search_entry(name)
        for row in rows:
            print(row)
    elif choice == '3':
        display_entries()
    elif choice == '4':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        update_user(name, phone)
    elif choice == '5':
        filename = input("Enter CSV filename: ")
        upload_csv(filename)
    elif choice == '6':
        break
    elif choice == '7':
        pattern = input("Enter pattern of Entry, that you want to delete: ")
        delete_entry(pattern)
    else:
        print("Invalid choice. Please try again.")

conn.close()
