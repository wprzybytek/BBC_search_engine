# Wyszukiwarka artykułów BBC News
## Autor
Wojciech Przybytek
## Opis
Jako bazę dokumentów przygotowano zbiór artykułów z portalu BBC News w latach 2003/2004. Baza zawiera ponad 2000 artykułów.  
Bazę zaimportowano do programu jako dataframe dzięki bibliotece pandas. Następnie każdy artykuł przetworzono i rozbito na listę występujących słów. W celu przetworzenia:
- zmieniono wszystkie litery na małe
- usunięto wszystkie znaki interpunkcyjne, specjalne itp
- usunięto wszystkie cyfry
- usunięto 'stop words'
- zamieniono słowa na ich rdzenie za pomocą algorytmu Porter Stemmer
 
Dla tak przetworzonych artykułów utworzono zbiór wszystkich słów jako unię słów w artykułach. Następnie dla każdego artykułu utworzono wektor cech aby otrzymać macierz rzadką, którą następnie przemonożono przez inverse document frequency.  
W programie zaimplementowano usuwanie szumu stosując low rank approximation, jednak wyniki dla małej liczby iteracji były subiektkywnie gorsze niż bez usuwania szumu. Lepsze wyniki pojawiały się dla dużej liczby iteracji, dlatego ze względów wydajnościowych algorytm nie jest wykorzystywany.
## Uruchomienie
### Serwer
Przed uruchomieniem serwera należy pobrać odpowiednie biblioteki w katalogu server komendą:
 - pip install -r requirements.txt

a sam serwer uruchomić:
 - python3 backend.py
### Aplikacja
Przed uruchomieniem aplikacji należy pobrać odpowiednie biblioteki w katalogu application komendą:
 - npm i package.json

a samą aplikację uruchomić:
 - npm start
## Uwagi
Ponieważ baza dokumentów dotyczy artykułów BBC z lat 2003/2004 to pisząc zapytanie należy mieć na uwadzę jakie artykuły mogły się pojawić w tym czasie. Przykładowe tematy to np. piłka nożna lub motoryzacja.
