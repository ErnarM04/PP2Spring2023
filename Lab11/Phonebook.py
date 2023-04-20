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

def delete_entry(pattern):
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", ('%'+pattern+'%', '%'+pattern+'%'))
    conn.commit()
    cur.close()

def display_entries(page):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    cur.close()
    i = 0
    limit = 10 * page
    for row in rows:
        if i < limit and i >= limit - 10:
            print(row)
        i+=1
    print(f"Page 1 / {len(rows) // 10 + 1}")
    page = input("Enter page or Q for quit: ")
    if page == "Q" or page == "q":
        page = 1000
    if int(page) >= 1 and int(page) <= len(rows) // 10 + 1:
        display_entries(page)

def search_entry(name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    rows = cur.fetchall()
    cur.close()
    return rows

def search_pattern(pattern):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", ('%'+pattern+'%', '%'+pattern+'%'))
    rows = cur.fetchall()
    cur.close()
    return rows

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

def many_users(name, phone):
    cur = conn.cursor()
    p = phone
    cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    phone = cur.fetchall()
    if phone == []:
        print(p, "does not exist")
    else:
        cur.execute("UPDATE phonebook SET name = %s WHERE phone = %s", (name, p))
    conn.commit()
    cur.close()

while True:
    print("Phonebook Program")
    print("1. Add Entry")
    print("2. Delete Entry")
    print("3. Display Entries")
    print("4. Search Entry")
    print("5. Search Entry by Pattern")
    print("6. Update Entry")
    print("7. Upload CSV File")
    print("8. Quit")
    print("9. Many Users")
    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_entry(name, phone)
    elif choice == '2':
        pattern = input("Enter pattern of Entry, that you want to delete: ")
        delete_entry(pattern)
    elif choice == '3':
        display_entries(1)
    elif choice == '4':
        name = input("Enter name to search: ")
        rows = search_entry(name)
        for row in rows:
            print(row)
    elif choice == '5':
        pattern = input("Enter pattern to search: ")
        rows = search_pattern(pattern)
        for row in rows:
            print(row)
    elif choice == '6':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        update_user(name, phone)
    elif choice == '7':
        filename = input("Enter CSV filename: ")
        upload_csv(filename)
    elif choice == '8':
        break
    elif choice == '9':
        while True:
            user = input("Enter username and phone number: ").split()
            if user[0] == "Q" or user[0] == "q":
                break
            many_users(user[0], user[1])
            print("Enter Q to quit")
    else:
        print("Invalid choice. Please try again.")

conn.close()