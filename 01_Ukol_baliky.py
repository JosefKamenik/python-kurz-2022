baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

balik = input("Zadej kod baliku:")

if (f"{baliky[balik]}") == "True":
  print("Balík byl předán kurýrovi")
elif (f"{baliky[balik]}") == "False":
  print("Balík zatím nebyl předán kurýrovi")
else:
  print("Balik neexistuje")