jami = [] 
def mein(nomm, mualiff, yll,be,tu):
    class Kitob:
        def __init__(self, nom, mualif, yl,bet,turi ):
            self.nom = nom
            self.mualif = mualif
            self.yi = yl
            self.bet = bet
            self.turi = turi
    kitob = Kitob(nomm, mualiff, yll,be,tu)
    jami.append(kitob)

def mn():
    return jami
