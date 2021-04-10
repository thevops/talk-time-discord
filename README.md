> English version [here](README.en.md)

# Talk Time - bot dla Discord

Integruj ludzi tworząc dwuosobowe czaty głosowe.


## Najlepsze dla

- integracje zespołowe/grupowe
- speed dating
- spotkania dyskusyjne

## Jak używać bota?

1. Dodaj bota do swojego serwera
2. Zbierz ludzi na jakimś (tym samym) kanale **głosowym** (minimum 4 osoby)

   `Każda z osób musi być wewnątrz jakiegoś kanału głosowego`
3. Wydaj polecenie:
   ```
    #talk-time-start @osoba1 @osoba2 @osoba3 @osoba4 .....
   ```
   Wspomnij każdą osobę, która bierze udział.

Bot stworzy potrzebne kanały głosowe, podzieli ludzi na 2 osobowe grupy i przeniesie ich do odpowiednich kanałów.

W przypadku nieparzystej liczby uczestników, ostatnia grupa będzie liczyła 3 osoby.

## Jak uruchomić aplikacja z użyciem Dockera?

1. Uzupełnij wartość DISCORD_TOKEN w pliku  `.env` na podstawie szablonu `.env.example`
2. Wykonaj: `make build`
3. Wykonaj: `make run`
