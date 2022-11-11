class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None


class BinarySearchTree:
    def __init__(self):
        self.root=None
        
    def Insert(self, data):
        newNode= Node(data)œ
        if self.root is None:
            self.root=newNode
            return True
        temp= self.root
        while True:
            if temp.data == newNode.data:
                return False
            
            if newNode.data< temp.data:
                if temp.left is None:
                    temp.left=newNode
                    return True
                temp= temp.left
            else:
                if temp.right is None:
                    temp.right=newNode
                    return True
                temp=temp.right
    
    
    def contains(self, data):
        currentNode= self.root
        while currentNode:
            if data< currentNode.data:
                currentNode= currentNode.left
            elif data > currentNode.data:
                currentNode= currentNode.right
            else:
                return True
        return False
                
            
            
        
        
myBinary=BinarySearchTree()
myBinary.Insert(2)
myBinary.Insert(1)
myBinary.Insert(3)
print(myBinary.root.data)
print(myBinary.root.left.data)
print(myBinary.root.right.data)
print(myBinary.contains(4))