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

# Define a function to search for an entry by name
def search_entry(name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (name,))
    rows = cur.fetchall()
    cur.close()
    return rows

# Define a function to display all entries in the phonebook
def display_entries():
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    cur.close()
    for row in rows:
        print(row)

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
    print("2. Search Entry")
    print("3. Display Entries")
    print("4. Upload CSV File")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")

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
        filename = input("Enter CSV filename: ")
        upload_csv(filename)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()
