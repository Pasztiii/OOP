from .jarat import Jarat

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, 50000)

    def jarat_tipus(self):
        return "Nemzetközi"
