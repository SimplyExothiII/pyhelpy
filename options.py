from appJar import gui
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

app3.go()