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
                

def transpose(m: Matrix):
    r,c = m.size()
    transpose_result = []
    for i in range(c):
        transpose_result.append([])
        for j in range(r):
            transpose_result[i].append(m[j][i])
    return Matrix(transpose_result)
    
if __name__ == '__main__':
    m1 = Matrix(
    [ [1, 0, 2],
      [-1, 3, 1] ]
    )
    m2 = Matrix(
    [ [3, 1],
      [2, 1],
      [1, 0]]
    )
    m3 = Matrix((2,3),1)

    print(transpose(m1))
    print(m1+m3)
    print(m1*m2)

