# Kolejka Priorytetowa na Kopcu Binarnym (Heap-based Priority Queue)

## O projekcie
Projekt zawiera autorską implementację kolejki priorytetowej typu **Max-Heap** (kopiec maksimum) w języku Python. Struktura ta pozwala na efektywne zarządzanie elementami o różnych priorytetach, gwarantując, że element o najwyższej randze jest zawsze dostępny w korzeniu drzewa.

Głównym celem projektu było zaimplementowanie mechanizmów kopca bez użycia biblioteki `heapq`, co pozwoliło na pełną kontrolę nad procesami restrukturyzacji drzewa (*up-heap* i *down-heap*).

## Architektura i Efektywność
Kolejka została zaimplementowana przy użyciu dynamicznie rozszerzanej tablicy (listy), co pozwala na zachowanie spójności danych przy minimalnym narzucie pamięciowym.

* **Mapowanie Drzewa na Tablicę:** Wykorzystano matematyczne zależności indeksowania węzłów:
  - Lewy syn: $2 \cdot i + 1$
  - Prawy syn: $2 \cdot i + 2$
  - Rodzic: $(i - 1) // 2$
* **Złożoność Obliczeniowa:**
  - Wstawianie (`enqueue`): $O(\log n)$
  - Pobieranie najwyższego priorytetu (`dequeue`): $O(\log n)$
  - Odczyt szczytu (`peek`): $O(1)$

## Implementacja Logiki Porównań
Klasa `Element` wykorzystuje techniki hermetyzacji (atrybuty prywatne) oraz przeciążanie operatorów porównania (`__lt__`, `__gt__`). Dzięki temu struktura `HeapQueue` jest generyczna – może przechowywać dowolne obiekty, o ile definiują one swój priorytet, a logika kopca pozostaje odseparowana od typu przechowywanych danych.

## Kluczowe Funkcjonalności
* **`enqueue(elem)`** – Dodaje element na koniec tablicy i wykonuje operację `_switch` (naprawa kopca w górę), aby przywrócić własność kopca.
* **`dequeue()`** – Wyciąga element z korzenia, przenosi ostatni liść na szczyt i wykonuje `_dequeue` (naprawa kopca w dół), zapewniając optymalny czas reorganizacji struktury.
* **`print_tree()`** – Rekurencyjna metoda wizualizacji struktury hierarch