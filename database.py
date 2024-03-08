import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('github_users.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create table for users
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Database setup complete.")