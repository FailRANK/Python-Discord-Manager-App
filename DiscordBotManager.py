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
#Gets the theme that was saved
ThemeData = open("Data/themedata.txt", "r").read()
Token = open("Data/token.txt", "r").read()
#See the command prefix and be able to change it
def ShowCommandPrefix():
    Clear()

    SetHeaderAndInfo("Data/commandprefix.txt", "Current Command Prefix", None)

    def SetCommandPrefix():
        SetFileContent("Data/commandprefix.txt", "w", textbox.get('1.0', tk.END).strip())
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

    SetHeaderAndInfo(["Data/commands.txt", "Data/responses.txt"], "Current Commands and Responses", True)

    def SetCommands():
        if textbox1.get('1.0', tk.END).isspace() or textbox2.get('1.0', tk.END).isspace():
            messagebox.showinfo("Error", "Invalid Input")
            return
        SetFileContent("Data/commands.txt", "a", textbox1.get('1.0', tk.END))
        SetFileContent("Data/responses.txt", "a", textbox2.get('1.0', tk.END))
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
        fr.close()
        fw.close()
        with open('Data/responses.txt', 'r') as fr:
            # reading line by line
            lines = fr.readlines()

        # pointer for position
            ptr = 1
        
            # opening in writing mode
            with open('Data/responses.txt', 'w') as fw:
                for line in lines:
                    # we want to remove 5th line
                    if ptr != int(number):
                        fw.write(line)
                    else:
                        fw.write("")
                    ptr += 1
        fr.close()
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
#See the ready message and be able to change it
def ShowStartup():
    Clear()

    SetHeaderAndInfo("Data/on_ready.txt", "Current Start Up Message", None)

    def SetOn_ready():
        Text = textbox.get('1.0', tk.END).strip()
        SetFileContent("Data/on_ready.txt", "w")
        ShowStartup()

    label = tk.Label(Display, text="New Start Up Message", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor).pack(pady = 10)
    textbox = tk.Text(Display, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor).pack(pady = 10)
    button = tk.Button(Display, text="Set", font=("Arial", 15, "bold"), command=SetOn_ready, bg=buttonbgcolor, fg=fgcolor).pack(pady = 10)
#Send Message
def ShowSendMessage():
    Clear()

    def message():
        if CMTB.get('1.0', tk.END).isspace():
            messagebox.showinfo("Error", "Invalid Input")
            return
        message_file = open("Data/message.txt", "w")
        message_file.write(CMTB.get('1.0', tk.END))
        message_file.close()
    
    def delay():
        if not DTB.get('1.0', tk.END).strip().isnumeric():
            messagebox.showinfo("Error", "Invalid Input")
            return
        with open('Data/message.txt', 'r') as fr:
            # reading line by line
            lines = fr.readlines()
            # pointer for position
            ptr = 1
        
            # opening in writing mode
            with open('Data/message.txt', 'w') as fw:
                for line in lines:
                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    else:
                        fw.write(DTB.get('1.0', tk.END).strip())
                    ptr += 1
        fr.close()
        fw.close()

    frame = tk.Frame(Display,bg=bgcolor).pack(pady=10, padx=10)
    CM = tk.Label(frame, text="Channel Message", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor).pack(pady = 10)
    CMTB = tk.Text(frame, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor).pack(pady = 10)
    SMB = tk.Button(frame, text="Send Message", command=message, font=("Arial", 15, "bold"), bg=buttonbgcolor, fg=fgcolor).pack(pady = 10)
    #DTB = tk.Text(frame, text="Delay", font=("Arial", 15, "bold"), bg=textboxbgcolor, fg=fgcolor).pack(pady = 10)
    DMB = tk.Button(frame, text="Set Delay", command=delay, font=("Arial", 15, "bold"), bg=buttonbgcolor, fg=fgcolor).pack(pady = 10)
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
        Text = textboxt.get('1.0', tk.END).strip()
        SetFileContent("Data/token.txt", "w", Text)
        Notice()
        Setup()

    label = tk.Label(Display, text="Current Token", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor).pack(pady = 10)
    textboxt = tk.Text(Display, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor).pack(pady = 10)
    button = tk.Button(Display, text="Set", font=("Arial", 15, "bold"), command=SetToken, bg=buttonbgcolor, fg=fgcolor).pack(pady = 10)
    hide = tk.Button(Display, text=show, font=("Arial", 15, "bold"), command=hidey, bg=buttonbgcolor, fg=fgcolor).pack(pady = 10)
    label = tk.Label(Display, text="Current Channel ID", font=("Arial", 15, "bold"), bg=bgcolor, fg=fgcolor).pack(pady = 10)
    textbox = tk.Text(Display, height=1, font=("Arial", 15), bg=textboxbgcolor, fg=fgcolor).pack(pady = 10)
    button = tk.Button(Display, text="Set Channel ID", font=("Arial", 15, "bold"), command=SetToken, bg=buttonbgcolor, fg=fgcolor).pack(pady = 10)

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
#Sets file content
def SetFileContent(name, type, content):
    file = open(name, type)
    file.write(content)
    file.close()
#Sets the header and info
def SetHeaderAndInfo(name, title, special):
    if special:
        file1 = open(name[0], "r")
        file2 = open(name[1], "r")
        Header.config(text=title)
        content = file2.readlines()
        line = 1
        for i in file1.readlines():
            Info.config(text=Info.cget('text') + "[" + str(line) + "] " + i.strip() + " " + "| " + content[line-1])
            line+=1
        file1.close()
        file2.close()
        return
    file=open(name, "r")
    Header.config(text=title)
    Info.config(text=file.read().strip())
    file.close()
#Notice
def Notice():
    if Token != "":
        SP.config(text="Setup")
    else:
        SP.config(text="Setup [!]")
Notice()    
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