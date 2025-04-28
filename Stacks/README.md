# Stacks

## Overview

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. Elements are added (pushed) and removed (popped) from the same end, called the "top" of the stack. This behaves like a physical stack of objects, where you can only add or remove the topmost item.

```
Stack Operation Visualization:

Initial:  [ ][ ][ ][ ][ ]  ← Top
          Empty Stack

Push(A):  [ ][ ][ ][ ][A]  ← Top
          Added 'A'

Push(B):  [ ][ ][ ][A][B]  ← Top
          Added 'B'

Pop():    [ ][ ][ ][A][ ]  ← Top
          Removed 'B'

Push(C):  [ ][ ][ ][A][C]  ← Top
          Added 'C'
```

## Key Characteristics

- **LIFO Principle**: Last element in is the first one out
- **One-ended Operations**: All operations occur at the top of the stack
- **Simple Interface**: Core operations are push, pop, and peek
- **Limited Access**: Only the top element is accessible at any time
- **Efficient Operations**: Most operations are O(1) time complexity

## Types of Stacks

### Array-based Stack
- Uses an array as the underlying data structure
- Fixed capacity unless implemented with dynamic arrays
- Better memory locality and cache performance
- Simple implementation with direct indexing

### Linked List-based Stack
- Uses a linked list (typically singly linked) as the underlying structure
- Dynamic size with no predefined limit
- Push and pop operations simply add/remove from the head
- No capacity constraints but higher memory overhead per element

### Min Stack
- Specialized stack that can retrieve the minimum value in O(1) time
- Maintains an auxiliary stack of minimums alongside the main stack
- Supports all standard stack operations plus getMin()
- Used in algorithms requiring quick access to minimum values

### Max Stack
- Specialized stack that can retrieve the maximum value in O(1) time
- Maintains an auxiliary stack of maximums alongside the main stack
- Supports all standard stack operations plus getMax()
- Used in algorithms requiring quick access to maximum values

## Time Complexity Comparison

| Operation   | Array-based | Linked List-based | Min Stack | Max Stack |
|-------------|-------------|-------------------|-----------|-----------|
| Push        | O(1)*       | O(1)              | O(1)      | O(1)      |
| Pop         | O(1)        | O(1)              | O(1)      | O(1)      |
| Peek (Top)  | O(1)        | O(1)              | O(1)      | O(1)      |
| isEmpty     | O(1)        | O(1)              | O(1)      | O(1)      |
| getMin      | O(n)        | O(n)              | O(1)      | O(n)      |
| getMax      | O(n)        | O(n)              | O(n)      | O(1)      |
| Search      | O(n)        | O(n)              | O(n)      | O(n)      |

\* O(n) in worst case for array-based stack when resizing is needed

## Space Complexity Comparison

| Stack Type        | Space Complexity |
|-------------------|------------------|
| Array-based       | O(n)             |
| Linked List-based | O(n)             |
| Min Stack         | O(n)             |
| Max Stack         | O(n)             |

## Common Applications

- **Array-based Stack**: 
  - Parsing expressions (including undo operations)
  - Browser history (back button functionality)
  - Function call management (call stack)

- **Linked List-based Stack**:
  - Memory management in environments without fixed allocation
  - Implementations requiring frequent resizing
  - Symbol tables in compilers

- **Min Stack**:
  - Tracking stock price minimums over periods
  - Algorithm design for problems requiring minimum element lookups
  - Online algorithms with minimum value constraints

- **Max Stack**:
  - Maximum sliding window problems
  - Tracking maximum values in data streams
  - Height/elevation-based calculations

## General Stack Applications

1. **Expression Evaluation and Conversion**
   - Evaluating postfix expressions
   - Converting between infix, prefix, and postfix notations
   - Checking for balanced parentheses

2. **Algorithmic Techniques**
   - Depth-First Search (DFS) graph traversal
   - Backtracking algorithms
   - Tree traversals (iterative implementations)

3. **Memory Management**
   - Function call stacks in programming languages
   - Nested operations management
   - Undo mechanisms in applications

4. **String Processing**
   - Parentheses/bracket matching
   - Syntax parsing
   - String reversal algorithms

## Advantages and Disadvantages

### Advantages
- Simple and intuitive data structure
- Efficient operations (constant time)
- Easy to implement and use
- Memory efficient for most applications
- Useful in many algorithmic scenarios

### Disadvantages
- Limited access (only top element)
- No random access to elements
- Fixed size in array implementations (unless using dynamic arrays)
- No direct access to minimum/maximum elements (in basic implementations)

## Implementation Notes

Each stack variant in this repository is implemented as a standalone Python module with:

- A main stack class with standard operations
- Comprehensive docstrings and type annotations
- Appropriate exception handling for empty stack operations
- Efficient implementations of specialized operations

## Directory Structure

```
stack/
│
├── README.md              # This file
├── array_stack/           # Array-based stack implementation
├── linked_list_stack/     # Linked List-based stack implementation
├── min_stack/             # Min Stack implementation
└── max_stack/             # Max Stack implementation
```

Each subdirectory contains:
- Implementation file(s)
- README.md with specific details
- Unit tests
- Example usage
