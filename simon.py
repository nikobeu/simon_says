# wer das ließt isst kinder

import random
import time

import keyboard

befehl = 0
fakebefehl = 0
erwartung = 0
press = 0
points = 0
highscore = 100
numpad_8_pressed = False
numpad_4_pressed = False
numpad_6_pressed = False
numpad_2_pressed = False
def on_key_event(event):
    global numpad_8_pressed
    if event.name == '8':
        numpad_8_pressed = True
    else:
        pass
def on_key_event(event):
    global numpad_4_pressed
    if event.name == '4':
        numpad_4_pressed = True
    else:
        pass
def on_key_event(event):
    global numpad_6_pressed
    if event.name == '6':
        numpad_6_pressed = True
    else:
        pass
def on_key_event(event):
    global numpad_2_pressed
    if event.name == '2':
        numpad_2_pressed = True
    else:
        pass


while True:
    while True:
        while True:
            befehl = 0
            fakebefehl = 0
            erwartung = 0
            press = 0

            simon = random.randrange(1, 9)

            if simon > int(5):
                if simon == 5:
                    break
                elif simon == 6:
                    befehl = str("Links")
                    erwartung = str(4)
                    break
                elif simon == 7:
                    befehl = str("Rechts")
                    erwartung = str(6)
                    break
                elif simon == 8:
                    befehl = str("Oben")
                    erwartung = str(8)
                    break
                elif simon == 9:
                    befehl = str("Unten")
                    erwartung = str(2)
                    break
                else:
                    print("du idiot hast nen fehler gemacht1")
            else:
                if simon == 5:
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
            print("\n\naktuelle punkte :", str(points),       "aktueller highscore : ", str(highscore))

            #print(simon)
            time.sleep(3)
            points = points+1
            break

        elif not befehl == False:
            # hier musst du wieder einstellen wie du das ganze auf den lcd machen willst
            print(fr"simon says", str(befehl))
            print("\n\naktuelle punkte :", str(points),       "aktueller highscore : ", str(highscore))
            #print(simon)
            points = points+1
            erwartung = False
            time.sleep(1)
            break

        else:
            break
