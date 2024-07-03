import dokon

def mein():
    while True:
        b = input(f"Kitob kiritasizmi (ha\yoq) ")
        if b=='yoq':
            break
        else:
            a = input("Kitobning nominin kiriting; ")
            b = input("Kitobning mualifini kiriting; ")
            c = input("Kitobning yilini kiriting; ")
            f = input("Kitobning betini kiriting; ")
            g = input("Kitobning turini kiriting; ")
            dokon.mein(a,b,c,f,g)
            print(a, "Nomli kitobni kiritdingiz !!!!!")   
    # a = input("dsds")
    # b = input("skdfd")
    # c = input("skskdc")
    # dokon.mein(a,b,c)
dokon.mein('diqqat', 'kel  nyu', 2015, 203, 'rivojlanish')
dokon.mein('diqqat2', 'kel  nyu', 2017, 200, 'rivojlanish')