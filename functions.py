def inputfunction():
    print("Üdv! Ez a program segít Vignere kódolt szöveget írni, olvasni, vagy feltörni.")
    choice=int(input("Melyik funkciót választja? Szöveg írása(1) Szöveg beolvasása(2) Szöveg feltörése(3) Kilépés(0)"))
    return choice

def inputtext():
    inputtext = input("Kérem adja meg az alapszöveget: ")
    return inputtext

def inputkey():
    inputkey = input("Kérem adja meg a kulcsot: ")

def encoding():
    plaintext = inputtext()
    print(plaintext)