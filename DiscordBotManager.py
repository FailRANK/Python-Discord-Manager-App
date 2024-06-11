#Imported libaries to create a application window
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
#Value used to hide discord token (very important to not show)
Hidden = True
#Used to know what tab you're on from left to right
Tab = 4
#Sets the window dimensions, title, and icon
Window = tk.Tk()
Window.state("zoomed")
Window.geometry("1000x750")
Window.title("Discord Bot Manager")
ico = Image.open('DiscordIcon.png')
photo = ImageTk.PhotoImage(ico)
Window.wm_iconphoto(False, photo)
#Gets the theme that was saved
ThemeData = open("Data/themedata.txt", "r").read()
#Reads the discord token
Token = open("Data/token.txt", "r").read()
#Sets text
BoldTextFont = ("Arial", 15, "bold")
TextFont = ("Arial", 15)
#See the command prefix and be able to change it
def ShowCommandPrefix():
    #Clears the previous tab
    Clear()
    #Change colour of button to green and changes tab value
    CPB.config(fg="#00ff00")
    global Tab
    Tab = 1
    #Changes header name and info
    SetHeaderAndInfo("Data/commandprefix.txt", "Current Command Prefix", None)
    #Writes the text inputed and refresh GUI
    def SetCommandPrefix():
        SetFileContent("Data/commandprefix.txt", "w", NCPTB.get('1.0', tk.END).strip())
        ShowCommandPrefix()
    #Sets GUI elements
    NCP = tk.Label(Display, text="New Command Prefix", font=BoldTextFont, bg=bgcolor, fg=fgcolor)
    NCP.pack()

    NCPTB = tk.Text(Display, height=1, font=TextFont, bg=textboxbgcolor, fg=fgcolor)
    NCPTB.pack(pady=5)

    NCPB = tk.Button(Display, text="Set", font=BoldTextFont, command=SetCommandPrefix, bg=buttonbgcolor, fg=fgcolor)
    NCPB.pack()
#See the commands and be able to change it
def ShowCommands():
    #Clears the previous tab
    Clear()
    #Change colour of button to green and changes tab value
    CB.config(fg="#00ff00")
    global Tab
    Tab = 2
    #Changes header name and info
    SetHeaderAndInfo(["Data/commands.txt", "Data/responses.txt"], "Current Commands and Responses", True)
    #Writes the text inputed and refresh GUI
    def SetCommands():
        if CTB.get('1.0', tk.END).isspace() or RPTB.get('1.0', tk.END).isspace():
            messagebox.showinfo("Error", "Invalid Input")
            return
        SetFileContent("Data/commands.txt", "a", CTB.get('1.0', tk.END))
        SetFileContent("Data/responses.txt", "a", RPTB.get('1.0', tk.END))
        ShowCommands()
    #Removes the index inputed and refresh GUI
    def Remove():
        if not RTB.get('1.0', tk.END).strip().isnumeric():
            messagebox.showinfo("Error", "Invalid Input")
            return
        commandstxt = open("Data/commands.txt")
        responsestxt = open("Data/responses.txt")
        number = RTB.get('1.0', tk.END).strip()
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
    #Sets GUI elements
    NCR = tk.Label(Display, text=" New Commands & Responses", font=BoldTextFont, bg=bgcolor, fg=fgcolor)
    NCR.pack()

    frame = tk.Frame(Display,bg=bgcolor)
    frame.pack(pady=5)

    CTB = tk.Text(frame, height=1, font=TextFont, bg=textboxbgcolor, fg=fgcolor, width=40)
    CTB.pack(padx = 10, side=tk.LEFT)

    RPTB = tk.Text(frame, height=1, font=TextFont, bg=textboxbgcolor, fg=fgcolor, width=40)
    RPTB.pack(padx = 10, side=tk.LEFT)

    NCRB = tk.Button(Display, text="Set", font=BoldTextFont, command=SetCommands, bg=buttonbgcolor, fg=fgcolor)
    NCRB.pack()
    
    index = tk.Label(Display, text="Index", font=BoldTextFont, bg=bgcolor, fg=fgcolor)
    index.pack(pady = (10,0))

    RTB = tk.Text(Display, height=1, font=TextFont, bg=textboxbgcolor, fg=fgcolor, width = 20)
    RTB.pack(pady = 5)

    RB = tk.Button(Display, text="Remove", font=BoldTextFont, command=Remove, bg=buttonbgcolor, fg=fgcolor)
    RB.pack()
