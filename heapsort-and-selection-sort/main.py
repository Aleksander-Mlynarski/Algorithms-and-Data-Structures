#nieskonczone
import random
import time

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
    def __init__(self, tab=None):
        if tab is None:
            self.tab = []
            self.size = 0
        else:
            self.tab = tab
            self.size = len(self.tab)
            if self.size > 0:
                for i in range(self.parent(self.size - 1), -1, -1):
                    self._dequeue(i)
    
    def left(self, idx):
        return 2 * idx + 1
    
    def right(self, idx):
        return 2 * idx + 2
    
    def parent(self, idx):
        return (idx - 1) // 2
    
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
        
        self.tab[0] = self.tab[self.size]
        self.tab[self.size] = root
        
        if self.size > 0:
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

def sort_swap(tab):
    n = len(tab)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if tab[j] < tab[m]:
                m = j
        tab[i], tab[m] = tab[m], tab[i]

def sort_shift(tab):
    n = len(tab)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if tab[j] < tab[m]:
                m = j
        if m != i:
            temp = tab.pop(m)
            tab.insert(i, temp)


if __name__ == '__main__':
    wybor = int(input("test 1 czy 2? "))
    
    if wybor == 1:
        dane = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
        
        tab_heap = [Element(d, p) for p, d in dane]
        kolejka = HeapQueue(tab_heap)
        kolejka.print_tab()
        kolejka.print_tree(0, 0)
        while not kolejka.is_empty():
            kolejka.dequeue()
        print(kolejka.tab)
        print("NIESTABILNE")
        
        tab_swap = [Element(d, p) for p, d in dane]
        sort_swap(tab_swap)
        print(tab_swap)
        print("NIESTABILNE")
        
        tab_shift = [Element(d, p) for p, d in dane]
        sort_shift(tab_shift)
        print(tab_shift)
        print("STABILNE")
        
    elif wybor == 2:
        tab_startowa = [int(random.random() * 100) for _ in range(10000)]
        tab1 = tab_startowa.copy()
        tab2 = tab_startowa.copy()
        tab3 = tab_startowa.copy()
        
        t_start = time.perf_counter()
        kolejka = HeapQueue(tab1)
        while not kolejka.is_empty():
            kolejka.dequeue()
        t_stop = time.perf_counter()
        print("{:.7f}".format(t_stop - t_start))
        
        t_start = time.perf_counter()
        sort_swap(tab2)
        t_stop = time.perf_counter()
        print("{:.7f}".format(t_stop - t_start))
        
        t_start = time.perf_counter()
        sort_shift(tab3)
        t_stop = time.perf_counter()
        print("{:.7f}".format(t_stop - t_start))