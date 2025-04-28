"""
Array-based Stack implementation in Python.

This module provides a generic stack data structure implementation
using a Python list (dynamic array) as the underlying storage.
"""

from typing import TypeVar, Generic, List, Iterator, Optional

T = TypeVar('T')

class EmptyStackError(Exception):
    """Exception raised when attempting to access elements from an empty stack."""
    pass

class ArrayStack(Generic[T]):
    """
    An array-based implementation of the Stack abstract data type.
    
    A stack is a collection that follows the Last-In-First-Out (LIFO) principle,
    meaning the last element added is the first one to be removed.
    
    This implementation uses a Python list as the underlying storage mechanism
    and supports all standard stack operations with appropriate error handling.
    
    Type parameters:
        T: The type of elements stored in the stack.
    
    Attributes:
        _data (List[T]): Internal list used to store stack elements.
    """
    
    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._data: List[T] = []
    
    def push(self, item: T) -> None:
        """
        Add an element to the top of the stack.
        
        Args:
            item: The element to add to the stack.
            
        Time complexity: O(1) amortized
        Space complexity: O(1)
        """
        self._data.append(item)
    
    def pop(self) -> T:
        """
        Remove and return the element at the top of the stack.
        
        Returns:
            The element at the top of the stack.
            
        Raises:
            EmptyStackError: If the stack is empty.
            
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.is_empty():
            raise EmptyStackError("Cannot pop from an empty stack")
        return self._data.pop()
    
    def peek(self) -> T:
        """
        Return the element at the top of the stack without removing it.
        
        Returns:
            The element at the top of the stack.
            
        Raises:
            EmptyStackError: If the stack is empty.
            
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.is_empty():
            raise EmptyStackError("Cannot peek at an empty stack")
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        
        Returns:
            True if the stack contains no elements, False otherwise.
            
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return len(self._data) == 0
    
    def size(self) -> int:
        """
        Return the number of elements in the stack.
        
        Returns:
            The number of elements in the stack.
            
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return len(self._data)
    
    def clear(self) -> None:
        """
        Remove all elements from the stack.
        
        Time complexity: O(1)
        Space complexity: O(1)
        """
        self._data.clear()
    
    def __len__(self) -> int:
        """
        Return the number of elements in the stack.
        
        This method enables the use of the built-in len() function.
        
        Returns:
            The number of elements in the stack.
            
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.size()
    
    def __str__(self) -> str:
        """
        Return a string representation of the stack.
        
        Returns:
            A string representation showing the stack contents from top to bottom.
            
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if self.is_empty():
            return "Stack: []"
        
        items = [str(item) for item in reversed(self._data)]
        return "Stack: [" + " (top), ".join(items) + " (bottom)]"
    
    def __repr__(self) -> str:
        """
        Return a detailed string representation of the stack.
        
        Returns:
            A string representation that could be used to recreate the stack.
            
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if self.is_empty():
            return f"{self.__class__.__name__}[]"
        
        items = [repr(item) for item in self._data]
        return f"{self.__class__.__name__}[{', '.join(items)}]"
    
    def __iter__(self) -> Iterator[T]:
        """
        Return an iterator over the stack elements from top to bottom.
        
        Returns:
            An iterator over stack elements.
            
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return reversed(self._data)
    
    def __contains__(self, item: T) -> bool:
        """
        Check if an item is in the stack.
        
        Args:
            item: The item to check for.
            
        Returns:
            True if the item is in the stack, False otherwise.
            
        Time complexity: O(n)
        Space complexity: O(1)
        """
        return item in self._data