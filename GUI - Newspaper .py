import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title("My First NewsPaper")
root.geometry("1600x1200")

# Heading 0
H = Label(text="Cricket Katta", font="Times 30 bold", bg="black", fg="white", borderwidth=3, padx=5, pady=5, relief=SUNKEN)
H.pack(fill=X)

# date 0
D = Label(text="Date : 04.05.2021",  bg = "black",fg="yellow", borderwidth=3, padx=5, pady=5, relief=SUNKEN ,
          font = "Helvetica 15 bold")
D.place(x=1150, y= 20)

# Left Text-1
T = Label(text=''' VIVO IPL 2021 POSTPONED ''', bg="black", fg="white", padx=12, pady=12 , font = "comicsans 20 bold")
T.place(x=10, y=100)

# left text 2
T4 = Label(text = '''The Indian Premier League Governing Council (IPL GC)
and Board ofControl for Cricket in India (BCCI) in an emergency
meeting has unanimously decided to postpone IPL 2021 season.

The BCCI does not want to compromise on the safety of the players,
support staff and the other participants involved in organising the IPL.
This decision was taken keeping the safety, health and wellbeing
of all the stakeholders in mind.
''',  bg = "black",fg = "white" , padx = 5 , pady = 5 , font = "comicsans 11 ", justify=tk.LEFT)
T4.place(x = 10 , y = 450)

# image 1
image = Image.open("C:/Users/Omkar/Downloads/001.jpg")

P = ImageTk.PhotoImage(image)
L = Label(image = P)
L.pack()
L.place(x=10, y=170)

# Right Text-2
T2 = Label(text=''' ABD: The force behind RCB's great early run''', bg="red", fg="white", padx=5, pady=5 ,
           font = "comicsans 20 bold")
T2.place(x=450, y=100)

# Text 2.1
T3 = Label(text = '''It was an exhibition of his cricketing intelligence,which is what makes
the South African such a special player.Add his copybook batting
technique to hisability to think on his feet, and you have the best T20
batsman in the world even at the age of 37.

For Dale Steyn, it is the way de Villiers’“eyes and hands work together
sowonderfully” that makes him special.Second is “courage”.He plays those
ramp shots when he gets down on his knee but de Villiers’never takes his
eyes offthe ball,said Steyn.

Steyn knows his game best. They are close friends. At South Africa they
have been teammates for long. And the great fast bowler also knows what
it is to be on the receiving end of AB’s blade in the IPL.

In the 2014 edition, at Bengaluru’s M Chinnaswamy Stadium, with Steyn
leading the Sunrisers Hyderabad attack, de Villiers took him for 24 runs
in the 19th over of the innings on way to a match-winning 89 not out.
Steyn’s first three overs had gone for just 16 runs. At the same venue,
two years earlier, de Villiers’ had smashed 23 runs off a Steyn over.''' , bg = "black",
fg = "white" , padx = 5 , pady = 5 , font = "comicsans 11 ", justify=tk.LEFT)
T3.place(x = 865 , y = 165)
 
#  image 2
I1 = Image.open("C:/Users/Omkar/Downloads/ABD (1).jpg")
I1 = I1.resize((400, 350), Image.ANTIALIAS)
P1 = ImageTk.PhotoImage(I1)
L1 = Label(image = P1)
L1.pack()
L1.place(x=450, y=160)
 
