from tkinter import *
from PIL import ImageTk, Image
from random import choice
import zodziai
zodis = choice(zodziai.tinkami_zodziai())
langas = Tk()

langas.title("Pakaruoklis")
langas.geometry("400x630")

virsus = Frame(langas)
apacia = Frame(langas)
lives6 = ImageTk.PhotoImage(Image.open("img\\lives6.png"))
lives5 = ImageTk.PhotoImage(Image.open("img\\lives5.png"))
lives4 = ImageTk.PhotoImage(Image.open("img\\lives4.png")) 
lives3 = ImageTk.PhotoImage(Image.open("img\\lives3.png"))
lives2 = ImageTk.PhotoImage(Image.open("img\\lives2.png"))
lives1 = ImageTk.PhotoImage(Image.open("img\\lives1.png"))   
lives0 = ImageTk.PhotoImage(Image.open("img\\lives0.png")) 

gyvybes = [lives6, lives5, lives4, lives3, lives2, lives1, lives0]

slaptos_raides = []
zodzio_raides = []
for raide in zodis:
    zodzio_raides.append(raide)
print(zodzio_raides)
spetos_raides = []
slaptos_raides = ["\u273a" for symbol in range(0, len(zodzio_raides))]

print(slaptos_raides)



def pasleptas_zodis():
    speta_raide = spejama_raide_entry.get().upper()
    if speta_raide.isalpha() is False:
        statusbaras["text"] = "Simbolis turi būti raidė"
    if len(speta_raide) > 1:
        statusbaras["text"] = "Spėti reikia vieną raidę"
    if speta_raide in zodzio_raides:
        slaptos_raides[zodzio_raides.index(speta_raide)] = speta_raide
    spejamas_zodis_label["text"] = " ".join(slaptos_raides) 
    spejama_raide_entry.delete(0, len(spejama_raide_entry.get()))


print("".join(zodzio_raides))
spejamas_zodis_label = Label(virsus, font=6, relief=SUNKEN, height=2, text=slaptos_raides)
spejamos_raides_label = Label(virsus, text="Įrašykite spėjamą raidę: ", font=1)
spejama_raide_entry = Entry(virsus, width=3)
mygtukas = Button(virsus,font=2, fg="#f00", text="Spėti\u261e", command=pasleptas_zodis)

fotke0 = Label(apacia, relief=RIDGE, image=lives0)
fotke1 = Label(apacia, relief=RIDGE, image=lives1)
fotke2 = Label(apacia, relief=RIDGE, image=lives2)
fotke3 = Label(apacia, relief=RIDGE, image=lives3)
fotke4 = Label(apacia, relief=RIDGE, image=lives4)
fotke5 = Label(apacia, relief=RIDGE, image=lives5)
fotke6 = Label(apacia, relief=RIDGE, bd=3, image=lives6)
statusbaras = Label(apacia, anchor=W, width=18, bd=2, font=3, relief=SUNKEN, height=2, text="Pradėkite žaidimą")


virsus.pack(side=TOP)
spejamas_zodis_label.grid(row=0, column=0, columnspan=4, sticky=W+E)
spejamos_raides_label.grid(row=1, column=0, sticky=W)
mygtukas.grid(row=1, column=3, padx=2, pady=2)
spejama_raide_entry.grid(row=1, column=1, padx=2)

apacia.pack(side=BOTTOM)
fotke6.grid(row=0, columnspan=2, sticky=N)
fotke5.grid(row=0, columnspan=2)
fotke4.grid(row=0, columnspan=2)
fotke3.grid(row=0, columnspan=2)
fotke2.grid(row=0, columnspan=2)
fotke1.grid(row=0, columnspan=2)
fotke0.grid(row=0, columnspan=2)
statusbaras.grid(row=1, column=0, columnspan=3, sticky=W+E, pady=2)


langas.mainloop()