#See the ready message and be able to change it
def ShowStartup():
    #Clears the previous tab
    Clear()
    #Change colour of button to green and changes tab value
    ORMB.config(fg="#00ff00")
    global Tab
    Tab = 3
    #Changes header name and info
    SetHeaderAndInfo("Data/on_ready.txt", "Current Start Up Message", None)
    #Writes the text inputed and refresh GUI
    def SetOn_ready():
        Text = NSUMTB.get('1.0', tk.END).strip()
        SetFileContent("Data/on_ready.txt", "w", Text)
        ShowStartup()
    #Sets GUI elements
    NSUM = tk.Label(Display, text="New Start Up Message", font=BoldTextFont, bg=bgcolor, fg=fgcolor)
    NSUM.pack()

    NSUMTB = tk.Text(Display, height=1, font=TextFont, bg=textboxbgcolor, fg=fgcolor)
    NSUMTB.pack(pady = 5)

    NSUMB = tk.Button(Display, text="Set", font=BoldTextFont, command=SetOn_ready, bg=buttonbgcolor, fg=fgcolor)
    NSUMB.pack()
#Send Message
def ShowSendMessage():
    #Clears the previous tab
    Clear()
    #Change colour of button to green and changes tab value
    SCMB.config(fg="#00ff00")
    global Tab
    Tab = 4
    #Writes the text inputed
    def message():
        if CMTB.get('1.0', tk.END).isspace():
            messagebox.showinfo("Error", "Invalid Input")
            return
        messagetxt = open("Data/message.txt", "w")
        messagetxt.write(CMTB.get('1.0', tk.END))
        messagetxt.close()
    #Sets GUI elements
    CM = tk.Label(Display, text="Channel Message", font=BoldTextFont, bg=bgcolor, fg=fgcolor)
    CM.pack()

    CMTB = tk.Text(Display, height=1, font=TextFont, bg=textboxbgcolor, fg=fgcolor)
    CMTB.pack(pady = 5)

    SMB = tk.Button(Display, text="Send Message", command=message, font=BoldTextFont, bg=buttonbgcolor, fg=fgcolor)
    SMB.pack()
#Set up token
def Setup():
    #Clears the previous tab
    Clear()
    #Change colour of button to green and changes tab value
    SP.config(fg="#00ff00")
    global Tab
    Tab = 5
    #Changes a button text depending on the variable state
    if Hidden:
        show = "Unhide"
    else:
        show = "Hide"
    #Depending on the variable state it is hidden or unhidden
    def hidey():
        global Hidden
        if Hidden:
            Hidden = False
        else:
            Hidden = True
        Setup()
    #Changes header name and info
    SetHeaderAndInfo("Data/token.txt", "Discord Token", None)
    #Hide the token info if Hidden is true
    if Hidden:
        Info.config(text="*Hidden*")
    #Writes the text inputed and refresh GUI
    def SetToken():
        Text = CTTB.get('1.0', tk.END).strip()
        SetFileContent("Data/token.txt", "w", Text)
        Notice()
        Setup()
    #Writes the text inputed and refresh GUI
    def SetChannel():
        Text = CCITB.get('1.0', tk.END).strip()
        SetFileContent("Data/channelid.txt", "w", Text)
        Setup()
    #Sets GUI elements
    CT = tk.Label(Display, text="Current Token", font=BoldTextFont, bg=bgcolor, fg=fgcolor)
    CT.pack()

    CTTB = tk.Text(Display, height=1, font=TextFont, bg=textboxbgcolor, fg=fgcolor)
    CTTB.pack(pady = 5)

    CTB = tk.Button(Display, text="Set", font=BoldTextFont, command=SetToken, bg=buttonbgcolor, fg=fgcolor)
    CTB.pack()

    CTB2 = tk.Button(Display, text=show, font=BoldTextFont, command=hidey, bg=buttonbgcolor, fg=fgcolor)
    CTB2.pack(pady=(5,10))

    CCI = tk.Label(Display, text="Channel ID", font=BoldTextFont, bg=bgcolor, fg=fgcolor)
    CCI.pack()

    file=open("Data/channelid.txt", "r")
    CCI2 = tk.Label(Display, text=file.read().strip(), font=TextFont, bg=bgcolor, fg=fgcolor)
    CCI2.pack(pady=(0,10))

    NCCITB = tk.Label(Display, text="Current Channel ID", font=BoldTextFont, bg=bgcolor, fg=fgcolor)
    NCCITB.pack()

    CCITB = tk.Text(Display, height=1, font=TextFont, bg=textboxbgcolor, fg=fgcolor)
    CCITB.pack(pady = 5)

    CCIB = tk.Button(Display, text="Set", font=BoldTextFont, command=SetChannel, bg=buttonbgcolor, fg=fgcolor)
    CCIB.pack()
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
    for i in Window.winfo_children():
        i.destroy()
    Main()
