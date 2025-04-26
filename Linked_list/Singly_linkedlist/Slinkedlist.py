"""
Singly Linked List Implementation

This module provides a comprehensive implementation of a Singly Linked List data structure.
"""

from typing import TypeVar, Generic, Optional, Iterator, Any, List

T = TypeVar('T')  # Generic type for the data stored in the list

class Node(Generic[T]):
    # A node in a singly linked list.
    # Each node contains a data element and a reference to the next node in the list.

    
    def __init__(self, data: T, next_node: Optional['Node[T]'] = None) -> None:
        """
        Initialize a new Node.
        
        Args:
            data: The data element to store
            next_node: Reference to the next node (default: None)
        """
        self.data: T = data
        self.next: Optional['Node[T]'] = next_node


class SinglyLinkedList(Generic[T]):
    """
    A singly linked list implementation.
    
    A linear data structure where each element points to the next element in the sequence.
    This implementation provides standard linked list operations with appropriate time
    complexities.
    """
    
    def __init__(self, iterable: Optional[List[T]] = None) -> None:
        """
        Initialize a new empty SinglyLinkedList, optionally with initial values.
        
        Args:
            iterable: Optional iterable of values to initialize the list with
        """
        self._head: Optional[Node[T]] = None
        self._size: int = 0
        
        # Add initial values if provided
        if iterable:
            for item in iterable:
                self.append(item)
    
    def __len__(self) -> int:
        """
        Return the number of elements in the list.
        
        Returns:
            The number of elements in the list
            
        Time Complexity: O(1)
        """
        return self._size
    
    def __iter__(self) -> Iterator[T]:
        """
        Return an iterator over the list's elements.
        
        Yields:
            The data elements of the list in order
            
        Time Complexity: O(n) overall, O(1) per element
        """
        current = self._head
        while current:
            yield current.data
            current = current.next
    
    def __str__(self) -> str:
        """
        Return a string representation of the list.
        
        Returns:
            A string representation in the form '[val1, val2, ...]'
            
        Time Complexity: O(n)
        """
        return f"[{', '.join(str(item) for item in self)}]"
    
    def __repr__(self) -> str:
        """
        Return a developer string representation of the list.
        
        Returns:
            A detailed string representation including the class name
            
        Time Complexity: O(n)
        """
        return f"{self.__class__.__name__}({list(self)})"
    
    def __bool__(self) -> bool:
        """
        Return True if the list is not empty, False otherwise.
        
        Returns:
            True if the list is not empty, False otherwise
            
        Time Complexity: O(1)
        """
        return self._head is not None
    
    def is_empty(self) -> bool:
        """
        Check if the list is empty.
        
        Returns:
            True if the list is empty, False otherwise
            
        Time Complexity: O(1)
        """
        return self._head is None
    
    @property
    def head_value(self) -> Optional[T]:
        """
        Get the value at the head of the list.
        
        Returns:
            The value at the head, or None if the list is empty
            
        Time Complexity: O(1)
        """
        return self._head.data if self._head else None
    
    def prepend(self, value: T) -> None:
        """
        Add a new element to the beginning of the list.
        
        Args:
            value: The value to add
            
        Time Complexity: O(1)
        """
        self._head = Node(value, self._head)
        self._size += 1
    
    def append(self, value: T) -> None:
        """
        Add a new element to the end of the list.
        
        Args:
            value: The value to add
            
        Time Complexity: O(n)
        """
        new_node = Node(value)
        
        if self.is_empty():
            self._head = new_node
        else:
            # Traverse to the end of the list
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        
        self._size += 1
    
    def insert_at(self, position: int, value: T) -> None:
        """
        Insert a new element at the specified position.
        
        Args:
            position: The position to insert at (0 <= position <= len(list))
            value: The value to insert
            
        Raises:
            IndexError: If the position is invalid
            
        Time Complexity: O(n) in worst case, O(1) if inserting at the head
        """
        # Validate position
        if position < 0 or position > self._size:
            raise IndexError(f"Position {position} out of range [0, {self._size}]")
        
        # Insert at the head if position is 0
        if position == 0:
            self.prepend(value)
            return
        
        # Insert in the middle or at the end
        current = self._head
        for i in range(position - 1):
            current = current.next  # type: ignore
        
        new_node = Node(value, current.next)  # type: ignore
        current.next = new_node  # type: ignore
        self._size += 1
    
    def get(self, position: int) -> T:
        """
        Get the element at the specified position.
        
        Args:
            position: The position of the element (0 <= position < len(list))
            
        Returns:
            The value at the specified position
            
        Raises:
            IndexError: If the position is invalid
            
        Time Complexity: O(n)
        """
        if self.is_empty():
            raise IndexError("Cannot get element from an empty list")
        
        if position < 0 or position >= self._size:
            raise IndexError(f"Position {position} out of range [0, {self._size - 1}]")
        
        current = self._head
        for i in range(position):
            current = current.next  # type: ignore
        
        return current.data  # type: ignore
    
    def remove_head(self) -> T:
        """
        Remove and return the first element.
        
        Returns:
            The value at the head
            
        Raises:
            IndexError: If the list is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list")
        
        value = self._head.data  # type: ignore
        self._head = self._head.next  # type: ignore
        self._size -= 1
        
        return value
    
    def remove(self, position: int) -> T:
        """
        Remove and return the element at the specified position.
        
        Args:
            position: The position of the element to remove (0 <= position < len(list))
            
        Returns:
            The removed value
            
        Raises:
            IndexError: If the position is invalid or the list is empty
            
        Time Complexity: O(n)
        """
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list")
        
        if position < 0 or position >= self._size:
            raise IndexError(f"Position {position} out of range [0, {self._size - 1}]")
        
        if position == 0:
            return self.remove_head()
        
        # Find the node before the one to be removed
        current = self._head
        for i in range(position - 1):
            current = current.next  # type: ignore
        
        # Update pointers to remove the node and update size
        value = current.next.data  # type: ignore
        current.next = current.next.next  # type: ignore
        self._size -= 1
        
        return value
    
    def search(self, value: T) -> int:
        """
        Search for a value in the list.
        
        Args:
            value: The value to search for
            
        Returns:
            The position of the first occurrence, or -1 if not found
            
        Time Complexity: O(n)
        """
        current = self._head
        position = 0
        
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def contains(self, value: T) -> bool:
        """
        Check if the list contains a value.
        
        Args:
            value: The value to check for
            
        Returns:
            True if the value is in the list, False otherwise
            
        Time Complexity: O(n)
        """
        return self.search(value) != -1
    
    def clear(self) -> None:
        """
        Remove all elements from the list.
        
        Time Complexity: O(1)
        """
        self._head = None
        self._size = 0
    
    def copy(self) -> 'SinglyLinkedList[T]':
        """
        Create a shallow copy of the list.
        
        Returns:
            A new SinglyLinkedList with the same elements
            
        Time Complexity: O(n)
        """
        return SinglyLinkedList(list(self))
    
    def reverse(self) -> None:
        """
        Reverse the list in-place.
        
        Time Complexity: O(n)
        """
        if self.is_empty() or self._size == 1:
            return
        
        prev = None
        current = self._head
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        self._head = prev
    
    def to_list(self) -> List[T]:
        """
        Convert the linked list to a Python list.
        
        Returns:
            A list containing all elements in the linked list
            
        Time Complexity: O(n)
        """
        return list(self)



# # Singly linked list data structure implementation in python

# # Node class
# class Node:
#     def __init__(self, data=None): # data is none by default
#         self.data = data
#         self.next = None

    
# # Linkedlist class
# class Linkedlist:

#     def __init__(self):
#         self.head = None  # head is none by default

#     def is_empty(self):  # check if the list is empty
#         return self.head == None
    
#     def addFront(self, data): # add node at the front of the list
#         new_node = Node(data)
#         cur = self.head
#         new_node.next = cur
#         self.head = new_node

#     def front(self):  # return the first node
#         return self.head
    
#     def back(self):  # return the last node
#         cur = self.head
#         while cur.next != None:
#             cur = cur.next
#         return cur
    
#     def removeFront(self):  # remove the first node
#         cur = self.head
#         self.head = cur.next
#         del cur

    

#     def append(self, data):  # add node at the end of the list
#         new_node = Node(data)
#         # if the list is empty
#         if self.head == None:
#             self.head = new_node
#             return
        
#         # if the list is not empty
#         cur = self.head
#         while cur.next != None:
#             cur = cur.next
#         cur.next = new_node

#     def length(self):  # return the length of the list
#         cur = self.head
#         total = 0
#         while cur != None:
#             total = total + 1
#             cur = cur.next
#         print(total)
    
#     def display(self):  # display the list
#         cur = self.head
#         print('head-->', end='')
#         while cur != None:
#             print(str(cur.data) + '->', end='')
#             cur = cur.next

#         print('Null')

#     def getindex(self, data):  # get the index of the node
#         index = 1
#         cur = self.head
#         while cur != None:
#             if cur.data == data:
#                 print(index) 
#             index+= 1
#             cur =cur.next
                
        

# my_list = Linkedlist()


# my_list.display()

