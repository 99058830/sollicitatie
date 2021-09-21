#Meer dan 4 jaar praktijkervaring met dieren-dressuur OF meer dan 5 jaar ervaring met jongleren OF meer dan 3 jaar praktijkervaring met acrobatiek
#In bezit van een Diploma MBO-4 ondernemen
#In bezit van een geldig Vrachtwagen rijbewijs
#In bezit van een hoge hoed
#Is man EN heeft Snor breder dan 10 cm OF is vrouw EN draagt rood krulhaar langer dan 20 cm
#Is langer dan 150 cm
#Is zwaarder dan 90 kg
#Heeft Certificaat “Overleven met gevaarlijk personeel”J

print("""
***********************************************
*   Sollicitatieformulier Circus directeur    *
***********************************************""")

naam = input("Wat is uw naam? ")
gewicht = int(input ("Wat is uw lichaamsgewicht in KG? "))
if gewicht > 90:
    gewicht = True
else:
    gewicht = False
print(gewicht)
lengte = int(input("Hoe lang bent u in centimeters? "))
if lengte > 150:
    lengte = True
else:
    lengte = False
print(lengte)
dierenDressuur = int(input("Hoeveel jaar heeft u praktijkervaring met dieren-dressuur? "))
if dierenDressuur > 4:
    dierenDressuur = True
else:
    dierenDressuur = False
print(dierenDressuur)
jongleren = int(input("Hoeveel jaar heeft u praktijk ervaring met jongleren? "))
if jongleren > 5:
    jongleren = True
else:
    jongleren = False
print(jongleren)
acrobatiek = int(input("Hoeveel jaar heeft u acrobatiek ervaring? "))
if acrobatiek > 3:
    acrobatiek = True
else:
    acrobatiek = False
print(acrobatiek)
diploma = str(input ("Heeft u een diploma MBO-4 ondernemen? J/N "))
if diploma == "J" or "j":
    diploma = True
else:
    diploma = False
print(diploma)
vrachtwagenRijbewijs = input ("Heeft u een geldig vrachtwagen rijbewijs? J/N ")
if vrachtwagenRijbewijs == "J" or "j":
    vrachtwagenRijbewijs = True
else:
    vrachtwagenRijbewijs = False
print(vrachtwagenRijbewijs)
hogeHoed = input ("Bent u in bezit van een hoge hoed? J/N ")
if hogeHoed == "J" or "j":
    hogeHoed = True
else:
    hogeHoed = False
print(hogeHoed)
certificaat = input ("Bent u in bezit van een certificaat overleven met gevaarlijk personeel? J/N ")
if certificaat == "j" or "J":
    certificaat = True
else:
    certificaat = False
print(certificaat)
manVrouw = input ("Bent u een man of vrouw? M/V ")
if manVrouw == "m" or "M":
    print(manVrouw)
    manSnor = int(input ("Hoe breedt is uw snor? in centimeter! "))
    if manSnor > 10:
        manSnor = True
    else:
        manSnor = False
    print(manSnor)
elif manVrouw == "v" or "V":
    vrouwLengte = int(input ("Heeft u rood krullend haar? Zo ja, wat is de lengte? in centimeters! "))
    if vrouwLengte > 20:
        vrouwLengte = True
    else:
        vrouwLengte = False
    print(vrouwLengte)

werkervaring = [dierenDressuur, jongleren, acrobatiek]
overig = [gewicht, lengte, diploma, vrachtwagenRijbewijs, hogeHoed, certificaat, manSnor]

overig = all(overig)
werkervaring = any(werkervaring)

aangenomen = overig and werkervaring

if aangenomen == True:
    print ("Beste",naam," gefeliciteerd, u bent aangenomen.")
else:
    print ("Beste",naam," helaas, u bent niet aagenomen.")