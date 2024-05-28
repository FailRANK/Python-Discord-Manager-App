#Import libaries to help create a application window
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
#Sets the window dimensions, title, and icon
Window = tk.Tk()
Window.geometry("1000x750")
Window.title("Discord Bot Manager")
ico = Image.open('DiscordIcon.png')
photo = ImageTk.PhotoImage(ico)
Window.wm_iconphoto(False, photo)
#Gets the theme that was saved
ThemeData = open("Data/themedata.txt", "r").read()
Token = open("Data/token.txt", "r").read()
#See the command prefix and be able to change it
def ShowCommandPrefix():
    Clear()

    def SetCommandPrefix():
        on_ready_file = open("Data/commandprefix.txt", "w")
        Text = textbox.get('1.0', tk.END)
        on_ready_file.write(Text.strip())
        on_ready_file.close()

    label = tk.Label(Display, text="Command Prefix", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor)
    label.pack(pady = 10)

    textbox = tk.Text(Display, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor)
    textbox.pack(pady = 10)

    button4 = tk.Button(Display, text="Change Command Prefix", font=("Arial", 15, "bold"), command=SetCommandPrefix, bg=buttonbgcolor, fg=fgcolor)
    button4.pack(pady = 10)

    List = []
    commandprefix_file = open("Data/commandprefix.txt", "r")
    for i in commandprefix_file.readlines():
        List.append(i.strip())
    Header.config(text="Command Prefix")
    Info.config(text=List)
    commandprefix_file.close()
#See the commands and be able to change it
def ShowCommands():
    Clear()

    def SetCommands():
        on_ready_file = open("Data/commands.txt", "a")
        Text = textbox1.get('1.0', tk.END)
        on_ready_file.write(Text.strip() + "\n")
        on_ready_file.close()
        on_ready_file = open("Data/responses.txt", "a")
        Text = textbox2.get('1.0', tk.END)
        on_ready_file.write(Text.strip() + "\n")
        on_ready_file.close()

    label = tk.Label(Display, text="Commands & Responses", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor)
    label.pack(pady=10, padx=10)

    frame = tk.Frame(Display,bg=bgcolor)
    frame.pack(pady=10, padx=10)

    textbox1 = tk.Text(frame, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor, width=50)
    textbox1.pack(pady = 10, side=tk.LEFT)

    textbox2 = tk.Text(frame, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor, width=50)
    textbox2.pack(pady = 10, side=tk.LEFT)

    button4 = tk.Button(Display, text="Add", font=("Arial", 15, "bold"), command=SetCommands, bg=buttonbgcolor, fg=fgcolor)
    button4.pack(pady = 10)
    
    button5 = tk.Button(Display, text="Remove", font=("Arial", 15, "bold"), bg=buttonbgcolor, fg=fgcolor)
    button5.pack(pady = 10)

    commands_file = open("Data/commands.txt", "r")
    responses_file = open("Data/responses.txt", "r")
    check = responses_file.readlines()
    Info.config(text="")
    line = 1
    for i in commands_file.readlines():
        Info.config(text=Info.cget('text') + "[" + str(line) + "] " + i.strip() + " " + "| " + check[line-1] + " ")
        line+=1
    Header.config(text="Commands & Responses")
    commands_file.close()
    responses_file.close()
#See the ready message and be able to change it
def ShowOn_ready():
    Clear()

    def SetOn_ready():
        on_ready_file = open("Data/on_ready.txt", "w")
        on_ready_file.write(textbox.get('1.0', tk.END))
        on_ready_file.close()

    label = tk.Label(Display, text="On Ready Message", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor)
    label.pack(pady = 10)

    textbox = tk.Text(Display, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor)
    textbox.pack(pady = 10)

    button4 = tk.Button(Display, text="Change Message", font=("Arial", 15, "bold"), command=SetOn_ready, bg=buttonbgcolor, fg=fgcolor)
    button4.pack(pady = 10)

    List = []
    on_ready_file = open("Data/on_ready.txt", "r")
    for i in on_ready_file.readlines():
        List.append(i.strip())
    Header.config(text="On Ready Message")
    Info.config(text=List)
    on_ready_file.close()
#Send Message
def message():
    message_file = open("Data/message.txt", "w")
    message_file.write(CMTB.get('1.0', tk.END))
    message_file.close()
