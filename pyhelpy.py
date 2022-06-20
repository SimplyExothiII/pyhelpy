# It imports the os, random, time and os.path modules.
import os
import os.path
import random
import time

print("[i] Made by iv1x/SimplyExothiII 2022")
time.sleep(1)
print("[Hi] ver 1.2.0")
time.sleep(1)
absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)
print("[Hi] Script file path is {}, filename is {}".format(path, filename))
time.sleep(1)
if os.path.isdir("jokes") == True:
    print("[Hi] Jokes folder found.")
    if os.listdir("jokes") == []:
        print("[Hi] No jokes in folder.")
    else:
        print("[Hi] Content in jokes folder found.")
else:
    print("[Hi] Jokes folder not found.")
time.sleep(1)
try:

    # It checks if the user has already made an account, if they have, it asks for the password, if
    # the password is correct, it says "Ready to go, username", if the password is incorrect, it ends
    # the script. If the user has not made an account, it asks for a username and password, then
    # creates a file with the username and password, then says "Hello, username. You're ready to go."
    
    class Account():
        def __init__(self, username, password):
            self.username = username
            self.password = password

    if os.path.isfile("username.txt") == True and os.path.isfile("password.txt") == True:
        f = open("username.txt", "r")
        print("[i] It seems you already made an account.")
        time.sleep(2)
        f.close()
        f = open("password.txt", "r")
        password1 = input("[+] Enter your password: ")
        if password1 == f.read():
            f.close()
            f = open("username.txt", "r")
        else:
            print("[i] Password incorrect. Ending script...")
            time.sleep(4)
            os._exit(0)
    elif os.path.isfile("username.txt") == True and os.path.isfile("password.txt") == False:
        print("[i] You have a username, but no password.")
        time.sleep(2)
        f = open("username.txt")
        Passwordnew = Account(f.read(), input("[+] Insert desired password: "))
        f.close()
        
        f = open("password.txt", "w")
        f.write(Passwordnew.password)
        f.close()
        time.sleep(2)
    elif os.path.isfile("username.txt") == False and os.path.isfile("password.txt") == True:
        print("[i] You have a password, but no username.")
        time.sleep(2)
        f = open("password.txt")
        Usernamenew = Account(input("[+] Insert desired username: "), f.read())
        f.close()

        f = open("username.txt", "w")
        f.write(Usernamenew.username)
        f.close()
        time.sleep(2)
    else:
        print("[i] Doesnt seem you have created an account.")
        Accountnew = Account(input("[+] Insert username: "), input("[+] Insert password: "))

        f = open("username.txt", "w")
        f.write(Accountnew.username)
        f.close()

        f = open("password.txt", "w")
        f.write(Accountnew.password)
        f.close()
        time.sleep(5)
    # It creates a folder in a directory you specify.

    def Folder():
        print("[?] Where do you want the folder to be in? (Directory)")
        time.sleep(1)
        print("[i] Like so: /desired/path/")
        time.sleep(1)
        directory1 = input("[+]: ")
        time.sleep(2)
        print("[?] Enter the name of the folder.")
        time.sleep(1)
        foldername = input("[+]: ")
        time.sleep(2)
        print("[...] Creating folder...")
        time.sleep(5)
        os.makedirs(directory1 + foldername)
        print("[i] Folder created in:", directory1 + foldername)
        time.sleep(6)
    # Creates a file in a directory you specify.

    def File():
        print("[?] Enter the file name.")
        time.sleep(1)
        filename1 = input("[+]: ")
        time.sleep(2)
        print("[?] Enter the directory you want the file in.")
        print("[i] Like so: /desired/path/")
        time.sleep(1)
        directory2 = input("[+]: ")
        time.sleep(2)
        if os.path.isdir(directory2) == False:
            os.makedirs(directory2)
            f = open(directory2 + filename1 + ".txt", "w")
            print("[?] Do you want content in the file?")
            time.sleep(1)
            ans1 = input("[+] Y/N: ")
            time.sleep(2)
            if ans1 == "Y":
                f.write(input("[+] Enter the content of the file: "))
                print("[i] Creating file...")
                time.sleep(4)
                print("[i] File created.")
                time.sleep(2)
            else:
                print("[i] Creating file...")
                time.sleep(4)
                print("[i] File created.")
                time.sleep(2)
        else:
            f = open(directory2 + filename1 + ".txt", "w")
            print("[?] Do you want content in the file?")
            ans1 = input("[+] Y/N: ")
            time.sleep(2)
            if ans1 == "Y":
                f.write(input("[+] Enter the content of the file: "))
                print("[i] Creating file...")
                time.sleep(4)
                print("[i] File created.")
                time.sleep(2)
            else:
                print("[i] File created.")
                time.sleep(2)
    # Deletes itself. 

    def Self_destruct():
        print("[?] Are you sure?")
        ans2 = input("[+] Y/N: ")
        time.sleep(1)
        if ans2 == "Y":
            print("[?] Wait, do you like me atleast?")
            ans3 = input("[+] Y/N: ")
            time.sleep(1)
            if ans3 == "Y":
                print("[i] Yay :D")
                os.remove("pyhelpy.py")
                pyhelpy = 0
                os._exit(0)
            else:
                print("[i] Aw :C")
                os.remove("pyhelpy.py")
                pyhelpy = 0
                os._exit(0)
        elif ans2 == "N":
            print("[i] Alright.")
            time.sleep(2)
    # If the jokes folder exists, and there's content in it, then print a random joke from the folder.
    
    def Joke():
        if os.path.isdir("jokes") == True:
            if os.listdir("jokes") == []:
                print("[i] No jokes inside of the jokes folder.")
                time.sleep(2)
            else:
                npath = path + "/jokes/joke"
                jokena = random.choice('abcdefghi')
                fullthing = npath + jokena
                if os.path.isfile(fullthing + ".txt") == True:
                    f = open(fullthing + ".txt")
                    print(f.read())
                    f.close()
                    time.sleep(4)
                    ans9 = input("[+] Exit? Y/N: ")
                    time.sleep(2)
                else:
                    print("[Hi]", fullthing + ".txt not found.")
                    time.sleep(2)
        else:
            print("[i] No jokes folder.")
            time.sleep(2)
    # It asks the user how their day was, and if they say it was bad, it asks if they want to hear a
    # joke.

    def Talk():
        f = open("username.txt", "r")
        print("[i] Hey", f.read() + ", how was your day?")
        time.sleep(2)
        ans5 = input("[+] (Good/Bad): ")
        time.sleep(1)
        if ans5 == "Good":
            f = open("username.txt", "r")
            print("[i] Happy to hear that,", f.read() + ".")
            time.sleep(2)
            print("[i] Im very sorry, but theres no more dialog due to my creator being without an idea for a longer talk after answering that you have a good day.")
            time.sleep(7)
        elif ans5 == "Bad":
            f = open("username.txt", "r")
            print("[i] Im sorry to hear that,", f.read() + ".", "Is there any way i can help?")
            time.sleep(3)
            ans6 = input("[+] (Y/N): ")
            time.sleep(1)
            if ans6 == "Y":
                print("[?] Do you wish to hear a joke?")
                time.sleep(2)
                ans7 = input("[+] (Y/N): ")
                if ans7 == "Y":
                    Joke()
                elif ans7 == "N":
                    print("[i] Oh, alright. Hope your day gets better!")
                    time.sleep(2)
                else:
                    print("[i] Your answer is unclear. Remember that answers are case sensitive.")
                    time.sleep(3)
            elif ans6 == "N":
                print("[i] Oh, alright. Hope your day gets better!")
                time.sleep(2)
            else:
                print("[i] Your answer is unclear. Remember that answers are case sensitive.")
                time.sleep(3)
        else:
            print("[i] Your answer was not entered correctly. Remember that answers are case sensitive.")
            time.sleep(4)

    def FunFact():
        time.sleep(2)
        print("[i] Im sorry. But currently there is no fun fact to be shown.")
        time.sleep(4)
        print("[i] If you want to give me a fun fact to add here, reply to the tweet that says")
        print("[i] Day 4 of #Python")
        time.sleep(6)

    pyhelpy = 1
    # Asking the user what function they want to use, then it runs the function.

    f.close()
    while pyhelpy > 0:   
        f = open("username.txt", "r")
        print("[?] Hello,", f.read() + ".", "How can i assist you?")
        time.sleep(2)
        print("[i] Functions: Folder, Self destruct, File, Exit, Joke, Talk.")
        ans4 = input("[+] Choose function: ")
        if ans4 == "Folder":
            Folder()
        elif ans4 == "Self destruct":
            Self_destruct()
        elif ans4 == "File":
            File()
        elif ans4 == "Talk":
            Talk()
        elif ans4 == "Joke":
            Joke()
        elif ans4 == "Exit":
            f = open("username.txt", "r")
            print("[i] Bye,", f.read() + ".")
            time.sleep(2)
            os._exit(0)
# Catching any errors that may occur and ending the script.

except:
    print("[i] An error was caused. Ending script...")
    time.sleep(4)
    os._exit(0)
