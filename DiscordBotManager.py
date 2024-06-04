#Import libaries to help create a application window
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
#Sets the window dimensions, title, and icon
Hidden = True
Window = tk.Tk()
Window.geometry("1000x750")
Window.title("Discord Bot Manager")
ico = Image.open('DiscordIcon.png')
photo = ImageTk.PhotoImage(ico)
Window.wm_iconphoto(False, photo)
#Window.attributes("-fullscreen", True)
#Gets the theme that was saved
ThemeData = open("Data/themedata.txt", "r").read()
Token = open("Data/token.txt", "r").read()
#See the command prefix and be able to change it
def ShowCommandPrefix():
    Clear()

    commandprefix_file = open("Data/commandprefix.txt", "r")
    Header.config(text="Current Command Prefix")
    Info.config(text=commandprefix_file.read().strip())
    commandprefix_file.close()

    def SetCommandPrefix():
        on_ready_file = open("Data/commandprefix.txt", "w")
        Text = textbox.get('1.0', tk.END)
        on_ready_file.write(Text.strip())
        on_ready_file.close()
        ShowCommandPrefix()

    label = tk.Label(Display, text="New Command Prefix", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor)
    label.pack(pady = 10)

    textbox = tk.Text(Display, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor)
    textbox.pack(pady = 10)

    button = tk.Button(Display, text="Set", font=("Arial", 15, "bold"), command=SetCommandPrefix, bg=buttonbgcolor, fg=fgcolor)
    button.pack(pady = 10)
#See the commands and be able to change it
def ShowCommands():
    Clear()

    def SetCommands():
        if textbox1.get('1.0', tk.END).isspace() or textbox2.get('1.0', tk.END).isspace():
            messagebox.showinfo("Error", "Invalid Input")
            return
        on_ready_file = open("Data/commands.txt", "a")
        Text = textbox1.get('1.0', tk.END)
        on_ready_file.write(Text)
        on_ready_file.close()
        on_ready_file = open("Data/responses.txt", "a")
        Text = textbox2.get('1.0', tk.END)
        on_ready_file.write(Text)
        on_ready_file.close()
        ShowCommands()

    def Remove():
        if not textbox3.get('1.0', tk.END).strip().isnumeric():
            messagebox.showinfo("Error", "Invalid Input")
            return
        commandstxt = open("Data/commands.txt")
        responsestxt = open("Data/responses.txt")
        number = textbox3.get('1.0', tk.END).strip()
        with open('Data/commands.txt', 'r') as fr:
            # reading line by line
            lines = fr.readlines()

        # pointer for position
            ptr = 1
        
            # opening in writing mode
            with open('Data/commands.txt', 'w') as fw:
                for line in lines:
                    # we want to remove 5th line
                    if ptr != int(number):
                        fw.write(line)
                    else:
                        fw.write("")
                    ptr += 1
        fw.close()
        ShowCommands()
    label = tk.Label(Display, text=" New Commands & Responses", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor)
    label.pack(pady=10, padx=10)

    frame = tk.Frame(Display,bg=bgcolor)
    frame.pack(pady=10, padx=10)

    textbox1 = tk.Text(frame, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor, width=40)
    textbox1.pack(padx = 10, pady = 10, side=tk.LEFT)

    textbox2 = tk.Text(frame, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor, width=40)
    textbox2.pack(padx = 10, pady = 10, side=tk.LEFT)

    button = tk.Button(Display, text="Add", font=("Arial", 15, "bold"), command=SetCommands, bg=buttonbgcolor, fg=fgcolor)
    button.pack(pady = 10)
    
    textbox3 = tk.Text(Display, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor, width = 20)
    textbox3.pack(pady = 10)

    button5 = tk.Button(Display, text="Remove", font=("Arial", 15, "bold"), command=Remove, bg=buttonbgcolor, fg=fgcolor)
    button5.pack(pady = 10)

    commands_file = open("Data/commands.txt", "r")
    responses_file = open("Data/responses.txt", "r")
    check = responses_file.readlines()
    Info.config(text="")
    line = 1
    for i in commands_file.readlines():
        Info.config(text=Info.cget('text') + "[" + str(line) + "] " + i.strip() + " " + "| " + check[line-1] + " ")
        line+=1
    Header.config(text="Current Commands & Responses")
    commands_file.close()
    responses_file.close()
