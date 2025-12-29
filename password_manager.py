import os, getpass, hashlib
from cryptography.fernet import Fernet

# Generate/load encryption key
if not os.path.exists("secret.key"):
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f: f.write(key)
cipher = Fernet(open("secret.key","rb").read())

MASTER_FILE="master.hash"

# Set master password
if not os.path.exists(MASTER_FILE):
    pw=getpass.getpass("Create master password: ")
    confirm=getpass.getpass("Confirm password: ")
    if pw!=confirm: exit("Passwords do not match!")
    with open(MASTER_FILE,"w") as f: f.write(hashlib.sha256(pw.encode()).hexdigest())

# Verify master password
pw=getpass.getpass("Enter master password: ")
with open(MASTER_FILE,"r") as f:
    if f.read()==hashlib.sha256(pw.encode()).hexdigest(): print("Access granted ✅")
    else: exit("Access denied ❌")
import json

VAULT_FILE = "vault.json"

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return {}
    with open(VAULT_FILE, "rb") as f:
        data = f.read()
        if data:
            return json.loads(cipher.decrypt(data))
        return {}

def save_vault(vault):
    encrypted = cipher.encrypt(json.dumps(vault).encode())
    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted)

def add_password():
    site = input("Website/App name: ")
    username = input("Username/Email: ")
    password = getpass.getpass("Password: ")
    vault = load_vault()
    vault[site] = {"username": username, "password": password}
    save_vault(vault)
    print("Password saved ✅")

def view_password():
    site = input("Enter Website/App name: ")
    vault = load_vault()
    if site in vault:
        print(f"Username: {vault[site]['username']}")
        print(f"Password: {vault[site]['password']}")
    else:
        print("No entry found ❌")

def delete_password():
    site = input("Enter Website/App name to delete: ")
    vault = load_vault()
    if site in vault:
        del vault[site]
        save_vault(vault)
        print("Password deleted ✅")
    else:
        print("No entry found ❌")

# Menu
while True:
    print("\n--- PASSWORD MANAGER ---")
    print("1. Add Password")
    print("2. View Password")
    print("3. Delete Password")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice=="1": add_password()
    elif choice=="2": view_password()
    elif choice=="3": delete_password()
    elif choice=="4": break
    else: print("Invalid choice ❌")
	
