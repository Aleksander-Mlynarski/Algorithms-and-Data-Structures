#nieskonczone
class element:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class my_List:
    def __init__(self, head = None):
        self.head = head
        self.tail = head
    
    def create_list(self):
        pass
        
    def destroy_list(self):
        current = self.head
        while current is not None:
            temp = current.next
            current.next = None
            current.prev = None
            current = temp
        self.head = None
        self.tail = None
        
    def add(self,data):
        el = element(data)
        el.next = self.head
        if self.head is not None:
            self.head.prev = el
        else:
            self.tail = el
        self.head = el
        
    def append(self, data):
        el = element(data)
        if self.head is not None:
            self.tail.next = el
            el.prev = self.tail
            self.tail = el
        else:
            self.head = el
            self.tail = el
            
    def remove(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
    
    def remove_end(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

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
        
    def reversed_str(self):
        text = ""
        current = self.tail
        while current is not None:
            text += "-> " + str(current.data) + "\n"
            current = current.prev
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
    print(uczelnie.reversed_str())
    print(uczelnie.length(), "\n")
    
    uczelnie.remove()
    print(uczelnie.get(), "\n")
    
    uczelnie.remove_end()
    print(uczelnie)
    print(uczelnie.reversed_str())

    uczelnie.destroy_list()
    print(uczelnie.is_empty(), "\n")
 
    uczelnie.remove()
    uczelnie.remove_end()
    
    uczelnie.append(data[0])
    uczelnie.remove_end()
    print(uczelnie.is_empty())
        