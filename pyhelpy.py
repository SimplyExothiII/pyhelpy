# It imports the os, random and os.path modules.
import os
import os.path
import random

absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)
print("[Hi] Script file path is {}, filename is {}".format(path, filename))
if os.path.isdir("jokes") == True:
    print("[Hi] Jokes folder found.")
    if os.listdir("jokes") == []:
        print("[Hi] No jokes in folder.")
    else:
        print("[Hi] Content in jokes folder found.")
else:
    print("[Hi] Jokes folder not found.")
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
        else:
            print("[i] Password incorrect. Ending script...")
            os._exit(0)

    else:
        print("[i] Doesnt seem you have created an account.")
        Accountnew = Account(input("[+] Insert username: "), input("[+] Insert password: "))

        f = open("username.txt", "w")
        f.write(Accountnew.username)
        f.close()

        f = open("password.txt", "w")
        f.write(Accountnew.password)
        f.close()

        f = open("username.txt", "r")


    # It creates a folder in a directory you specify.

    def Folder():
        print("[?] Where do you want the folder to be in? (Directory)")
        print("[i] Like so: /desired/path/")
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
        print("[i] Like so: /desired/path/")
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
                pyhelpy = 0
                os._exit(0)
            else:
                print("[i] Aw :C")
                os.remove("pyhelpy.py")
                pyhelpy = 0
                os._exit(0)
    
    # If the jokes folder exists, and there's content in it, then print a random joke from the folder.
    
    def Joke():
        if os.path.isdir("jokes") == True:
            if os.listdir("jokes") == []:
                print()
            else:
                print("[Hi] Content in jokes folder found.")
                npath = path + "/jokes/joke"
                jokena = random.choice('abcdefghi')
                f = open(npath + jokena + ".txt")
                print(f.read())
                f.close()
                ans9 = input("[+] Exit? Y/N: ")
        else:
            print()
        
    # It asks the user how their day was, and if they say it was bad, it asks if they want to hear a
    # joke.

    def Talk():
        f = open("username.txt", "r")
        print("[i] Hey", f.read() + ", how was your day?")
        ans5 = input("[+] (Good/Bad): ")
        if ans5 == "Good":
            f = open("username.txt", "r")
            print("[i] Happy to hear that,", f.read() + ".")
            print("[i] Im very sorry, but theres no more dialog due to my creator being without an idea for a longer talk after answering that you have a good day.")
        elif ans5 == "Bad":
            f = open("username.txt", "r")
            print("[i] Im sorry to hear that,", f.read() + ".", "Is there any way i can help?")
            ans6 = input("[+] (Y/N): ")
            if ans6 == "Y":
                print("[?] Do you wish to hear a joke?")
                ans7 = input("[+] (Y/N): ")
                if ans7 == "Y":
                    Joke()
                elif ans7 == "N":
                    print("[i] Oh, alright. Hope your day gets better!")
                else:
                    print("[i] Your answer is unclear. Remember that answers are case sensitive.")
            elif ans6 == "N":
                print("[i] Oh, alright. Hope your day gets better!")
            else:
                print("[i] Your answer is unclear. Remember that answers are case sensitive.")
        else:
            print("[i] Your answer was not entered correctly. Remember that answers are case sensitive.")


    pyhelpy = 1

    # Asking the user what function they want to use, then it runs the function.

    f.close()
    while pyhelpy > 0:   
        f = open("username.txt", "r")
        print("[?] Hello,", f.read() + ".", "How can i assist you? (Made by iv1x/SimplyExothiII, 2022)")
        print("[i] Functions: Folder, Self_destruct, File, Exit, Joke, Talk.")
        ans4 = input("[+] Choose function: ")
        if ans4 == "Folder":
            Folder()
        elif ans4 == "Self_destruct":
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
            os._exit(0)

# Catching any errors that may occur and ending the script.






except:
    print("[i] An error was caused. Ending script...")
    os._exit(0)
