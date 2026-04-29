# Optymalizacja i Analiza Algorytmów Sortowania: HeapSort (In-Situ) oraz Selection Sort

## O projekcie
Projekt przedstawia niskopoziomową implementację i analizę porównawczą dwóch klasycznych algorytmów sortowania: **HeapSort (sortowanie przez kopcowanie)** oraz **Selection Sort (sortowanie przez wybieranie)**. 

Głównym wyzwaniem inżynierskim w tym projekcie była optymalizacja pamięciowa. Algorytm HeapSort został zrealizowany wariancie **in-situ** (w miejscu), co oznacza, że sortowanie odbywa się bez alokacji dodatkowej pamięci na nową tablicę – złożoność pamięciowa wynosi $O(1)$.

## Zaimplementowane Algorytmy

### 1. HeapSort (In-Situ)
Algorytm oparty na strukturze kopca typu Max-Heap (kopiec maksymalny), zoptymalizowany pod kątem działania na tablicy jednowymiarowej.
* **Inicjalizacja $O(N)$:** Tablica wejściowa jest transformowana w kopiec algorytmem *Bottom-Up*, wywołującym procedurę naprawczą (`_dequeue`) od ostatniego rodzica w dół aż do korzenia.
* **Sortowanie $O(N \log N)$:** Korzeń kopca (wartość maksymalna) jest zamieniany z ostatnim elementem tablicy. Następnie logiczny rozmiar kopca (`self.size`) jest dekrementowany, a nowy korzeń jest przesuwany w dół drzewa w celu przywrócenia własności Max-Heap. Proces ten pozostawia na końcu tablicy posortowany rosnąco ciąg danych.
* **Stabilność:** Z uwagi na przeskoki elementów w strukturze drzewa, algorytm ten jest **niestabilny**.

### 2. Selection Sort
Zaimplementowano dwa warianty algorytmu w celu zbadania wpływu manipulacji danymi na stabilność sortowania:
* **Wariant SWAP (`sort_swap`):** Wykorzystuje klasyczną, szybką zamianę indeksów. Jest to metoda **niestabilna**, ponieważ dalekosiężny swap może zaburzyć relatywną kolejność elementów o tym samym kluczu.
* **Wariant SHIFT (`sort_shift`):** Wykorzystuje operacje wyjęcia (`pop`) i wstawienia (`insert`), przesuwając fragment tablicy. Choć generuje to większy narzut obliczeniowy, gwarantuje, że algorytm staje się **stabilny**.

## Tryby Diagnostyczne (Moduł Testowy)
Aplikacja zawiera interaktywny interfejs konsolowy (wybór trybu 1 lub 2), realizujący dwa kompleksowe scenariusze testowe:

### Test 1: Weryfikacja Stabilności (Krotki)
Analiza zachowania algorytmów przy sortowaniu niestandardowych obiektów klasy `Element`, zawierających zduplikowane priorytety (klucze) oraz przypisane do nich unikalne dane znakowe (np. `(5, 'A')`, `(5, 'B')`). Test udowadnia analitycznie i wizualnie różnice w zachowaniu stabilności badanych funkcji.

### Test 2: Benchmark Wydajnościowy (Złożoność Czasowa)
Ewaluacja wydajności algorytmów na silnie obciążonym zestawie danych (10 000 losowych liczb całkowitych z przedziału 0-99). Moduł korzysta z precyzyjnego licznika `time.perf_counter()` do zmierzenia i porównania narzutu czasowego narzucanego przez każdą z metod, operując na niezależnych kopiach tablicy w celu zachowania rzetelności pomiarów.