import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

List = []

ThemeData = open("Data/themedata.txt", "r").read()

def ShowCommandPrefix():
    Clear()

    def SetCommandPrefix():
        on_ready_file = open("Data/commandprefix.txt", "w")
        print(textbox.get('1.0', tk.END))
        Text = textbox.get('1.0', tk.END)
        on_ready_file.write(Text.strip())
        on_ready_file.close()

    label = tk.Label(frame2, text="Command Prefix", font=("Arial", 15, "bold"))
    label.pack(pady = 10)

    textbox = tk.Text(frame2, height=1, font=("Arial", 15))
    textbox.pack(pady = 10)

    button4 = tk.Button(frame2, text="Change Command Prefix", font=("Arial", 15, "bold"), command=SetCommandPrefix)
    button4.pack(pady = 10)

    List = []
    commandprefix_file = open("Data/commandprefix.txt", "r")
    for i in commandprefix_file.readlines():
        List.append(i.strip())
    header.config(text="Command Prefix")
    label2.config(text=List)
    commandprefix_file.close()

def ShowCommands():
    Clear()

    List = []
    commands_file = open("Data/commands.txt", "r")
    for i in commands_file.readlines():
        List.append(i.strip())
    header.config(text="Commands")
    label2.config(text=List)
    commands_file.close()

def ShowResponses():
    Clear()

    List = []
    responses_file = open("Data/responses.txt", "r")
    header.config(text="Responses")
    for i in responses_file.readlines():
        List.append(i.strip())
    header.config(text="Responses")
    label2.config(text=List)
    responses_file.close()

def ShowOn_ready():
    Clear()

    def SetOn_ready():
        on_ready_file = open("Data/on_ready.txt", "w")
        print(textbox.get('1.0', tk.END))
        on_ready_file.write(textbox.get('1.0', tk.END))
        on_ready_file.close()

    label = tk.Label(frame2, text="On Ready Message", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor)
    label.pack(pady = 10)

    textbox = tk.Text(frame2, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor)
    textbox.pack(pady = 10)

    button4 = tk.Button(frame2, text="Change Message", font=("Arial", 15, "bold"), command=SetOn_ready, bg=buttonbgcolor, fg=fgcolor)
    button4.pack(pady = 10)

    List = []
    on_ready_file = open("Data/on_ready.txt", "r")
    for i in on_ready_file.readlines():
        List.append(i.strip())
    header.config(text="On Ready Message")
    label2.config(text=List)
    on_ready_file.close()

def message():
    message_file = open("Data/message.txt", "w")
    message_file.write(textbox2.get('1.0', tk.END))
    message_file.close()

def ChangeTheme():
    global ThemeData
    if ThemeData == "Light":
        ThemeData = "Dark"
        Data = open("Data/themedata.txt", "w")
        Data.write("Dark")
        Data.close()
    else:
        ThemeData = "Light"
        Data = open("Data/themedata.txt", "w")
        Data.write("Light")
        Data.close()
    SetTheme()

def Clear():
    for i in frame2.winfo_children():
        i.destroy()
    
#Set up app GUI
root = tk.Tk()
root.geometry("1000x750")
root.title("Discord Bot Manager")
ico = Image.open('DiscordIcon.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

Title = tk.Label(root, text="Discord Bot Manager", font=("Arial", 30, "bold"))
Title.pack(pady = 10)

frame = tk.Frame(root)
frame.pack(pady=10)

button = tk.Button(frame, text="Command Prefix", font=("Arial", 15, "bold"), command=ShowCommandPrefix)
button.pack(padx=10,pady=10, side=tk.LEFT)

button1 = tk.Button(frame, text="Commands", font=("Arial", 15, "bold"), command=ShowCommands)
button1.pack(padx=10,pady=10, side=tk.LEFT)

button2 = tk.Button(frame, text="Responses", font=("Arial", 15, "bold"), command=ShowResponses)
button2.pack(padx=10,pady=10, side=tk.LEFT)

button3 = tk.Button(frame, text="On Ready Message", font=("Arial", 15, "bold"), command=ShowOn_ready)
button3.pack(padx=10,pady = 10, side=tk.LEFT)

header = tk.Label(root, font=("Arial", 15, "bold"))
header.pack(pady = 10)

label2 = tk.Label(root, font=("Arial", 15))
label2.pack(pady = 10)

frame2 = tk.Frame(root)
frame2.pack(pady=10)

label3 = tk.Label(root, text="Channel Message", font=("Arial", 15, "bold"))
label3.pack(pady = 10)

textbox2 = tk.Text(root, height=1, font=("Arial", 15))
textbox2.pack(pady = 10)

button5 = tk.Button(root, text="Send Message", command=message, font=("Arial", 15, "bold"))
button5.pack(pady = 10)

Theme = tk.Button(root, text="Theme: " + ThemeData, command=ChangeTheme, font=("Arial", 15, "bold"))
Theme.pack(side=tk.BOTTOM)

def SetTheme():
    global bgcolor
    global fgcolor
    global buttonbgcolor
    global textboxbgcolor
    if ThemeData == "Light":
        bgcolor = "#ffffff"
        fgcolor = "#000"
        buttonbgcolor = "#ebedef"
        textboxbgcolor = "#ebedef"
    else:
        bgcolor = "#313338"
        fgcolor = "#fff"
        buttonbgcolor = "#232428"
        textboxbgcolor = "#383a40"
    root.config(bg=bgcolor)
    Title.config(bg=bgcolor, fg=fgcolor)
    frame.config(bg=bgcolor)
    button.config(bg=buttonbgcolor, fg=fgcolor)
    button1.config(bg=buttonbgcolor, fg=fgcolor)
    button2.config(bg=buttonbgcolor, fg=fgcolor)
    button3.config(bg=buttonbgcolor, fg=fgcolor)
    header.config(bg=bgcolor, fg=fgcolor)
    label2.config(bg=bgcolor, fg=fgcolor)
    frame2.config(bg=bgcolor)
    #label.config(bg=bgcolor, fg=fgcolor)
    #textbox.config(bg=textboxbgcolor, fg=fgcolor)
    #button4.config(bg=buttonbgcolor, fg=fgcolor)
    label3.config(bg=bgcolor, fg=fgcolor)
    textbox2.config(bg=textboxbgcolor, fg=fgcolor)
    button5.config(bg=buttonbgcolor, fg=fgcolor)
    Theme.config(text="Theme: " + ThemeData,bg=buttonbgcolor, fg=fgcolor)

SetTheme()

root.mainloop()