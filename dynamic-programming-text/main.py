def recursion_a(P, T, i, j):

    if i == 0:
        return j

    if j == 0:
        return i
        
    insert_cost = 1 + recursion_a(P,T,i,j-1)
    delete_cost = 1 + recursion_a(P,T,i-1,j)
    
    if P[i] != T[j]:
        switch_cost = 1 + recursion_a(P,T,i-1,j-1)
    else:
        switch_cost = recursion_a(P,T,i-1,j-1)
    
    return min(insert_cost, delete_cost, switch_cost)

def PD_b(P, T):
    rows = len(P)
    cols = len(T)
    D = []
    parents = []
    for x in range(rows):
        D.append([])
        parents.append([])
        for y in range(cols):
            D[x].append(0)
            parents[x].append("X")
            
    for x in range(rows):
        D[x][0] = x
        if(x>0):
            parents[x][0] = "D"
    
    for x in range(cols):
        D[0][x] = x
        if(x>0):
            parents[0][x] = "I" 
 
    for i in range(1, rows):
        for j in range(1, cols):
            switch_cost = D[i-1][j-1] + int(P[i] != T[j])
            insert_cost = 1 + D[i][j-1]
            delete_cost = 1 + D[i-1][j]
    
            min_cost = min(insert_cost, delete_cost, switch_cost) 
            D[i][j] = min_cost
            
            if min_cost == switch_cost and P[i] != T[j]:
                parents[i][j] = "R"
            elif min_cost == switch_cost and P[i] == T[j]:
                parents[i][j] = "M"
            elif min_cost == insert_cost:
                parents[i][j] = "I"
            elif min_cost == delete_cost:
                parents[i][j] = "D"
    return D[rows-1][cols-1], parents
                
def path_replay(parents):
    i = len(parents) - 1
    j = len(parents[0]) - 1
    path = []
    
    while parents[i][j] != "X":
        curr = parents[i][j]
        path.append(curr)
        
        if curr == "M" or curr == "R":
            i -= 1
            j -= 1
        elif curr == "I":
            j -= 1
        elif curr == "D":
            i -= 1
            
    res = ""
    idx = len(path) - 1
    while idx >= 0:
        res += path[idx]
        idx -= 1
        
    return res
    
def PD_d(P, T):
    rows = len(P)
    cols = len(T)
    D = []
    parents = []
    for x in range(rows):
        D.append([])
        parents.append([])
        for y in range(cols):
            D[x].append(0)
            parents[x].append("X")
            
    for x in range(rows):
        D[x][0] = x
        if(x>0):
            parents[x][0] = "D"
    
    for x in range(cols):
        D[0][x] = x
        if(x>0):
            parents[0][x] = 0 
 
    for i in range(1, rows):
        for j in range(1, cols):
            switch_cost = D[i-1][j-1] + int(P[i] != T[j])
            insert_cost = 1 + D[i][j-1]
            delete_cost = 1 + D[i-1][j]
    
            min_cost = min(insert_cost, delete_cost, switch_cost) 
            D[i][j] = min_cost
            
            if min_cost == switch_cost and P[i] != T[j]:
                parents[i][j] = "R"
            elif min_cost == switch_cost and P[i] == T[j]:
                parents[i][j] = "M"
            elif min_cost == insert_cost:
                parents[i][j] = "I"
            elif min_cost == delete_cost:
                parents[i][j] = "D"
                
    min_cost = D[rows-1][0]
    min_col = 0
    
    for x in range(1, cols):
        if D[rows-1][x] < min_cost:
            min_cost = D[rows-1][x]
            min_col = x
            
    i = rows - 1
    j = min_col
    
    while parents[i][j] != "X":
        curr = parents[i][j]
        if curr == "M" or curr == "R":
            i -= 1
            j -= 1
        elif curr == "I":
            j -= 1
        elif curr == "D":
            i -= 1

    start_idx = j + 1
    
    return start_idx, min_cost
    
def longest_seq(P, T):
    rows = len(P)
    cols = len(T)
    D = []
    parents = []
    for x in range(rows):
        D.append([])
        parents.append([])
        for y in range(cols):
            D[x].append(0)
            parents[x].append("X")
            
    for x in range(rows):
        D[x][0] = x
        if(x>0):
            parents[x][0] = "D"
    
    for x in range(cols):
        D[0][x] = x
        if(x>0):
            parents[0][x] = "I" 
 
    for i in range(1, rows):
        for j in range(1, cols):
            if P[i] != T[j]:
                switch_cost = D[i-1][j-1] + 100000
            else:
                switch_cost = D[i-1][j-1]
                
            insert_cost = 1 + D[i][j-1]
            delete_cost = 1 + D[i-1][j]
    
            min_cost = min(insert_cost, delete_cost, switch_cost) 
            D[i][j] = min_cost
            
            if min_cost == switch_cost and P[i] != T[j]:
                parents[i][j] = "R"
            elif min_cost == switch_cost and P[i] == T[j]:
                parents[i][j] = "M"
            elif min_cost == insert_cost:
                parents[i][j] = "I"
            elif min_cost == delete_cost:
                parents[i][j] = "D"
                
    return parents
   
def longest_monotonic_seq(path, P):
    res = ""
    idx = 1
    for it in path:
        if it == "M":
            res += P[idx]
            idx += 1
        elif it == "D" or it == "R":
            idx += 1
    return res
    
if __name__ == '__main__':   
    P1 = ' kot'
    T1 = ' pies'
    i1 = len(P1)-1
    j1 = len(T1)-1
    res1 = recursion_a(P1,T1,i1,j1)
    print(res1)
    
    P2 = ' biały autobus'
    T2 = ' czarny autokar'
    res2, parents2 = PD_b(P2, T2)
    print(res2)
    
    P3 = ' thou shalt not'
    T3 = ' you should not'
    cost3, parents3 = PD_b(P3, T3)
    res3 = path_replay(parents3)
    print(res3)
    
    P4 = ' ban'
    P5 = ' bin'
    T4 = ' mokeyssbanana'
    start4, cost4 = PD_d(P4, T4)
    start5, cost5 = PD_d(P5, T4)
    print(f"{start4}, {cost4}")
    print(f"{start5}, {cost5}")
    
    P6 = ' democrat'
    T6 = ' republican'
    parents6 = longest_seq(P6, T6)
    path6 = path_replay(parents6)
    res6 = longest_monotonic_seq(path6, P6)
    print(res6)

    T7 = ' 243517698'
    T7_list = list(T7[1:])
    T7_list.sort()
    P7 = ' ' + "".join(T7_list)
    
    parents7 = longest_seq(P7, T7)
    path7 = path_replay(parents7)
    res7 = longest_monotonic_seq(path7, P7)
    print(res7)