#See the ready message and be able to change it
def ShowStartup():
    Clear()

    def SetOn_ready():
        on_ready_file = open("Data/on_ready.txt", "w")
        on_ready_file.write(textbox.get('1.0', tk.END))
        on_ready_file.close()
        ShowStartup()

    label = tk.Label(Display, text="New Start Up Message", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor)
    label.pack(pady = 10)

    textbox = tk.Text(Display, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor)
    textbox.pack(pady = 10)

    button = tk.Button(Display, text="Set", font=("Arial", 15, "bold"), command=SetOn_ready, bg=buttonbgcolor, fg=fgcolor)
    button.pack(pady = 10)

    on_ready_file = open("Data/on_ready.txt", "r")
    Header.config(text="Current Start Up Message")
    Info.config(text=on_ready_file.read().strip())
    on_ready_file.close()
#Send Message
def ShowSendMessage():
    def message():
        if CMTB.get('1.0', tk.END).isspace():
            messagebox.showinfo("Error", "Invalid Input")
            return
        message_file = open("Data/message.txt", "w")
        message_file.write(CMTB.get('1.0', tk.END))
        message_file.close()

    Header.config(text="")
    Info.config(text="")
    Clear()
    frame = tk.Frame(Display,bg=bgcolor)
    frame.pack(pady=10, padx=10)

    CM = tk.Label(frame, text="Channel Message", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor)
    CM.pack(pady = 10)

    CMTB = tk.Text(frame, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor)
    CMTB.pack(pady = 10)

    SMB = tk.Button(frame, text="Send Message", command=message, font=("Arial", 15, "bold"), bg=buttonbgcolor, fg=fgcolor)
    SMB.pack(pady = 10)
#Set up token
def Setup():
    Clear()

    if Hidden:
        show = "Unhide"
    else:
        show = "Hide"

    def hidey():
        global Hidden
        if Hidden:
            Hidden = False
        else:
            Hidden = True
        Setup()

    def SetToken():
        tokentxt = open("Data/token.txt", "w")
        Text = textboxt.get('1.0', tk.END)
        tokentxt.write(Text.strip())
        tokentxt.close()
        Setup()

    label = tk.Label(Display, text="Current Token", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor)
    label.pack(pady = 10)

    textboxt = tk.Text(Display, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor)
    textboxt.pack(pady = 10)

    button = tk.Button(Display, text="Set", font=("Arial", 15, "bold"), command=SetToken, bg=buttonbgcolor, fg=fgcolor)
    button.pack(pady = 10)

    hide = tk.Button(Display, text=show, font=("Arial", 15, "bold"), command=hidey, bg=buttonbgcolor, fg=fgcolor)
    hide.pack(pady = 10)

    label = tk.Label(Display, text="Current Channel ID", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor)
    label.pack(pady = 10)

    textbox = tk.Text(Display, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor)
    textbox.pack(pady = 10)

    button = tk.Button(Display, text="Set Channel ID", font=("Arial", 15, "bold"), command=SetToken, bg=buttonbgcolor, fg=fgcolor)
    button.pack(pady = 10)

    tokentxt = open("Data/token.txt", "r")
    if Hidden:
        Info.config(text="*Hidden*")
    else:
        Info.config(text=tokentxt.read())
    tokentxt.close()
    Header.config(text="Discord Token")
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

ORMB = tk.Button(ButtonFrame, text="Start Up Message", font=("Arial", 15, "bold"), command=ShowStartup)
ORMB.pack(padx=10,pady = 10, side=tk.LEFT)

SCMB = tk.Button(ButtonFrame, text="Send Message", font=("Arial", 15, "bold"), command=ShowSendMessage)
SCMB.pack(padx=10,pady = 10, side=tk.LEFT)

Header = tk.Label(Window, font=("Arial", 15, "bold"))
Header.pack(pady = 10)

Info = tk.Label(Window, font=("Arial", 15))
Info.pack(pady = 10)

Display = tk.Frame(Window)
Display.pack(pady=10)

Theme = tk.Button(Window, text="Theme: " + ThemeData, command=ChangeTheme, font=("Arial", 15, "bold"))
Theme.pack(side=tk.BOTTOM)

SP = tk.Button(ButtonFrame, command=Setup, font=("Arial", 15, "bold"))
SP.pack(padx = 10, pady = 10, side=tk.LEFT)
if Token != "":
    SP.config(text="Setup")
else:
    SP.config(text="Setup [!]")
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
    SCMB.config(bg=buttonbgcolor, fg=fgcolor)
    Header.config(bg=bgcolor, fg=fgcolor)
    Info.config(bg=bgcolor, fg=fgcolor)
    Display.config(bg=bgcolor)
    Theme.config(text="Theme: " + ThemeData,bg=buttonbgcolor, fg=fgcolor)
    SP.config(bg=buttonbgcolor, fg=fgcolor)

SetTheme()

Window.mainloop()