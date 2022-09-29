import zodziai
from random import choice

zodis = choice(zodziai.tinkami_zodziai())
print(zodis)




# print(zodzio_raides)

# speta_raide = input("Įveskite raidę: ")
# spetos_raides.append(speta_raide)

def pasleptas_zodis():
    spetos_raides = []
    zodzio_raides = []
    slaptas_zodis = []
    for raide in zodis:
        zodzio_raides.append(raide)

    while len(zodzio_raides) > 0:
        
        print(f"spetos raides: {' '.join(spetos_raides)}")
        speta_raide = input("Įveskite raidę: ").upper()
        if speta_raide not in spetos_raides:
            spetos_raides.append(speta_raide)
        if speta_raide in zodzio_raides:
            while speta_raide in zodzio_raides: zodzio_raides.remove(speta_raide)
            # zodzio_raides.remove(speta_raide)
        elif speta_raide in spetos_raides:
            print("Jus jau spejote sia raide") 
    
        print(slaptas_zodis)
    print(zodis)

pasleptas_zodis()
      
