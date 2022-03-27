from math import ceil

telefon = input("Zadej telefonni cislo, na které chceš odeslat zprávu: ")

if (len(telefon)) == 9 or (len(telefon)) == 13:
    zprava = input("Napiš zprávu, kterou chceš odeslat: ")
    print(ceil(len(zprava)/180)*3)
if not (len(telefon)) ==9 and not (len(telefon)) == 13:
    print("Zadej správné telefonní číslo")