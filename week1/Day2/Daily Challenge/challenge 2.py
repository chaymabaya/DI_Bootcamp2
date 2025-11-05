chaine = input ("entrer une chaine")
nouvelle_chaine = ""
dernier_chaine = ""
for lettre in chaine :
    if lettre != dernier_chaine :
        nouvelle_chaine = nouvelle_chaine + lettre
        dernier_chaine = lettre

print("Chaîne modifiée :", nouvelle_chaine)
