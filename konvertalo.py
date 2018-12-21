def konvertalo(fajl_neve):
    with open(fajl_neve) as file:
        szoveg = file.read()
        szo = szoveg.split(" ")
        for betu in szo:
            if betu != '\n':
               print(chr(int(betu,2)), end='')
            else:
                print('')
