from tkinter import *
from PIL import ImageTk, Image

langas = Tk()

langas.title("Pakaruoklis")

virsus = Frame(langas)
apacia = Frame(langas)
lives6 = ImageTk.PhotoImage(Image.open("img\\lives6.png"))
lives5 = ImageTk.PhotoImage(Image.open("img\\lives5.png"))
lives4 = ImageTk.PhotoImage(Image.open("img\\lives4.png")) 
lives3 = ImageTk.PhotoImage(Image.open("img\\lives3.png"))
lives2 = ImageTk.PhotoImage(Image.open("img\\lives2.png"))
lives1 = ImageTk.PhotoImage(Image.open("img\\lives1.png"))   
lives0 = ImageTk.PhotoImage(Image.open("img\\lives0.png")) 

def pasleptas_zodis():
    pass


spejamas_zodis_label = Label(virsus, font=6, relief=SUNKEN, height=2, text="\u273a \u273a \u273a \u273a \u273a \u273a \u273a \u273a",)
spejamos_raides_label = Label(virsus, text="Įrašykite spėjamą raidę: ", font=1)
spejama_raide_entry = Entry(virsus, width=3)
mygtukas = Button(virsus,font=2, fg="#f00", text="Spėti\u261e")

fotke0 = Label(apacia, relief=RIDGE, image=lives0)
fotke1 = Label(apacia, relief=RIDGE, image=lives1)
fotke2 = Label(apacia, relief=RIDGE, image=lives2)
fotke3 = Label(apacia, relief=RIDGE, image=lives3)
fotke4 = Label(apacia, relief=RIDGE, image=lives4)
fotke5 = Label(apacia, relief=RIDGE, image=lives5)
fotke6 = Label(apacia, relief=RIDGE, bd=3, image=lives6)
statusbaras_left = Label(apacia, anchor=W, width=20, bd=2, font=3, relief=SUNKEN, height=2, text="Pradėkite žaidimą")
statusbaras_right = Label(apacia, bd=2, font=3, relief=SUNKEN, height=2, text="Galimi 6 neteisingi spėjimai")

virsus.pack(side=TOP)
spejamas_zodis_label.grid(row=0, column=0, columnspan=4, sticky=W+E)
spejamos_raides_label.grid(row=1, column=0, sticky=W)
mygtukas.grid(row=1, column=3)
spejama_raide_entry.grid(row=1, column=1)

apacia.pack(side=BOTTOM)
fotke6.grid(row=0, columnspan=2)
fotke5.grid(row=0, columnspan=2)
fotke4.grid(row=0, columnspan=2)
fotke3.grid(row=0, columnspan=2)
fotke2.grid(row=0, columnspan=2)
fotke1.grid(row=0, columnspan=2)
fotke0.grid(row=0, columnspan=2)
statusbaras_left.grid(row=1, column=0, sticky=W+E)
statusbaras_right.grid(row=1, column=1, sticky=W+E)

langas.mainloop()