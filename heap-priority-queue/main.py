class Element():
    def __init__(self, dane, priorytet):
        self.__dane = dane
        self.__priorytet = priorytet
    def __lt__(self, other):
        return self.__priorytet < other.__priorytet
    def __gt__(self, other):
        return self.__priorytet > other.__priorytet
        
    def __repr__(self):
        return f"{self.__priorytet} : {self.__dane}"
    
class HeapQueue():
    def __init__(self):
        self.tab = []
        self.size = 0
    
    def left(self, idx):
        return 2 * idx + 1
    
    def right(self, idx):
        return 2 * idx + 2
    
    def parent(self, idx):
        return (idx - 1) //2
    
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def peek(self):
        if self.is_empty() is True:
            return None
        return self.tab[0]
    
    def dequeue(self):
        if self.is_empty() is True:
            return None
            
        root = self.tab[0]
        self.size -= 1
        
        if self.size > 0:
            self.tab[0] = self.tab[self.size]
            self._dequeue(0)
        return root
        
    def _dequeue(self, idx):
        max_idx = idx
        left_child = self.left(idx)
        right_child = self.right(idx)
        
        if left_child < self.size and self.tab[left_child] > self.tab[max_idx]:
            max_idx = left_child
            
        if right_child < self.size and self.tab[right_child] > self.tab[max_idx]:
            max_idx = right_child
            
        if max_idx != idx:
            self.tab[idx], self.tab[max_idx] = self.tab[max_idx], self.tab[idx]
            self._dequeue(max_idx)
        
    def enqueue(self, elem):
        if self.size == len(self.tab):
            self.tab.append(elem)
        elif self.size < len(self.tab):
            self.tab[self.size] = elem

        self.size += 1
        self._switch(self.size - 1)
        
    def _switch(self, idx):
        if idx > 0:
            par = self.parent(idx)
            if self.tab[idx] > self.tab[par]:
                self.tab[idx], self.tab[par] = self.tab[par], self.tab[idx]
                self._switch(par)
        
    
    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx<self.size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)
    
if __name__ == '__main__':
    kolejka = HeapQueue()
    
    priorytety = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    data = "GRYMOTYLA"
    
    for i in range(len(priorytety)):
        p = priorytety[i]
        d = data[i]
        kolejka.enqueue(Element(d, p))
        
    kolejka.print_tree(0, 0)
    kolejka.print_tab()
    
    pierwsza = kolejka.dequeue()
    
    print(kolejka.peek())
    kolejka.print_tab()
    print(pierwsza)
    
    while not kolejka.is_empty():
        print(kolejka.dequeue())
        
    kolejka.print_tab()