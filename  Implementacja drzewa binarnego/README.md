# Drzewo Poszukiwań Binarnych (Binary Search Tree - BST)

## O projekcie
Repozytorium zawiera obiektową implementację drzewa binarnych poszukiwań (BST) w języku Python. Projekt demonstruje wykorzystanie hierarchicznych struktur danych do optymalizacji procesów wyszukiwania, wstawiania oraz usuwania elementów o złożoności średniej $O(\log n)$.

Implementacja kładzie nacisk na poprawne zarządzanie referencjami węzłów podczas operacji niszczących (usuwanie) oraz wykorzystanie rekurencji do nawigacji po strukturze drzewa.

## Architektura i Główne Mechanizmy

### 1. Zarządzanie Węzłami (Node Logic)
Każdy element drzewa jest instancją klasy `Node`, przechowującą parę `klucz:wartość` oraz wskaźniki na lewe i prawe poddrzewo. Zastosowanie generycznych kluczy pozwala na przechowywanie dowolnych danych podlegających relacji porządku.

### 2. Algorytmy i Operacje
* **Wstawianie (Insertion):** Realizowane rekurencyjnie. Algorytm automatycznie obsługuje aktualizację wartości w przypadku napotkania istniejącego już klucza, zapobiegając duplikacji danych.
* **Wyszukiwanie (Search):** Zaimplementowane wariancie iteracyjnym, co pozwala na oszczędność stosu wywołań przy głębokich strukturach.
* **Usuwanie (Deletion):** Najbardziej złożony element implementacji, obsługujący trzy scenariusze:
    - Usunięcie liścia (węzeł bez dzieci).
    - Usunięcie węzła z jednym dzieckiem (przepięcie referencji).
    - Usunięcie węzła z dwoma dziećmi – algorytm odnajduje **następcę in-order** (najmniejszy element w prawym poddrzewie), dokonuje zamiany wartości i rekurencyjnie usuwa zbędny węzeł.
* **Analiza Wysokości:** Metoda `height()` wyznacza maksymalną ścieżkę od korzenia do liścia, co jest kluczowe dla monitorowania stopnia degradacji (zbalansowania) drzewa.

## Wizualizacja i Diagnostyka
Struktura udostępnia dwa tryby prezentacji danych:
- **In-order Traversal:** Wypisanie elementów w kolejności rosnącej kluczy, potwierdzające poprawność struktury BST.
- **Top-down Visualization:** Graficzna reprezentacja drzewa obrócona o 90 stopni, pozwalająca na szybką ocenę wizualną relacji rodzic-dziecko oraz poziomu zbalansowania gałęzi.

## Scenariusz Testowy (Stress Test)
Dołączony moduł uruchomieniowy weryfikuje odporność drzewa na dynamiczne zmiany:
1. Budowa drzewa z nieuporządkowanego zestawu danych wejściowych.
2. Aktualizacja istniejących rekordów.
3. Seria usunięć kluczy o różnym stopniu skomplikowania (usuwanie liści, węzłów pośrednich oraz korzenia).
4. Walidacja wysokości drzewa po restrukturyzacji.