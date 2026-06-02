from typing import List, Tuple
import copy
class Matrix:
    def __init__(self, initializer: Tuple[int, int] | List[List[int]],default_val: int = 0):
        if isinstance(initializer, tuple):
            self.r = initializer[0]
            self.c = initializer[1]
            self.__matrix = []
            for i in range(self.r):
                self.__matrix.append([])
                for j in range(self.c):
                    self.__matrix[i].append(default_val)
        else:
            self.r = len(initializer)
            self.c = len(initializer[0])
            self.__matrix = initializer        
    def __add__(self, other: "Matrix"):
        if self.size() != other.size():
            raise ValueError
        add_result = []
        for r in range(self.r):
            add_result.append([])
            for c in range(self.c):
                add_result[r].append(self[r][c] + other[r][c])
        return Matrix(add_result)
        
    def __mul__(self,other: "Matrix"):
        if self.c != other.r:
            raise ValueError
        mul_result = []
        for r in range(self.r):
            mul_result.append([])
            for c in range(other.c):
                s=0
                for d in range(self.c):
                    s+= self[r][d] * other[d][c]
                mul_result[r].append(s)
        return Matrix(mul_result)
        
    def __eq__(self,other: "Matrix"):
        for r in range(self.r):
            for c in range(self.c):
                if (self[r][c] != other[r][c]):
                    return False
        return True
                
    def __getitem__(self, indeks):
        return self.__matrix[indeks]
    
    def size(self):
        row = len(self.__matrix)
        col = len(self.__matrix[0])
        return row,col
    
    def __str__(self):
        text = ""
        for r in range(self.r):
            text += "|"
            for c in range(self.c):
                text += f"{self[r][c]:2}" + " "
            text += "|\n"
        return text
        
    def add_row(self, row):
        self.__matrix.append(row)
        self.r += 1

    def add_column(self, col):
        if self.r > 0:
            for i in range(self.r):
                self.__matrix[i].append(col[i])
            self.c += 1

    def remove_row(self, idx):
        self.__matrix.pop(idx)
        self.r -= 1

    def remove_column(self, idx):
        for i in range(self.r):
            self.__matrix[i].pop(idx)
        self.c -= 1
                
class Vertex:
    def __init__(self, key):
        self.key = key
    def __hash__(self):
        return hash(self.key)
    def __eq__(self, other):
        return self.key == other.key
    def __repr__(self):
        return str(self.key)
    

class Macierz_sasiedztwa:
    def __init__(self, default_val: int = 0):
        self.nodes: List = []
        self._default = default_val
        self.matrix = Matrix((0,0), default_val)

    def is_empty(self):
        return len(self.nodes) == 0

    def _index_of(self, vertex):
        if isinstance(vertex, int):
            return vertex
        return self.nodes.index(vertex)

    def insert_vertex(self, vertex):
        if vertex in self.nodes:
            return

        n = len(self.nodes)

        if n == 0:
            self.matrix = Matrix((1, 1), self._default)
            self.nodes.append(vertex)
            return

        self.matrix.add_column([self._default] * n)
        self.matrix.add_row([self._default] * (n + 1))
        self.nodes.append(vertex)

    def insert_edge(self, vertex1, vertex2, edge=1):

        i = self._index_of(vertex1)
        j = self._index_of(vertex2)
        self.matrix[i][j] = edge
        self.matrix[j][i] = edge

    def delete_vertex(self, vertex):
        idx = self._index_of(vertex)
        del self.nodes[idx]
        n = len(self.nodes)
        if n == 0:
            self.matrix = Matrix((0,0), self._default)
            return
        self.matrix.remove_row(idx)
        self.matrix.remove_column(idx)

    def delete_edge(self, vertex1, vertex2):
        i = self._index_of(vertex1)
        j = self._index_of(vertex2)
        self.matrix[i][j] = self._default
        self.matrix[j][i] = self._default

    def get_edge(self, vertex1, vertex2):
        i = self._index_of(vertex1)
        j = self._index_of(vertex2)
        return self.matrix[i][j]

    def vertices(self):
        for i in range(len(self.nodes)):
            yield i

    def neighbours(self, vertex_id):
        idx = vertex_id
        n = len(self.nodes)
        for j in range(n):
            val = self.matrix[idx][j]
            if val != self._default:
                yield j, val

    def get_vertex(self, vertex_id):
        if isinstance(vertex_id, int):
            return self.nodes[vertex_id]
        return self.nodes[self._index_of(vertex_id)]

        
