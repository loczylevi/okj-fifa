#Csapat;    Helyezes;    Valtozas;     Pontszam

#   0           1            2            3

with open("fifa.txt","r",encoding="latin2") as f:
    fejlec = f.readline()
    lista = [sor.strip().split(";") for sor in f]
    
print(f"3.feladat: A világranglistán {len(lista)} csapat szerepel")

pontok = sum([int(sor[3]) for sor in lista])

print(f"4.feladat: A csapatok átlagos pontszáma {str(pontok / len(lista)).replace('.',',')} pont")


valtozasok = [(sor[2],sor[0],sor[1],sor[3]) for sor in lista]

valtozas,csapat,helyezes,pontszam = max(valtozasok)

print(f"""5.feladat: A legtöbbet javító csapat:
       Helyezés: {helyezes}
       Csapat: {csapat}
       Pontszám: {pontszam}""")

van_e_magyaroroszag = [sor for sor in lista if sor[0] == "Magyarország"]

if van_e_magyaroroszag:
    print("6.feladat: A csapatok között van Magyarország")
else:
    print("6.feladat: A csapatok között nincs Magyarország")
    
stat = dict()
for sor in lista:
    stat[sor[2]] = stat.get(sor[2], 0) + 1

print("7.feladat:")

statisztika = [print(f"       {valtozas} helyett változott: {db} csapat") for valtozas,db in stat.items() if db > 1]
