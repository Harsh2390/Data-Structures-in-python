"""
Unit tests for the DoublyLinkedList implementation.

This module provides comprehensive tests for all functionality of the
DoublyLinkedList class, including edge cases and error conditions.
"""

import unittest
import time
from typing import Any, List, Optional
from Dlinkedlist import DoublyLinkedList, Node


class TestNode(unittest.TestCase):
    """Test cases for the Node class."""
    
    def test_node_initialization(self) -> None:
        """Test initialization of a Node."""
        node = Node[int](5)
        self.assertEqual(node.data, 5)
        self.assertIsNone(node.prev)
        self.assertIsNone(node.next)
        
        # Test with prev and next references
        prev_node = Node[int](3)
        next_node = Node[int](7)
        node = Node[int](5, prev=prev_node, next=next_node)
        self.assertEqual(node.data, 5)
        self.assertEqual(node.prev, prev_node)
        self.assertEqual(node.next, next_node)
    
    def test_node_repr(self) -> None:
        """Test string representation of a Node."""
        node = Node[int](5)
        self.assertEqual(repr(node), "Node(data=5)")


class TestDoublyLinkedList(unittest.TestCase):
    """Test cases for the DoublyLinkedList class."""
    
    def setUp(self) -> None:
        """Set up a fresh DoublyLinkedList for each test."""
        self.empty_list = DoublyLinkedList[int]()
        
        # Create a list with elements [1, 2, 3, 4, 5]
        self.populated_list = DoublyLinkedList[int]()
        for i in range(1, 6):
            self.populated_list.append(i)
    
    def test_initialization(self) -> None:
        """Test initialization of an empty DoublyLinkedList."""
        self.assertIsNone(self.empty_list.head)
        self.assertIsNone(self.empty_list.tail)
        self.assertEqual(len(self.empty_list), 0)
    
    def test_append(self) -> None:
        """Test appending elements to the list."""
        # Append to an empty list
        node1 = self.empty_list.append(10)
        self.assertEqual(self.empty_list.head, node1)
        self.assertEqual(self.empty_list.tail, node1)
        self.assertEqual(len(self.empty_list), 1)
        
        # Append to a non-empty list
        node2 = self.empty_list.append(20)
        self.assertEqual(self.empty_list.head, node1)
        self.assertEqual(self.empty_list.tail, node2)
        self.assertEqual(node1.next, node2)
        self.assertEqual(node2.prev, node1)
        self.assertEqual(len(self.empty_list), 2)
        
        # Verify data
        self.assertEqual(self.empty_list.head.data, 10)
        self.assertEqual(self.empty_list.tail.data, 20)
    
    def test_prepend(self) -> None:
        """Test prepending elements to the list."""
        # Prepend to an empty list
        node1 = self.empty_list.prepend(10)
        self.assertEqual(self.empty_list.head, node1)
        self.assertEqual(self.empty_list.tail, node1)
        self.assertEqual(len(self.empty_list), 1)
        
        # Prepend to a non-empty list
        node2 = self.empty_list.prepend(20)
        self.assertEqual(self.empty_list.head, node2)
        self.assertEqual(self.empty_list.tail, node1)
        self.assertEqual(node2.next, node1)
        self.assertEqual(node1.prev, node2)
        self.assertEqual(len(self.empty_list), 2)
        
        # Verify data
        self.assertEqual(self.empty_list.head.data, 20)
        self.assertEqual(self.empty_list.tail.data, 10)
    
    def test_insert_after(self) -> None:
        """Test inserting elements after a specified node."""
        # Test with a populated list
        node = self.populated_list.head
        self.assertIsNotNone(node)
        
        # Insert after the first node
        new_node = self.populated_list.insert_after(node, 100)
        self.assertEqual(new_node.data, 100)
        self.assertEqual(new_node.prev, node)
        self.assertIsNotNone(node.next)
        self.assertEqual(new_node.next, node.next)
        self.assertEqual(len(self.populated_list), 6)
        
        # Convert to list for easier verification
        expected = [1, 100, 2, 3, 4, 5]
        actual = list(self.populated_list)
        self.assertEqual(actual, expected)
        
        # Test inserting after the last node
        node = self.populated_list.tail
        self.assertIsNotNone(node)
        
        new_node = self.populated_list.insert_after(node, 200)
        self.assertEqual(new_node.data, 200)
        self.assertEqual(new_node.prev, node)
        self.assertIsNone(new_node.next)
        self.assertEqual(self.populated_list.tail, new_node)
        self.assertEqual(len(self.populated_list), 7)
        
        # Convert to list for easier verification
        expected = [1, 100, 2, 3, 4, 5, 200]
        actual = list(self.populated_list)
        self.assertEqual(actual, expected)
        
        # Test with an external node
        external_node = Node[int](999)
        with self.assertRaises(ValueError):
            self.populated_list.insert_after(external_node, 300)
    
    def test_insert_before(self) -> None:
        """Test inserting elements before a specified node."""
        # Test with a populated list
        node = self.populated_list.tail
        self.assertIsNotNone(node)
        
        # Insert before the last node
        new_node = self.populated_list.insert_before(node, 100)
        self.assertEqual(new_node.data, 100)
        self.assertEqual(new_node.next, node)
        self.assertIsNotNone(node.prev)
        self.assertEqual(new_node.prev, node.prev)
        self.assertEqual(len(self.populated_list), 6)
        
        # Convert to list for easier verification
        expected = [1, 2, 3, 4, 100, 5]
        actual = list(self.populated_list)
        self.assertEqual(actual, expected)
        
        # Test inserting before the first node
        node = self.populated_list.head
        self.assertIsNotNone(node)
        
        new_node = self.populated_list.insert_before(node, 200)
        self.assertEqual(new_node.data, 200)
        self.assertEqual(new_node.next, node)
        self.assertIsNone(new_node.prev)
        self.assertEqual(self.populated_list.head, new_node)
        self.assertEqual(len(self.populated_list), 7)
        
        # Convert to list for easier verification
        expected = [200, 1, 2, 3, 4, 100, 5]
        actual = list(self.populated_list)
        self.assertEqual(actual, expected)
        
        # Test with an external node
        external_node = Node[int](999)
        with self.assertRaises(ValueError):
            self.populated_list.insert_before(external_node, 300)
    
    def test_insert_at(self) -> None:
        """Test inserting elements at specific indices."""
        # Insert at index 0 (prepend)
        node = self.populated_list.insert_at(0, 100)
        self.assertEqual(node.data, 100)
        self.assertEqual(self.populated_list.head, node)
        self.assertEqual(len(self.populated_list), 6)
        
        # Insert at the end (append)
        end_index = len(self.populated_list)
        node = self.populated_list.insert_at(end_index, 200)
        self.assertEqual(node.data, 200)
        self.assertEqual(self.populated_list.tail, node)
        self.assertEqual(len(self.populated_list), 7)
        
        # Insert in the middle
        node = self.populated_list.insert_at(3, 300)
        self.assertEqual(node.data, 300)
        self.assertEqual(len(self.populated_list), 8)
        
        # Convert to list for easier verification
        expected = [100, 1, 2, 300, 3, 4, 5, 200]
        actual = list(self.populated_list)
        self.assertEqual(actual, expected)
        
        # Test out of range
        with self.assertRaises(IndexError):
            self.populated_list.insert_at(-1, 400)
        
        with self.assertRaises(IndexError):
            self.populated_list.insert_at(len(self.populated_list) + 1, 400)
    
    def test_remove(self) -> None:
        """Test removing a specified node."""
        # Test with a populated list
        node = self.populated_list.head
        self.assertIsNotNone(node)
        
        # Remove the first node
        data = self.populated_list.remove(node)
        self.assertEqual(data, 1)
        self.assertEqual(len(self.populated_list), 4)
        
        # Convert to list for easier verification
        expected = [2, 3, 4, 5]
        actual = list(self.populated_list)
        self.assertEqual(actual, expected)
        
        # Remove the last node
        node = self.populated_list.tail
        self.assertIsNotNone(node)
        
        data = self.populated_list.remove(node)
        self.assertEqual(data, 5)
        self.assertEqual(len(self.populated_list), 3)
        
        # Convert to list for easier verification
        expected = [2, 3, 4]
        actual = list(self.populated_list)
        self.assertEqual(actual, expected)
        
        # Remove a middle node
        node = self.populated_list.head
        self.assertIsNotNone(node)
        self.assertIsNotNone(node.next)
        
        data = self.populated_list.remove(node.next)
        self.assertEqual(data, 3)
        self.assertEqual(len(self.populated_list), 2)
        
        # Convert to list for easier verification
        expected = [2, 4]
        actual = list(self.populated_list)
        self.assertEqual(actual, expected)
        
        # Test with an external node
        external_node = Node[int](999)
        with self.assertRaises(ValueError):
            self.populated_list.remove(external_node)
    
    def test_remove_first(self) -> None:
        """Test removing the first node."""
        # Test with a populated list
        data = self.populated_list.remove_first()
        self.assertEqual(data, 1)
        self.assertEqual(len(self.populated_list), 4)
        
        # Convert to list for easier verification
        expected = [2, 3, 4, 5]
        actual = list(self.populated_list)
        self.assertEqual(actual, expected)
        
        # Test with a single-element list
        single_list = DoublyLinkedList[int]()
        single_list.append(99)
        
        data = single_list.remove_first()
        self.assertEqual(data, 99)
        self.assertEqual(len(single_list), 0)
        self.assertIsNone(single_list.head)
        self.assertIsNone(single_list.tail)
        
        # Test with an empty list
        empty_list = DoublyLinkedList[int]()
        with self.assertRaises(ValueError):
            empty_list.remove_first()
    
    def test_remove_last(self) -> None:
        """Test removing the last node."""
        # Test with a populated list
        data = self.populated_list.remove_last()
        self.assertEqual(data, 5)
        self.assertEqual(len(self.populated_list), 4)
        
        # Convert to list for easier verification
        expected = [1, 2, 3, 4]
        actual = list(self.populated_list)
        self.assertEqual(actual, expected)
        
        # Test with a single-element list
        single_list = DoublyLinkedList[int]()
        single_list.append(99)
        
        data = single_list.remove_last()
        self.assertEqual(data, 99)
        self.assertEqual(len(single_list), 0)
        self.assertIsNone(single_list.head)
        self.assertIsNone(single_list.tail)
        
        # Test with an empty list
        empty_list = DoublyLinkedList[int]()
        with self.assertRaises(ValueError):
            empty_list.remove_last()
    
    def test_remove_at(self) -> None:
        """Test removing a node at a specific index."""
        # Remove at index 0 (first)
        data = self.populated_list.remove_at(0)
        self.assertEqual(data, 1)
        self.assertEqual(len(self.populated_list), 4)
        
        # Remove at the end (last)
        end_index = len(self.populated_list) - 1
        data = self.populated_list.remove_at(end_index)
        self.assertEqual(data, 5)
        self.assertEqual(len(self.populated_list), 3)
        
        # Remove in the middle
        data = self.populated_list.remove_at(1)
        self.assertEqual(data, 3)
        self.assertEqual(len(self.populated_list), 2)
        
        # Convert to list for easier verification
        expected = [2, 4]
        actual = list(self.populated_list)
        self.assertEqual(actual, expected)
        
        # Test out of range
        with self.assertRaises(IndexError):
            self.populated_list.remove_at(-1)
        
        with self.assertRaises(IndexError):
            self.populated_list.remove_at(len(self.populated_list))
    
    def test_get_at(self) -> None:
        """Test getting a node at a specific index."""
        # Get the first node
        node = self.populated_list.get_at(0)
        self.assertEqual(node.data, 1)
        
        # Get the last node
        node = self.populated_list.get_at(len(self.populated_list) - 1)
        self.assertEqual(node.data, 5)
        
        # Get a middle node
        node = self.populated_list.get_at(2)
        self.assertEqual(node.data, 3)
        
        # Test out of range
        with self.assertRaises(IndexError):
            self.populated_list.get_at(-1)
        
        with self.assertRaises(IndexError):
            self.populated_list.get_at(len(self.populated_list))
    
    def test_find(self) -> None:
        """Test finding a node with a specific value."""
        # Find an existing value
        node = self.populated_list.find(3)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 3)
        
        # Find a non-existing value
        node = self.populated_list.find(99)
        self.assertIsNone(node)
        
        # Find in an empty list
        node = self.empty_list.find(1)
        self.assertIsNone(node)
    
    def test_clear(self) -> None:
        """Test clearing the list."""
        # Clear a populated list
        self.populated_list.clear()
        self.assertEqual(len(self.populated_list), 0)
        self.assertIsNone(self.populated_list.head)
        self.assertIsNone(self.populated_list.tail)
        
        # Clear an already empty list
        self.empty_list.clear()
        self.assertEqual(len(self.empty_list), 0)
        self.assertIsNone(self.empty_list.head)
        self.assertIsNone(self.empty_list.tail)
    
    def test_reverse(self) -> None:
        """Test reversing the list."""
        # Store original values
        original = list(self.populated_list)
        
        # Reverse the list
        self.populated_list.reverse()
        
        # Check if values are reversed
        reversed_values = list(self.populated_list)
        self.assertEqual(reversed_values, list(reversed(original)))
        
        # Check head and tail
        self.assertEqual(self.populated_list.head.data, 5)
        self.assertEqual(self.populated_list.tail.data, 1)
        
        # Test with an empty list
        self.empty_list.reverse()
        self.assertIsNone(self.empty_list.head)
        self.assertIsNone(self.empty_list.tail)
        
        # Test with a single element
        single_list = DoublyLinkedList[int]()
        single_list.append(99)
        single_list.reverse()
        self.assertEqual(single_list.head.data, 99)
        self.assertEqual(single_list.tail.data, 99)
    
    def test_getitem(self) -> None:
        """Test getting values by index."""
        # Get by positive index
        self.assertEqual(self.populated_list[0], 1)
        self.assertEqual(self.populated_list[2], 3)
        self.assertEqual(self.populated_list[4], 5)
        
        # Get by negative index
        self.assertEqual(self.populated_list[-1], 5)
        self.assertEqual(self.populated_list[-3], 3)
        self.assertEqual(self.populated_list[-5], 1)
        
        # Test out of range
        with self.assertRaises(IndexError):
            _ = self.populated_list[5]
        
        with self.assertRaises(IndexError):
            _ = self.populated_list[-6]
        
        # Test slice
        slice_list = self.populated_list[1:4]
        self.assertIsInstance(slice_list, DoublyLinkedList)
        self.assertEqual(list(slice_list), [2, 3, 4])
        
        # Test slice with step
        slice_list = self.populated_list[0:5:2]
        self.assertEqual(list(slice_list), [1, 3, 5])
        
        # Test empty slice
        slice_list = self.populated_list[5:10]
        self.assertEqual(len(slice_list), 0)
    
    def test_setitem(self) -> None:
        """Test setting values by index."""
        # Set by positive index
        self.populated_list[2] = 99
        self.assertEqual(self.populated_list[2], 99)
        
        # Set by negative index
        self.populated_list[-1] = 88
        self.assertEqual(self.populated_list[4], 88)
        
        # Test out of range
        with self.assertRaises(IndexError):
            self.populated_list[5] = 77
        
        with self.assertRaises(IndexError):
            self.populated_list[-6] = 77
    
    def test_iter(self) -> None:
        """Test iteration through the list."""
        # Test with a populated list
        expected = [1, 2, 3, 4, 5]
        actual = list(iter(self.populated_list))
        self.assertEqual(actual, expected)
        
        # Test with an empty list
        empty_iter = iter(self.empty_list)
        self.assertEqual(list(empty_iter), [])
    
    def test_contains(self) -> None:
        """Test membership checking."""
        # Check existing values
        self.assertTrue(1 in self.populated_list)
        self.assertTrue(3 in self.populated_list)
        self.assertTrue(5 in self.populated_list)
        
        # Check non-existing values
        self.assertFalse(0 in self.populated_list)
        self.assertFalse(6 in self.populated_list)
        
        # Check in an empty list
        self.assertFalse(1 in self.empty_list)
    
    def test_len(self) -> None:
        """Test getting the length of the list."""
        # Test populated list
        self.assertEqual(len(self.populated_list), 5)
        
        # Test empty list
        self.assertEqual(len(self.empty_list), 0)
        
        # Test after modifications
        self.populated_list.append(6)
        self.assertEqual(len(self.populated_list), 6)
        
        self.populated_list.remove_first()
        self.assertEqual(len(self.populated_list), 5)
    
    def test_str(self) -> None:
        """Test string representation."""
        # Test populated list
        self.assertEqual(str(self.populated_list), "[1, 2, 3, 4, 5]")
        
        # Test empty list
        self.assertEqual(str(self.empty_list), "[]")
    
    def test_repr(self) -> None:
        """Test detailed string representation."""
        # Test populated list
        self.assertEqual(repr(self.populated_list), "DoublyLinkedList([1, 2, 3, 4, 5])")
        
        # Test empty list
        self.assertEqual(repr(self.empty_list), "DoublyLinkedList([])")
    
    def test_different_types(self) -> None:
        """Test the list with different data types."""
        # Test with strings
        str_list = DoublyLinkedList[str]()
        str_list.append("hello")
        str_list.append("world")
        self.assertEqual(list(str_list), ["hello", "world"])
        
        # Test with floats
        float_list = DoublyLinkedList[float]()
        float_list.append(1.1)
        float_list.append(2.2)
        self.assertEqual(list(float_list), [1.1, 2.2])
        
        # Test with mixed types using Any
        mixed_list = DoublyLinkedList[Any]()
        mixed_list.append(1)
        mixed_list.append("hello")
        mixed_list.append(3.14)
        self.assertEqual(list(mixed_list), [1, "hello", 3.14])
    
    def test_performance(self) -> None:
        """Test performance characteristics of the list."""
        # Create a large list
        large_list = DoublyLinkedList[int]()
        n = 10000
        
        # Measure append performance
        start_time = time.time()
        for i in range(n):
            large_list.append(i)
        append_time = time.time() - start_time
        
        # Append should be O(1), so it should be fast even for large lists
        self.assertLess(append_time, 1.0)  # Should be well under 1 second
        
        # Measure access time for first and last elements (should be fast)
        start_time = time.time()
        _ = large_list[0]
        _ = large_list[-1]
        end_access_time = time.time() - start_time
        
        # End access should be O(1)
        self.assertLess(end_access_time, 0.01)  # Should be very fast
        
        # Measure access time for a middle element (should be slower)
        start_time = time.time()
        _ = large_list[n // 2]
        middle_access_time = time.time() - start_time
        
        # Middle access should be O(n) but we optimize to O(n/2)
        # It should be slower than end access but still reasonable
        self.assertGreater(middle_access_time, end_access_time)
        self.assertLess(middle_access_time, 0.1)  # Should still be relatively fast


if __name__ == "__main__":
    unittest.main()