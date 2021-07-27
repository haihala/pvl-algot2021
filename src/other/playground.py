# Tyyppiannotaatiot
def funktio(x: int) -> int:
    return 2*x


# Testit ja assert
def test_funktio():
    assert funktio(2) == 4


# +=, -=, /=, *=, jne
muuttuja = 1
muuttuja = muuttuja + 1
# Tekee tismalleen saman kuin
muuttuja += 1
# Sama juttu muilla operaattoreilla

# Unpacking
a, b = [1, 2]
# on sama kuin
a = 1
b = 2

# Range
for i in range(5):
    print(i)
# Tulostaa:
# 0
# 1
# 2
# 3
# 4

lista = ['porkkana', 'omena', 'päärynä']
for i in lista:
    print(i)
# Tulostaa:
# porkkana
# omena
# päärynä

for i in range(len(lista)):
    print(i)
# Tulostaa:
# 0
# 1
# 2

for i in enumerate(lista):
    print(i)
# Tulostaa:
# (0, 'porkkana')
# (1, 'omena')
# (2, 'päärynä')

# Voi myös tehdä
for indeksi, rehu in enumerate(lista):
    ...
# Tällöin indeksi muuttujaan menee indeksi, kuten range(len(lista)) versiossa
# ja rehu muuttujaan menee merkkijono

# List comprehension
# Listoja ei voi muokata kun niitä iteroi (syytä vaikka pythonin sisäisiä optimointeja)
uusi_lista = []
for rehu in lista:
    uusi_lista.append(rehu)
# On sama kuin
uusi_lista = [
    rehu
    for rehu in lista
]
# On sama kuin
uusi_lista = [rehu for rehu in lista]

# Tämä on hyödyllistä, koska se mahdollistaa helppoja pikkumuokkauksia
parillinen_range = [i*2 for i in range(5)]
# [0, 2, 4, 6, 8]
# myös:
parillinen_range = [funktio(i) for i in range(5)]

# Noihin voi sisällyttää ehtoja joilla on helppo vaikka suodattaa
parillinen_range2 = [
    i
    for i in range(5)
    if i % 2 == 0
]
# [0, 2, 4]
# Edellinen on yleinen rivitystyyli josta itse pidän

# Yhden rivin if
juttu = 'eka on porkkana' if lista[0] == 'porkkana' else 'ei oo porkkanaa ekana'
# Rakenne on kutakuinkin: <jos ehto pätee> if <ehto> else <jos ehto ei päde>

# Näitä voi yhdistää
parillinen_range3 = [
    i if i % 2 == 0 else i+1
    for i in range(5)
]
# [0, 2, 2, 4, 4]

# List comprehensioneitä voi kans laittaa sisäkkäin
range_range = [
    i
    # Kannattaa aloittaa lukeminen ensin vastaan tulevasta for rivistä
    for r in range(5)
    for i in range(r)
]
# [0, 0, 1, 0, 1, 2, 0, 1, 2, 3]
# Sitä voi miettiä näin eroteltuna:
# [(0), (0, 1), (0, 1, 2), (0, 1, 2, 3)]
# Edellinen tekee saman kuin:
range_range_collector = []
for r in range(5):
    for i in range(r):
        range_range_collector.append(i)


# Mursu (tää on aika uus juttu ja kaikki ei tykkää)
if norppa := lista:
    print(norppa)
# On sama kuin
norppa = lista
if norppa:
    print(norppa)
