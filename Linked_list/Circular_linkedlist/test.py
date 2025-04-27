"""
Unit tests for the CircularLinkedList class.
"""

import unittest
from Clinkedlist import CircularLinkedList


class TestCircularLinkedList(unittest.TestCase):
    """
    Test cases for the CircularLinkedList class.
    """
    
    def setUp(self):
        """
        Set up a new CircularLinkedList before each test.
        """
        self.cll = CircularLinkedList()
    
    def test_empty_list(self):
        """
        Test operations on an empty list.
        """
        self.assertTrue(self.cll.is_empty())
        self.assertEqual(len(self.cll), 0)
        self.assertEqual(str(self.cll), "CircularLinkedList([])")
        self.assertEqual(self.cll.to_list(), [])
        self.assertIsNone(self.cll.find(5))
        self.assertFalse(5 in self.cll)
        
        with self.assertRaises(IndexError):
            self.cll.get_at(0)
        
        with self.assertRaises(IndexError):
            self.cll.remove_at(0)
    
    def test_append(self):
        """
        Test appending elements to the list.
        """
        self.cll.append(1)
        self.assertEqual(len(self.cll), 1)
        self.assertEqual(self.cll.to_list(), [1])
        
        self.cll.append(2)
        self.assertEqual(len(self.cll), 2)
        self.assertEqual(self.cll.to_list(), [1, 2])
        
        self.cll.append(3)
        self.assertEqual(len(self.cll), 3)
        self.assertEqual(self.cll.to_list(), [1, 2, 3])
    
    def test_prepend(self):
        """
        Test prepending elements to the list.
        """
        self.cll.prepend(1)
        self.assertEqual(len(self.cll), 1)
        self.assertEqual(self.cll.to_list(), [1])
        
        self.cll.prepend(2)
        self.assertEqual(len(self.cll), 2)
        self.assertEqual(self.cll.to_list(), [2, 1])
        
        self.cll.prepend(3)
        self.assertEqual(len(self.cll), 3)
        self.assertEqual(self.cll.to_list(), [3, 2, 1])
    
    def test_insert_after(self):
        """
        Test inserting elements after a target value.
        """
        # Insert after in empty list should fail
        self.assertFalse(self.cll.insert_after(1, 2))
        
        # Insert after in a list with one element
        self.cll.append(1)
        self.assertTrue(self.cll.insert_after(1, 2))
        self.assertEqual(self.cll.to_list(), [1, 2])
        
        # Insert after in a list with multiple elements
        self.cll.append(3)
        self.assertTrue(self.cll.insert_after(2, 2.5))
        self.assertEqual(self.cll.to_list(), [1, 2, 2.5, 3])
        
        # Insert after the last element
        self.assertTrue(self.cll.insert_after(3, 4))
        self.assertEqual(self.cll.to_list(), [1, 2, 2.5, 3, 4])
        
        # Insert after a non-existing value
        self.assertFalse(self.cll.insert_after(10, 11))
        self.assertEqual(self.cll.to_list(), [1, 2, 2.5, 3, 4])
    
    def test_insert_at(self):
        """
        Test inserting elements at a specific index.
        """
        # Insert at invalid indices
        with self.assertRaises(IndexError):
            self.cll.insert_at(-1, 0)
        
        with self.assertRaises(IndexError):
            self.cll.insert_at(1, 0)
        
        # Insert at the beginning of an empty list
        self.cll.insert_at(0, 1)
        self.assertEqual(self.cll.to_list(), [1])
        
        # Insert at the end
        self.cll.insert_at(1, 3)
        self.assertEqual(self.cll.to_list(), [1, 3])
        
        # Insert in the middle
        self.cll.insert_at(1, 2)
        self.assertEqual(self.cll.to_list(), [1, 2, 3])
    
    def test_remove(self):
        """
        Test removing elements by value.
        """
        # Remove from empty list
        self.assertFalse(self.cll.remove(1))
        
        # Remove from a list with one element
        self.cll.append(1)
        self.assertTrue(self.cll.remove(1))
        self.assertTrue(self.cll.is_empty())
        
        # Remove from a list with multiple elements
        self.cll.append(1)
        self.cll.append(2)
        self.cll.append(3)
        self.assertTrue(self.cll.remove(2))
        self.assertEqual(self.cll.to_list(), [1, 3])
        
        # Remove the last element
        self.assertTrue(self.cll.remove(3))
        self.assertEqual(self.cll.to_list(), [1])
        
        # Remove the first element
        self.assertTrue(self.cll.remove(1))
        self.assertTrue(self.cll.is_empty())
        
        # Remove a non-existing value
        self.cll.append(1)
        self.assertFalse(self.cll.remove(2))
        self.assertEqual(self.cll.to_list(), [1])
    
    def test_remove_at(self):
        """
        Test removing elements at a specific index.
        """
        # Remove from empty list
        with self.assertRaises(IndexError):
            self.cll.remove_at(0)
        
        # Remove at invalid indices
        self.cll.append(1)
        with self.assertRaises(IndexError):
            self.cll.remove_at(-1)
        
        with self.assertRaises(IndexError):
            self.cll.remove_at(1)
        
        # Remove the only element
        self.assertEqual(self.cll.remove_at(0), 1)
        self.assertTrue(self.cll.is_empty())
        
        # Remove from a list with multiple elements
        self.cll.append(1)
        self.cll.append(2)
        self.cll.append(3)
        
        # Remove the first element
        self.assertEqual(self.cll.remove_at(0), 1)
        self.assertEqual(self.cll.to_list(), [2, 3])
        
        # Remove the last element
        self.assertEqual(self.cll.remove_at(1), 3)
        self.assertEqual(self.cll.to_list(), [2])
    
    def test_find(self):
        """
        Test finding elements by value.
        """
        # Find in empty list
        self.assertIsNone(self.cll.find(1))
        
        # Find in a list with one element
        self.cll.append(1)
        self.assertEqual(self.cll.find(1), 0)
        self.assertIsNone(self.cll.find(2))
        
        # Find in a list with multiple elements
        self.cll.append(2)
        self.cll.append(3)
        self.assertEqual(self.cll.find(1), 0)
        self.assertEqual(self.cll.find(2), 1)
        self.assertEqual(self.cll.find(3), 2)
        self.assertIsNone(self.cll.find(4))
    
    def test_get_at(self):
        """
        Test getting elements at a specific index.
        """
        # Get from empty list
        with self.assertRaises(IndexError):
            self.cll.get_at(0)
        
        # Get at invalid indices
        self.cll.append(1)
        with self.assertRaises(IndexError):
            self.cll.get_at(-1)
        
        with self.assertRaises(IndexError):
            self.cll.get_at(1)
        
        # Get from a list with one element
        self.assertEqual(self.cll.get_at(0), 1)
        
        # Get from a list with multiple elements
        self.cll.append(2)
        self.cll.append(3)
        self.assertEqual(self.cll.get_at(0), 1)
        self.assertEqual(self.cll.get_at(1), 2)
        self.assertEqual(self.cll.get_at(2), 3)
    
    def test_clear(self):
        """
        Test clearing the list.
        """
        self.cll.clear()  # Clear empty list
        self.assertTrue(self.cll.is_empty())
        
        self.cll.append(1)
        self.cll.append(2)
        self.cll.clear()
        self.assertTrue(self.cll.is_empty())
        self.assertEqual(len(self.cll), 0)
        self.assertEqual(self.cll.to_list(), [])
    
    def test_from_list(self):
        """
        Test creating a circular linked list from a Python list.
        """
        empty_list = CircularLinkedList.from_list([])
        self.assertTrue(empty_list.is_empty())
        
        single_element_list = CircularLinkedList.from_list([1])
        self.assertEqual(single_element_list.to_list(), [1])
        
        multiple_element_list = CircularLinkedList.from_list([1, 2, 3])
        self.assertEqual(multiple_element_list.to_list(), [1, 2, 3])
    
    def test_rotate(self):
        """
        Test rotating the list.
        """
        # Rotate empty list
        self.cll.rotate(1)  # Should not raise an error
        self.assertTrue(self.cll.is_empty())
        
        # Rotate list with one element
        self.cll.append(1)
        self.cll.rotate(1)
        self.assertEqual(self.cll.to_list(), [1])
        
        # Rotate list with multiple elements
        self.cll.append(2)
        self.cll.append(3)
        self.cll.append(4)
        
        # Rotate clockwise
        self.cll.rotate(1)
        self.assertEqual(self.cll.to_list(), [4, 1, 2, 3])
        
        self.cll.rotate(2)
        self.assertEqual(self.cll.to_list(), [2, 3, 4, 1])
        
        # Rotate counterclockwise
        self.cll.rotate(-1)
        self.assertEqual(self.cll.to_list(), [3, 4, 1, 2])
        
        # Rotate by the size of the list (should be a no-op)
        self.cll.rotate(4)
        self.assertEqual(self.cll.to_list(), [3, 4, 1, 2])
        
        # Rotate by more than the size of the list
        self.cll.rotate(5)
        self.assertEqual(self.cll.to_list(), [2, 3, 4, 1])
    
    def test_iteration(self):
        """
        Test iterating through the list.
        """
        # Iterate through empty list
        for _ in self.cll:
            self.fail("Should not iterate through empty list")
        
        # Iterate through list with one element
        self.cll.append(1)
        items = []
        for item in self.cll:
            items.append(item)
        self.assertEqual(items, [1])
        
        # Iterate through list with multiple elements
        self.cll.append(2)
        self.cll.append(3)
        items = []
        for item in self.cll:
            items.append(item)
        self.assertEqual(items, [1, 2, 3])
        
        # Test multiple iterations
        items = []
        for item in self.cll:
            items.append(item)
        self.assertEqual(items, [1, 2, 3])
    
    def test_contains(self):
        """
        Test the __contains__ method.
        """
        # Check empty list
        self.assertFalse(1 in self.cll)
        
        # Check list with one element
        self.cll.append(1)
        self.assertTrue(1 in self.cll)
        self.assertFalse(2 in self.cll)
        
        # Check list with multiple elements
        self.cll.append(2)
        self.cll.append(3)
        self.assertTrue(1 in self.cll)
        self.assertTrue(2 in self.cll)
        self.assertTrue(3 in self.cll)
        self.assertFalse(4 in self.cll)
    
    def test_str_and_repr(self):
        """
        Test the string representation methods.
        """
        self.assertEqual(str(self.cll), "CircularLinkedList([])")
        self.assertEqual(repr(self.cll), "CircularLinkedList([])")
        
        self.cll.append(1)
        self.assertEqual(str(self.cll), "CircularLinkedList([1])")
        self.assertEqual(repr(self.cll), "CircularLinkedList([1])")
        
        self.cll.append(2)
        self.cll.append(3)
        self.assertEqual(str(self.cll), "CircularLinkedList([1, 2, 3])")
        self.assertEqual(repr(self.cll), "CircularLinkedList([1, 2, 3])")


if __name__ == "__main__":
    unittest.main()