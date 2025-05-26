from models.belfoldi_jarat import BelfoldiJarat
from models.nemzetkozi_jarat import NemzetkoziJarat
from models.legitarsasag import LegiTarsasag
import datetime

class UserInterface:
    def __init__(self):
        self.legitarsasag = LegiTarsasag("PéldaLégitársaság")
        self._elore_feltoltott_adatok()

    def _elore_feltoltott_adatok(self):
        self.legitarsasag.jarat_hozzaadas(BelfoldiJarat("B001", "Budapest"))
        self.legitarsasag.jarat_hozzaadas(BelfoldiJarat("B002", "Debrecen"))
        self.legitarsasag.jarat_hozzaadas(NemzetkoziJarat("N001", "London"))

        foglalasok = [
            ("Kovács Anna", "B001", 5),
            ("Szabó Béla", "B002", 3),
            ("Nagy István", "N001", 10),
            ("Tóth Mária", "B001", 7),
            ("Farkas Ádám", "N001", 15),
            ("Kiss Júlia", "B002", 8)
        ]

        for nev, jarat, napok in foglalasok:
            datum = datetime.date.today() + datetime.timedelta(days=napok)
            self.legitarsasag.foglalas_hozzaadas(nev, jarat, datum)

    def futtat(self):
        while True:
            print("\n--- Repülőjegy Foglalási Rendszer ---")
            print("1. Jegy foglalása")
            print("2. Foglalás lemondása")
            print("3. Foglalások listázása")
            print("4. Kilépés")

            valasztas = input("Válassz egy opciót: ")

            if valasztas == "1":
                self._jegy_foglalas()
            elif valasztas == "2":
                self._lemondas()
            elif valasztas == "3":
                self.legitarsasag.foglalasok_listazasa()
            elif valasztas == "4":
                print("Kilépés...")
                break
            else:
                print("Érvénytelen opció.")

    def _jegy_foglalas(self):
        nev = input("Utas neve: ")
        jaratszam = input("Járatszám: ")
        datum_str = input("Dátum (ÉÉÉÉ-HH-NN): ")
        try:
            datum = datetime.datetime.strptime(datum_str, "%Y-%m-%d").date()
            eredmeny = self.legitarsasag.foglalas_hozzaadas(nev, jaratszam, datum)
            print(eredmeny)
        except ValueError:
            print("Hibás dátumformátum.")

    def _lemondas(self):
        nev = input("Utas neve: ")
        jaratszam = input("Járatszám: ")
        print(self.legitarsasag.foglalas_lemondas(nev, jaratszam))
