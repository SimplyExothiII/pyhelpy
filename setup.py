from appJar import gui
import tkinter
import os

app = gui("Setup", "700x400")

app.setBg("green")

app.addLabel("title", "Hello and welcome to the pyhelpy installer!")
app.setLabelBg("title", "orange")

app.setFont(24)

def press(button):
    if button == "Start":
        app.infoBox("Install", "Installation will begin shortly.")
        where = app.directoryBox("Where?")
        try:
            os.makedirs(where + "/pyhelpy")
            logind = where + "/pyhelpy/login.py"
            optionsd = where + "/pyhelpy/options.py"
            pyhelpyd = where + "/pyhelpy/pyhelpy-gui.py"
            with open(logind, "w") as outputer:
                outputer.write("""from appJar import gui
import tkinter
import os
app = gui("Login Window", "600x300")
def press(button):
    if button == "Cancel":
        app.stop()
    elif button == "Login":
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        check = 0
        f = open("Username.txt")
        if usr == f.read():
            check += 1
        f.close()
        f = open ("Password.txt")
        if pwd == f.read():
            check += 1
        f.close()
        if check == 2:
            app.infoBox("Success", "Successfully logged in.")
            question = app.questionBox("Sudo", "Do you wish to use pyhelpy with sudo?")
            if question == True:
                question2 = app.questionBox("Confirm", "Are you sure?")
                if question2 == True:
                    question3 = app.questionBox("Confirm confirmation", "Are you really sure?")
                    if question3 == True:
                        app.warningBox("Warning", "If anything happens to your system, it is NOT my fault.")
                        app.infoBox("Joke", "Just kidding! Its too dangerous to launch with sudo.")
                        app.stop()
                    else:
                        app.stop()
                else:
                    app.stop()
            elif question == False:
                app.stop()
        elif check != 2:
            app.errorBox("Failure", "Could not login. Are you sure you entered the right credentials? Try again.")
    elif button == "Submit":
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        if len(usr) < 3:
            app.errorBox("Exception", "The username needs to be atleast 3 letters long!")
        elif len(pwd) < 3:
            app.errorBox("Exception", "The password needs to be atleast 3 letters long!")
        elif len(usr) < 3 and len(pwd) < 3:
            app.errorBox("Exception", "The username and password needs to be atleast 3 letters long!")
        else:
            f = open("Username.txt", "w")
            f.write(usr)
            f.close()

            f = open("Password.txt", "w")
            f.write(pwd)
            f.close()
            app.infoBox("Success", "Successfully made an account.")
            app.stop()

app.setBg("grey")

app.addLabel("title", "Log into your pyhelpy account.")
app.setLabelBg("title", "orange")

app.addLabelEntry("Username")
app.setLabelBg("Username", "yellow")
app.addLabelSecretEntry("Password")
app.setLabelBg("Password", "blue")

if os.path.exists("Username.txt") and os.path.exists("Password.txt") == True:
    app.addButtons(["Login", "Cancel"], press)
else:
    app.addButtons(["Submit", "Cancel"], press)

app.setFont(18)

app.go()

                """)
                outputer.close()
            with open(optionsd, "w") as outputero:
                outputero.write("""from appJar import gui
import os
import tkinter

app3 = gui("Options", "300x200")

if os.path.exists("startlog.txt") == True and os.path.exists("loadscreen.txt") == True:
    loadind = open("loadscreen.txt")
    op1 = loadind.read()
    loadind.close()
    startlogin = open("startlog.txt")
    op2 = startlogin.read()
    startlogin.close()
    options={"Show loading screen at start":op1, "Log in at start":op2}
    app3.addProperties("Options", options)
elif os.path.exists("loadscreen.txt") == True and os.path.exists("startlog.txt") == False:
    loadind = open("loadscreen.txt")
    op1 = loadind.read()
    loadind.close()
    options={"Show loading screen at start":op1, "Log in at start":True}
    app3.addProperties("Options", options)
elif os.path.exists("startlog.txt") == True and os.path.exists("loadscreen.txt") == False:
    startlogin = open("startlog.txt")
    op2 = startlogin.read()
    startlogin.close()
    options={"Show loading screen at start":True, "Log in at start":op2}
    app3.addProperties("Options", options)
else:
    options={"Show loading screen at start":True, "Log in at start":True}
    app3.addProperties("Options", options)


def presseded(button):
    if button == "Save & Exit":
        
        load = app3.getProperty("Options", "Show loading screen at start")
        log = app3.getProperty("Options", "Log in at start")
        if load == True:
            load = "True"
        elif load == False:
            load = "False"
        if log == True:
            log = "True"
        elif log == False:
            log = "False"
        with open("loadscreen.txt", "w") as loaded:
            loaded.write(load)
            loaded.close()
        with open("startlog.txt", "w") as startloge:
            startloge.write(log)
            startloge.close()
        app3.stop()

app3.addButtons(["Save & Exit"], presseded)

app3.go()""")
                outputero.close()
            with open(pyhelpyd, "w") as outputeror:
                outputeror.write("""from appJar import gui
import tkinter
import os
import random

if os.path.exists("startlog.txt") == True:
    login = open("startlog.txt")
    login2 = login.read()
    login.close()
    if login2 == "True":
        os.system("python3 login.py")
elif os.path.exists("startlog.txt") == False:
    os.system("python3 login.py")

app2 = gui("Pyhelpy", "800x400")

if os.path.exists("loadscreen.txt") == True:
    splash = open("loadscreen.txt")
    splash2 = splash.read()
    splash.close()
    if splash2 == "True":
        app2.showSplash("Pyhelpy", "yellow", "blue", "orange")
elif os.path.exists("loadscreen.txt") == False:
    app2.showSplash("Pyhelpy", "yellow", "blue", "orange")

app2.setLabelFont(size=16, family="Comic sans")
app2.setButtonFont(size=14, family="Verdana")

app2.setFont(20)

if os.path.exists("backgroundcolour.txt") == True:
    f = open("backgroundcolour.txt")
    app2.setBg(f.read())

def pressed(button):
    if button == "Beta tests":
        app2.infoBox("Information", "Want to apply for a beta tester? You will have early access to most of the newer versions, but theres no reward. If you want to become one, message me on twitter! @_iv1x_here")

app2.addLabel("title", "Welcome to pyhelpy!")
app2.setLabelBg("title", "yellow")
app2.addLabel("description", "Choose a function:")
app2.setLabelBg("description", "orange")

def pressing(button):
    if button == "Create .txt file":
        feat = app2.saveBox(title="File creator", fileName="", dirName="", fileExt=".txt", fileTypes="", asFile=False, parent=None)
        content = app2.textBox("Content", "Type in the content of the file, if you dont want any content just click cancel.")
        with open(feat, "w") as output:
            output.write(content)
    elif button == "Create folder":
        feast = app2.directoryBox("Where?")
        feast2 = app2.textBox("Name?", "Name of the folder:")
        os.makedirs(feast + "/" + feast2)
    elif button == "Joke":
        fun = random.randint(1, 9)
        if fun == 1:
            app2.infoBox("Joke", "Helvetica and Times New Roman walk into a bar. “Get out of here!” shouts the bartender. “We don’t serve your type.”")
        elif fun == 2:
            app2.infoBox("Joke", "What’s the best thing about Switzerland? I don’t know, but the flag is a big plus.")
        elif fun == 3:
            app2.infoBox("Joke", "What do you call an aligator in a vest? An investigator.")
        elif fun == 4:
            app2.infoBox("Joke", "A guy is sitting at home when he hears a knock at the door. He opens the door and sees a snail on the porch. He picks up the snail and throws it as far as he can. Three years later there’s a knock on the door. He opens it and sees the same snail. The snail says: ‘What the hell was that all about?’")
        elif fun == 5:
            app2.infoBox("Joke", "Why didnt the shark swallow the clownfish? Because it tasted funny.")
        elif fun == 6:
            app2.infoBox("Joke", "Why was six afraid of seven? Because seven eight(ate) nine.")
        elif fun == 7:
            app2.infoBox("Joke", "Why didnt the skeleton go to the party? Because he had no-body to go with.")
        elif fun == 8:
            app2.infoBox("Joke", "Why did the teacher wear sunglasses to class? Because her students were so bright (intelligent).")
        elif fun == 9:
            app2.infoBox("Joke", "What do you call a five-foot psychic that escaped from jail? A small medium at large.")
    elif button == "Exit":
        app2.stop()
    elif button == "Fun Fact":
        fun = random.randint(1, 20)
        if fun == 1:
            app2.infoBox("Fun fact", "This version was made in over a week, but the thought of making it was actually over a month!")
        elif fun == 2:
            app2.infoBox("Fun fact", "There is over 0 beta testers for this version!")
            app2.addButtons(["Beta tests"], pressed)
        elif fun == 3:
            app2.infoBox("Fun fact", "Argentina had five presidents in ten days in 2001.")
        elif fun == 4:
            app2.infoBox("Fun fact", "91% of people skip the first piece of bread simply because its ugly.")
        elif fun == 5:
            app2.infoBox("Fun fact", "Brands and logos will hit you most if you are depressed or frightened.")
        elif fun == 6:
            app2.infoBox("Fun fact", "The more photos you capture during an event or moment, you are less likely to recall it later.")
        elif fun == 7:
            app2.infoBox("Fun fact", "Breast cancers account for 30% of all cancer diagnosed in women.")
        elif fun == 8:
            app2.infoBox("Fun fact", "In 1891, in Ohio, the first car accident happened.")
        elif fun == 9:
            app2.infoBox("Fun fact", "You cant cry in space because theres nowhere for your tears to fall.")
        elif fun == 10:
            app2.infoBox("Fun fact", "Abraham Lincoln was a professional wrestler long before he became the 16th president of the United States.")
        elif fun == 11:
            app2.infoBox("Fun fact", "Every hour, humans shed roughly 600,000 skin particles.")
        elif fun == 12:
            app2.infoBox("Fun fact", "Cows sweat through their noses.")
        elif fun == 13:
            app2.infoBox("Fun fact", "Bananas contain a little amount of radioactivity.")
        elif fun == 14:
            app2.infoBox("Fun fact", "A little nap can aid in the retention of new knowledge.")
        elif fun == 15:
            app2.infoBox("Fun fact", "Turtles have existed for around 215 million years.")
        elif fun == 16:
            app2.infoBox("Fun fact", "According to studies, coloring your room blue can help you be more creative.")
        elif fun == 17:
            app2.infoBox("Fun fact", "The earths core is nearly the same temperature as the sun.")
        elif fun == 18:
            app2.infoBox("Fun fact", "Women in India use nose rings to show that they are married.")
        elif fun == 19:
            app2.infoBox("Fun fact", "Every time you open up the refrigerator door, up to 30% of cold air is lost.")
        elif fun == 20:
            app2.infoBox("Fun fact", "Cockroaches are served fried in China, Thailand and other Asian countries.")
            
    elif button == "Background colour":
        colo = app2.colourBox()
        with open("backgroundcolour.txt", "w") as outputing:
            outputing.write(colo)
        app2.setBg(colo)
        app2.setLabelBg("title", "yellow")
        app2.setLabelBg("description", "orange")
    elif button == "Options":
        os.system("python3 options.py")


app2.addButtons(["Create .txt file", "Create folder", "Joke", "Exit", "Fun Fact"], pressing)
app2.addButtons(["Background colour", "Options"], pressing)
 
app2.go()""")
                outputeror.close()
            app.infoBox("Installation", "Installation done, instead of running setup.py, run pyhelpy-gui in the folder you installed it in.")
            app.stop()
        except:
            app.errorBox("Error", "An unexpected error was caused.")
    elif button == "Quit":
        app.stop()

app.addButton("Start", press)
app.addButton("Quit", press)

app.go()