# pvl-algot2021
Repo päivölän algotunnin esimerkeille ja tehtäville.

## Tarpeet

1. Asenna git (Evolla jo asennettuna)
2. Asenna python3 (Evolla jo asennettuna)
3. `git clone https://github.com/haihala/pvl-algot2021.git`
4. `cd pvl-algot2021`
5. Asenna python kirjastot `python3 -m pip install -r requirements.txt`

## src/exercises

Tehtäviä algotunnille. Kaikkiin tehtäviin on kirjoitettu testi että ratkaisu toimii.

Testit voi ajaa komennolla: `python3 -m pytest <tiedosto>` tai `python3 <tiedosto>`, ensimmäinen antaa lisäinfoa.

Jos se passaa testit, ratkaisu toimii.

### find_max.py

Löydä suurin numero listasta. Lista **ei** ole järjestyksessä.


### prime_factors.py

Löydä annetun numeron alkulukutekijät.

### list_index_sum_to_total.py

Löydä annetusta järjestyksessä olevasta listasta indeksit kahdelle alkiolle joiden arvo summaa annettuun numeroon. Ratkaisu on aina olemassa.

Testin lukeminen on omasta mielestäni selkeämpi kun edellinen selitys.

## src/example_solutions

Muutamia malliratkaisuja edellisiin tehtäviin.

## src/searching

Testaa ja penkittää hakualgoja.

Käytö: `python3 searching [test] [bench]` jos olet `src` kansiossa

Jos annat `test`, ajaa testit. Jos annat `bench` ajaa benchmarkit. Voi tehdä molemmat kerralla.s

Algoritmit:

- Linear search (sorted and unsorted)
- Binary search
  - Suomeksi puolitushaku
- Python 'index' (sorted and unsorted)

## src/sorting

Testaa ja penkittää sorttausalgoja, toimii samalla tavalla kun `src/searching`

Algoritmit:

- Bogo sort
- Stalin sort
- Bubble sort
- Insertion sort
- Quick sort
- Python 'sorted'

## Other

Ne jotka ei mennyt mihinkään muualle.

### onotation.py

Muutamia funktioita joilla voi kysellä O-notaatiosta

### playground.py

Irtonaisia python temppuja. Tämä on olemassa niin ettei tarvitse livekoodaa jos tulee vastaan jotain hämmentävää.

### fast_inverse_square_root.c

Praise lord Carmack

## Muuta materiaalia

Diat: https://docs.google.com/presentation/d/10M7v8ff80dIeOi_iMS23VvtQp1P9WtYEQdKQs8HzaaY/edit?usp=sharing

Datatähti: https://datatahti.fi/

Project Euler: https://projecteuler.net/archives

O-notaatio cheat sheet: https://www.bigocheatsheet.com/