def Ullmann(used_col,curr_row, Matrix_M, P, G, calls):
    calls +=1
    if (curr_row == Matrix_M.r):
        M_G = Matrix_M * G
        M_G_T = transpose(M_G)
        if (Matrix_M * M_G_T == P):
            izo_list.append(copy.deepcopy(Matrix_M))
        return calls
            
    for c in range(Matrix_M.c):
        if(used_col[c] ==  False):
            used_col[c] = True

            for i in range(Matrix_M.c):
                Matrix_M[curr_row][i] = 0
            Matrix_M[curr_row][c] = 1 
            
            calls = Ullmann(used_col, curr_row + 1, Matrix_M, P, G, calls)
            
            used_col[c] = False
    return calls
    
def Ullmann2(used_col,curr_row, Matrix_M, P, G, calls):
    calls +=1
    if (curr_row == Matrix_M.r):
        M_G = Matrix_M * G
        M_G_T = transpose(M_G)
        if (Matrix_M * M_G_T == P):
            izo_list.append(copy.deepcopy(Matrix_M))
        return calls
            
    for c in range(Matrix_M.c):
        if (used_col[c] == False and Matrix_M[curr_row][c] != 0):
            used_col[c] = True
            Matrix_M_copy = copy.deepcopy(Matrix_M)
            for i in range(Matrix_M.c):
                Matrix_M_copy[curr_row][i] = 0
            Matrix_M_copy[curr_row][c] = 1 
            
            calls = Ullmann2(used_col, curr_row + 1, Matrix_M_copy, P, G, calls)
            
            used_col[c] = False
    return calls
            
        
def transpose(m: Matrix):
    r,c = m.size()
    transpose_result = []
    for i in range(c):
        transpose_result.append([])
        for j in range(r):
            transpose_result[i].append(m[j][i])
    return Matrix(transpose_result)
    
if __name__ == '__main__':
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]
    
    G_obj = Macierz_sasiedztwa()
    
    for v in ['A', 'B', 'C', 'D', 'E', 'F']:
        G_obj.insert_vertex(v)
    for v1, v2, nb in graph_G:
        G_obj.insert_edge(v1, v2, nb)
        
    P_obj = Macierz_sasiedztwa()
    
    for v in ['A', 'B', 'C']:
        P_obj.insert_vertex(v)
    for v1, v2, nb in graph_P:
        P_obj.insert_edge(v1, v2, nb)
        
    G = G_obj.matrix
    P = P_obj.matrix
    
    M_v1 = Matrix((P.r, G.r), 0)
    used_v1 = [False] * G.r
    izo_list = [] 
    
    calls_v1 = Ullmann(used_v1, 0, M_v1, P, G, 0)
    wynik_v1 = len(izo_list)
    
    M0 = Matrix((P.r, G.r), 0)
    
    for i in range(P.r):
        for j in range(G.r):
            if sum(P[i]) <= sum(G[j]):
                M0[i][j] = 1
                
    used_v2 = [False] * G.r
    izo_list = [] 
    
    calls_v2 = Ullmann2(used_v2, 0, M0, P, G, 0)
    wynik_v2 = len(izo_list)

    print(f"{wynik_v1} {calls_v1}")
    print(f"{wynik_v2} {calls_v2}")
