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
        if index<0 or index>self.length:
            print("Index is out of rnage")
            return False
        currentNode= self.head
        for _ in range(index):
            currentNode= currentNode.nextNode
        return currentNode
    
    def insert(self,value, index):                  #Insert element in the list at given index
        if index<0 or index>self.length:
            return False
        if index==0:
            self.preppend(value)
            return True
        if index == self.length:
            self.append(value)
            return True
        newNode= Node(value)
        temp= self.get(index-1)
        newNode.nextNode=temp.nextNode
        temp.nextNode=newNode
        self.length+=1
        return True
    
    def pop(self):                          # Delete at the end of the list method
        if self.length==0:
            print("list is empty.")
            return None
        currentNode= self.head
        prev=self.head
        while currentNode.nextNode:
            prev=currentNode
            currentNode= currentNode.nextNode
        self.tail=prev
        self.tail.nextNode=None
        self.length-=1
        
        if self.length==0:
            self.head=None
            self.tail=None
        return currentNode
    
    
    def reverse(self):
        temp=self.head
        self.head= self.tail
        self.tail=temp
        after= temp.nextNode
        before=None
        for _ in range(self.length):
            after= temp.nextNode
            temp.nextNode=before
            before=temp
            temp = after
    
    
    def merge_two_sorted_linkedlist(self, list2):
        dummyhead=None
        l1_head= self.head
        l2_head= list2.head
        if l1_head is None:
            return l2_head
        if l2_head is None:
            return l1_head
        if l1_head and l2_head:
            if l1_head.data<= l2_head.data:
                currenthead= l1_head
                l1_head= currenthead.nextNode
            else:
                currenthead= l2_head
                l2_head=currenthead.nextNode
        dummyhead= currenthead
        while l1_head and l2_head:
            if l1_head.data<= l2_head.data:
                currenthead.nextNode= l1_head
                currenthead=l1_head
                l1_head=currenthead.nextNode
            else:
                currenthead.nextNode= l2_head
                currenthead=l2_head
                l2_head=currenthead.nextNode
        if l1_head:
            currenthead.nextNode=l1_head
        if l2_head:
            currenthead.nextNode=l2_head
        return dummyhead
                
                
    
                
                
           
        
        
        
        
        
    
myList= singleLinkedList()
myList.preppend(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(5)

#print(myList.get(1))
#myList.insert(9,3)
#myList.pop()
#myList.reverse()

myList1= singleLinkedList()
myList1.preppend(1)
myList1.append(2)
myList1.append(4)
myList1.append(4)
myList1.append(5)
myList2= singleLinkedList()
myList2.append(1)
myList2.append(1)
myList2.append(5)
myList2.append(6)
myList2.printing()
myList1.merge_two_sorted_linkedlist(myList2)
myList1.printing()

#print(myList.length)
