import pandas as pd
import csv

with open('pokemon.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dex = []
    name = []
    hp = []
    attack = []
    defense = []
    sp_atk = []
    sp_def = []
    speed = []
    bst = []
    type1 = []
    type2 = []
    gen = []
    gender_ratio = []
    for row in readCSV:
        dex.append(row[0])
        name.append(row[1])
        hp.append(row[2])
        attack.append(row[3])
        defense.append(row[4])
        sp_atk.append(row[5])
        sp_def.append(row[6])
        speed.append(row[7])
        bst.append(row[8])
        type1.append(row[9])
        type2.append(row[10])
        gen.append(row[11])
        gender_ratio.append(row[12])

team = []

def compare_pkmn(pkmn):
    try:
        index_num = name.index(pkmn)
        print(name[index_num] + " stats")
        print("Base Stat Total: " + bst[index_num])
        if type2[index_num] == "":
            print("Type: " + type1[index_num])
        else:
            print("Type: " + type1[index_num] + ", " + type2[index_num])

    except ValueError:
        print("Please enter a valid Pokemon")
    return

def search_by_name(pkmn):
    try:
        index_num = name.index(pkmn)
        print(name[index_num] + " stats")
        print("Base Stat Total: " + bst[index_num])
        if type2[index_num] == "":
            print("Type: " + type1[index_num])
        else:
            print("Type: " + type1[index_num] + ", " + type2[index_num])
        option = input("Select an option: \n1. Add to team \n2. See more stats \n3. Compare with another Pokemon")
        if option == '1':
            team.append(pkmn)
            print("Your team: ")
            print(team)
        elif option == '2':
            print("HP: " + hp[index_num])
            print("Attack: " + attack[index_num])
            print("Defense: " + defense[index_num])
            print("Sp. Atk.: " + sp_atk[index_num])
            print("Sp. Def.: " + sp_def[index_num])
            print("Speed: " + speed[index_num])
            if input("Add to team? ") == "Yes":
                team.append(pkmn)

        elif option == '3':
            compare_with = input("Compare with? ")
            compare_pkmn(compare_with)

        else:
            print("That was not a valid option. Enter 1, 2, or 3.")

    except ValueError:
        print("Please enter a valid Pokemon")

    return

while len(team) < 6:
    search_by_name(input("Search for a Pokemon: "))
    if len(team) < 6:
        print("You have " + str(len(team)) + " Pokemon in your team.")
print("You finally have a complete team!")
