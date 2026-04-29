class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
    
class BstTree():
    def __init__(self):
        self.root = None
        
    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current.value
                
            elif key < current.key:
                current = current.left
                
            else:
                current = current.right
                
        return None
    
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
        
    def _insert(self, root, key, value):
        if root is None:
            return Node(key, value)
            
        if root.key == key:
            root.value = value
            return root
            
        if root.key < key:
            root.right = self._insert(root.right, key, value)
        else:
            root.left = self._insert(root.left, key, value)
            
        return root
                
    
    def delete(self, key):
        self.root = self._delete(self.root, key)
    def _delete(self, root, key):
        if root is None:
            return root
            
        if root.key < key:
            root.right = self._delete(root.right, key)
        elif root.key > key:
            root.left = self._delete(root.left, key)    
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
                
            temp = root.right
            while temp.left is not None:
                temp = temp.left
                
            root.key = temp.key
            root.value = temp.value
            root.right = self._delete(root.right, temp.key)
            
        return root
            
            
    def print_as_list(self):
        self.txt = " "
        self._print_as_list(self.root)
        print(self.txt)
        
    def _print_as_list(self, root):
        if root is not None:
            self._print_as_list(root.left)
            self.txt += f"{root.key} {root.value},"
            self._print_as_list(root.right)
    
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left, lvl+5)
    
    def height(self):
        return self._height(self.root)
        
    def _height(self, root):

        if root is None:
            return 0
            
        left_h = self._height(root.left)
        right_h = self._height(root.right)
        
        if left_h > right_h:
            return left_h + 1
        else:
            return right_h + 1
        
if __name__ == '__main__':
    tree = BstTree()
    
    keys = [50,15,62,5,20,58,91,3,8,37,60,24]
    values = ["A","B","C","D","E","F", "G", "H", "I", "J","K","L"]
    for i in range(len(keys)):
        tree.insert(keys[i], values[i])
        
    tree.print_tree()
    tree.print_as_list()
    print(tree.search(24))
    
    tree.insert(20, "AA")
    tree.insert(6, 'M')
    tree.delete(62)
    tree.insert(59, 'N')
    tree.insert(100, 'P')
    tree.delete(8)
    tree.delete(15)
    tree.insert(55, 'R')
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    
    print(tree.height())
    tree.print_as_list()
    tree.print_tree()