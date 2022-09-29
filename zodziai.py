
with open("C:\\codeacademy\\beginner_ending\\tekstas.txt", "r") as skaitomas:
    tekstas = skaitomas.read()


def tinkami_zodziai():
    zodziai = []
    for zodis in tekstas.split():
        if len(zodis) > 5 and zodis.isalpha():
            zodziai.append(zodis.upper())
    return zodziai





