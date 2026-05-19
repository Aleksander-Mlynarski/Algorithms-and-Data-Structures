from pygame import ver

import polska
from typing import List, Tuple

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
                
class Vertex:
    def __init__(self, key):
        self.key = key
    def __hash__(self):
        return hash(self.key)
    def __eq__(self, other):
        return self.key == other.key
    def __repr__(self):
        return str(self.key)
    
class Lista_sasiedztwa:
    def __init__(self):
        self.nodes = {}
        
    def is_empty(self):
        if (len(self.nodes)) == 0:
            return True
            
    def insert_vertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = {}
        
    def insert_edge(self, vertex1, vertex2,edge):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        self.nodes[vertex1][vertex2] = edge
        self.nodes[vertex2][vertex1] = edge
        
    def delete_vertex(self, vertex):
        for sasiad in self.nodes:
            if vertex in self.nodes[sasiad]:
                del self.nodes[sasiad][vertex]
        del self.nodes[vertex]
    
    def delete_edge(self, vertex1, vertex2):
        del self.nodes[vertex1][vertex2]
        del self.nodes[vertex2][vertex1]
    
    def get_edge(self, vertex1, vertex2):
        return self.nodes[vertex1][vertex2]
    
    def vertices(self):
        return self.nodes.keys()
    
    def neighbours(self, vertex_id):
        return self.nodes[vertex_id].items()
    
    def get_vertex(self, vertex_id):
        return vertex_id

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

        new_rows = []

        for i in range(n):
            row = []
            for j in range(n):
                row.append(self.matrix[i][j])
            row.append(self._default)
            new_rows.append(row)

        new_row = []
        for j in range(n + 1):
            new_row.append(self._default)
        new_rows.append(new_row)

        self.matrix = Matrix(new_rows)
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
        new_rows = []
        old_n = n + 1
        for i in range(old_n):
            if i == idx:
                continue
            row = []
            for j in range(old_n):
                if j == idx:
                    continue
                row.append(self.matrix[i][j])
            new_rows.append(row)
        self.matrix = Matrix(new_rows)

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


if __name__ == '__main__':
    GRAF = Macierz_sasiedztwa()
    for vertex1, vertex2 in polska.graf:
        GRAF.insert_vertex(vertex1)
        GRAF.insert_vertex(vertex2)
        GRAF.insert_edge(vertex1, vertex2)
    GRAF.delete_vertex("K")
    GRAF.delete_edge("W", "E")
    polska.draw_map(GRAF)
