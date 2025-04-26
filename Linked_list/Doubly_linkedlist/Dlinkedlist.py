"""
Doubly Linked List Implementation
This module provides a comprehensive implementation of the Doubly Linked List data structure
with type hints, proper error handling, and Pythonic interfaces.
"""

from typing import TypeVar, Generic, Optional, Iterator, Any, Union, overload, cast


T = TypeVar('T')  # Generic type for the data stored in the linked list


class Node(Generic[T]):
    """
    A node in a doubly linked list.
    
    Each node contains data and references to the next and previous nodes.
    """
    
    def __init__(self, data: T, prev: Optional['Node[T]'] = None, next: Optional['Node[T]'] = None):
        """
        Initialize a new node with the given data and optional prev/next references.
        
        Args:
            data: The data to store in the node.
            prev: Reference to the previous node (default None).
            next: Reference to the next node (default None).
        """
        self.data = data
        self.prev = prev
        self.next = next
    
    def __repr__(self) -> str:
        """
        Return a string representation of the node.
        
        Returns:
            A string in the format "Node(data=<data>)".
        """
        return f"Node(data={self.data})"


class DoublyLinkedList(Generic[T]):
    """
    A doubly linked list implementation.
    
    This class provides a comprehensive implementation of a doubly linked list
    with operations for insertion, deletion, searching, and traversal.
    The list supports bidirectional traversal with both head and tail pointers.
    """
    
    def __init__(self):
        """
        Initialize an empty doubly linked list.
        """
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self._size: int = 0
    
    def append(self, value: T) -> Node[T]:
        """
        Add a new node with the given value to the end of the list.
        
        Args:
            value: The value to append.
            
        Returns:
            The newly created node.
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(value)
        
        if self.head is None:
            # If the list is empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Set the new node's prev to the current tail
            new_node.prev = self.tail
            # Set the current tail's next to the new node
            if self.tail:
                self.tail.next = new_node
            # Update the tail to the new node
            self.tail = new_node
        
        self._size += 1
        return new_node
    
    def prepend(self, value: T) -> Node[T]:
        """
        Add a new node with the given value to the beginning of the list.
        
        Args:
            value: The value to prepend.
            
        Returns:
            The newly created node.
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(value)
        
        if self.head is None:
            # If the list is empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Set the new node's next to the current head
            new_node.next = self.head
            # Set the current head's prev to the new node
            if self.head:
                self.head.prev = new_node
            # Update the head to the new node
            self.head = new_node
        
        self._size += 1
        return new_node
    
    def insert_after(self, node: Node[T], value: T) -> Node[T]:
        """
        Insert a new node with the given value after the specified node.
        
        Args:
            node: The node after which to insert.
            value: The value to insert.
            
        Returns:
            The newly created node.
            
        Raises:
            ValueError: If the node is not in this list.
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Validate that the node belongs to this list
        if not self._validate_node(node):
            raise ValueError("The provided node does not belong to this list")
        
        new_node = Node(value, prev=node, next=node.next)
        
        if node.next:
            node.next.prev = new_node
        else:
            # If we're inserting after the tail, update the tail
            self.tail = new_node
        
        node.next = new_node
        self._size += 1
        return new_node
    
    def insert_before(self, node: Node[T], value: T) -> Node[T]:
        """
        Insert a new node with the given value before the specified node.
        
        Args:
            node: The node before which to insert.
            value: The value to insert.
            
        Returns:
            The newly created node.
            
        Raises:
            ValueError: If the node is not in this list.
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Validate that the node belongs to this list
        if not self._validate_node(node):
            raise ValueError("The provided node does not belong to this list")
        
        new_node = Node(value, prev=node.prev, next=node)
        
        if node.prev:
            node.prev.next = new_node
        else:
            # If we're inserting before the head, update the head
            self.head = new_node
        
        node.prev = new_node
        self._size += 1
        return new_node
    
    def insert_at(self, index: int, value: T) -> Node[T]:
        """
        Insert a new node with the given value at the specified index.
        
        Args:
            index: The index at which to insert (0 <= index <= len).
            value: The value to insert.
            
        Returns:
            The newly created node.
            
        Raises:
            IndexError: If the index is out of range.
            
        Time Complexity: 
            Best Case: O(1) for index 0 or len
            Average Case: O(n/2) as we approach from the nearest end
            Worst Case: O(n) for middle index in a long list
            
        Space Complexity: O(1)
        """
        # Handle special cases for efficiency
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")
        
        if index == 0:
            return self.prepend(value)
        elif index == len(self):
            return self.append(value)
        
        # Decide whether to traverse from head or tail based on which is closer
        if index <= len(self) // 2:
            # Traverse from head
            current = self.head
            for i in range(index):
                if current:
                    current = current.next
                else:
                    break
            
            if current:
                return self.insert_before(current, value)
        else:
            # Traverse from tail
            current = self.tail
            for i in range(len(self) - 1, index - 1, -1):
                if current:
                    current = current.prev
                else:
                    break
            
            if current and current.next:
                return self.insert_after(current, value)
        
        # This should never happen if index validation is correct
        raise RuntimeError("Unexpected error in insert_at")
    
    def remove(self, node: Node[T]) -> T:
        """
        Remove the specified node from the list.
        
        Args:
            node: The node to remove.
            
        Returns:
            The data stored in the removed node.
            
        Raises:
            ValueError: If the node is not in this list.
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Validate that the node belongs to this list
        if not self._validate_node(node):
            raise ValueError("The provided node does not belong to this list")
        
        # Update the previous node's next pointer
        if node.prev:
            node.prev.next = node.next
        else:
            # If removing the head, update the head
            self.head = node.next
        
        # Update the next node's prev pointer
        if node.next:
            node.next.prev = node.prev
        else:
            # If removing the tail, update the tail
            self.tail = node.prev
        
        # Clear the node's pointers to help with garbage collection
        data = node.data
        node.prev = None
        node.next = None
        
        self._size -= 1
        return data
    
    def remove_first(self) -> T:
        """
        Remove the first node from the list.
        
        Returns:
            The data stored in the removed node.
            
        Raises:
            ValueError: If the list is empty.
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.head is None:
            raise ValueError("Cannot remove from an empty list")
        
        return self.remove(self.head)
    
    def remove_last(self) -> T:
        """
        Remove the last node from the list.
        
        Returns:
            The data stored in the removed node.
            
        Raises:
            ValueError: If the list is empty.
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.tail is None:
            raise ValueError("Cannot remove from an empty list")
        
        return self.remove(self.tail)
    
    def remove_at(self, index: int) -> T:
        """
        Remove the node at the specified index.
        
        Args:
            index: The index of the node to remove (0 <= index < len).
            
        Returns:
            The data stored in the removed node.
            
        Raises:
            IndexError: If the index is out of range.
            
        Time Complexity: 
            Best Case: O(1) for index 0 or len-1
            Average Case: O(n/2) as we approach from the nearest end
            Worst Case: O(n) for middle index in a long list
            
        Space Complexity: O(1)
        """
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        
        # Handle special cases for efficiency
        if index == 0:
            return self.remove_first()
        elif index == len(self) - 1:
            return self.remove_last()
        
        # Get the node at the specified index
        node = self.get_at(index)
        return self.remove(node)
    
    def get_at(self, index: int) -> Node[T]:
        """
        Get the node at the specified index.
        
        Args:
            index: The index of the node to get (0 <= index < len).
            
        Returns:
            The node at the specified index.
            
        Raises:
            IndexError: If the index is out of range.
            
        Time Complexity: 
            Best Case: O(1) for index 0 or len-1
            Average Case: O(n/2) as we approach from the nearest end
            Worst Case: O(n) for middle index in a long list
            
        Space Complexity: O(1)
        """
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        
        # Decide whether to traverse from head or tail based on which is closer
        if index <= len(self) // 2:
            # Traverse from head
            current = self.head
            for i in range(index):
                if current:
                    current = current.next
                else:
                    break
        else:
            # Traverse from tail
            current = self.tail
            for i in range(len(self) - 1, index, -1):
                if current:
                    current = current.prev
                else:
                    break
        
        if current is None:
            raise IndexError("Index out of range")
        
        return current
    
    def find(self, value: T) -> Optional[Node[T]]:
        """
        Find the first node containing the specified value.
        
        Args:
            value: The value to search for.
            
        Returns:
            The first node containing the value, or None if not found.
            
        Time Complexity: 
            Best Case: O(1) if found at the beginning
            Average Case: O(n/2)
            Worst Case: O(n) if at end or not found
            
        Space Complexity: O(1)
        """
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        
        return None
    
    def clear(self) -> None:
        """
        Remove all nodes from the list.
        
        Time Complexity: O(1) for the operation itself, 
                         though garbage collection may take O(n)
        Space Complexity: O(1)
        """
        # Help garbage collection by breaking links
        current = self.head
        while current:
            next_node = current.next
            current.prev = None
            current.next = None
            current = next_node
        
        self.head = None
        self.tail = None
        self._size = 0
    
    def _validate_node(self, node: Node[T]) -> bool:
        """
        Validate that a node belongs to this list.
        
        This is a simplified validation that checks if the node
        is reachable from the head of the list.
        
        Args:
            node: The node to validate.
            
        Returns:
            True if the node is in the list, False otherwise.
        
        Time Complexity: O(n) in worst case
        Space Complexity: O(1)
        """
        # For empty lists, no node is valid
        if self.head is None:
            return False
        
        # Quick check for head and tail
        if node is self.head or node is self.tail:
            return True
        
        # Check if the node is reachable from the head
        current = self.head
        while current:
            if current is node:
                return True
            current = current.next
        
        return False
    
    def reverse(self) -> None:
        """
        Reverse the order of nodes in the list.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.head is None or self.head is self.tail:
            # Empty list or single element, nothing to reverse
            return
        
        current = self.head
        # Swap head and tail
        self.head, self.tail = self.tail, self.head
        
        while current:
            # Swap the next and prev pointers
            current.next, current.prev = current.prev, current.next
            # Move to the next node (which is now current.prev due to swap)
            current = current.prev
    
    @overload
    def __getitem__(self, index: int) -> T: ...
    
    @overload
    def __getitem__(self, index: slice) -> 'DoublyLinkedList[T]': ...
    
    def __getitem__(self, index: Union[int, slice]) -> Union[T, 'DoublyLinkedList[T]']:
        """
        Get the value at the specified index, or a slice of the list.
        
        Args:
            index: The index or slice of the list to get.
            
        Returns:
            The value at the index, or a new list containing the sliced elements.
            
        Raises:
            IndexError: If the index is out of range.
            
        Time Complexity: 
            Index access: Same as get_at
            Slice: O(k) where k is the size of the slice
            
        Space Complexity: 
            Index access: O(1)
            Slice: O(k) where k is the size of the slice
        """
        if isinstance(index, int):
            # Handle negative indices
            if index < 0:
                index += len(self)
            
            node = self.get_at(index)
            return node.data
        elif isinstance(index, slice):
            # Handle slice
            start, stop, step = index.indices(len(self))
            result = DoublyLinkedList[T]()
            
            # Get the node at the start position
            if start < len(self):
                current = self.get_at(start)
            else:
                current = None
            
            # Traverse in the appropriate direction based on step
            idx = start
            while current and idx < stop:
                result.append(current.data)
                
                # Skip nodes according to step
                for _ in range(step):
                    if current:
                        current = current.next
                        idx += 1
                    else:
                        break
            
            return result
        else:
            raise TypeError("Indices must be integers or slices")
    
    def __setitem__(self, index: int, value: T) -> None:
        """
        Set the value at the specified index.
        
        Args:
            index: The index to set (0 <= index < len).
            value: The value to set.
            
        Raises:
            IndexError: If the index is out of range.
            
        Time Complexity: Same as get_at
        Space Complexity: O(1)
        """
        # Handle negative indices
        if index < 0:
            index += len(self)
        
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        
        node = self.get_at(index)
        node.data = value
    
    def __iter__(self) -> Iterator[T]:
        """
        Return an iterator over the values in the list.
        
        Returns:
            An iterator yielding the values in the list.
            
        Time Complexity: O(1) for initialization, O(n) for full traversal
        Space Complexity: O(1)
        """
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __contains__(self, value: T) -> bool:
        """
        Check if the list contains the specified value.
        
        Args:
            value: The value to check for.
            
        Returns:
            True if the value is in the list, False otherwise.
            
        Time Complexity: Same as find
        Space Complexity: O(1)
        """
        return self.find(value) is not None
    
    def __len__(self) -> int:
        """
        Return the number of nodes in the list.
        
        Returns:
            The number of nodes.
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._size
    
    def __str__(self) -> str:
        """
        Return a string representation of the list.
        
        Returns:
            A string in the format "[value1, value2, ...]".
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if self.head is None:
            return "[]"
        
        values = [str(val) for val in self]
        return f"[{', '.join(values)}]"
    
    def __repr__(self) -> str:
        """
        Return a detailed string representation of the list.
        
        Returns:
            A string in the format "DoublyLinkedList([value1, value2, ...])".
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return f"DoublyLinkedList({str(self)})"
