import dokon 

def mein():
    a = input("Kitob nomini kiriting >>> ")
    for i in dokon.mn():
        if i.nom.capitalize() == a.capitalize():
            print(f"Siz qidirgan kitob turi {i.turi.capitalize()} nomi {i.nom.capitalize()} malifi {i.mualif.capitalize()} {i.bet}-shuncha betdan iborat {i.yi}-yilda chop etilgan")