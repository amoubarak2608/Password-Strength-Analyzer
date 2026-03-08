# Password Strength Analyzer

A command-line tool built in Python that analyzes the strength of a password and warns against commonly used passwords.

## Features
- Checks password length
- Detects uppercase, lowercase, numbers, and special characters
- Rates password as: Weak, Medium, Strong, or Very Strong
- Checks against a list of 100 most common passwords and warns the user

## How to Run
1. Make sure Python is installed
2. Clone this repo or download the files
3. Run in terminal:
python analyzer.py
4. Enter a password when prompted

## Example Output
Enter a password to analyze: Hello!234
Password: Hello!234
Length: 9
Has Uppercase: True
Has Lowercase: True
Has Numbers: True
Has Special Characters: True
Rating: strong

Enter a password to analyze: 123456
This password is very common and should not be used.

## Files
- analyzer.py - main program
- common_passwords.txt - list of 100 most common passwords

## Legal Notice
This tool is for educational purposes only.
