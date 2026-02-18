# Brute Force Password Project

## Description

This project shows how a simple brute force attack works using Python.

The program tries many possible combinations until it finds the correct password.  
The goal of this project is to understand why short and simple passwords are not secure.

This project is only for educational purposes.

---

## How to Run the Program

1. Clone the repository:

   git clone https://github.com/pachecojromar-glitch/bruteforce-password.git

2. Go into the project folder:

   cd bruteforce-password

3. Run the program:

   python bruteforce.py

---

## Example Output

Password found: abcdefghij  
Attempts: 731  
Execution time: 0.0021 seconds  

---

## How It Works

The program:

- Defines a test password (for example: "abcdefghij")
- Uses lowercase letters as possible characters
- Tries all combinations starting from length 1
- Stops when it finds the correct password
- Shows the number of attempts and the time needed

---

## Reflection

If the password is short, the program finds it very fast.

But if the password has:

- 8 or more characters
- Uppercase letters
- Lowercase letters
- Numbers
- Symbols

The number of possible combinations becomes extremely large.

This means the attack could take years.

That is why strong passwords are very important in cybersecurity.
