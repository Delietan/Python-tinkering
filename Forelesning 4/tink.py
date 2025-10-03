svar = float(input("Skriv inn et tall: "))
størsteTall = "tomt"

if svar == "":
    print("Du skrev ikke inn noe tall.")
else:
    størsteTall = svar
    
while svar != "":
    svar = float(input("Skriv inn et tall: "))
    if svar > størsteTall:
        størsteTall = svar

if størsteTall != "tomt":
    print("Ditt støreste tall var", størsteTall)