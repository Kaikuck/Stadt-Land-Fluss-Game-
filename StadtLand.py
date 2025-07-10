#stadt land fluss game
import random
import json

InputData = open ("countries+cities.json")

buchstaben = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def load_database():
        return json.load(InputData)

def sort_database(json_array):
    # nach Ländern sortieren
    names = [item['name'] for item in json_array]
    # nach Städten sortieren
    all_cities = []
    for item in json_array:
        all_cities.extend(item['cities'])
    return names, all_cities

def zufallsbuchstabe():
    return random.choice(buchstaben)

def pruefe_antwort(kategorie, antwort, buchstabe):
        antwort = antwort.strip().capitalize()
        if not antwort.startswith(buchstabe):
            return False
        if kategorie == "Stadt":
            return antwort in staedte
        elif kategorie == "Land":
            return antwort in laender
        return False

def spielrunde():
        buchstabe = zufallsbuchstabe()
        print(f"Der Buchstabe ist: {buchstabe}")
        for kategorie in kategorien:
            antwort = input(f"{kategorie} mit {buchstabe}: ")
            if pruefe_antwort(kategorie, antwort, buchstabe):
                print("Richtig!")
            else:
                print("Leider falsch oder nicht in der Datenbank.")


if __name__ == "__main__":
    print("Willkommen zu Stadt, Land, Fluss!")
    print("---------------------------------")
    # Datenbanken für Städte und Länder laden 
    couCitArray = load_database()
    names, all_cities = sort_database(couCitArray)
    print(names)
    print(all_cities)


    spielrunde()
