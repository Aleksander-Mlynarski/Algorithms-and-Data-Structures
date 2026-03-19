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
 
    def Chio(self):
        if self.c != self.r:
            raise ValueError
            
        n = self.r
        sign = 1
        
        if n==1:
            return self.__matrix[0][0]
        if n==2:
            return self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[1][0] * self.__matrix[0][1]
            
        copied_matrix = copy.deepcopy(self.__matrix)
        a11 = copied_matrix[0][0]
        
        if a11 == 0:
            for row in range(1,n):
                if copied_matrix[row][0] != 0:
                    copied_matrix[0], copied_matrix[row] = copied_matrix[row], copied_matrix[0]
                    a11 = copied_matrix[0][0]
                    sign = -sign
                    break
            else:
                return 0
                
        next_matrix = []
        for i in range(1, n):
            next_row = []
            for j in range(1, n):
                value = a11 * copied_matrix[i][j] - copied_matrix[i][0] * copied_matrix[0][j]
                next_row.append(value)
            next_matrix.append(next_row)
                        
        return sign * (Matrix(next_matrix).Chio() // (a11 ** (n - 2)))
    
    
if __name__ == '__main__':
    m1 = Matrix(
    [
    [5 , 1 , 1 , 2 , 3],
    [4 , 2 , 1 , 7 , 3],
    [2 , 1 , 2 , 4 , 7],
    [9 , 1 , 0 , 7 , 0],
    [1 , 4 , 7 , 2 , 2]
    ])
    m2 = Matrix(
    [
    [0 , 1 , 1 , 2 , 3],
    [4 , 2 , 1 , 7 , 3],
    [2 , 1 , 2 , 4 , 7],
    [9 , 1 , 0 , 7 , 0],
    [1 , 4 , 7 , 2 , 2]
    ])
    m3 = Matrix(
    [
    [0 , 0 , 0 , 0 , 0],
    [4 , 2 , 1 , 7 , 3],
    [2 , 1 , 2 , 4 , 7],
    [9 , 1 , 0 , 7 , 0],
    [1 , 4 , 7 , 2 , 2]
    ])
    
    m4 = Matrix(
    [
    [0 , 1 , 1 , 2 , 3],
    [0 , 2 , 1 , 7 , 3],
    [0 , 1 , 2 , 4 , 7],
    [0 , 1 , 0 , 7 , 0],
    [0 , 4 , 7 , 2 , 2]
    ])
    
    print(m1.Chio())
    print(m2.Chio())
    print(m3.Chio())
    print(m4.Chio())