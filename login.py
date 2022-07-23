from appJar import gui
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

                