#Clear window elements
def Clear():
    Header.config(text="")
    Info.config(text="")
    for i in ButtonFrame.winfo_children():
        i.config(fg=fgcolor)
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
        file1, file2 = open(name[0], "r"), open(name[1], "r")
        Header.config(text=title)
        lines, line = file2.readlines(), 1
        for i in file1.readlines():
            Info.config(text=Info.cget('text') + "[" + str(line) + "] " + i.strip() + " " + "| " + lines[line-1])
            line+=1
        file1.close(), file2.close()
        return
    file=open(name, "r")
    Header.config(text=title)
    Info.config(text=file.read().strip())
    file.close()
#Notice if token is empty
def Notice():
    if Token != "":
        SP.config(text="Setup")
    else:
        SP.config(text="Setup [!]")
#Contains all the main components for the window
def Main():
    global SP
    global Header
    global Info
    global Display
    global bgcolor
    global fgcolor
    global buttonbgcolor
    global textboxbgcolor
    global ButtonFrame
    global CPB
    global CB
    global ORMB
    global SCMB
    #Sets Theme
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
    
    #Sets up all the necessary GUI elements
    Window.config(bg=bgcolor)

    Title = tk.Label(Window, text="Discord Bot Manager", font=("Arial", 30, "bold"), bg=bgcolor, fg=fgcolor)
    Title.pack(pady = 20)

    ButtonFrame = tk.Frame(Window, bg=bgcolor)
    ButtonFrame.pack()

    CPB = tk.Button(ButtonFrame, text="Command Prefix", font=BoldTextFont, command=ShowCommandPrefix, bg=buttonbgcolor, fg=fgcolor)
    CPB.pack(padx=10, side=tk.LEFT)

    CB = tk.Button(ButtonFrame, text="Commands & Responses", font=BoldTextFont, command=ShowCommands, bg=buttonbgcolor, fg=fgcolor)
    CB.pack(padx=10, side=tk.LEFT)

    ORMB = tk.Button(ButtonFrame, text="Start Up Message", font=BoldTextFont, command=ShowStartup, bg=buttonbgcolor, fg=fgcolor)
    ORMB.pack(padx=10, side=tk.LEFT)

    SCMB = tk.Button(ButtonFrame, text="Send Message", font=BoldTextFont, command=ShowSendMessage, bg=buttonbgcolor, fg=fgcolor)
    SCMB.pack(padx=10, side=tk.LEFT)

    SP = tk.Button(ButtonFrame, command=Setup, font=BoldTextFont, bg=buttonbgcolor, fg=fgcolor)
    SP.pack(padx = 10, side=tk.LEFT)

    Header = tk.Label(Window, font=BoldTextFont, bg=bgcolor, fg=fgcolor)
    Header.pack(pady=(20,0))

    Info = tk.Label(Window, font=TextFont, bg=bgcolor, fg=fgcolor)
    Info.pack(pady=(0,10))

    Display = tk.Frame(Window, bg=bgcolor)
    Display.pack()

    Theme = tk.Button(Window, text="Theme: " + ThemeData, command=ChangeTheme, font=BoldTextFont, bg=buttonbgcolor, fg=fgcolor)
    Theme.pack(side=tk.BOTTOM)
    
    Notice()

    if Tab == 1:
        ShowCommandPrefix()
    elif Tab == 2:
        ShowCommands()
    elif Tab == 3:
        ShowStartup()
    elif Tab == 4:
        ShowSendMessage()
    else:
        Setup()
#Calls the function
Main()
#Causes window to not close
Window.mainloop()