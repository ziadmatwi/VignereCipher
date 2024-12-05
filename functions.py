def inputfunction():
    print("Üdv! Ez a program segít Vignere kódolt szöveget írni, olvasni, vagy feltörni.")
    choice=int(input("Melyik funkciót választja? Szöveg írása(1) Szöveg beolvasása(2) Szöveg feltörése(3) Kilépés(0)"))
    return choice

def inputtext():
    plaintext = input("Kérem adja meg az alapszöveget: ").upper().replace(" ", "")
    return plaintext

def inputkey():
    inputkey = input("Kérem adja meg a kulcsot: ").upper

def encoding():
    plaintext = inputtext()
    print(plaintext)