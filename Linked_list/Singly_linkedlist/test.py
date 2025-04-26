"""
Unit tests for the SinglyLinkedList implementation.
"""

import unittest
from Slinkedlist import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    """Test cases for the SinglyLinkedList class."""
    
    def test_initialization(self):
        """Test initialization of the list with and without values."""
        # Test empty initialization
        ll = SinglyLinkedList()
        self.assertEqual(len(ll), 0)
        self.assertTrue(ll.is_empty())
        
        # Test initialization with values
        ll = SinglyLinkedList([1, 2, 3])
        self.assertEqual(len(ll), 3)
        self.assertEqual(list(ll), [1, 2, 3])
    
    def test_prepend(self):
        """Test adding elements to the beginning of the list."""
        ll = SinglyLinkedList()
        ll.prepend(1)
        self.assertEqual(ll.head_value, 1)
        self.assertEqual(len(ll), 1)
        
        ll.prepend(2)
        self.assertEqual(ll.head_value, 2)
        self.assertEqual(len(ll), 2)
        self.assertEqual(list(ll), [2, 1])
    
    def test_append(self):
        """Test adding elements to the end of the list."""
        ll = SinglyLinkedList()
        ll.append(1)
        self.assertEqual(ll.head_value, 1)
        self.assertEqual(len(ll), 1)
        
        ll.append(2)
        self.assertEqual(ll.head_value, 1)
        self.assertEqual(len(ll), 2)
        self.assertEqual(list(ll), [1, 2])
    
    def test_insert_at(self):
        """Test inserting elements at specific positions."""
        ll = SinglyLinkedList([1, 3, 4])
        
        # Insert at the beginning
        ll.insert_at(0, 0)
        self.assertEqual(list(ll), [0, 1, 3, 4])
        
        # Insert in the middle
        ll.insert_at(2, 2)
        self.assertEqual(list(ll), [0, 1, 2, 3, 4])
        
        # Insert at the end
        ll.insert_at(5, 5)
        self.assertEqual(list(ll), [0, 1, 2, 3, 4, 5])
        
        # Test invalid positions
        with self.assertRaises(IndexError):
            ll.insert_at(-1, 10)
        
        with self.assertRaises(IndexError):
            ll.insert_at(7, 10)
    
    def test_get(self):
        """Test retrieving elements at specific positions."""
        ll = SinglyLinkedList([1, 2, 3, 4, 5])
        
        # Get first element
        self.assertEqual(ll.get(0), 1)
        
        # Get middle element
        self.assertEqual(ll.get(2), 3)
        
        # Get last element
        self.assertEqual(ll.get(4), 5)
        
        # Test invalid positions
        with self.assertRaises(IndexError):
            ll.get(-1)
        
        with self.assertRaises(IndexError):
            ll.get(5)
        
        # Test empty list
        empty_ll = SinglyLinkedList()
        with self.assertRaises(IndexError):
            empty_ll.get(0)
    
    def test_remove_head(self):
        """Test removing the head element."""
        ll = SinglyLinkedList([1, 2, 3])
        
        # Remove head
        self.assertEqual(ll.remove_head(), 1)
        self.assertEqual(len(ll), 2)
        self.assertEqual(list(ll), [2, 3])
        
        # Remove again
        self.assertEqual(ll.remove_head(), 2)
        self.assertEqual(len(ll), 1)
        self.assertEqual(list(ll), [3])
        
        # Remove last element
        self.assertEqual(ll.remove_head(), 3)
        self.assertEqual(len(ll), 0)
        self.assertTrue(ll.is_empty())
        
        # Test empty list
        with self.assertRaises(IndexError):
            ll.remove_head()
    
    def test_remove(self):
        """Test removing elements at specific positions."""
        ll = SinglyLinkedList([1, 2, 3, 4, 5])
        
        # Remove first element
        self.assertEqual(ll.remove(0), 1)
        self.assertEqual(list(ll), [2, 3, 4, 5])
        
        # Remove middle element
        self.assertEqual(ll.remove(1), 3)
        self.assertEqual(list(ll), [2, 4, 5])
        
        # Remove last element
        self.assertEqual(ll.remove(2), 5)
        self.assertEqual(list(ll), [2, 4])
        
        # Test invalid positions
        with self.assertRaises(IndexError):
            ll.remove(-1)
        
        with self.assertRaises(IndexError):
            ll.remove(2)
        
        # Test empty list
        ll.clear()
        with self.assertRaises(IndexError):
            ll.remove(0)
    
    def test_search(self):
        """Test searching for elements in the list."""
        ll = SinglyLinkedList([1, 2, 3, 2, 1])
        
        # Find existing elements
        self.assertEqual(ll.search(1), 0)  # First occurrence
        self.assertEqual(ll.search(2), 1)  # First occurrence
        self.assertEqual(ll.search(3), 2)
        
        # Find non-existing element
        self.assertEqual(ll.search(4), -1)
        
        # Test empty list
        empty_ll = SinglyLinkedList()
        self.assertEqual(empty_ll.search(1), -1)
    
    def test_contains(self):
        """Test checking if an element exists in the list."""
        ll = SinglyLinkedList([1, 2, 3])
        
        # Test existing elements
        self.assertTrue(ll.contains(1))
        self.assertTrue(ll.contains(2))
        self.assertTrue(ll.contains(3))
        
        # Test non-existing element
        self.assertFalse(ll.contains(4))
        
        # Test empty list
        empty_ll = SinglyLinkedList()
        self.assertFalse(empty_ll.contains(1))
    
    def test_clear(self):
        """Test clearing the list."""
        ll = SinglyLinkedList([1, 2, 3])
        ll.clear()
        
        self.assertEqual(len(ll), 0)
        self.assertTrue(ll.is_empty())
        self.assertEqual(list(ll), [])
    
    def test_copy(self):
        """Test creating a copy of the list."""
        ll1 = SinglyLinkedList([1, 2, 3])
        ll2 = ll1.copy()
        
        # Check copied list has same elements
        self.assertEqual(list(ll1), list(ll2))
        
        # Check they are different objects
        self.assertIsNot(ll1, ll2)
        
        # Modifying one should not affect the other
        ll1.append(4)
        self.assertEqual(list(ll1), [1, 2, 3, 4])
        self.assertEqual(list(ll2), [1, 2, 3])
    
    def test_reverse(self):
        """Test reversing the list in-place."""
        # Test with multiple elements
        ll = SinglyLinkedList([1, 2, 3, 4, 5])
        ll.reverse()
        self.assertEqual(list(ll), [5, 4, 3, 2, 1])
        
        # Test with one element
        ll = SinglyLinkedList([1])
        ll.reverse()
        self.assertEqual(list(ll), [1])
        
        # Test with empty list
        ll = SinglyLinkedList()
        ll.reverse()
        self.assertEqual(list(ll), [])
    
    def test_to_list(self):
        """Test converting the linked list to a Python list."""
        # Test with multiple elements
        ll = SinglyLinkedList([1, 2, 3])
        self.assertEqual(ll.to_list(), [1, 2, 3])
        
        # Test with empty list
        ll = SinglyLinkedList()
        self.assertEqual(ll.to_list(), [])
    
    def test_iteration(self):
        """Test iterating over the list."""
        ll = SinglyLinkedList([1, 2, 3])
        
        # Test iterator
        items = []
        for item in ll:
            items.append(item)
        
        self.assertEqual(items, [1, 2, 3])
    
    def test_string_representation(self):
        """Test string representation of the list."""
        ll = SinglyLinkedList([1, 2, 3])
        
        # Test __str__
        self.assertEqual(str(ll), "[1, 2, 3]")
        
        # Test __repr__
        self.assertEqual(repr(ll), "SinglyLinkedList([1, 2, 3])")
        
        # Test empty list
        empty_ll = SinglyLinkedList()
        self.assertEqual(str(empty_ll), "[]")
        self.assertEqual(repr(empty_ll), "SinglyLinkedList([])")
    
    def test_bool(self):
        """Test boolean evaluation of the list."""
        # Test non-empty list
        ll = SinglyLinkedList([1, 2, 3])
        self.assertTrue(bool(ll))
        
        # Test empty list
        empty_ll = SinglyLinkedList()
        self.assertFalse(bool(empty_ll))


if __name__ == '__main__':
    unittest.main()