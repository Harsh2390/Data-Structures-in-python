# Singly linked list data structure implementation in python

# Node class
class Node:
    def __init__(self, data=None): # data is none by default
        self.data = data
        self.next = None

    
# Linkedlist class
class Linkedlist:

    def __init__(self):
        self.head = None  # head is none by default

    def is_empty(self):  # check if the list is empty
        return self.head == None
    
    def addFront(self, data): # add node at the front of the list
        new_node = Node(data)
        cur = self.head
        new_node.next = cur
        self.head = new_node

    def front(self):  # return the first node
        return self.head
    
    def back(self):  # return the last node
        cur = self.head
        while cur.next != None:
            cur = cur.next
        return cur
    
    def removeFront(self):  # remove the first node
        cur = self.head
        self.head = cur.next
        del cur

    

    def append(self, data):  # add node at the end of the list
        new_node = Node(data)
        # if the list is empty
        if self.head == None:
            self.head = new_node
            return
        
        # if the list is not empty
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):  # return the length of the list
        cur = self.head
        total = 0
        while cur != None:
            total = total + 1
            cur = cur.next
        print(total)
    
    def display(self):  # display the list
        cur = self.head
        print('head-->', end='')
        while cur != None:
            print(str(cur.data) + '->', end='')
            cur = cur.next

        print('Null')

    def getindex(self, data):  # get the index of the node
        index = 1
        cur = self.head
        while cur != None:
            if cur.data == data:
                print(index) 
            index+= 1
            cur =cur.next
                
        

my_list = Linkedlist()


my_list.display()

