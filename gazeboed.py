#! /usr/bin/env python3

from tkinter import *
from random import randint
import os
from math import ceil

os.chdir(os.path.dirname(sys.argv[0]))

class APP:

    def __init__(self, frame):
        self.backColour = "#043605"
        self.foreColour = "red"
        self.options=Menubutton(
            frame, image = cog, bg=self.backColour, fg=self.foreColour, activebackground=self.foreColour, relief="flat")
        self.dropdown = Menu(self.options, tearoff = 0, bd=1, relief="flat", bg= self.backColour, fg = self.foreColour)
        self.options.configure(menu = self.dropdown)

        self.dropdown.add_command(label = "Option 1")
        self.dropdown.add_command(label = "Option 2")
        self.dropdown.add_separator()
        self.dropdown.add_command(label = "Quit", command = root.destroy)
        self.options.pack()
        self.options.place(relx=0.955, y=0)

        self.titlelogo = Canvas(frame, bg = self.backColour, bd = 0, relief = "ridge", highlightthickness = 0, width = 498, height = 381)
        self.titlelogo.pack(expand = YES, fill = BOTH)
        self.titlelogo.create_image(0, 0, image = logo, anchor = NW)
        self.titlelogo.place(relx = 0.5, rely = 0.32, anchor = CENTER)

        self.titletext = Label(frame, text = "GAZEBOED", fg = self.foreColour, bg = self.backColour, font = "courier 100 bold")
        self.titletext.pack()
        self.titletext.place(relx = 0.5, rely = 0.63, anchor = CENTER)

        self.tagline = Label(frame, text = "More than 40 ways to make you wish\nyou'd never been born.", fg = "#048C00", bg = self.backColour, font = "courier 30 bold")
        self.tagline.pack()
        self.tagline.place(relx = 0.5, rely = 0.75, anchor = CENTER)

        self.go = Button(frame, bg = self.foreColour, fg = self.backColour, highlightbackground = self.foreColour, text = "Let's Get Gazeboed!",
                         activebackground = self.foreColour, highlightcolor = self.foreColour, font = "Courier 30 bold", command = self.optionsPage)
        self.go.pack(padx = 1, pady = 1)
        self.go.place(relx = 0.5, rely = 0.87, anchor = CENTER)

    def optionsPage(self):
        self.titlelogo.destroy()
        self.titletext.destroy()
        self.go.destroy()
        self.tagline.destroy()

        self.playerstitle = Label(frame, text="Players:", fg=self.foreColour, bg=self.backColour, font="courier 50 bold")
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

        self.addbutton = Button(frame, bg=self.foreColour, fg=self.backColour, highlightbackground=self.foreColour, image = addim,
                         activebackground=self.foreColour, highlightcolor=self.foreColour, font="helvetica 8 bold", command=self.addPlayer)
        self.addbutton.pack()
        self.addbutton.place(relx = 0.175, rely = 0.1)

        self.delbutton = Button(frame, bg=self.foreColour, fg=self.backColour, highlightbackground=self.foreColour, image = subim,
                         activebackground=self.foreColour, highlightcolor=self.foreColour, font="helvetica 8 bold", command=self.delPlayer)
        self.delbutton.pack()
        self.delbutton.place(relx = -1)

        root.bind('<Return>', self.addPlayer)
        root.bind('<Delete>', self.delPlayer)

        self.resourcetitle = Label(frame, text = 'Resources and Options:', fg=self.foreColour, bg=self.backColour, font='courier 50 bold')
        self.resourcetitle.pack()
        self.resourcetitle.place(rely = 0.7, relx = 0.5, anchor = N)

        self.iscards = IntVar()
        self.isballs = IntVar()
        self.ispostit = IntVar()
        self.ispaper = IntVar()
        self.isquick = IntVar()

        self.cards = Checkbutton(frame, text="Playing Cards", variable=self.iscards, bg=self.backColour, fg=self.foreColour)
        self.cards.pack()
        self.cards.place(rely = 0.85, relx = 0.17, anchor=CENTER)

        self.balls = Checkbutton(frame, text="Ping Pong Balls", variable=self.isballs, bg=self.backColour, fg=self.foreColour)
        self.balls.pack()
        self.balls.place(rely = 0.85, relx = 0.33, anchor=CENTER)

        self.postit = Checkbutton(frame, text="PostIts", variable=self.ispostit, bg=self.backColour, fg=self.foreColour)
        self.postit.pack()
        self.postit.place(rely = 0.85, relx = 0.5, anchor=CENTER)

        self.paper = Checkbutton(frame, text="Paper", variable=self.ispaper, bg=self.backColour, fg=self.foreColour)
        self.paper.pack()
        self.paper.place(rely = 0.85, relx = 0.67, anchor=CENTER)

        self.quick = Checkbutton(frame, text="Quick Games Only", variable=self.isquick, bg=self.backColour, fg=self.foreColour)
        self.quick.pack()
        self.quick.place(rely = 0.85, relx = 0.83, anchor=CENTER)

        self.startbutton = Button(frame, bg=self.foreColour, fg=self.backColour, highlightbackground=self.foreColour, text="  Go! ",
                           activebackground=self.foreColour, highlightcolor=self.foreColour, font="helvetica 20 bold", command=self.leaveOptions)
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
        self.balls.destroy()
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
        self.gameNameLbl = Label(frame, fg=self.foreColour, bg=self.backColour, font='courier 70 bold')
        self.gameNameLbl.pack()
        self.gameNameLbl.place(rely=0.43,relx=0.5,anchor=S)
        self.gameDescLbl = Label(frame, fg=self.foreColour, bg=self.backColour, font ='courier 30 bold')
        self.gameDescLbl.pack()
        self.gameDescLbl.place(rely=0.45,relx=0.5,anchor=N)
        self.rerun = False
        self.queue = []
        labelx = 0.05*w

        self.cntTrex = -1       #Rule0
        self.lblTrex = Label(frame, fg=self.backColour, bg=self.backColour, highlightbackground=self.foreColour, highlightthickness=1, font='courier 20 bold', text = "T-Rex")
        self.lblTrex.pack()
        self.lblTrex.place(rely = 0.95, x = labelx, anchor = W)
        root.update()
        labelx += self.lblTrex.winfo_width() + 10

        self.cntPoint = -1      #Rule1
        self.lblPoint = Label(frame, fg=self.backColour, bg=self.backColour, highlightbackground=self.foreColour, highlightthickness=1, font='courier 20 bold', text="Pointless")
        self.lblPoint.pack()
        self.lblPoint.place(rely=0.95, x = labelx, anchor=W)
        root.update()
        labelx += self.lblPoint.winfo_width() + 10

        self.cntD = -1          #Rule2
        self.lblD = Label(frame, fg=self.backColour, bg=self.backColour, highlightbackground=self.foreColour, highlightthickness=1, font='courier 20 bold', text="D Word")
        self.lblD.pack()
        self.lblD.place(rely=0.95, x = labelx, anchor=W)
        root.update()
        labelx += self.lblD.winfo_width() + 10

        self.cntChild = -1      #Rule3
        self.lblChild = Label(frame, fg=self.backColour, bg=self.backColour, highlightbackground=self.foreColour, highlightthickness=1, font='courier 20 bold', text="Small Children Present")
        self.lblChild.pack()
        self.lblChild.place(rely=0.95, x = labelx, anchor=W)
        root.update()
        labelx += self.lblChild.winfo_width() + 10

        self.cntWeak = -1       #Rule4
        self.lblWeak = Label(frame, fg=self.backColour, bg=self.backColour, highlightbackground=self.foreColour, highlightthickness=1, font='courier 20 bold', text="Weak Hands")
        self.lblWeak.pack()
        self.lblWeak.place(rely=0.95, x=labelx, anchor=W)
        root.update()
        labelx += self.lblWeak.winfo_width() + 10

        self.status = False     #Rule6
        self.lblStatus = Label(frame, fg=self.backColour, bg=self.backColour, highlightbackground=self.foreColour, highlightthickness=1, font='courier 20 bold', text="Status")
        self.lblStatus.pack()
        self.lblStatus.place(rely=0.95, x = labelx, anchor=W)
        root.update()
        labelx += self.lblStatus.winfo_width() + 10

        self.cntSnake = -1  # Rule5
        self.lblSnake = Label(frame, fg=self.backColour, bg=self.backColour, highlightbackground=self.foreColour,
                              highlightthickness=1, font='courier 20 bold', text="Snakeyes")
        self.lblSnake.pack()
        self.lblSnake.place(rely=0.95, x = labelx, anchor=W)

        self.numGames = 44
        self.arrCount = []
        self.arrForeColour = []
        self.arrBackColour = []
        self.arrActive = []
        self.frequent = 10
        self.moderate = 20
        self.rare = 30
        self.seldom = 40
        self.once = 999999
        self.categoriesParameter = 5
        self.nhieParam = 5
        for i in range(0,self.numGames + 1):
            self.arrCount.append(0)
        for i in range(0,7):
            self.arrForeColour.append("Black")
            self.arrBackColour.append("White")
            self.arrActive.append(False)
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

            if self.cntSnake > 0:
                self.cntSnake -=1
            elif self.cntSnake == 0:
                self.queue.append("Snake")
                self.cntSnake = -1

        #queue extraction
            if len(self.queue) > 0:
                executor = self.queue[0]
                for i in range(1,len(self.queue)-1):
                    self.queue[i-1] = self.queue[i]
                self.queue.remove(self.queue[len(self.queue)-1])

        #general counters decrement
            for i in range(0,self.numGames+1):
                if not i == 34:
                    self.arrCount[i]-=1
                else:
                    print(self.arrCount[i])

    #main sequence
        self.rerun = False
        rno = randint(1,self.numGames)
        #executor = "Snake"
    #rule enders
        if executor == "Trex":
            self.gameName = ("T-Rex")
            self.gameDesc = ("You no longer have to drink with T-rex arms.")
            self.backColour = "Magenta"
            self.foreColour = "White"
            self.arrActive[0] = False
            self.arrCount[14] = self.frequent
        elif executor == "Point":
            self.gameName = ("Pointless")
            self.gameDesc = ("You can now point again.")
            self.backColour = "Magenta"
            self.foreColour = "White"
            self.arrActive[1] = False
            self.arrCount[15] = self.frequent
        elif executor == "D":
            self.gameName = ("D's Back Now")
            self.gameDesc = ("You may say drink as you please again.")
            self.backColour = "Magenta"
            self.foreColour = "White"
            self.arrActive[2] = False
            self.arrCount[16] = self.frequent
        elif executor == "Child":
            self.gameName = ("The Little Shits Have\nFucked Off Now")
            self.gameDesc = ("You may swear again.")
            self.backColour = "Magenta"
            self.foreColour = "White"
            self.arrActive[3] = False
            self.arrCount[17] = self.frequent
        elif executor == "Weak":
            self.gameName = ("Weak Hands")
            self.gameDesc = ("You can drink with whatever hand you want again.")
            self.backColour = "Magenta"
            self.foreColour = "White"
            self.arrActive[4] = False
            self.arrCount[18] = self.frequent
        elif executor == "Snake":
            self.gameName = ("Snakeyes")
            self.gameDesc = ("No more snakeyes.")
            self.backColour = "Magenta"
            self.foreColour ="White"
            self.arrActive[5] = False
            self.arrCount[37] = self.frequent


    #games
        elif rno == 1:
            if self.arrCount[1] <= 0:
                self.gameName =("Fuzzy Duck - %s starts" %(self.players[randint(0,self.p)]))
                self.gameDesc =("Everybody repeats the phrase 'Fuzzy Duck' in a clockwise\ndirection, until somebody gets it wrong. If somebody says\n'Does He?' you must change direction and say 'Ducky Fuzz'\ninstead.")
                self.backColour = "Yellow"
                self.foreColour = "Blue"
                self.arrCount[1] = self.moderate
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 2:
            if (self.iscards.get() == 1) and (self.isquick.get()==0) and (self.arrCount[2] <= 0):
                self.gameName =("Fuzzy Winker")
                self.gameDesc =("Deal card face down to everyone. Ace is winker,\nKing is fuzz. Winker subtly winks at someone, who\nthen says after a short delay 'The winker hath winked'.\nfuzz then announces themselves and guesses until\ncorrect, drinks for each wrong guess. Winker drinks for\neach player not guessed.")
                self.backColour = "DarkBlue"
                self.foreColour = "Red"
                self.arrCount[2] = self.rare
            else:
                self.rerun=True
                self.gameChange()
        elif rno == 3:
            if (self.ispostit.get() == 1) and (self.arrCount[3] <= 0):
                ply1 = randint(0,self.p)
                ply2 = randint(0,self.p - 1)
                if ply2 >= ply1:
                    ply2 +=1
                self.gameName = ("Who Is %s?\n%s decides" %(self.players[ply1], self.players[ply2]))
                self.gameDesc = ("One player writes a name of a famous person on a\npost-it, and sticks it on the other's head. The\nperson with the post it then has to ask yes or no\nquestions, drink if the answer's no.")
                self.backColour = "Red"
                self.foreColour = "Yellow"
                self.arrCount[3] = self.frequent
            else:
                self.rerun=True
                self.gameChange()
        elif rno == 4:
            if (self.ispostit.get() == 1) and (self.arrCount[4] <= 0):
                self.gameName = ("%s\nWrite a Cheeky Post-It" %(self.players[randint(0,self.p)]))
                self.gameDesc = ("Write a short message on a post-it then pass\nit round so only one player can see it at a time\nanybody who laughs must drink, if nobody laughs\n you drink.")
                self.backColour = "Orange"
                self.foreColour = "Purple"
                self.arrCount[4] = self.frequent
            else:
                self.rerun=True
                self.gameChange()
        elif rno == 5:
            if (self.ispaper.get() == 1) and (self.arrCount[5] <= 0):
                ply1 = randint(0, self.p)
                ply2 = randint(0, self.p - 1)
                if ply2 >= ply1:
                    ply2 += 1
                self.gameName = ("Drinktionary")
                self.gameDesc = ("%s whisper a word to %s, who then has to draw it.\nIf nobody guesses within a reasonable time then the\ndrawer takes a shot. If it's guessed too quickly then\nthe whisperer takes a shot." %(self.players[ply1], self.players[ply2]))
                self.backColour = "White"
                self.foreColour = "Black"
                self.arrCount[5] = self.moderate
            else:
                self.rerun=True
                self.gameChange()
        elif rno == 6:
            if self.arrCount[6] <= 0:
                self.gameName = ("I'm Going to the Bar\n%s starts." %(self.players[randint(0,self.p)]))
                self.gameDesc = ("The first player says 'I'm Going to the Bar,\n and I'm going to bring...' and then names a drink.\nThe next player then repeats and then adds another drink,\nand so on.")
                self.backColour = "Black"
                self.foreColour = "Yellow"
                self.arrCount[6] = self.seldom
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 7:
            if self.arrCount[7] <= 0:
                self.gameName = ("Bail Out!")
                self.gameDesc = ("Everybody grab a second cup and a spoon. You have one\nminute to transfer as much drink into the empty cup as\npossible, without lifting either cup. anything left in\nthe first cup you'll have to down.\nSpillage is lickage.")
                self.backColour = "Black"
                self.foreColour = "Orange"
                self.arrCount[7] = self.seldom
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 8:
            if self.arrCount[8] <= 0:
                self.gameName = ("Target: 21\n"
                                "%s starts." %(self.players[randint(0,self.p)]))
                self.gameDesc = ("Count to 21, each player can only say up to three numbers\nat a time, then the next player continues. If two numbers are\nsaid then the next player is skipped. if three numbers\nare said then play changes direction. The player who says\n21 drinks.")
                self.backColour = "Orange"
                self.foreColour = "Green"
                self.arrCount[8] = self.moderate
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 9:
            if self.arrCount[9] <= 0:
                self.gameName = ("Sevens\n%s starts" %(self.players[randint(0,self.p)]))
                self.gameDesc = ("Everybody says one number at a time, counting sequentially.\nIf a number with a seven in it or a multiple of seven falls\non you then don't say anything - if you do, drink.")
                self.backColour = "Grey"
                self.foreColour = "Cyan"
                self.arrCount[9] = self.moderate
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 10:
            if self.arrCount[10] <= 0:
                ply1 = randint(0, self.p)
                ply2 = randint(0, self.p - 1)
                if ply2 >= ply1:
                    ply2 += 1
                self.gameName = ("Drunk Dial:\n%s give your phone\nto %s" %(self.players[ply1], self.players[ply2]))
                self.gameDesc = ("You can send one text or online message to anybody in their\ncontacts except for family members and one veto. You may keep\nthe phone for half an hour, and continue the conversation.\nAt no point in the night can anybody send a message to say\nit was a game.\n(Get out clause: 2 shots.)")
                self.backColour = "Red"
                self.foreColour = "White"
                self.arrCount[10] = self.rare
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 11:
            self.gameName = ("GECKO!")
            self.gameDesc = ("Everybody get at least 3 limbs on a wall ASAP.\nLast person to do so drinks.")
            self.backColour = "Green"
            self.foreColour = "Orange"
        elif rno == 12:
            self.gameName = ("AIR RAID!")
            self.gameDesc = ("Everybody get under something ASAP.\nLast person to do so drinks.")
            self.backColour = "Blue"
            self.foreColour = "Red"
        elif rno == 13:
            self.gameName = ("LAVA!")
            self.gameDesc = ("Everybody get on your feet and off the floor ASAP.\nLast person to do so drinks.")
            self.backColour = "DarkOrange"
            self.foreColour = "Yellow"
        elif rno == 14:
            if self.cntTrex < 0 and self.arrCount[14] <= 0:
                self.gameName = ("T-Rex")
                self.gameDesc = ("For the next few turns, everyone has to drink with\nT-rex arms.")
                self.backColour = "LimeGreen"
                self.foreColour = "White"
                self.cntTrex = randint(6,10)
                self.arrActive[0] = True
                self.arrCount[14] = self.frequent
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 15:
            if self.cntPoint < 0 and self.arrCount[15] <= 0:
                self.gameName = ("Pointless")
                self.gameDesc = ("For the next few turns, nobody is allowed to point\nwith their hands in any way.")
                self.backColour = "LimeGreen"
                self.foreColour = "White"
                self.cntPoint = randint(6,10)
                self.arrActive[1] = True
                self.arrCount[15] = self.frequent
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 16:
            if self.cntD < 0 and self.arrCount[16] <= 0:
                self.gameName = ("No D's Please")
                self.gameDesc = ("For the next few turns, nobody is allowed to say\n the D word (drink).")
                self.backColour = "LimeGreen"
                self.foreColour = "White"
                self.cntD = randint(6,10)
                self.arrActive[2] = True
                self.arrCount[16] = self.frequent
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 17:
            if self.cntChild < 0 and self.arrCount[17] <= 0:
                self.gameName = ("Small Children Present")
                self.gameDesc = ("No swearing for the next few turns.")
                self.backColour = "LimeGreen"
                self.foreColour = "White"
                self.cntChild = randint(6,10)
                self.arrActive[3] = True
                self.arrCount[17] = self.frequent
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 18:
            if self.cntWeak < 0 and self.arrCount[18] <= 0:
                self.gameName = ("Weak Hands")
                self.gameDesc = ("For the next few turns, drink only with your weak hands.")
                self.backColour = "LimeGreen"
                self.foreColour = "White"
                self.cntWeak = randint(6,10)
                self.arrActive[4] = True
                self.arrCount[18] = self.frequent
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 19:
            if not self.status:
                self.gameName = ("Status")
                self.gameDesc = ("From this point on, if somebody says status immediately\nafter you say something, you must post it on facebook.")
                self.backColour = "LimeGreen"
                self.foreColour = "White"
                self.status = True
                self.arrActive[6] = True
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 20:
            self.gameName = ("SECURITY CHECK!")
            self.gameDesc = ("If your drink isn't exactly a finger's length\nfrom the edge of the table, drink.")
            self.backColour = "DarkBlue"
            self.foreColour = "Red"

    #categories
        elif rno == 21:
            if self.arrCount[21] <= 0 and randint(1,self.categoriesParameter) == 1:
                self.gameName = ("Categories")
                self.gameDesc = ("Name a Selly Oak bar/restaurant, %s starts." %(self.players[randint(0,self.p)]))
                self.backColour = "Purple"
                self.foreColour = "White"
                self.arrCount[21] = self.once
                self.categoriesParameter += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 22:
            if self.arrCount[22] <= 0 and randint(1,self.categoriesParameter) == 1:
                self.gameName = ("Categories")
                self.gameDesc = ("Name a foreign currency, %s starts." %(self.players[randint(0,self.p)]))
                self.backColour = "Purple"
                self.foreColour = "White"
                self.arrCount[22] = self.once
                self.categoriesParameter += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 23:
            if self.arrCount[23] <= 0 and randint(1,self.categoriesParameter) == 1:
                self.gameName = ("Categories")
                self.gameDesc = ("Name a Lord of the Rings character, %s starts." %(self.players[randint(0,self.p)]))
                self.backColour = "Purple"
                self.foreColour = "White"
                self.arrCount[23] = self.once
                self.categoriesParameter += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 24:
            if self.arrCount[24] <= 0 and randint(1,self.categoriesParameter) == 1:
                self.gameName = ("Categories")
                self.gameDesc = ("Name a Star Wars character, %s starts." %(self.players[randint(0,self.p)]))
                self.backColour = "Purple"
                self.foreColour = "White"
                self.arrCount[24] = self.once
                self.categoriesParameter += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 25:
            if self.arrCount[25] <= 0 and randint(1,self.categoriesParameter) == 1:
                self.gameName = ("Categories")
                self.gameDesc = ("Name a sex position, %s starts." %(self.players[randint(0,self.p)]))
                self.backColour = "Purple"
                self.foreColour = "White"
                self.arrCount[25] = self.once
                self.categoriesParameter += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 26:
            if self.arrCount[26] <= 0 and randint(1,self.categoriesParameter) == 1:
                self.gameName = ("Categories")
                self.gameDesc = ("Name a porn site, %s starts." %(self.players[randint(0,self.p)]))
                self.backColour = "Purple"
                self.foreColour = "White"
                self.arrCount[26] = self.once
                self.categoriesParameter += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 27:
            if self.arrCount[27] <= 0 and randint(1,self.categoriesParameter) == 1:
                self.gameName = ("Categories")
                self.gameDesc = ("Name a reality TV show, %s starts." %(self.players[randint(0,self.p)]))
                self.backColour = "Purple"
                self.foreColour = "White"
                self.arrCount[27] = self.once
                self.categoriesParameter += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 28:
            if self.arrCount[28] <= 0 and randint(1,self.categoriesParameter) == 1:
                self.gameName = ("Categories")
                self.gameDesc = ("Name a road in Selly Oak, %s starts." %(self.players[randint(0,self.p)]))
                self.backColour = "Purple"
                self.foreColour = "White"
                self.arrCount[28] = self.once
                self.categoriesParameter += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 29:
            if self.arrCount[29] <= 0 and randint(1,self.categoriesParameter) == 1:
                self.gameName = ("Categories")
                self.gameDesc = ("Name a building on campus, %s starts." %(self.players[randint(0,self.p)]))
                self.backColour = "Purple"
                self.foreColour = "White"
                self.arrCount[29] = self.once
                self.categoriesParameter += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 30:
            if self.arrCount[30] <= 0 and randint(1,self.categoriesParameter) == 1:
                self.gameName = ("Categories")
                self.gameDesc = ("Name a Disney film, %s starts." %(self.players[randint(0,self.p)]))
                self.backColour = "Purple"
                self.foreColour = "White"
                self.arrCount[30] = self.once
                self.categoriesParameter += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 31:
            if self.arrCount[31] <= 0:
                self.gameName = ("Categories")
                self.gameDesc = ("%s choose a category and start." %(self.players[randint(0,self.p)]))
                self.backColour = "Purple"
                self.foreColour = "White"
                self.arrCount[31] = self.moderate
            else:
                self.rerun = True
                self.gameChange()
    #version 1.1 additions
        elif rno == 32:
            if self.arrCount[32] <= 0:
                ply1 = randint(0, self.p)
                ply2 = randint(0, self.p - 1)
                if ply2 >= ply1:
                    ply2 += 1
                self.gameName = ("Truth or Shot")
                self.gameDesc = ("%s ask %s a question.\nThey can either answer the question or take a shot" %(self.players[ply1], self.players[ply2]))
                self.backColour = "Black"
                self.foreColour = "White"
                self.arrCount[32] = self.frequent
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 33:
            if self.arrCount[33] <= 0:
                self.gameName = ("Medusa")
                self.gameDesc = ("Everyone close their eyes, and on the count of three\nlook at someone and open them. If that person is looking\nback at you then drink.")
                self.backColour = "DarkGreen"
                self.foreColour = "Yellow"
                self.arrCount[33] = self.moderate
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 34:
            self.gameName = ("Dirty Pint")
            self.gameDesc = ("%s add some drink to the dirty pint" %(self.players[randint(0,self.p)]))
            self.backColour = "Brown"
            self.foreColour = "Orange"
            self.arrCount[34] += 1
        elif rno == 35:
            if self.arrCount[34] >= 2:
                self.gameName = ("Dirty Pint")
                self.gameDesc = ("%s drink two fingers from the dirty pint" %(self.players[randint(0,self.p)]))
                self.backColour = "Brown"
                self.foreColour = "Orange"
                self.arrCount[34] -= 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 36:
            if self.arrCount[36] <= 0:
                self.gameName = ("Confession or Shot")
                self.gameDesc = ("%s, tell a secret that most people in\nthe room don't know, or take a shot." %(self.players[randint(0,self.p)]))
                self.backColour = "Black"
                self.foreColour = "White"
                self.arrCount[36] = self.moderate
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 37:
            if self.cntSnake < 0:
                plySnake = randint(0,self.p)
                self.gameName = ("Snakeyes")
                self.gameDesc = ("%s is now snakeyes. Anyone who makes eye contact\nwith them has to drink." %(self.players[plySnake]))
                self.backColour = "LimeGreen"
                self.foreColour = "White"
                self.cntSnake = randint(6,10)
                self.arrActive[5] = True
                self.lblSnake.config(text="Snakeyes:%s" %(self.players[plySnake]))
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 38:
            if self.arrCount[38] <= 0 and randint(1,self.nhieParam) == 1:
                self.gameName = ("Never Have I Ever\nFarted During Sex")
                self.gameDesc = ("Drink if you have.")
                self.backColour = "White"
                self.foreColour = "Purple"
                self.arrCount[38] = self.once
                self.nhieParam += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 39:
            if self.arrCount[39] <= 0 and randint(1,self.nhieParam) == 1:
                self.gameName = ("Never Have I Ever\nSmoked Weed")
                self.gameDesc = ("Drink if you have.")
                self.backColour = "White"
                self.foreColour = "Purple"
                self.arrCount[39] = self.once
                self.nhieParam += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 40:
            if self.arrCount[40] <= 0 and randint(1,self.nhieParam) == 1:
                self.gameName = ("Never Have I Ever\nFallen Asleep in the Cinema")
                self.gameDesc = ("Drink if you have.")
                self.backColour = "White"
                self.foreColour = "Purple"
                self.arrCount[40] = self.once
                self.nhieParam += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 41:
            if self.arrCount[41] <= 0 and randint(1,self.nhieParam) == 1:
                self.gameName = ("Never Have I Ever\nOwned an iPhone")
                self.gameDesc = ("Drink if you have.")
                self.backColour = "White"
                self.foreColour = "Purple"
                self.arrCount[41] = self.once
                self.nhieParam += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 42:
            if self.arrCount[42] <= 0 and randint(1,self.nhieParam) == 1:
                self.gameName = ("Never Have I Ever\nBeen in the Back\n of a Police Car")
                self.gameDesc = ("Drink if you have.")
                self.backColour = "White"
                self.foreColour = "Purple"
                self.arrCount[42] = self.once
                self.nhieParam += 1
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 43:
            if self.arrCount[43] <= 0 and self.p > 2:
                self.gameName = "Flip Cup!"
                team1 = []
                team2 = []
                for i in range(0, self.p + 1):
                    team1.append(i)
                    team2.append(i)
                teamsize = ceil(self.p/2)
                plyNo = self.p
                for i in range(0,teamsize):
                    delplay = randint(0,plyNo)
                    team1.remove(team1[delplay])
                    plyNo -=1
                for i in range(0,len(team1)):
                    team2.remove(team1[i])
                self.gameDesc = self.players[team1[0]] + "\tvs\t" + self.players[team2[0]] + "\n"
                for i in range(1,teamsize):
                    self.gameDesc += self.players[team1[i]] + "\t\t" + self.players[team2[i]] + "\n"
                if not (len(team2) == len(team1)):

                    self.gameDesc += self.players[team1[len(team1)-1]] + "\t\t "
                self.backColour = "White"
                self.foreColour = "Red"
                self.arrCount[43] = self.rare
            else:
                self.rerun = True
                self.gameChange()
        elif rno == 44:
            if self.arrCount[44] <= 0 and self.arrCount[34] >= 2 and self.isballs.get() == 1:
                ply1 = randint(0, self.p)
                ply2 = randint(0, self.p - 1)
                if ply2 >= ply1:
                    ply2 += 1
                self.gameName = ("Slap Cup!\n%s and\n%s start" %(self.players[ply1], self.players[ply2]))
                self.gameDesc = ("Two players have an empty cup and a ping pong ball each,\nthey have to bounce the ball off the table and into the cup.\nWhen they get it in they pass their cup to the left, if they\nget it in first time then they can pass it to any other player\nwithout a cup. If you get it in before the person to your\nleft then you slap their cup out the way and they have to\ndown the dirty pint.")
                self.backColour = "White"
                self.foreColour = "Red"
                self.arrCount[44] = self.moderate
            else:
                self.rerun = True
                self.gameChange()

        else:
            print("Out of range. Sadface.")

        self.gameNameLbl.config(text=self.gameName, fg=self.foreColour, bg=self.backColour)
        self.gameDescLbl.config(text=self.gameDesc, fg=self.foreColour, bg=self.backColour)
        frame.config(bg=self.backColour)
        self.options.config(bg=self.backColour, fg=self.foreColour, activebackground=self.foreColour)
        self.dropdown.config(bg= self.backColour, fg = self.foreColour)

        #LABELS
        for i in range(0, 7):
            if self.arrActive[i]:
                self.arrForeColour[i] = self.foreColour
            else:
                self.arrForeColour[i] = self.backColour
            self.arrBackColour[i] = self.backColour

        self.lblTrex.config(bg=self.arrBackColour[0], fg=self.arrForeColour[0], highlightbackground=self.arrForeColour[0])
        self.lblPoint.config(bg=self.arrBackColour[1], fg=self.arrForeColour[1], highlightbackground=self.arrForeColour[1])
        self.lblD.config(bg=self.arrBackColour[2], fg=self.arrForeColour[2], highlightbackground=self.arrForeColour[2])
        self.lblChild.config(bg=self.arrBackColour[3], fg=self.arrForeColour[3], highlightbackground=self.arrForeColour[3])
        self.lblWeak.config(bg=self.arrBackColour[4], fg=self.arrForeColour[4], highlightbackground=self.arrForeColour[4])
        self.lblSnake.config(bg=self.arrBackColour[5], fg=self.arrForeColour[5], highlightbackground=self.arrForeColour[5])
        self.lblStatus.config(bg=self.arrBackColour[6], fg=self.arrForeColour[6], highlightbackground=self.arrForeColour[6])

#COMING SOON:
#Options to change number of players mid-game
#Options to increase or decrease intensity


root = Tk()
[w, h] = root.winfo_screenwidth(), root.winfo_screenheight() - 20
print(w,h)
root.wm_attributes('-type', 'splash')
#root.attributes('-fullscreen', True)
#root.overrideredirect(True)
#root.geometry("{0}x{1}+0+0".format(w, h))

cog = PhotoImage(file="settings.jpg")
logo = PhotoImage(file="gazeboed4.png")
addim = PhotoImage(file="plus.png")
subim = PhotoImage(file="minus.png")

frame = Frame(root, width=w, height=h, bg="#043605", relief="flat")
frame.pack_propagate(0)  # don't shrink
frame.pack()

app = APP(frame)
root.mainloop()
#root.destroy()


