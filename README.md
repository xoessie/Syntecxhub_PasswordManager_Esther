# Password Manager Project

## Project Overview
This is a simple local password manager built with Python.
It allows users to securely store, view, and delete passwords using a master password.
All passwords are encrypted using Fernet (AES).

## Features
- Set and verify a master password
- Add passwords with username/email
- View stored passwords
- Delete passwords
- Encrypted storage in vault.json

## Tools & Libraries
- Python 3
- cryptography (Fernet)
- getpass, os, json, hashlib

## How to Run
1. Open terminal in project folder
2. Run: python3 password_manager.py
3. Enter master password
4. Use the menu to Add, View, Delete passwords

## Test Steps / Results
1. Add Password → example Gmail entry ✅
2. View Password → displayed correctly ✅
3. Delete Password → removed successfully ✅
4. Exit → program closed correctly ✅
