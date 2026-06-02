import math
import time

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def triangle_cost(points, i, k, j):
    return distance(points[i], points[j]) + distance(points[j], points[k]) + distance(points[k], points[i])

def rec(points, i, j):
    if j < i + 2:
        return 0
        
    min_cost = float('inf')
    for k in range(i + 1, j):
        cost = triangle_cost(points, i, k, j ) + rec(points, i, k) + rec(points, k, j)
        if cost < min_cost:
            min_cost = cost
            
    return min_cost

def it(points):
    n = len(points)
    D = []

    for r in range(n):
        row = []
        for c in range(n):
            row.append(0.0)
        D.append(row)
        
    for x in range(2, n):
        for i in range(n - x):
            j = i + x
            min_cost = float('inf')
            for k in range(i + 1, j):
                cost = triangle_cost(points, i, k, j ) + D[i][k] + D[k][j]
                if cost < min_cost:
                    min_cost = cost
            D[i][j] = min_cost

    return D[0][n-1]

if __name__ == '__main__':
    points1 = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]
    points2 = [[0, 0], [4, 0], [5, 4], [4, 5], [2, 5], [1, 4], [0, 3], [0, 2]]
    
    start = time.time()
    res1_rec = rec(points1, 0, len(points1) - 1)
    time1_rec = time.time() - start
    
    start = time.time()
    res1_it = it(points1)
    time1_it = time.time() - start
    
    start = time.time()
    res2_rec = rec(points2, 0, len(points2) - 1)
    time2_rec = time.time() - start
    
    start = time.time()
    res2_it = it(points2)
    time2_it = time.time() - start
    
    print(res1_rec, time1_rec)
    print(res1_it, time1_it)
    print(res2_rec, time2_rec)
    print(res2_it, time2_it)