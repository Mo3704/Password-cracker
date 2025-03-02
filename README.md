Password Cracker (Dictionary & Brute Force Attack) 

This program simulates a password-cracking tool using dictionary attack and brute-force attack.
It provides a GUI where the user enters:
Username
A 5-letter password (a-z , A-Z)
Then, the program tries to crack the password by checking a dictionary file first.
If the dictionary attack fails, it brute-forces all possible 5-letter passwords and displays each attempt in real-time.

Dictionary Attack Function:
reads each givem password in dictionary and compares it with user-given password.
If found, it prints the result and stops.
If not found, it proceeds to the brute-force attack.

Brute-Force Attack Function:
Generates all possible 5-letter passwords using itertools.product().
Displays each attempt in real-time in the GUI.
If a match is found, it stops the attack.


password dictionary refrence source :
https://github.com/danielmiessler/SecLists/blob/master/Passwords/Default-Credentials/default-passwords.txt
