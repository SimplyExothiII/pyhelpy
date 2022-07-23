from appJar import gui
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
 
app2.go()