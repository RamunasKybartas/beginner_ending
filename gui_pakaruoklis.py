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

fotkes = [lives6, lives5, lives4, lives3, lives2, lives1, lives0]

slaptos_raides = []
zodzio_raides = []
for raide in zodis:
    zodzio_raides.append(raide)
print(zodzio_raides)
spetos_raides = []
slaptos_raides = ["\u273a" for symbol in range(0, len(zodzio_raides))]
gyvybes = IntVar()
ft_index = IntVar()
raidziu_setas = set(zodis)
print(slaptos_raides)

def rasti_raides(zodzio_raides, speta_raide):
    keiciamos_raides = [i for i, raide in enumerate(zodzio_raides) if raide == speta_raide]
    string_raides = "".join(map(str,keiciamos_raides))
    return string_raides

# def gauti_skaicius(keiciamos_raides_index):
#     for i in keiciamos_raides_index:
#         print(i)


def pasleptas_zodis():
    speta_raide = spejama_raide_entry.get().upper()
    if speta_raide.isalpha() is False:
        statusbaras["text"] = "Simbolis turi būti raidė"
        gyvybes.set(gyvybes.get()+1)
        fotke.config(image=fotkes[ft_index.get()])
    if len(speta_raide) > 1:
        statusbaras["text"] = "Spėti reikia vieną raidę"
        gyvybes.set(gyvybes.get()+1)
        fotke.config(image=fotkes[ft_index.get()])
    if speta_raide in zodzio_raides:
        rasti_raides(zodzio_raides, speta_raide)
        for string_raides in range(len(zodzio_raides)):
            if speta_raide == zodzio_raides[string_raides]:
                slaptos_raides[string_raides] = speta_raide
    if speta_raide in raidziu_setas: 
        raidziu_setas.remove(speta_raide)
    else:
        ft_index.set(ft_index.get()+1)  
        gyvybes.set(gyvybes.get()+1)
        fotke.config(image=fotkes[ft_index.get()])
                    
    if len(raidziu_setas) == 0:
        statusbaras["text"] = "Laimėjote!"
    if gyvybes.get() == 6:
        statusbaras["text"] = "Pralaimėjote!"
    spejamas_zodis_label["text"] = slaptos_raides
    spejama_raide_entry.delete(0, len(spejama_raide_entry.get()))

print("".join(zodzio_raides))
spejamas_zodis_label = Label(virsus, font=6, relief=SUNKEN, height=2, text=slaptos_raides)
spejamos_raides_label = Label(virsus, text="Įrašykite spėjamą raidę: ", font=1)
spejama_raide_entry = Entry(virsus, width=3)
mygtukas = Button(virsus,font=2, fg="#f00", text="Spėti\u261e", command=pasleptas_zodis)
spejama_raide_entry.bind("<Return>", lambda event: pasleptas_zodis())


fotke = Label(apacia, relief=RIDGE, image=lives6)
statusbaras = Label(apacia, anchor=W, width=18, bd=2, font=3, relief=SUNKEN, height=2, text="Pradėkite žaidimą")


virsus.pack(side=TOP)
spejamas_zodis_label.grid(row=0, column=0, columnspan=4, sticky=W+E)
spejamos_raides_label.grid(row=1, column=0, sticky=W)
mygtukas.grid(row=1, column=3, padx=2, pady=2)
spejama_raide_entry.grid(row=1, column=1, padx=2)

apacia.pack(side=BOTTOM)
fotke.grid(row=0, columnspan=2, sticky=N)

statusbaras.grid(row=1, column=0, columnspan=3, sticky=W+E, pady=2)


langas.mainloop()

    





        
