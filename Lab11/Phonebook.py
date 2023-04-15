import psycopg2, csv

# Connect to the database
conn = psycopg2.connect(
    host='localhost',
    dbname='Phonebook',
    user='postgres',
    password='20112004erkow',
    port = '6566'
)

# Define a function to add a new entry to the phonebook
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

# Define a function to display all entries in the phonebook
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

# Define a function to search for an entry by name
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
    cur.execute("SELECT COUNT(*) FROM phonebook WHERE name = %s", (name,))
    count = cur.fetchone()[0]
    if count == 0:
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    else:
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
    conn.commit()
    cur.close()

# Function to upload a CSV file into the phonebook table
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

# Main program loop
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
    choice = input("Enter your choice (1-8): ")

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
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()
