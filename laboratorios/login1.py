import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Lara1382",
    database="login_system"
)

cursor = db.cursor()

# registrar usuario
def register_user(username, password):
    try:
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(sql, (username, password))
        db.commit()
        print("User registered successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# login
def login_user(username, password):
    slq = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(slq, (username, password))
    result = cursor.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# menu
def main():
    print("Welcome to the login system!")
    print("1. Register")
    print("2. Login")
    option = int(input("Select an option: "))

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if option == 1:
        register_user(username, password)
    elif option == 2:
        login_user(username, password)
    else:
        print("Invalid option.")

main()