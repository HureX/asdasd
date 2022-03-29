elso = int(input("A 1. megállónál felszállók száma:"))
masodik = int(input("A 2. megállónál felszállók száma:"))
harmadik = int(input("A 3. megállónál felszállók száma:"))
negyedik  = int(input("A 4. megállónál felszállók száma:"))
otodik  = int(input("A 5. megállónál felszállók száma:"))
hatodik  = int(input("A 6. megállónál felszállók száma:"))
hetedik  = int(input("A 7. megállónál felszállók száma:"))
nyolcadik  = int(input("A 8. megállónál felszállók száma:"))
kilencedik  = int(input("A 9. megállónál felszállók száma:"))
tizedik  = int(input("A 10. megállónál felszállók száma:"))

osszead = elso + masodik + harmadik + negyedik + otodik + hatodik + hetedik + nyolcadik + kilencedik + tizedik ;
atlagszamitas = osszead / 10 ;

print ("Az iskolánál {0} tanuló fog leszállni a buszról.".format(osszead))
print ("A megállókban az átlagosan felszálló tanulók száma {0} fő.".format(atlagszamitas))

