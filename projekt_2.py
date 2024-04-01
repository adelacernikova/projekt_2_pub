"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - COWS & BULLS
author: Adéla Černíková
email: adela.cernikova@seznam.cz
discord: adelacernikova_89606
"""

import time
import random

oddelovac = "-" * 40


# Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, 
# pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky
def zkontroluj_cislo(hadane, hledane):
    hadane_list = list(hadane)
    hadane_set = set(hadane)
    if hadane_list[0] == "0":
        print("cislo zacina 0")
    elif hadane.isdigit():
        if int(hadane) > 9999:
            print("zadane cislo je moc dlouhe")
        elif int(hadane) <1000:
            print("zadane cislo je moc kratke")
        elif len(hadane_list) > len(hadane_set):
            print("cislice se opakuji")
        else:
            porovnani_cisel(hadane, hledane) # funkce definovana nize
    else:
        print("Zadana hodnota neni cislo")




# Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), 
# příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). 
# Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows).
def porovnani_cisel(hadane, hledane):
    bulls = 0
    cows = 0
    hledane_list = list(hledane)
    for index, symbol in enumerate(str(hadane)):
        if symbol == hledane_list[index]:
            bulls += 1
        elif symbol in hledane_list:
            cows += 1
    if bulls == 1:
        text_bulls = "bull"
    else:
        text_bulls = "bulls"
    if cows == 1:
        text_cows = "cow"
    else:
        text_cows = "cows"
    print(bulls, text_bulls, cows, text_cows)



# uzivatel opakuje zadavani cisel dokud se hadane cislo nerovna hledanemu cislu
def opakovani(hadane, hledane):
    pocet_hadani = 1
    while hadane != hledane:
        print("hledane cislo: ", hledane)
        zkontroluj_cislo(hadane,  hledane)
        pocet_hadani += 1
        print(oddelovac)
        hadane = input ()
    print("Correct, you've guessed the right number in", pocet_hadani, "guesses!")






######################### spousteni programu #############################
    
# Program pozdraví užitele a vypíše úvodní text
print ("Hi there!",
       oddelovac,
      "I've generated a random 4 digit number for you.",
      "Let's play a bulls and cows game.",
      oddelovac,  
      "Enter a number:",
      oddelovac, sep="\n")

hadane_cislo = input ()

# Začáteční čas hádání
cas_zacatek = time.time()


# Program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
def vygeneruj_cislo():
    cislice = random.sample(range(1, 10), 4)  
    return ''.join(map(str,cislice))

hledane_cislo = vygeneruj_cislo()


# spousteni opakovaci casti zadavani cisla uzivatelem, dokud nenajde hledane cislo
opakovani(hadane_cislo,  hledane_cislo)

print (oddelovac)

# Koncový čas hadani
cas_konec = time.time()

# Vypočtení délky běhu kódu
doba_behu = cas_konec - cas_zacatek
print("It took {:.2f} seconds".format(doba_behu))

print (oddelovac)

