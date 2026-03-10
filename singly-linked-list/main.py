class element:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class my_List:
    def __init__(self, head = None):
        self.head = head
    
    def create_list(self):
        pass
        
    def destroy_list(self):
        self.head = None
        
    def add(self,data):
        el = element(data)
        el.next = self.head
        self.head = el
        
    def append(self, data):
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = element(data)
        else:
            self.head = element(data)
            
    def remove(self):
        if self.head is not None:
            self.head = self.head.next
    
    def remove_end(self):
        if self.head is None:
            pass

        elif self.head.next is None:
            self.head = None
        
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    
    def length(self):
        n = 0
        current = self.head
        while current is not None:
            n+=1
            current = current.next
        return n
    
    def get(self):
        return self.head.data
        
    def __str__(self):
        text = ""
        current = self.head
        while current is not None:
            text += "-> " + str(current.data) + "\n"
            current = current.next
        return text
                    
    
    
if __name__ == '__main__':
    data = [('AGH', 'Kraków', 1919),
    ('UJ', 'Kraków', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznań', 1919),
    ('PG', 'Gdańsk', 1945)]
    
    uczelnie = my_List()
        
    for i in range(3):
        uczelnie.append(data[i])
    for i in range(3, len(data)):
        uczelnie.add(data[i])
    print(uczelnie)
    
    print(uczelnie.length(), "\n")
    
    uczelnie.remove()
    print(uczelnie.get(), "\n")
    
    uczelnie.remove_end()
    print(uczelnie)

    uczelnie.destroy_list()
    print(uczelnie.is_empty(), "\n")
 
    uczelnie.remove()
    uczelnie.remove_end()
    
    uczelnie.append(data[0])
    uczelnie.remove_end()
    print(uczelnie.is_empty())
        