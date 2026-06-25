import math
import time


def odleglosc(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def koszt_trojkata(punkty, i, k, j):
    return odleglosc(punkty[i], punkty[k]) + odleglosc(punkty[k], punkty[j]) + odleglosc(punkty[j], punkty[i])


def triangulacja_rekurencyjna(punkty, i, j):
    if j < i + 2:
        return 0.0
    najlepszy = float("inf")
    for k in range(i + 1, j):
        koszt = triangulacja_rekurencyjna(punkty, i, k) + triangulacja_rekurencyjna(punkty, k, j) + koszt_trojkata(punkty, i, k, j)
        if koszt < najlepszy:
            najlepszy = koszt
    return najlepszy


def triangulacja_iteracyjna(punkty):
    n = len(punkty)
    if n < 3:
        return 0.0
    dp = [[0.0 for _ in range(n)] for _ in range(n)]
    for dlugosc in range(2, n):
        for i in range(0, n - dlugosc):
            j = i + dlugosc
            najlepszy = float("inf")
            for k in range(i + 1, j):
                koszt = dp[i][k] + dp[k][j] + koszt_trojkata(punkty, i, k, j)
                if koszt < najlepszy:
                    najlepszy = koszt
            if najlepszy != float("inf"):
                dp[i][j] = najlepszy
    return dp[0][n - 1]


def policz_i_wypisz(punkty, numer):
    t1 = time.perf_counter()
    koszt_rek = triangulacja_rekurencyjna(punkty, 0, len(punkty) - 1)
    t2 = time.perf_counter()
    koszt_it = triangulacja_iteracyjna(punkty)
    t3 = time.perf_counter()
    print(f"Zbior {numer}:")
    print(f"Rekurencyjnie: koszt = {koszt_rek:.4f}, czas = {t2 - t1:.6f} s")
    print(f"Iteracyjnie DP: koszt = {koszt_it:.4f}, czas = {t3 - t2:.6f} s")
    print()


if __name__ == "__main__":
    punkty1 = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]
    punkty2 = [[0, 0], [4, 0], [5, 4], [4, 5], [2, 5], [1, 4], [0, 3], [0, 2]]
    policz_i_wypisz(punkty1, 1)
    policz_i_wypisz(punkty2, 2)
