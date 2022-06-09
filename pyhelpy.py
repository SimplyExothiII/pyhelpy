import os
import os.path

# Basically importing shit.

try:

    class Account():
        def __init__(self, username, password):
            self.username = username
            self.password = password

    if os.path.isfile("username.txt") == True:
        f = open("username.txt", "r")
        print("[i] It seems you already made an account.", "Hello " + (f.read()) + ".")
        f.close()
        f = open("password.txt", "r")
        password1 = input("[+] Enter your password:")
        if password1 == f.read():
            f.close()
            f = open("username.txt", "r")
            print("[i] Ready to go,", f.read())
        else:
            print("[i] Password incorrect. Ending script...")
            os._exit(0)

    else:
        print("[i] Doesnt seem you have created an account.")
        Accountnew = Account(input("Insert username: "), input("Insert password: "))

        f = open("username.txt", "w")
        f.write(Accountnew.username)
        f.close()

        f = open("password.txt", "w")
        f.write(Accountnew.password)
        f.close()

        f = open("username.txt", "r")
        print("Hello,", f.read() + ".", "Youre ready to go.")

    # Accounting.

    def Folder():
        print("[?] Where do you want the folder to be in? (Directory)")
        directory1 = input("[+]: ")
        print("[?] Enter the name of the folder.")
        foldername = input("[+]: ")
        print("[...] Creating folder...")
        os.makedirs(directory1 + foldername)
        print("[i] Folder created in:", directory1 + foldername)

    # Functions.
except:
    print("[i] An error was caused. Ending script...")
    os._exit(0)