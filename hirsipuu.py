import random

def valitse_sana(sanat):
    return random.choice(sanat)

def näytä_sana(sana, arvattuja_kirjaimia):
    näytetty_sana = ""
    for kirjain in sana:
        if kirjain in arvattuja_kirjaimia:
            näytetty_sana += kirjain
        else:
            näytetty_sana += "_"
    return näytetty_sana

def play_hangman():
    sanat = ['lehmä', 'porsas', 'kana', 'lammas', 'ankka']
    max_yritykset = 3  # Maksimi sallitut väärät arvaukset
    arvattuja_kirjaimia = []  # Lista tallentamaan arvatut kirjaimet
    sana = valitse_sana(sanat)  # Valitaan sana satunnaisesti
    yritykset = 0  # Laskuri väärille arvauksille

    print("Tervetuloa Hangman-peliin!")
    print("Arvaa sana. Sinulla on", max_yritykset, "yritystä.")

    while True:
        print("\nNykyinen sana:", näytä_sana(sana, arvattuja_kirjaimia))  # Näytä nykyinen tila sanasta
        arvaa = input("Syötä kirjain: ").lower()  # Pyydä pelaajaa syöttämään kirjain ja muuttaa se pienaakkoseksi

        if arvaa in arvattuja_kirjaimia:  # Tarkistaa, onko kirjain jo arvattu
            print("Olet jo arvannut tuon kirjaimen. Yritä uudelleen.")
            continue

        arvattuja_kirjaimia.append(arvaa)  # Lisää arvattu kirjain listaan arvatuista kirjaimista

        if arvaa not in sana:  # Tarkistaa, ettei arvattu kirjain ole sanassa
            yritykset += 1  # Kasvattaa väärin arvattujen lukumäärää
            print("Väärä arvaus! Sinulla on", max_yritykset - yritykset, "yritystä jäljellä.")
            if yritykset == max_yritykset:  # Tarkistaa, onko väärin arvattujen enimmäismäärä saavutettu
                print("\nValitettavasti hävisit! Sana oli:", sana)
                break
        else:
            if "_" not in näytä_sana(sana, arvattuja_kirjaimia):  # Tarkistaa, onko kaikki kirjaimet arvattu
                print("\nOnnittelut! Voitit! Sana oli:", sana)
                break

play_hangman()
