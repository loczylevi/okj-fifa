class Fifa:
    def __init__(self,sor):
        csapat,helyezes,valtozas,pontszam = sor.strip().split(";")
        self.csapat = csapat
        self.helyezes = int(helyezes)
        self.valtozas = int(valtozas)
        self.pontszam = int(pontszam)
        
with open("fifa.txt","r",encoding="latin2") as f:
    fejlec = f.readline()
    lista = [Fifa(sor) for sor in f]
    
print(f"3.feladat: A világranglistán {len(lista)} csapat szerepel")

pontok = sum([sor.pontszam for sor in lista])

print(f"4.feladat: A csapatok átlagos pontszáma {str(pontok / len(lista)).replace('.',',')} pont")


valtozasok = [(sor.valtozas,sor.csapat,sor.helyezes,sor.pontszam) for sor in lista]

valtozas,csapat,helyezes,pontszam = max(valtozasok)

print(f"""5.feladat: A legtöbbet javító csapat:
       Helyezés: {helyezes}
       Csapat: {csapat}
       Pontszám: {pontszam}""")

van_e_magyaroroszag = [sor for sor in lista if sor.csapat == "Magyarország"]

if van_e_magyaroroszag:
    print("6.feladat: A csapatok között van Magyarország")
else:
    print("6.feladat: A csapatok között nincs Magyarország")
    
stat = dict()
for sor in lista:
    stat[sor.valtozas] = stat.get(sor.valtozas, 0) + 1

print("7.feladat:")

statisztika = [print(f"       {valtozas} helyett változott: {db} csapat") for valtozas,db in stat.items() if db > 1]