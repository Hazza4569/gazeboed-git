#mbdcb,c#! /usr/bin/env python3

from Tkinter import *
from PIL import Image, ImageTk
from random import randint

root_dir = "/home/tamara/desktop/gazeboed"
print(randint(1,10))

class APP:

    def __init__(self, frame):

        self.options=Menubutton(
            frame, image = cog, bg=backColour, fg=foreColour, activebackground=foreColour, relief="flat")
        self.dropdown = Menu(self.options, tearoff = 0, bd=1, relief="flat", bg= backColour, fg = foreColour)
        self.options.configure(menu = self.dropdown)

        self.dropdown.add_command(label = "Option 1")
        self.dropdown.add_command(label = "Option 2")
        self.dropdown.add_separator()
        self.dropdown.add_command(label = "Quit", command = root.destroy)
        self.options.pack()
        self.options.place(x=(w - 62), y=0)

        self.titlelogo = Canvas(frame, bg = backColour, bd = 0, relief = "ridge", highlightthickness = 0, width = 498, height = 381)
        self.titlelogo.pack(expand = YES, fill = BOTH)
        self.titlelogo.create_image(0, 0, image = logo, anchor = NW)
        self.titlelogo.place(relx = 0.5, rely = 0.37, anchor = CENTER)

        self.titletext = Label(frame, text = "GAZEBOED", fg = foreColour, bg = backColour, font = "courier 100 bold")
        self.titletext.pack()
        self.titletext.place(relx = 0.5, rely = 0.7, anchor = CENTER)

        self.go = Button(frame, bg = foreColour, fg = backColour, highlightbackground = foreColour, text = "Let's Get Gazeboed!",
                         activebackground = foreColour, highlightcolor = foreColour, font = "helvetica 20", command = self.optionsPage)
        self.go.pack()
        self.go.place(relx = 0.5, rely = 0.85, anchor = CENTER)

    def optionsPage(self):
        self.titlelogo.destroy()
        self.titletext.destroy()
        self.go.destroy()

        self.playerstitle = Label(frame, text="Players:", fg=foreColour, bg=backColour, font="courier 50 bold")
        self.playerstitle.pack()
        self.playerstitle.place(relx = 0.5, rely = -0.01, anchor = N)

        self.p = 0
        self.row = 0
        self.perrow = 0
        self.playersfield = []
        self.players=[]
        self.input=[]
        self.input.append(StringVar())
        self.playersfield.append(Entry(frame, relief = 'flat', textvariable=self.input[0]))
        self.playersfield[self.p].pack(pady = 3)
        self.playersfield[self.p].place(relx=0.05, rely=0.1)
        root.focus_set()
        self.playersfield[self.p].focus_set()
        root.focus_force()

        self.addbutton = Button(frame, bg=foreColour, fg=backColour, highlightbackground=foreColour, image = addim,
                         activebackground=foreColour, highlightcolor=foreColour, font="helvetica 8 bold", command=self.addPlayer)
        self.addbutton.pack()
        self.addbutton.place(relx = 0.175, rely = 0.1)

        self.delbutton = Button(frame, bg=foreColour, fg=backColour, highlightbackground=foreColour, image = subim,
                         activebackground=foreColour, highlightcolor=foreColour, font="helvetica 8 bold", command=self.delPlayer)
        self.delbutton.pack()
        self.delbutton.place(relx = -1)

        root.bind('<Return>', self.addPlayer)
        root.bind('<Delete>', self.delPlayer)

        self.resourcetitle = Label(frame, text = 'Resources and Options:', fg=foreColour, bg=backColour, font='courier 50 bold')
        self.resourcetitle.pack()
        self.resourcetitle.place(rely = 0.7, relx = 0.5, anchor = N)

        self.iscards = IntVar()
        self.isnuts = IntVar()
        self.ispostit = IntVar()
        self.ispaper = IntVar()
        self.isquick = IntVar()

        self.cards = Checkbutton(frame, text="Playing Cards", variable=self.iscards, bg=backColour, fg=foreColour)
        self.cards.pack()
        self.cards.place(rely = 0.85, relx = 0.17, anchor=CENTER)

        self.nuts = Checkbutton(frame, text="Nuts", variable=self.isnuts, bg=backColour, fg=foreColour)
        self.nuts.pack()
        self.nuts.place(rely = 0.85, relx = 0.33, anchor=CENTER)

        self.postit = Checkbutton(frame, text="PostIts", variable=self.ispostit, bg=backColour, fg=foreColour)
        self.postit.pack()
        self.postit.place(rely = 0.85, relx = 0.5, anchor=CENTER)

        self.paper = Checkbutton(frame, text="Paper", variable=self.ispaper, bg=backColour, fg=foreColour)
        self.paper.pack()
        self.paper.place(rely = 0.85, relx = 0.67, anchor=CENTER)

        self.quick = Checkbutton(frame, text="Quick Games Only", variable=self.isquick, bg=backColour, fg=foreColour)
        self.quick.pack()
        self.quick.place(rely = 0.85, relx = 0.83, anchor=CENTER)

        self.startbutton = Button(frame, bg=foreColour, fg=backColour, highlightbackground=foreColour, text="  Go! ",
                           activebackground=foreColour, highlightcolor=foreColour, font="helvetica 20 bold", command=self.leaveOptions)
        self.startbutton.pack()
        self.startbutton.place(relx=0.93,rely=0.93)

        
    def addPlayer(self, event=None):
        unique = True
        for i in range(0, self.p):
            if self.players[i] == self.input[self.p].get():
                unique = False
        if self.input[self.p].get() and unique:
            self.players.append(self.input[self.p].get())
            self.playersfield[self.p].config(state='readonly')
            self.p += 1
            self.addEntry()

    def delPlayer(self, event=None):
        if self.p > 0:
            self.players.remove(self.players[self.p - 1])
            self.playersfield[self.p - 1].config(state='normal')
            self.playersfield[self.p - 1].focus_set()
            self.input.remove(self.input[self.p])
            self.playersfield[self.p].destroy()
            self.playersfield.remove(self.playersfield[self.p])
            self.p -= 1

            if (self.p - (self.perrow-1)*self.row) < 0:
                self.row -= 1
            self.addbutton.place(relx = 0.175 + (200*self.row)/w, rely= 0.1 + (30*(self.p - self.row*(self.perrow-1)))/h)
            self.delbutton.place(relx = 0.175 + (200*self.row)/w, rely= 0.1 + (30*(self.p - self.row*(self.perrow-1)-1))/h)
    
    def addEntry(self):
        self.input.append(StringVar())
        self.playersfield.append(Entry(frame, relief = 'flat', textvariable=self.input[self.p]))
        self.playersfield[self.p].pack()

        if ((self.p-(self.perrow - 1)*self.row)*30 + 0.1*h) > h*2/3:
            if self.row == 0:
                self.perrow = self.p + 1
            self.row += 1

        self.addbutton.place(relx = 0.175 + (200*self.row)/w, rely= 0.1 + (30*(self.p - self.row*(self.perrow - 1)))/h)
        self.delbutton.place(relx = 0.175 + (200*self.row)/w, rely= 0.1 + (30*(self.p - self.row*(self.perrow - 1) - 1))/h)
        self.playersfield[self.p].place(x=0.05*w + 200*self.row, y = 0.1*h + 30*(self.p - self.row*(self.perrow-1)))
        self.playersfield[self.p].focus_set()

    def leaveOptions(self):
        for i in range(self.p,-1, -1):
            self.playersfield[i].destroy()
        self.cards.destroy()
        self.nuts.destroy()
        self.postit.destroy()
        self.paper.destroy()
        self.quick.destroy()
        self.playerstitle.destroy()
        self.resourcetitle.destroy()
        self.startbutton.destroy()
        self.addbutton.destroy()
        self.delbutton.destroy()
        self.p -=1
        self.mainSequence()

    def mainSequence(self):
        self.gameName=""
        self.gameDesc=""
        self.gameNameLbl = Label(frame, fg=foreColour, bg=backColour, font='courier 70 bold')
        self.gameNameLbl.pack()
        self.gameNameLbl.place(rely=0.49,relx=0.5,anchor=S)
        self.gameDescLbl = Label(frame, fg=foreColour, bg=backColour, font ='courier 30')
        self.gameDescLbl.pack()
        self.gameDescLbl.place(rely=0.51,relx=0.5,anchor=N)
        self.gameChange()


    def gameChange(self):
        rno = 2
        plyno = randint(0,self.p)
        print(self.iscards.get())
        if rno == 1:
            self.gameName =("Fuzzy Duck - %s starts" % (self.players[plyno]))
            self.gameDesc =("Everybody repeats the phrase 'Fuzzy Duck' in a clockwise\ndirection, until somebody gets it wrong. If somebody says\n'Does He?' you must change direction and say 'Ducky Fuzz'\ninstead.")
            backColour = "Yellow"
            foreColour = "Blue"
        elif rno == 2:
            if (self.iscards.get() == 1) and (self.isquick.get()==0):
                self.gameName =("Fuzzy Winker")
                self.gameDesc =("Deal card face down to everyone. Ace is winker,\nKing is fuzz. Winker subtly winks at someone, who\nthen says after a short delay 'The winker hath winked'.\nfuzz then announces themselves and guesses until\ncorrect, drinks for each wrong guess. Winker drinks for\neach player not guessed.")
                backColour = "DarkBlue"
                foreColour = "Red"

        self.gameNameLbl.config(text=self.gameName, fg=foreColour, bg=backColour)
        self.gameDescLbl.config(text=self.gameDesc, fg=foreColour, bg=backColour)
        frame.config(bg=backColour)
        self.options.config(bg=backColour, fg=foreColour, activebackground=foreColour)
        self.dropdown.config(bg= backColour, fg = foreColour)
        

root = Tk()
[w, h] = root.winfo_screenwidth(), root.winfo_screenheight() - 20
print(w,h)
#root.wm_attributes('-type', 'splash')
root.attributes('-fullscreen', True)
#root.overrideredirect(True)
#root.geometry("{0}x{1}+0+0".format(w, h))

settings = root_dir + "/settings.png"
gazebo = root_dir + "/gazeboed4.png"
plus = root_dir + "/plus.png"
minus = root_dir + "/minus.png"
cog = ImageTk.PhotoImage(Image.open("settings.png"))
logo = ImageTk.PhotoImage(Image.open("gazeboed4.png"))
addim = ImageTk.PhotoImage(Image.open("plus.png"))
subim = ImageTk.PhotoImage(Image.open("minus.png"))

#frontPage.start(frontPage)
backColour = "#043605"
foreColour = "red"
frame = Frame(root, width=w, height=h, bg=backColour, relief="flat")
frame.pack_propagate(0)  # don't shrink
frame.pack()

app = APP(frame)
root.mainloop()
#root.destroy()


