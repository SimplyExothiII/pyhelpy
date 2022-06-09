# It imports the os and os.path modules.
import os
import os.path

try:

    # It checks if the user has already made an account, if they have, it asks for the password, if
    # the password is correct, it says "Ready to go, username", if the password is incorrect, it ends
    # the script. If the user has not made an account, it asks for a username and password, then
    # creates a file with the username and password, then says "Hello, username. You're ready to go."
    
    class Account():
        def __init__(self, username, password):
            self.username = username
            self.password = password

    if os.path.isfile("username.txt") == True:
        f = open("username.txt", "r")
        print("[i] It seems you already made an account.", "Hello " + (f.read()) + ".")
        f.close()
        f = open("password.txt", "r")
        password1 = input("[+] Enter your password: ")
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

    # It creates a folder in a directory you specify.

    def Folder():
        print("[?] Where do you want the folder to be in? (Directory)")
        directory1 = input("[+]: ")
        print("[?] Enter the name of the folder.")
        foldername = input("[+]: ")
        print("[...] Creating folder...")
        os.makedirs(directory1 + foldername)
        print("[i] Folder created in:", directory1 + foldername)

    # Creates a file in a directory you specify.
    def File():
        print("[?] Enter the file name.")
        filename1 = input("[+]: ")
        print("[?] Enter the directory you want the file in.")
        directory2 = input("[+]: ")
        if os.path.isdir(directory2) == False:
            os.makedirs(directory2)
            f = open(directory2 + filename1 + ".txt", "w")
            print("[?] Do you want content in the file?")
            ans1 = input("[+] Y/N: ")
            if ans1 == "Y":
                f.write(input("[+] Enter the content of the file: "))
                print("[i] File created.")
            else:
                print("[i] File created.")
        else:
            f = open(directory2 + filename1 + ".txt", "w")
            print("[?] Do you want content in the file?")
            ans1 = input("[+] Y/N: ")
            if ans1 == "Y":
                f.write(input("[+] Enter the content of the file: "))
                print("[i] File created.")
            else:
                print("[i] File created.")
    # Deletes itself. 
    def Self_destruct():
        print("[?] Are you sure?")
        ans2 = input("[+] Y/N: ")
        if ans2 == "Y":
            print("[?] Wait, do you like me atleast?")
            ans3 = input("[+] Y/N: ")
            if ans3 == "Y":
                print("[i] Yay :D")
                os.remove("pyhelpy.py")
            else:
                print("[i] Aw :C")
                os.remove("pyhelpy.py")
    
    pyhelpy = 1
    # Asking the user what function they want to use, then it runs the function.
    f.close()
    while pyhelpy > 0:   
        f = open("username.txt", "r")
        print("[i] Hello,", f.read() + ".", "How can i assist you? (Made by iv1x/SimplyExothiII, 2022)")
        print("[i] Functions: Folder, Self_destruct, File, Exit")
        ans4 = input("[+] Choose function: ")
        if ans4 == "Folder":
            Folder()
        elif ans4 == "Self_destruct":
            Self_destruct()
        elif ans4 == "File":
            File()
        elif ans4 == "Exit":
            f = open("username.txt", "r")
            print("[i] Bye,", f.read() + ".")
            os._exit(0)
# Catching any errors that may occur and ending the script.
except:
    print("[i] An error was caused. Ending script...")
    os._exit(0)
