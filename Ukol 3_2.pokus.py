from math import ceil

overeni = False

def funkce_overeni(telefon):
   #sem pises co ta funkce dela..
    if (len(telefon)) == 9:
        return True
    elif len(telefon) == 13:
        return True
    else:
        overeni = False

def funkce_vypocet_ceny(zprava):
  # sem pises co ta druha funkce dela
    return ceil(len(zprava)/180)*3

telefon = (input("Zadej telefonni cislo, na které chceš odeslat zprávu: "))

if (funkce_overeni(telefon)) == True:
    zprava = input("Napiš zprávu, kterou chceš odeslat: ")
else:
    print("Napiš správné číslo")
    
print(f"Výsledná cena za odeslání zprávy je {funkce_vypocet_ceny(zprava)} korun.")