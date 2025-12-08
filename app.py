import os
import sqlite3

DATABASE_PATH = os.environ.get("DATABASE_PATH", "/data/test_users.db")

def init_database():
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """)

    cursor.execute("INSERT INTO users (name, email) VALUES ('Anna Andersson', 'anna@test.se');")
    cursor.execute("INSERT INTO users (name, email) VALUES ('Bo Bengtsson', 'bo@test.se');")

    connection.commit()
    connection.close()
    print("Database initialized with test users")

def display_users():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    connection.close()

    if users:
        print("Current users in database:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    else:
        print("No users found in database.")

def clear_test_data():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users")
    connection.commit()
    connection.close()
    print("All test data cleared from the database.")

def anonymize_data():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("""
    UPDATE users
    SET name = 'Anonymized User', email = 'anon@example.com'
    """)
    connection.commit()
    connection.close()
    print("All user data anonymized.")

if __name__ == "__main__":
    print("Initializing database...")
    init_database()
    display_users()
    clear_test_data()
    display_users()
