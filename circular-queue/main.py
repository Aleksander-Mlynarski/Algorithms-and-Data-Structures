class Queue():
    def __init__(self):
        self.size = 5
        self.tab = [None for i in range(self.size)]
        self.id_write = 0
        self.id_read = 0
        
    def is_empty(self):
        if self.id_write == self.id_read:
            return True
    
    def peek(self):
        return self.tab[self.id_read]
    
    def dequeue(self):
        if self.is_empty() is True:
            return None
        else:
            el = self.tab[self.id_read]
            self.id_read = (self.id_read + 1) % self.size
        return el
        
    def enqueue(self, data):
        self.tab[self.id_write] = data
        self.id_write = (self.id_write + 1) % self.size
        if self.id_write == self.id_read:
            bigger_tab = [None for i in range(2 * self.size)]
            idn = self.size
            for i in range(self.size):
                idn = (self.id_read + i) % self.size
                bigger_tab[i] =  self.tab[idn]
            self.tab = bigger_tab
            self.id_write = self.size
            self.size = 2 * self.size
            self.id_read = 0
    
    def __str__(self):
        text = "["
        i = self.id_read
        while i != self.id_write:
            text += str(self.tab[i])
            i = (i+1) % self.size
            if i != self.id_write:
                text += ","
        text = text + "]\n"
        return text
        
    def stan(self):
        print(self.tab)
        
if __name__ == '__main__':
    data = Queue()
    
    data.enqueue(0)
    data.enqueue(1)
    
    print(data.dequeue())
    
    print(data.peek())
    
    data.enqueue(2)
    data.enqueue(3)
    data.enqueue(4)
    
    data.dequeue()
    
    print(data)
    
    data.enqueue(5)
    data.enqueue(6)
    data.enqueue(7)
    data.enqueue(8)
    
    data.stan()
    
    print(data.dequeue())
    print("\n")
    
    while data.is_empty() is not True:
        print(data.dequeue())
   
    print(data)
    