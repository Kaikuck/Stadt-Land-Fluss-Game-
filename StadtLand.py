#stadt land fluss game
import random

kategorien = ["Stadt", "Land", "Fluss"]
buchstaben = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def zufallsbuchstabe():
    return random.choice(buchstaben)

def spielrunde():
    buchstabe = zufallsbuchstabe()
    print(f"Der Buchstabe ist: {buchstabe}")
    for kategorie in kategorien:
        antwort = input(f"{kategorie} mit {buchstabe}: ")
        # Hier könnte man die Antworten speichern oder auswerten

if __name__ == "__main__":
    print("Willkommen zu Stadt, Land, Fluss!")
    print("---------------------------------")
    # Datenbanken für Städte, Länder und Flüsse (vereinfachte Beispiele)
    staedte = {
    "Aachen",
    "Aarhus",
    "Alicante",
    "Ankara",
    "Antwerpen",
    "Barcelona",
    "Berlin",
    "Brüssel",
    "Bukarest",
    "Dublin",
    "Düsseldorf",
    "Edinburgh",
    "Frankfurt",
    "Glasgow",
    "Hamburg",
    "Helsinki",
    "Istanbul",
    "Kopenhagen",
    "Köln",
    "Krakau",
    "Lissabon",
    "London",
    "Lyon",
    "Madrid",
    "Mailand",
    "München",
    "Neapel",
    "Oslo",
    "Osnabrück",
    "Paris",
    "Prag",
    "Rom",
    "Rotterdam",
    "Sofia",
    "Stockholm",
    "Stuttgart",
    "Tallinn",
    "Turin",
    "Ufa",
    "Valencia",
    "Vilnius",
    "Warschau",
    "Wien",
    "Zagreb",
    "Zürich"}
    laender = {"Albanien",
    "Andorra",
    "Armenien",
    "Aserbaidschan",
    "Belgien",
    "Bosnien und Herzegowina",
    "Bulgarien",
    "Chile",
    "Dänemark",
    "Deutschland",
    "Estland",
    "Finnland",
    "Frankreich",
    "Georgien",
    "Griechenland",
    "Irland",
    "Island",
    "Italien",
    "Kasachstan",
    "Kosovo",
    "Kroatien",
    "Lettland",
    "Liechtenstein",
    "Litauen",
    "Luxemburg",
    "Malta",
    "Moldau",
    "Monaco",
    "Montenegro",
    "Niederlande",
    "Nordmazedonien",
    "Norwegen",
    "Österreich",
    "Oman",
    "Polen",
    "Portugal",
    "Rumänien",
    "Russland",
    "San Marino",
    "Schweden",
    "Schweiz",
    "Serbien",
    "Slowakei",
    "Slowenien",
    "Spanien",
    "Tschechien",
    "Türkei",
    "Ukraine",
    "Ungarn",
    "Vatikanstadt",
    "Vereinigtes Königreich",
    "Weißrussland"}
    fluesse = {"Alster",
    "Amper",
    "Dnepr",
    "Don",
    "Donau",
    "Drau",
    "Elbe",
    "Ems",
    "Enns",
    "Erft",
    "Glomma",
    "Inn",
    "Isar",
    "Isonzo",
    "Lahn",
    "Lech",
    "Lippe",
    "Loire",
    "Main",
    "Marne",
    "Memel",
    "Mosel",
    "Mulde",
    "Mur",
    "Neckar",
    "Newa",
    "Oder",
    "Po",
    "Pruth",
    "Rhein",
    "Rhône",
    "Saale",
    "Sava",
    "Schelde",
    "Seine",
    "Sieg",
    "Spree",
    "Tajo",
    "Temse",
    "Themse",
    "Tiber",
    "Tisza",
    "Ural",
    "Vistula",
    "Waag",
    "Weichsel",
    "Weser"}

    def pruefe_antwort(kategorie, antwort, buchstabe):
        antwort = antwort.strip().capitalize()
        if not antwort.startswith(buchstabe):
            return False
        if kategorie == "Stadt":
            return antwort in staedte
        elif kategorie == "Land":
            return antwort in laender
        elif kategorie == "Fluss":
            return antwort in fluesse
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

    spielrunde()