#Set up token
def Setup():
    Clear()

    def ResetToken():
        on_ready_file = open("Data/token.txt", "w")
        on_ready_file.write("")
        on_ready_file.close()

    def SetToken():
        on_ready_file = open("Data/token.txt", "w")
        Text = textbox.get('1.0', tk.END)
        on_ready_file.write(Text.strip())
        on_ready_file.close()

    label = tk.Label(Display, text="Discord Bot Token", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor)
    label.pack(pady = 10)

    textbox = tk.Text(Display, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor)
    textbox.pack(pady = 10)

    button4 = tk.Button(Display, text="Set Token", font=("Arial", 15, "bold"), command=SetToken, bg=buttonbgcolor, fg=fgcolor)
    button4.pack(pady = 10)

    button5 = tk.Button(Display, text="Reset Token", font=("Arial", 15, "bold"), command=ResetToken, bg=buttonbgcolor, fg=fgcolor)
    button5.pack(pady = 10)

    List = []
    commandprefix_file = open("Data/token.txt", "r")
    for i in commandprefix_file.readlines():
        List.append(i.strip())
    Header.config(text="Discord Token")
    Info.config(text=List)
    commandprefix_file.close()
#Changes window theme
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
#Clear window elements
def Clear():
    for i in Display.winfo_children():
        i.destroy()
#Sets up all the necessary GUI elements
Title = tk.Label(Window, text="Discord Bot Manager", font=("Arial", 30, "bold"))
Title.pack(pady = 10)

ButtonFrame = tk.Frame(Window)
ButtonFrame.pack(pady=10)

CPB = tk.Button(ButtonFrame, text="Command Prefix", font=("Arial", 15, "bold"), command=ShowCommandPrefix)
CPB.pack(padx=10,pady=10, side=tk.LEFT)

CB = tk.Button(ButtonFrame, text="Commands & Responses", font=("Arial", 15, "bold"), command=ShowCommands)
CB.pack(padx=10,pady=10, side=tk.LEFT)

ORMB = tk.Button(ButtonFrame, text="On Ready Message", font=("Arial", 15, "bold"), command=ShowOn_ready)
ORMB.pack(padx=10,pady = 10, side=tk.LEFT)

Header = tk.Label(Window, font=("Arial", 15, "bold"))
Header.pack(pady = 10)

Info = tk.Label(Window, font=("Arial", 15))
Info.pack(pady = 10)

Display = tk.Frame(Window)
Display.pack(pady=10)

CM = tk.Label(Window, text="Channel Message", font=("Arial", 15, "bold"))
CM.pack(pady = 10)

CMTB = tk.Text(Window, height=1, font=("Arial", 15))
CMTB.pack(pady = 10)

SMB = tk.Button(Window, text="Send Message", command=message, font=("Arial", 15, "bold"))
SMB.pack(pady = 10)

Theme = tk.Button(Window, text="Theme: " + ThemeData, command=ChangeTheme, font=("Arial", 15, "bold"))
Theme.pack(side=tk.BOTTOM)

SP = tk.Button(Window, command=Setup, font=("Arial", 15, "bold"))
SP.pack(side=tk.BOTTOM)
if Token != "":
    SP.config(text="Setup")
else:
    SP.config(text="Setup[!]")
#Sets window theme
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
    Window.config(bg=bgcolor)
    Title.config(bg=bgcolor, fg=fgcolor)
    ButtonFrame.config(bg=bgcolor)
    CPB.config(bg=buttonbgcolor, fg=fgcolor)
    CB.config(bg=buttonbgcolor, fg=fgcolor)
    ORMB.config(bg=buttonbgcolor, fg=fgcolor)
    Header.config(bg=bgcolor, fg=fgcolor)
    Info.config(bg=bgcolor, fg=fgcolor)
    Display.config(bg=bgcolor)
    #label.config(bg=bgcolor, fg=fgcolor)
    #textbox.config(bg=textboxbgcolor, fg=fgcolor)
    #button4.config(bg=buttonbgcolor, fg=fgcolor)
    CM.config(bg=bgcolor, fg=fgcolor)
    CMTB.config(bg=textboxbgcolor, fg=fgcolor)
    SMB.config(bg=buttonbgcolor, fg=fgcolor)
    Theme.config(text="Theme: " + ThemeData,bg=buttonbgcolor, fg=fgcolor)
    SP.config(bg=buttonbgcolor, fg=fgcolor)

SetTheme()

Window.mainloop()