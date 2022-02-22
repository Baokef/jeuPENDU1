import random

with open("mots.txt") as file:
    data = file.read()
    mots = data.split()
    resultat = random.choice(mots).lower()

    # mots_position = random.randint(0, len(mots)-1)
    # resultat = mots[mots_position]

    essais = 6
    panneau = ""
    lettre_dans_resultat = ""
for l in resultat:
    panneau = panneau + "_ "
print(">> Bienvenue dans le pendu <<")
while essais > 0:
    print("\nMot à deviner : ", panneau)
    proposition = input("proposez une lettre : ")

    if proposition in resultat:
        lettre_dans_resultat = lettre_dans_resultat + proposition
        print("ok!!!")
    else:
        print("mauvais choix")
        essais = essais - 1
        print("nombre de choix restant : ", essais)
        if essais == 0:
            print("--------------\n")
            print("   |........|||")
        if essais <= 1:
            print("   |--------|-|-")
            print("   |---------|--")
        if essais <= 2:
            print("   |         0")
        if essais <= 3:
            print("   |        / \\")
        if essais <= 4:
            print("   |         |")
        if essais <= 5:
            print("   |         |")
            print("   |        / \\")
        if essais <= 6:
            print("  /|\\        ")
            print("---|-----------------")

    panneau = ""
    for x in resultat:
        if x in lettre_dans_resultat:
            panneau += x + " "
        else:
            panneau += "_ "

    if "_" not in panneau:
        print("BRAVO...!")
        break

print()
print("!!!Game is over!!!!")
print(resultat)
