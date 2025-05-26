from .jegy_foglalas import JegyFoglalas
import datetime

class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def jarat_hozzaadas(self, jarat):
        self.jaratok.append(jarat)

    def foglalas_hozzaadas(self, utas_nev, jaratszam, datum):
        jarat = next((j for j in self.jaratok if j.jaratszam == jaratszam), None)
        if not jarat:
            return "Hibás járatszám."
        if datum < datetime.date.today():
            return "A dátum nem lehet múltbeli."
        foglalas = JegyFoglalas(jarat, utas_nev, datum)
        self.foglalasok.append(foglalas)
        return f"Foglalás sikeres. Ár: {jarat.jegyar} Ft"

    def foglalas_lemondas(self, utas_nev, jaratszam):
        for f in self.foglalasok:
            if f.utas_nev == utas_nev and f.jarat.jaratszam == jaratszam:
                self.foglalasok.remove(f)
                return "Foglalás lemondva."
        return "A foglalás nem található."

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincs aktív foglalás.")
        for f in self.foglalasok:
            print(f"{f.utas_nev} - {f.jarat.jaratszam} ({f.jarat.celallomas}) - {f.datum} - {f.jarat.jarat_tipus()} - {f.jarat.jegyar} Ft")
