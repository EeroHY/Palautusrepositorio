from tuomari import Tuomari
from tekoaly import Tekoaly
from KiviPaperiSakset import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = Tekoaly()
        self.tuomari = Tuomari()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print("Toisen pelaajan siirto: " + tokan_siirto)
        return tokan_siirto
