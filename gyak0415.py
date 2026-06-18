import os


class Diak:
    def __init__(self, nev: str, osztaly: str, atlag: float):
        self.nev = nev
        self.osztaly = osztaly
        self.atlag = atlag

    def __repr__(self):
        return f"Diak(nev={self.nev!r}, osztaly={self.osztaly!r}, atlag={self.atlag})"


def beolvasas(fajlnev: str):
    diakok = []
    with open(fajlnev, encoding="utf-8") as fajl:
        for sor in fajl:
            sor = sor.strip()
            if not sor:
                continue
            reszek = sor.split(";")
            if len(reszek) != 3:
                continue
            nev, osztaly, atlag_str = [r.strip() for r in reszek]
            try:
                atlag = float(atlag_str.replace(",", "."))
            except ValueError:
                continue
            diakok.append(Diak(nev, osztaly, atlag))
    return diakok


def csoport_atlag(diakok):
    if not diakok:
        return 0.0
    return sum(d.atlag for d in diakok) / len(diakok)


def legjobb_tanulo(diakok):
    if not diakok:
        return None
    return max(diakok, key=lambda d: d.atlag)


def evfolyamok(diakok):
    eredmeny = set()
    for d in diakok:
        if d.osztaly and d.osztaly[0].isdigit():
            eredmeny.add(int(d.osztaly[0]))
    return eredmeny


def main():
    munkakonyvtar = os.path.dirname(__file__)
    fajlnev = os.path.join(munkakonyvtar, "diak.txt")

    diakok = beolvasas(fajlnev)

    print(f"Csoportlétszám: {len(diakok)} fő")
    print(f"Csoportátlag: {csoport_atlag(diakok):.2f}")

    legjobb = legjobb_tanulo(diakok)
    if legjobb:
        print(f"Legjobb tanuló: {legjobb.nev}, átlaga: {legjobb.atlag:.2f}")
    else:
        print("Nincs tanuló a fájlban.")

    megtalalt_evfolyamok = evfolyamok(diakok)
    kovetelt_evfolyamok = set(range(9, 13))
    hiányzik = sorted(kovetelt_evfolyamok - megtalalt_evfolyamok)

    if not hiányzik:
        print("A 9-12. évfolyamok mindegyike megtalálható a csoportban.")
    else:
        hiányzo_szoveg = ", ".join(str(ev) for ev in hiányzik)
        print(f"Hiányzó évfolyam(ok): {hiányzo_szoveg}")


if __name__ == "__main__":
    main()
