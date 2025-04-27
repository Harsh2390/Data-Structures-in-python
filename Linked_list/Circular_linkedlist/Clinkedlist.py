# Circular Linked List Implementation in Python

from typing import TypeVar, Generic, Optional, List, Any, Iterator, Generator

T = TypeVar('T')  # Type variable for generic typing


class Node(Generic[T]):
    """
    A node in a circular linked list.
    
    Each node contains a value and a reference to the next node in the list.
    """
    
    def __init__(self, value: T) -> None:
        """
        Initialize a new node with the given value.
        
        Args:
            value: The value to store in the node
        """
        self.value: T = value
        self.next: Optional['Node[T]'] = None


class CircularLinkedList(Generic[T]):
    """
    A singly circular linked list implementation.
    
    This class provides a complete implementation of a circular linked list with
    methods for adding, removing, and accessing elements, as well as support for
    iteration and standard Python operations.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty circular linked list.
        """
        self._tail: Optional[Node[T]] = None  # Reference to the last node
        self._size: int = 0  # Number of nodes in the list
        self._iter_node: Optional[Node[T]] = None  # For iteration support
        self._iter_count: int = 0  # For counting iterations
    
    def append(self, value: T) -> None:
        """
        Add a new node with the given value to the end of the list.
        
        Args:
            value: The value to add to the list
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(value)
        
        # If the list is empty
        if self._tail is None:
            new_node.next = new_node  # Point to itself
            self._tail = new_node
        else:
            # Insert after tail and update tail
            new_node.next = self._tail.next  # New node points to head
            self._tail.next = new_node  # Tail points to new node
            self._tail = new_node  # Update tail to be the new node
        
        self._size += 1
    
    def prepend(self, value: T) -> None:
        """
        Add a new node with the given value to the beginning of the list.
        
        Args:
            value: The value to add to the list
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(value)
        
        # If the list is empty
        if self._tail is None:
            new_node.next = new_node  # Point to itself
            self._tail = new_node
        else:
            # Insert at the beginning
            new_node.next = self._tail.next  # New node points to head
            self._tail.next = new_node  # Tail points to new node
        
        self._size += 1
    
    def insert_after(self, target_value: T, value: T) -> bool:
        """
        Insert a new node with the given value after the first occurrence of the target value.
        
        Args:
            target_value: The value to search for
            value: The value to insert
            
        Returns:
            True if the insertion was successful, False if the target value was not found
            
        Time Complexity: O(n) - where n is the number of nodes in the list
        Space Complexity: O(1)
        """
        if self.is_empty():
            return False
        
        current = self._tail.next  # Start at the head
        
        # Traverse the list
        while True:
            if current.value == target_value:
                # Insert new node after current
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                
                # Update tail if needed
                if current == self._tail:
                    self._tail = new_node
                
                self._size += 1
                return True
            
            current = current.next
            # If we've completed a full traversal
            if current == self._tail.next:
                break
        
        return False  # Target value not found
    
    def insert_at(self, index: int, value: T) -> None:
        """
        Insert a new node with the given value at the specified index.
        
        Args:
            index: The index at which to insert the value (0-based)
            value: The value to insert
            
        Raises:
            IndexError: If the index is out of range
            
        Time Complexity: O(n) - where n is the number of nodes in the list
        Space Complexity: O(1)
        """
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        
        # Special cases
        if index == 0:
            self.prepend(value)
            return
        
        if index == self._size:
            self.append(value)
            return
        
        # General case
        current = self._tail.next  # Start at the head
        for _ in range(index - 1):
            current = current.next
        
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        
        self._size += 1
    
    def remove(self, value: T) -> bool:
        """
        Remove the first occurrence of the specified value from the list.
        
        Args:
            value: The value to remove
            
        Returns:
            True if the value was found and removed, False otherwise
            
        Time Complexity: O(n) - where n is the number of nodes in the list
        Space Complexity: O(1)
        """
        if self.is_empty():
            return False
        
        current = self._tail.next  # Start at the head
        prev = self._tail  # Start prev at the tail
        
        # Traverse the list
        while True:
            if current.value == value:
                # Remove the node
                prev.next = current.next
                
                # Update tail if needed
                if current == self._tail:
                    if self._size == 1:
                        self._tail = None  # List becomes empty
                    else:
                        self._tail = prev  # Update tail to previous node
                
                self._size -= 1
                return True
            
            prev = current
            current = current.next
            
            # If we've completed a full traversal
            if current == self._tail.next:
                break
        
        return False  # Value not found
    
    def remove_at(self, index: int) -> T:
        """
        Remove and return the node at the specified index.
        
        Args:
            index: The index of the node to remove (0-based)
            
        Returns:
            The value of the removed node
            
        Raises:
            IndexError: If the index is out of range or the list is empty
            
        Time Complexity: O(n) - where n is the number of nodes in the list
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list")
        
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        # Special case: removing the only node
        if self._size == 1:
            value = self._tail.value
            self._tail = None
            self._size = 0
            return value
        
        # Special case: removing the head
        if index == 0:
            head = self._tail.next
            value = head.value
            self._tail.next = head.next
            self._size -= 1
            return value
        
        # General case
        current = self._tail.next  # Start at the head
        prev = self._tail  # Start prev at the tail
        
        for _ in range(index):
            prev = current
            current = current.next
        
        value = current.value
        prev.next = current.next
        
        # Update tail if removing the last node
        if current == self._tail:
            self._tail = prev
        
        self._size -= 1
        return value
    
    def find(self, value: T) -> Optional[int]:
        """
        Find the index of the first occurrence of the specified value.
        
        Args:
            value: The value to search for
            
        Returns:
            The index of the value if found, None otherwise
            
        Time Complexity: O(n) - where n is the number of nodes in the list
        Space Complexity: O(1)
        """
        if self.is_empty():
            return None
        
        current = self._tail.next  # Start at the head
        index = 0
        
        # Traverse the list
        while True:
            if current.value == value:
                return index
            
            current = current.next
            index += 1
            
            # If we've completed a full traversal
            if current == self._tail.next:
                break
        
        return None  # Value not found
    
    def get_at(self, index: int) -> T:
        """
        Get the value at the specified index.
        
        Args:
            index: The index of the value to get (0-based)
            
        Returns:
            The value at the specified index
            
        Raises:
            IndexError: If the index is out of range or the list is empty
            
        Time Complexity: O(n) - where n is the number of nodes in the list
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot get from an empty list")
        
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        current = self._tail.next  # Start at the head
        
        for _ in range(index):
            current = current.next
        
        return current.value
    
    def clear(self) -> None:
        """
        Remove all nodes from the list.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._tail = None
        self._size = 0
        self._iter_node = None
        self._iter_count = 0
    
    def is_empty(self) -> bool:
        """
        Check if the list is empty.
        
        Returns:
            True if the list is empty, False otherwise
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._size == 0
    
    def size(self) -> int:
        """
        Get the number of nodes in the list.
        
        Returns:
            The number of nodes in the list
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._size
    
    def to_list(self) -> List[T]:
        """
        Convert the circular linked list to a Python list.
        
        Returns:
            A list containing all values in the circular linked list
            
        Time Complexity: O(n) - where n is the number of nodes in the list
        Space Complexity: O(n)
        """
        result = []
        
        if self.is_empty():
            return result
        
        current = self._tail.next  # Start at the head
        
        # Traverse the list
        while True:
            result.append(current.value)
            current = current.next
            
            # If we've completed a full traversal
            if current == self._tail.next:
                break
        
        return result
    
    @classmethod
    def from_list(cls, values: List[T]) -> 'CircularLinkedList[T]':
        """
        Create a new circular linked list from a Python list.
        
        Args:
            values: A list of values to add to the circular linked list
            
        Returns:
            A new circular linked list containing the specified values
            
        Time Complexity: O(n) - where n is the number of values in the list
        Space Complexity: O(n)
        """
        circular_list = cls()
        
        for value in values:
            circular_list.append(value)
        
        return circular_list
    
    def rotate(self, k: int) -> None:
        """
        Rotate the list by k positions.
        
        Positive values rotate clockwise (the kth element becomes the first),
        negative values rotate counterclockwise (the kth-from-last element becomes the first).
        
        Args:
            k: The number of positions to rotate
            
        Time Complexity: O(n) - where n is the number of nodes in the list
        Space Complexity: O(1)
        """
        if self.is_empty() or k % self._size == 0:
            return  # No rotation needed
        
        # Normalize k to be within the range [0, size-1]
        k = k % self._size
        
        if k < 0:
            k = self._size + k
        
        # Rotate by moving the tail pointer
        for _ in range(k):
            self._tail = self._tail.next
    
    def __iter__(self) -> 'CircularLinkedList[T]':
        """
        Get an iterator for the circular linked list.
        
        Returns:
            The circular linked list as an iterator
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._iter_node = None if self.is_empty() else self._tail.next
        self._iter_count = 0
        return self
    
    def __next__(self) -> T:
        """
        Get the next value in the iteration.
        
        Returns:
            The next value in the iteration
            
        Raises:
            StopIteration: If the iteration is complete
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self._iter_node is None or self._iter_count >= self._size:
            raise StopIteration
        
        value = self._iter_node.value
        self._iter_node = self._iter_node.next
        self._iter_count += 1
        
        return value
    
    def __len__(self) -> int:
        """
        Get the number of nodes in the list.
        
        Returns:
            The number of nodes in the list
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._size
    
    def __contains__(self, value: T) -> bool:
        """
        Check if the list contains the specified value.
        
        Args:
            value: The value to check for
            
        Returns:
            True if the value is in the list, False otherwise
            
        Time Complexity: O(n) - where n is the number of nodes in the list
        Space Complexity: O(1)
        """
        return self.find(value) is not None
    
    def __str__(self) -> str:
        """
        Get a string representation of the circular linked list.
        
        Returns:
            A string representation of the list
            
        Time Complexity: O(n) - where n is the number of nodes in the list
        Space Complexity: O(n)
        """
        return f"CircularLinkedList({self.to_list()})"
    
    def __repr__(self) -> str:
        """
        Get the official string representation of the circular linked list.
        
        Returns:
            The official string representation of the list
            
        Time Complexity: O(n) - where n is the number of nodes in the list
        Space Complexity: O(n)
        """
        return self.__str__()
