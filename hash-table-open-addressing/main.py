class Hash_table():
    def __init__(self, size, c1 = 1, c2 = 0):
        self.size = size
        self.tab = [None for i in range(size)]
        self.c1 =  c1
        self.c2 = c2
        
    def get_hash(self, key):
        if isinstance(key, int):
            hash = key
        else:
            hash =  sum(ord(char) for char in key)
            
        return hash % self.size
    
    def search(self, key):
        h = self.get_hash(key)
        for i in range(self.size):
            id = (h + self.c1 * i + self.c2 * (i**2)) % self.size
            
            if self.tab[id] is None:
                return None
                
            if self.tab[id].key == key:
                if self.tab[id].is_deleted == False:
                    return self.tab[id].value
                else:
                    return None
        return None
    
    def insert(self, key, value):
        h = self.get_hash(key)
        for i in range(self.size):
            id = (h + self.c1 * i + self.c2 * (i**2)) % self.size
            if self.tab[id] is None or self.tab[id].is_deleted == True:
                self.tab[id] = Element(key, value)
                break
                
            if self.tab[id].key == key:
                self.tab[id].value = value
                break
        else:
            print("Brak miejsca")
        
    def remove(self, key):
        h = self.get_hash(key)
        for i in range(self.size):
            id = (h + self.c1 * i + self.c2 * (i**2)) % self.size
            
            if self.tab[id] is None:
                print("Brak danej")
                break
                
            if self.tab[id].key == key:
                self.tab[id].is_deleted = True
                break
        else:
            print("Brak danej")

    def __str__(self):
        text = "{"
        for i in range(self.size):
            item = self.tab[i]
            if item is not None and item.is_deleted == False:
                text += str(item)
            else:
                text += "None"
            if i < self.size - 1:
                text += ", "
        text += "}"
        return text
            
class Element():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.is_deleted = False
        
    def __str__(self):
        return f"{self.key}:{self.value}"
    
def test_1(size, c1 = 1, c2 = 0):
    ht = Hash_table(size, c1, c2)
    keys = [1,2,3,4,5,18,31,8,9,10,11,12,13,14,15]
    values = ["A","B","C","D","E","F", "G", "H", "I", "J","K","L","M","N","O"]
    for i in range(len(keys)):
        k = keys[i]
        v = values[i]
        ht.insert(k,v)
    print(ht)
    
    print(ht.search(5))
    
    print(ht.search(14))
    
    ht.insert(5,"Z")
    
    print(ht.search(5))
    
    ht.remove(5)

    print(ht)

    print(ht.search(31)) 
    
    ht.insert("test", "W")
    print(ht)    

def test_2(size, c1 = 1, c2 = 0):
    ht = Hash_table(size, c1, c2)
    keys = [13 * i for i in range(1,16)]
    values = ["A","B","C","D","E","F", "G", "H", "I", "J","K","L","M","N","O"]
    for i in range(len(keys)):
        k = keys[i]
        v = values[i]
        ht.insert(k,v)
    print(ht)
    
    print(ht.search(5))
    
    print(ht.search(14))
    
    ht.insert(5,"Z")
    
    print(ht.search(5))
    
    ht.remove(5)

    print(ht)

    print(ht.search(31)) 
    
    ht.insert("test", "W")
    print(ht)    
    
if __name__ == '__main__':
    test_1(13)
    print("\n")
    test_2(13)
    print("\n")
    test_2(13,0,1)
    print("\n")
    test_1(13,0,1)