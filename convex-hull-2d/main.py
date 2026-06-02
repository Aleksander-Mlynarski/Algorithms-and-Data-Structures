class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"({self.x}, {self.y})"
def direction(p1, p2, p3):
    a = (p2.y - p1.y)*(p3.x - p2.x) - (p3.y - p2.y)*(p2.x - p1.x)
    if(a>0):
        return 1
    if(a<0):
        return -1
    else:
        return 0
    
def distance_sq(p1,p2):
    return (p2.x - p1.x)**2 + (p2.y - p1.y)**2
    
def Jarvis_right_turned(points):
    radical_left = 0
    my_list = []
    n = len(points)
    for i in range(n):
        if points[i].x < points[radical_left].x:
            radical_left = i
        elif points[i].x == points[radical_left].x:
            if points[i].y < points[radical_left].y:
                radical_left = i
    p = radical_left
    while True:
        q = (p+1) % n
        my_list.append(points[p])
        for r in range(n):
            turn = direction(points[p], points[q], points[r])
            if turn == 1:
                q = r
            elif turn == 0 :
                #porownanie dla kwadratow, dla oszczednosci
                if(distance_sq(points[p], points[r]) > distance_sq(points[p], points[q])):
                    q = r
        p = q
        if p == radical_left:
            break
    return my_list
    
def Graham(points):
    n = len(points)
    lowest = 0
    for i in range(n):
        if points[i].y < points[lowest].y:
            lowest = i
        elif points[i].y == points[lowest].y:
            if points[i].x < points[lowest].x:
                lowest = i

    points[0], points[lowest] = points[lowest], points[0]
    p0 = points[0]

    for i in range(1, n - 1):
        for j in range(1, n - i):
            turn = direction(p0, points[j], points[j+1])
            if turn == 1 or (turn == 0 and distance_sq(p0, points[j]) > distance_sq(p0, points[j+1])):
                points[j], points[j+1] = points[j+1], points[j]

    filtered_points = [points[0]]
    for i in range(1,n):
        if i < n - 1 and direction(p0, points[i], points[i+1]) == 0:
            continue
        filtered_points.append(points[i])

    if len(filtered_points) < 3:
        return filtered_points

    my_list = [filtered_points[0], filtered_points[1], filtered_points[2]]

    for i in range(3, len(filtered_points)):
        while len(my_list) > 1 and direction(my_list[-2], my_list[-1], filtered_points[i]) != -1:
            my_list.pop()
        my_list.append(filtered_points[i])

    return my_list
    
if __name__ == '__main__':
    points1_before = (2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)
    points1 = [Point(x, y) for x, y in points1_before]
    print(Jarvis_right_turned(points1))
    
    points2_before = (0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)
    points2 = [Point(x, y) for x, y in points2_before]
    print(Graham(points2))