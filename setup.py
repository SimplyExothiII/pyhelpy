import time
import os
import platform
operatingsystem = platform.system()
print("[i] Hello! Welcome to the pyhelpy v.1.2.2 installer.")
time.sleep(3)
print("[i] Do you wish to start the installation?")
time.sleep(2)
ans1 = input("[+] Y/N: ")
if ans1 == "Y":
    f = open("pyhelpy.py", "w")
    print("installing main script...")
    time.sleep(2)
    f.write("""
# It imports the os, random, time and os.path modules.
import os
import os.path
import random
import time

print("[i] Made by iv1x/SimplyExothiII 2022")
time.sleep(1)
print("[Hi] ver 1.2.2")
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
        print("[i] I made this project for fun, but now i want to make it a proffessional one.")
        time.sleep(4)
        print("[i] If you want to give me a fun fact to add here, reply to the tweet that says")
        print("[i] Day 4 of #Python")
        print("[i] Or just message me about it on twitter")
        print("[i] Of course, i will credit you.")
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
    """)
    print("done")
    print("installing jokes...")
    time.sleep(1)
    print("creating folder...")
    os.makedirs("jokes")
    time.sleep(1)
    f.close()
    f = open("jokes/jokea.txt", "w")
    f.write("""Helvetica and Times New Roman walk into a bar. 
    “Get out of here!” shouts the bartender. “We dont serve your type." """)
    print("jokea.txt done")
    f.close()
    time.sleep(1)
    f = open("jokes/jokeb.txt", "w")
    f.write("""Whats the best thing about Switzerland? 
    I dont know, but the flag is a big plus.""")
    f.close()
    print("jokeb.txt done")
    time.sleep(1)
    f = open("jokes/jokec.txt", "w")
    f.write("What do you call an aligator in a vest? An investigator.")
    f.close()
    print("jokec.txt done")
    time.sleep(1)
    f = open("jokes/joked.txt", "w")
    f.write("""A guy is sitting at home when he hears a knock at the door. 
He opens the door and sees a snail on the porch. 
He picks up the snail and throws it as far as he can. 
Three years later there’s a knock on the door. 
He opens it and sees the same snail. 
The snail says: ‘What the hell was that all about?’""")
    f.close()
    print("joked.txt done")
    time.sleep(1)
    f = open("jokes/jokee.txt", "w")
    f.write("""Why didnt the shark swallow the clownfish?
Because it tasted funny.""")
    f.close()
    print("jokee.txt done")
    time.sleep(1)
    f = open("jokes/jokef.txt", "w")
    f.write("""Why was six afraid of seven?
Because seven eight(ate) nine.""")
    print("jokef.txt done")
    f.close()
    time.sleep(1)
    f = open("jokes/jokeg.txt", "w")
    f.write("""Why didnt the skeleton go to the party?
Because he had no-body to go with.""")
    f.close()
    print("jokeg.txt done")
    time.sleep(1)
    f = open("jokes/jokeh.txt", "w")
    f.write("""Why did the teacher wear sunglasses to class?
Because her students were so bright (intelligent).""")
    f.close()
    print("jokeh.txt done")
    time.sleep(1)
    f = open("jokes/jokei.txt", "w")
    f.write("""What do you call a five-foot psychic that escaped from jail?
A small medium at large.""")
    f.close()
    print("jokei.txt done")
    print("[i] Jokes installation done, would you like to run the pyhelpy script now?")
    ans2 = input("[+] Y/N: ")
    if ans2 == "Y":
        print("[i] Running script...")
        time.sleep(2)
        if operatingsystem == "Linux":
            os.system("python3 pyhelpy.py")
        elif operatingsystem == "Windows":
            os.system("python pyhelpy.py")
        elif operatingsystem == "Darwin":
            os.system("python3 pyhelpy.py")
    if ans2 == "N":
        print("[i] Alright, bye!")
        time.sleep(2)
        os._exit()
