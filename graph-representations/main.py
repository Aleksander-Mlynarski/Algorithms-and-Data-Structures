#nieskonczone
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
    
class Lista_sasiedztwa:
    def __init__(self):
        self.nodes = {}
        
    def is_empty(self):
        if (len(self.nodes)) == 0:
            return True
            
    def insert_vertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = {}
        
    def insert_edge(self, vertex1, vertex2,edge = 1):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        self.nodes[vertex1][vertex2] = edge

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

    def BFS(self, start, end):
        parent = {}
        visited = set()
        visited.add(start)
        queue = []
        queue.append(start)
        
        while len(queue) > 0:
            current = queue.pop(0)
            
            if (current == end):
                break
            
            for neighbour, edge in self.neighbours(current):
                if (neighbour not in visited and edge.rest > 0):
                    visited.add(neighbour)
                    parent[neighbour] = current
                    queue.append(neighbour)
        return parent    
            
    def min_rest(self, start, end, parent):
        if (end not in parent):
            return 0
            
        current = end
        min_capacity = float('inf')
        
        while (current != start):
            p = parent[current]
            edge = self.get_edge(p, current)
            
            if (edge.rest < min_capacity):
                min_capacity = edge.rest
                
            current = p
        return min_capacity
        
    def augmentation(self, start, end, parent, min_capacity):
        current = end
        
        while (current != start):
            p = parent[current]
            
            edge = self.get_edge(p, current)
            rev_edge = self.get_edge(current, p)

            edge.rest = edge.rest - min_capacity
            rev_edge.rest = rev_edge.rest + min_capacity
  
            if (edge.flag == False):
                edge.flow = edge.flow + min_capacity
            else:
                rev_edge.flow = rev_edge.flow - min_capacity
                
            current = p
    def FF(self, start, end):
        while True:
            parent = self.BFS(start, end)
            min_capacity = self.min_rest(start, end, parent)
            
            if (min_capacity == 0):
                break
                
            self.augmentation(start, end, parent, min_capacity)
        max_flow = 0
        for v in self.vertices():
            if (end in self.nodes[v]):
                edge = self.get_edge(v, end)
                if (edge.flag == False):
                    max_flow = max_flow + edge.flow
                    
        return max_flow    
        
    def printGraph(g):
        print("------GRAPH------")
        for v in g.vertices():
            print(v, end = " -> ")
            for (n, w) in g.neighbours(v):
                print(n, w, end=";")
            print()
        print("-------------------")

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

class Edge:
    def __init__(self, capacity, flag):
        if (self.flag == True):
            self.capacity = 0
            self.rest = 0
        else:
            self.capacity = capacity
            self.rest = self.capacity
        
        if (self.flag == True):
            self.rest = 0
        else:
            self.rest = self.capacity
            
    def __repr__(self):
        return f"{self.capacity} {self.flow} {self.rest} {self.flag}"
        

if __name__ == '__main__':
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3 = [('s', 'a', 3), ('s', 'd', 2), ('a', 'b', 4), ('b', 'c', 5), ('c', 't', 6), ('a', 'f', 3),  ('f', 't', 3), ('d', 'e', 2), ('e','f',2)]
