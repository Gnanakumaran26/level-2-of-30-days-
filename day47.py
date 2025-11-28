import hashlib
import json
import os
from cryptography.fernet import Fernet

# -------------------------------
# Generate or load encryption key
# -------------------------------

KEY_FILE = "secret.key"
DATA_FILE = "passwords.json"


def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return key


key = load_key()
fernet = Fernet(key)


# -------------------------------
# Save password (encrypted)
# -------------------------------
def save_password(service, username, password):
    encrypted_password = fernet.encrypt(password.encode()).decode()

    if not os.path.exists(DATA_FILE):
        data = {}
    else:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

    data[service] = {"username": username, "password": encrypted_password}

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print("✔ Password saved!")


# -------------------------------
# Load password (decrypt)
# -------------------------------
def load_password(service):
    if not os.path.exists(DATA_FILE):
        print("❌ No saved passwords found.")
        return

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    if service not in data:
        print("❌ Service not found!")
        return

    encrypted_pass = data[service]["password"]
    decrypted_pass = fernet.decrypt(encrypted_pass.encode()).decode()

    print("\n----------------------------------")
    print(f"Service  : {service}")
    print(f"Username : {data[service]['username']}")
    print(f"Password : {decrypted_pass}")
    print("----------------------------------\n")


# -------------------------------
# Main Program
# -------------------------------
while True:
    print("\n--- PASSWORD MANAGER ---")
    print("1. Save new password")
    print("2. Get saved password")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        service = input("Service Name: ")
        username = input("Username: ")
        password = input("Password: ")
        save_password(service, username, password)

    elif choice == "2":
        service = input("Enter service name: ")
        load_password(service)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
