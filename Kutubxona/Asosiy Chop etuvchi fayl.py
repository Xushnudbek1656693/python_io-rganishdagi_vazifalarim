import kitob_haqida
import kitob_qosh
import kitob_royxat

while True:
    id = int(input("""
"Bizning onlayn kutubxonamizga xush kelibsz bolimlardan birini tanlang. "
1) Kitob qosh
2) Kitob royxati
3) Kitob qidirish
4) Chiqish
>>> """))
    if id == 1:
        kitob_qosh.mein()
    elif id == 2:
        kitob_royxat.mein()
    elif id == 3:
        kitob_haqida.mein()
    elif id == 4:
        print("Bizning dokonimizdan foydalanganingiz uchun raxmat. ")
        break
    else:
        print("Xato bolm tanladingiz iltimos boshqa bolim tanlang !!!!!")




