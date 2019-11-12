Mnożenie macieży NxN gdzie N=2^n. Algorytm Strassena versus mnożenie z
definicji. Dla jakich N algorytm Strassena zaczyna się opłacać?

- mnozenie_defi.py - metoda do obliczania mnożenia macierzy z definicji
- strassen.py - zawiera metodę strassen do obliczania mnożenia macierzy z
algorytmu Strassena oraz metody dodawanie i odejmowanie macierzy
- projekt_run.py - zawiera test pokazujący wartości liczbowe uzyskanych
średnich czasów egzekucji dla danej metody w danej liczbie prób i przy
określonych macierzach NxN
(wymagane pakiety matplotlib.pyplot oraz numpy)
- info.txt - informacje odnośnie zaimplementowanego algorytmu Strassena
oraz wniosek

Aby uzyskać wyniki wystarczy w terminalu wprowadzić komendę:
python3 projekt_run.py

i odczekać chwilę czasu, aż wygeneruje się wykres, zaś w terminalu ukażą
się średnie czasy egzekucji dla poszczególnych macierzy.

Autor: Andżelika Picheta