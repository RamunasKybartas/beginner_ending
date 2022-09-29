import zodziai
from random import choice

zodis = choice(zodziai.tinkami_zodziai())
print(zodis)

def pasleptas_zodis():
    spetos_raides = []
    zodzio_raides = []
    slaptos_raides = []
    gyvybes = 6
    for raide in zodis:
        zodzio_raides.append(raide)

    for zvaigzdute in range(len(zodis)):
            slaptos_raides.append("\u273a")

    while len(zodzio_raides) > 0 and gyvybes > 0:
        
        print("Zodis: "," ".join(slaptos_raides))
        speta_raide = input("Įveskite raidę: ").upper()
        print(f"spetos raides: {' '.join(spetos_raides)}")
        
        for i in range(len(zodis)):
            if speta_raide == zodis[i]:
                slaptos_raides[i] = speta_raide
        
        if speta_raide in zodzio_raides:
            while speta_raide in zodzio_raides: zodzio_raides.remove(speta_raide)
        else:
            gyvybes -= 1
        
        if speta_raide not in spetos_raides:
            spetos_raides.append(speta_raide)
        else:
            print("Jus jau spejote sia raide")    
        
    if gyvybes == 0:
            print("Jums pritruko gyvybiu")
    else:
        print("Sveikiname, atspejote zodi")
        
    print(zodis)

pasleptas_zodis()
      

            
