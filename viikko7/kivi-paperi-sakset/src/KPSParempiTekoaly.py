from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from KiviPaperiSakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)
        self.tuomari = Tuomari()

    def _ensimmaisen_siirto(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        self.tekoaly.aseta_siirto(ekan_siirto)
        return ekan_siirto

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print("Toisen pelaajan siirto: " + tokan_siirto)
        return tokan_siirto
