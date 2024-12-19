from KPSPelaajaVsPelaaja import KPSPelaajaVsPelaaja
from KPSParempiTekoaly import KPSParempiTekoaly
from KPSTekoaly import KPSTekoaly


def luo_peli(tyyppi):
    if tyyppi == 'a':
        return KPSPelaajaVsPelaaja()
    if tyyppi == 'b':
        return KPSTekoaly()
    if tyyppi == 'c':
        return KPSParempiTekoaly()

    return None
