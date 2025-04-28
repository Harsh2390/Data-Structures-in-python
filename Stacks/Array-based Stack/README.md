# Array-based Stack Implementation

## Overview

A Stack is a fundamental data structure that follows the Last-In-First-Out (LIFO) principle, where elements are added and removed from the same end, called the "top" of the stack. This implementation uses an array (Python list) as the underlying storage mechanism.

## Conceptual Model

A Stack can be visualized as a vertical collection of elements where both insertion and deletion happen at the same end, called the "top":

```
    │         │         
    │    D    │  ← Top (Last In, First Out)
    │    C    │         
    │    B    │        
    │    A    │  ← Bottom
    └─────────┘        
```

The stack follows these key principles:
- Elements are added to the top (push operation)
- Elements are removed from the top (pop operation)
- Only the top element is accessible at any time (peek operation)
- The last element added is the first one to be removed (LIFO property)

## Mathematical/Theoretical Foundation

The Stack data structure is mathematically defined as an abstract data type (ADT) that supports the following operations:
- **push(e)**: Add element e to the top of the stack
- **pop()**: Remove and return the top element from the stack
- **peek()**: Return the top element without removing it
- **is_empty()**: Return True if the stack contains no elements, False otherwise

Formally, a stack S of length n can be represented as a sequence where S = (a₀, a₁, ..., aₙ₋₁) with aₙ₋₁ being the top element.

## Time and Space Complexity

### Time Complexity

| Operation | Best Case | Average Case | Worst Case | Description |
|-----------|-----------|--------------|------------|-------------|
| push(e)   | O(1)      | O(1)         | O(n)*      | Add element to top |
| pop()     | O(1)      | O(1)         | O(1)       | Remove element from top |
| peek()    | O(1)      | O(1)         | O(1)       | View top element |
| is_empty()| O(1)      | O(1)         | O(1)       | Check if stack is empty |
| size()    | O(1)      | O(1)         | O(1)       | Get number of elements |
| clear()   | O(1)      | O(1)         | O(1)       | Remove all elements |

\* The worst case for push is O(n) when the underlying array needs to be resized, but this is an amortized O(1) operation over many pushes.

### Space Complexity

The space complexity of an array-based stack is O(n), where n is the number of elements in the stack.

## Applications and Use Cases

Stacks are widely used in various domains and algorithms:

1. **Function call management**: Used by programming language environments to manage function calls and returns (call stack)
2. **Expression evaluation**: Parsing and evaluating arithmetic expressions, checking for balanced parentheses
3. **Undo mechanisms**: Implementing undo functionality in applications
4. **Backtracking algorithms**: Used in algorithms that need to "remember" states to backtrack
5. **Browser history**: Managing the history of visited pages
6. **Depth-First Search**: Implementation of graph traversal algorithms
7. **Memory management**: Allocation and deallocation of memory in some systems

## Advantages and Limitations

### Advantages
- Simple and intuitive implementation
- Constant time operations (in most cases)
- Efficient memory usage with dynamic arrays
- Natural fit for problems that exhibit LIFO behavior

### Limitations
- Only the top element is accessible
- No random access to other elements
- Limited functionality compared to more complex data structures
- Array-based implementation may waste memory due to pre-allocation

## Implementation Details

This implementation uses Python's built-in list as the underlying array structure. Key design decisions include:

1. **Dynamic resizing**: Leveraging Python list's automatic resizing capability
2. **Type hints**: Using Python's type hinting for better code clarity and tooling support
3. **Iterator protocol**: Implementing `__iter__` and related methods for iteration support
4. **String representation**: Custom string representation for better debugging
5. **Exception handling**: Proper exception handling for edge cases (e.g., popping from empty stack)
6. **Index-based access**: Using list's index-based operations for efficient implementation

## Usage Example

```python
from stack import ArrayStack

# Create a new stack
stack = ArrayStack[int]()

# Push elements
stack.push(10)
stack.push(20)
stack.push(30)

# Check size
print(f"Stack size: {len(stack)}")  # Output: Stack size: 3

# Peek at top element
print(f"Top element: {stack.peek()}")  # Output: Top element: 30

# Pop elements
while not stack.is_empty():
    print(f"Popped: {stack.pop()}")

# Output:
# Popped: 30
# Popped: 20
# Popped: 10

# Iteration example
stack = ArrayStack[str]()
stack.push("apple")
stack.push("banana")
stack.push("cherry")

print("Stack contents:")
for item in stack:
    print(item)

# Output:
# Stack contents:
# cherry
# banana
# apple
```
