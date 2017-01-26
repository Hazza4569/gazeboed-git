#mbdcb,c#! /usr/bin/env python3

from tkinter import *
from PIL import Image, ImageTk
from random import randint

root_dir = "/home/harry/desktop/gazeboed"

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
        self.options.place(relx=0.97, y=0)

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
        self.playersfield[self.p].place(x=0.05*w, rely=0.1)
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
        self.gameNameLbl.place(rely=0.43,relx=0.5,anchor=S)
        self.gameDescLbl = Label(frame, fg=foreColour, bg=backColour, font ='courier 30 bold')
        self.gameDescLbl.pack()
        self.gameDescLbl.place(rely=0.45,relx=0.5,anchor=N)
        self.rerun = False
        self.queue = []
        self.cntTrex = -1
        self.cntPoint = -1
        self.cntD = -1
        self.cntChild = -1
        self.cntWeak = -1
        self.status = False
        self.gameChange()
        root.bind('<space>', self.gameChange)

    def gameChange(self, event=None):
        executor = "none"

        if not self.rerun:
        #counter decrementations
            if self.cntTrex > 0:
                self.cntTrex -=1
            elif self.cntTrex == 0:
                self.queue.append("Trex")
                self.cntTrex = -1

            if self.cntPoint > 0:
                self.cntPoint -=1
            elif self.cntPoint == 0:
                self.queue.append("Point")
                self.cntPoint = -1

            if self.cntD > 0:
                self.cntD -=1
            elif self.cntD == 0:
                self.queue.append("D")
                self.cntD = -1

            if self.cntChild > 0:
                self.cntChild -= 1
            elif self.cntChild == 0:
                self.queue.append("Child")
                self.cntChild = -1

            if self.cntWeak > 0:
                self.cntWeak -=1
            elif self.cntChild == 0:
                self.queue.append("Weak")
                self.cntWeak = -1

        #queue extraction
            if len(self.queue) > 0:
                executor = self.queue[0]
                for i in range(1,len(self.queue)-1):
                    self.queue[i-1] = self.queue[i]
                self.queue.remove(self.queue[len(self.queue)-1])

    #main sequence
        self.rerun = False
        rno = randint(1,31)

    #rule enders
        if executor == "Trex":
            self.gameName = ("T-Rex")
            self.gameDesc = ("You no longer have to drink with T-rex arms.")
            backColour = "Cyan"
            foreColour = "White"
        elif executor == "Point":
            self.gameName = ("Pointless")
            self.gameDesc = ("You can now point again.")
            backColour = "Cyan"
            foreColour = "White"
        elif executor == "D":
            self.gameName = ("D's Back Now")
            self.gameDesc = ("You may say drink as you please again.")
            backColour = "Cyan"
            foreColour = "White"
        elif executor == "Child":
            self.gameName = ("The Little Shits Have\nFucked Off Now")
            self.gameDesc = ("You may swear again.")
            backColour = "Cyan"
            foreColour = "White"
        elif executor == "Weak":
            self.gameName = ("Weak Hands")
            self.gameDesc = ("You can drink with whatever hand you want again.")
            backColour = "Cyan"
            foreColour = "White"

    #games
        elif rno == 1:
            self.gameName =("Fuzzy Duck - %s starts" %(self.players[randint(0,self.p)]))
            self.gameDesc =("Everybody repeats the phrase 'Fuzzy Duck' in a clockwise\ndirection, until somebody gets it wrong. If somebody says\n'Does He?' you must change direction and say 'Ducky Fuzz'\ninstead.")
            backColour = "Yellow"
            foreColour = "Blue"
        elif rno == 2:
            if (self.iscards.get() == 1) and (self.isquick.get()==0):
                self.gameName =("Fuzzy Winker")
                self.gameDesc =("Deal card face down to everyone. Ace is winker,\nKing is fuzz. Winker subtly winks at someone, who\nthen says after a short delay 'The winker hath winked'.\nfuzz then announces themselves and guesses until\ncorrect, drinks for each wrong guess. Winker drinks for\neach player not guessed.")
                backColour = "DarkBlue"
                foreColour = "Red"
            else:
                self.rerun=True
                self.gameChange()
        elif rno == 3:
            if (self.ispostit.get() == 1):
                self.gameName = ("Who Is %s? %s decides" %(self.players[randint(0,self.p)], self.players[randint(0,self.p)]))
                self.gameDesc = ("One player writes a name of a famous person on a\npost-it, and sticks it on the other's head. The\nperson with the post it then has to ask yes or no\nquestions, drink if the answer's no.")
                backColour = "Red"
                foreColour = "Yellow"
            else:
                self.rerun=True
                self.gameChange()
        elif rno == 4:
            if (self.ispostit.get() == 1):
                self.gameName = ("%s\nWrite a Cheeky Post-It" %(self.players[randint(0,self.p)]))
                self.gameDesc = ("Write a short message on a post-it then pass\nit round so only one player can see it at a time\nanybody who laughs must drink, if nobody laughs\n you drink.")
                backColour = "Orange"
                foreColour = "Purple"
            else:
                self.rerun=True
                self.gameChange()
        elif rno == 5:
            if (self.ispaper.get() == 1):
                self.gameName = ("Drinktionary")
                self.gameDesc = ("%s whisper a word to %s, who then has to draw it.\nIf nobody guesses within a reasonable time then the\ndrawer takes a shot. If it's guessed too quickly then\nthe whisperer takes a shot." %(self.players[randint(0,self.p)], self.players[randint(0,self.p)]))
                backColour = "White"
                foreColour = "Black"
            else:
                self.rerun=True
                self.gameChange()
        elif rno == 6:
            self.gameName = ("I'm Going to the Bar\n%s starts." %(self.players[randint(0,self.p)]))
            self.gameDesc = ("The first player says 'I'm Going to the Bar,\n and I'm going to bring...' and then names a drink.\nThe next player then repeats and then adds another drink,\nand so on.")
            backColour = "Black"
            foreColour = "Yellow"
        elif rno == 7:
            self.gameName = ("Bail Out!")
            self.gameDesc = ("Everybody grab a second cup and a spoon. You have one\nminute to transfer as much drink into the empty cup as\npossible, without lifting either cup. anything left in\nthe first cup you'll have to down.")
            backColour = "Black"
            foreColour = "Orange"
        elif rno == 8:
            self.gameName = ("Target: 21\n"
                             "%s starts." %(self.players[randint(0,self.p)]))
            self.gameDesc = ("Count to 21, each player can only say up to three numbers\nat a time, then the next player continues. If two numbers are\nsaid then the next player is skipped. if three numbers\nare said then play changes direction. The player who says\n21 drinks.")
            backColour = "Orange"
            foreColour = "Green"
        elif rno == 9:
            self.gameName = ("Sevens\n%s starts" %(self.players[randint(0,self.p)]))
            self.gameDesc = ("Everybody says one number at a time, counting sequentially.\nIf a number with a seven in it or a multiple of seven falls\non you then don't say anything - if you do, drink.")
            backColour = "Grey"
            foreColour = "Cyan"
        elif rno == 10:
            self.gameName = ("Drunk Dial:\n%s give your phone\nto %s" %(self.players[randint(0,self.p)], self.players[randint(0,self.p)]))
            self.gameDesc = ("You can send one text or online message to anybody in their\ncontacts except for family members and one veto. You may keep\nthe phone until they reply or for half an hour.\n(Get out clause: 2 shots.)")
            backColour = "Red"
            foreColour = "White"
        elif rno == 11:
            self.gameName = ("GECKO!")
            self.gameDesc = ("Everybody get at least 3 limbs on a wall ASAP.\nLast person to do so drinks.")
            backColour = "Green"
            foreColour = "Orange"
        elif rno == 12:
            self.gameName = ("AIR RAID!")
            self.gameDesc = ("Everybody get under something ASAP.\nLast person to do so drinks.")
            backColour = "Blue"
            foreColour = "Red"
        elif rno == 13:
            self.gameName = ("LAVA!")
            self.gameDesc = ("Everybody get off the floor ASAP.\nLast person to do so drinks.")
            backColour = "DarkOrange"
            foreColour = "Yellow"
        elif rno == 14:
            if self.cntTrex < 0:
                self.gameName = ("T-Rex")
                self.gameDesc = ("For the next few turns, everyone has to drink with\nT-rex arms.")
                backColour = "LimeGreen"
                foreColour = "White"
                self.cntTrex = randint(6,10)
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 15:
            if self.cntPoint < 0:
                self.gameName = ("Pointless")
                self.gameDesc = ("For the next few turns, nobody is allowed to point\nwith their hands in any way.")
                backColour = "LimeGreen"
                foreColour = "White"
                self.cntPoint = randint(6,10)
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 16:
            if self.cntD < 0:
                self.gameName = ("No D's Please")
                self.gameDesc = ("For the next few turns, nobody is allowed to say\n the D word (drink).")
                backColour = "LimeGreen"
                foreColour = "White"
                self.cntD = randint(6,10)
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 17:
            if self.cntChild < 0:
                self.gameName = ("Small Children Present")
                self.gameDesc = ("No swearing for the next few turns.")
                backColour = "LimeGreen"
                foreColour = "White"
                self.cntChild = randint(6,10)
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 18:
            if self.cntWeak < 0:
                self.gameName = ("Weak Hands")
                self.gameDesc = ("For the next few turns, drink only with your weak hands.")
                backColour = "LimeGreen"
                foreColour = "White"
                self.cntWeak = randint(6,10)
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 19:
            if not self.status:
                self.gameName = ("Status")
                self.gameDesc = ("From this point on, if somebody says status immediately\nafter you say something, you must post it on facebook.")
                backColour = "LimeGreen"
                foreColour = "White"
                self.status = True
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 20:
            self.gameName = ("SECURITY CHECK!")
            self.gameDesc = ("If your drink isn't exactly a finger's length\nfrom the edge of the table, drink.")
            backColour = "DarkBlue"
            foreColour = "Red"
    #categories
        elif rno == 21:
            self.gameName = ("Categories")
            self.gameDesc = ("Name a Selly Oak bar/restaurant, %s starts." %(self.players[randint(0,self.p)]))
            backColour = "Purple"
            foreColour = "White"
        elif rno == 22:
            self.gameName = ("Categories")
            self.gameDesc = ("Name a foreign currency, %s starts." %(self.players[randint(0,self.p)]))
            backColour = "Purple"
            foreColour = "White"
        elif rno == 23:
            self.gameName = ("Categories")
            self.gameDesc = ("Name a Lord of the Rings character, %s starts." %(self.players[randint(0,self.p)]))
            backColour = "Purple"
            foreColour = "White"
        elif rno == 24:
            self.gameName = ("Categories")
            self.gameDesc = ("Name a Star Wars character, %s starts." %(self.players[randint(0,self.p)]))
            backColour = "Purple"
            foreColour = "White"
        elif rno == 25:
            self.gameName = ("Categories")
            self.gameDesc = ("Name a sex position, %s starts." %(self.players[randint(0,self.p)]))
            backColour = "Purple"
            foreColour = "White"
        elif rno == 26:
            self.gameName = ("Categories")
            self.gameDesc = ("Name a porn site, %s starts." %(self.players[randint(0,self.p)]))
            backColour = "Purple"
            foreColour = "White"
        elif rno == 27:
            self.gameName = ("Categories")
            self.gameDesc = ("Name a reality TV show, %s starts." %(self.players[randint(0,self.p)]))
            backColour = "Purple"
            foreColour = "White"
        elif rno == 28:
            self.gameName = ("Categories")
            self.gameDesc = ("Name a road in Selly Oak, %s starts." %(self.players[randint(0,self.p)]))
            backColour = "Purple"
            foreColour = "White"
        elif rno == 29:
            self.gameName = ("Categories")
            self.gameDesc = ("Name a building on campus, %s starts." %(self.players[randint(0,self.p)]))
            backColour = "Purple"
            foreColour = "White"
        elif rno == 30:
            self.gameName = ("Categories")
            self.gameDesc = ("Name a Disney film, %s starts." %(self.players[randint(0,self.p)]))
            backColour = "Purple"
            foreColour = "White"
        elif rno == 31:
            self.gameName = ("Categories")
            self.gameDesc = ("%s choose a category and start." %(self.players[randint(0,self.p)]))
            backColour = "Purple"
            foreColour = "White"

        self.gameNameLbl.config(text=self.gameName, fg=foreColour, bg=backColour)
        self.gameDescLbl.config(text=self.gameDesc, fg=foreColour, bg=backColour)
        frame.config(bg=backColour)
        self.options.config(bg=backColour, fg=foreColour, activebackground=foreColour)
        self.dropdown.config(bg= backColour, fg = foreColour)
        

root = Tk()
[w, h] = root.winfo_screenwidth(), root.winfo_screenheight() - 20
print(w,h)
root.wm_attributes('-type', 'splash')
#root.attributes('-fullscreen', True)
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


