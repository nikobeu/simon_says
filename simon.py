# wer das ließt isst kinder

import random

befehl = 0
fakebefehl = 0
erwartung = 0
press = 0

while True:
    while True:

        befehl = 0
        fakebefehl = 0
        erwartung = 0
        press = 0

        simon = random.randrange(1, 9)

        if simon > int(5):
            if simon == 5:
                befehl = str("drehe dich 3 mal")
                break
            elif simon == 6:
                befehl = str("Links")
                erwartung = "Left"
                break
            elif simon == 7:
                befehl = str("Rechts")
                erwartung = "Right"
                break
            elif simon == 8:
                befehl = str("Oben")
                erwartung = "Up"
                break
            elif simon == 9:
                befehl = str("Unten")
                erwartung = "Down"
                break
            else:
                print("du idiot hast nen fehler gemacht1")
        else:
            if simon == 5:
                befehl = str("drehe dich 3 mal")
                break
            if simon == 1:
                fakebefehl = str("Links")
                erwartung = False
                break
            elif simon == 2:
                fakebefehl = str("Rechts")
                erwartung = False
                break
            elif simon == 3:
                fakebefehl = str("Oben")
                erwartung = False
                break
            elif simon == 4:
                fakebefehl = str("Unten")
                erwartung = False
                break
            else:
                print("du idiot hast nen fehler gemacht2")

    if not fakebefehl == False:
        #hier musst du einstellen wie du das ganze auf den lcd machen willst
        print(fr"drücke jetzt", str(fakebefehl))
        print(simon)
        input()

    elif not befehl == False:
    # hier musst du wieder einstellen wie du das ganze auf den lcd machen willst
        print(fr"simon says", str(befehl))
        print(simon)
        input()

    else:
        print("du hast nen schaden")


