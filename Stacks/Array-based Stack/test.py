"""
Unit tests for the Array-based Stack implementation.
"""

import unittest
from stack import ArrayStack, EmptyStackError

class TestArrayStack(unittest.TestCase):
    """Test suite for the ArrayStack class."""
    
    def setUp(self):
        """Set up a new stack before each test."""
        self.stack = ArrayStack[int]()
    
    def test_initialization(self):
        """Test that a new stack is empty."""
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
        
    def test_push(self):
        """Test pushing elements onto the stack."""
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.assertFalse(self.stack.is_empty())
        
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        
    def test_pop(self):
        """Test popping elements from the stack."""
        self.stack.push(1)
        self.stack.push(2)
        
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.size(), 1)
        
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.size(), 0)
        self.assertTrue(self.stack.is_empty())
    
    def test_pop_empty(self):
        """Test popping from an empty stack raises an exception."""
        with self.assertRaises(EmptyStackError):
            self.stack.pop()
    
    def test_peek(self):
        """Test peeking at the top element."""
        self.stack.push(1)
        self.stack.push(2)
        
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.size(), 2)  # Size should not change
    
    def test_peek_empty(self):
        """Test peeking at an empty stack raises an exception."""
        with self.assertRaises(EmptyStackError):
            self.stack.peek()
    
    def test_clear(self):
        """Test clearing the stack."""
        self.stack.push(1)
        self.stack.push(2)
        
        self.stack.clear()
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
    
    def test_len(self):
        """Test the __len__ method."""
        self.assertEqual(len(self.stack), 0)
        
        self.stack.push(1)
        self.stack.push(2)
        
        self.assertEqual(len(self.stack), 2)
    
    def test_string_representation(self):
        """Test the string representation of the stack."""
        # Empty stack
        self.assertEqual(str(self.stack), "Stack: []")
        
        # Non-empty stack
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        
        expected = "Stack: [3 (top), 2, 1 (bottom)]"
        self.assertEqual(str(self.stack), expected)
    
    def test_iteration(self):
        """Test iterating over the stack."""
        values = [1, 2, 3, 4, 5]
        
        for val in values:
            self.stack.push(val)
        
        # Iteration should be in LIFO order (top to bottom)
        expected = list(reversed(values))
        actual = list(self.stack)
        
        self.assertEqual(actual, expected)
    
    def test_contains(self):
        """Test the __contains__ method."""
        self.stack.push(1)
        self.stack.push(2)
        
        self.assertTrue(1 in self.stack)
        self.assertTrue(2 in self.stack)
        self.assertFalse(3 in self.stack)

    def test_generic_type(self):
        """Test that the stack works with different types."""
        # String stack
        string_stack = ArrayStack[str]()
        string_stack.push("hello")
        string_stack.push("world")
        
        self.assertEqual(string_stack.pop(), "world")
        self.assertEqual(string_stack.pop(), "hello")
        
        # Float stack
        float_stack = ArrayStack[float]()
        float_stack.push(1.1)
        float_stack.push(2.2)
        
        self.assertEqual(float_stack.pop(), 2.2)
        self.assertEqual(float_stack.pop(), 1.1)

if __name__ == '__main__':
    unittest.main()