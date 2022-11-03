class Node:
    def __init__(self,data):
        self.data=data          #data to add to the list
        self.nextNode= None     # pointer to the next node

class singleLinkedList:
    def __init__(self):
        self.head=None           # head of the list
        self.tail=None           # tail of the list
        self.length=0
    # insert the element at the beginning of the list
    def preppend(self,data):            
        newNode= Node(data)
        if self.length==0:
            self.head= newNode
            self.tail= newNode
            self.length+=1
            return
        currentNode= self.head
        self.head=newNode
        newNode.nextNode=currentNode
        self.length+=1
        
    # print element of the list
    def printing(self):
        currentNode= self.head
        while currentNode:
            print(currentNode.data, "-> ", end="")
            currentNode= currentNode.nextNode
        print("None")
    
    # adding element at the end of list 
    def append(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            self.length+=1
            return
        else:
            self.tail.nextNode= newNode
            self.tail= newNode
            self.length+=1
            
    def get(self, index):                       # get method to get element using its indexes
        pos=0
        currentNode= self.head
        if index> self.length or index<0:
            print("index is out the range")
            return
        if currentNode is None:
            return None
        if index==0:
            return currentNode.data
        while pos < index-1 and index< self.length:
            currentNode= currentNode.nextNode
            pos+=1
        if currentNode:
            return currentNode.data
                
                  
    
myList= singleLinkedList()
myList.preppend(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(5)
#myList.printing()
print(myList.get(1))
#print(myList.length)
