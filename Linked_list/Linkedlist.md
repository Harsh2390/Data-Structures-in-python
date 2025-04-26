# Linked Lists

## Overview

A linked list is a linear data structure consisting of a sequence of elements where each element points to the next element in the sequence. Unlike arrays, linked lists don't store elements in contiguous memory locations, instead using pointers or references to connect elements together.

```
Singly Linked List:
[Node] -> [Node] -> [Node] -> [Node] -> null
  |        |        |        |
 data     data     data     data

Doubly Linked List:
null <- [Node] <-> [Node] <-> [Node] <-> [Node] -> null
         |          |          |          |
        data       data       data       data
```

## Key Characteristics

- **Dynamic Size**: Linked lists can grow or shrink during execution
- **No Random Access**: Elements must be accessed sequentially
- **Efficient Insertions/Deletions**: No need to shift elements (unlike arrays)
- **Extra Memory**: Requires additional memory for storing references
- **No Locality of Reference**: Elements are not stored contiguously in memory

## Types of Linked Lists

### Singly Linked List
- Each node contains data and a reference to the next node
- Traversal is one-directional (forward only)
- Memory efficient compared to other variants
- Limited operations (cannot easily traverse backward)

### Doubly Linked List
- Each node contains data and references to both next and previous nodes
- Bidirectional traversal possible
- More memory overhead than singly linked lists
- More efficient for certain operations (like deletion when given a node)

### Circular Linked List
- Can be either singly or doubly linked
- The last node points back to the first node (no null termination)
- Enables continuous traversal through the list
- Useful for applications requiring cyclical representation

### Skip List
- Probabilistic data structure with multiple layers
- Express lanes for faster traversal (O(log n) search time)
- Combines linked list simplicity with tree-like search efficiency
- Randomized structure that provides expected O(log n) operations

### XOR Linked List
- Memory-efficient variant of a doubly linked list
- Uses bitwise XOR operation to store both next and previous references in a single pointer
- Significantly reduces memory usage
- More complex implementation and limited language support

## Time Complexity Comparison

| Operation           | Singly Linked | Doubly Linked | Circular      | Skip List         | XOR Linked    |
|---------------------|---------------|---------------|---------------|-------------------|---------------|
| Access (by index)   | O(n)          | O(n)          | O(n)          | O(n)              | O(n)          |
| Search              | O(n)          | O(n)          | O(n)          | O(log n) expected | O(n)          |
| Insertion (at head) | O(1)          | O(1)          | O(1)          | O(log n) expected | O(1)          |
| Insertion (at tail) | O(n) / O(1)*  | O(1)          | O(1)          | O(log n) expected | O(1)          |
| Insertion (middle)  | O(n)          | O(n)          | O(n)          | O(log n) expected | O(n)          |
| Deletion (at head)  | O(1)          | O(1)          | O(1)          | O(log n) expected | O(1)          |
| Deletion (at tail)  | O(n)          | O(1)          | O(1)          | O(log n) expected | O(1)          |
| Deletion (middle)   | O(n)          | O(n)**        | O(n)**        | O(log n) expected | O(n)**        |

\* O(1) if tail reference is maintained
\** O(1) if the node pointer is given directly, O(n) if search is required first

## Space Complexity Comparison

| List Type           | Space Complexity per Node |
|---------------------|---------------------------|
| Singly Linked       | O(n) - One reference      |
| Doubly Linked       | O(n) - Two references     |
| Circular            | Same as base type         |
| Skip List           | O(n log n) expected       |
| XOR Linked          | O(n) - One reference      |

## Common Applications

- **Singly Linked List**: 
  - Implementation of stacks and queues
  - Symbol tables in compiler design
  - Undo functionality in applications

- **Doubly Linked List**:
  - Browser's forward and backward navigation
  - Music player's next and previous functionality
  - LRU cache implementation

- **Circular Linked List**:
  - Round-robin scheduling
  - Circular buffers
  - Games with turns (like multiplayer card games)

- **Skip List**:
  - Alternative to balanced trees
  - Database indexing
  - Efficient implementation of sorted sets

- **XOR Linked List**:
  - Memory-constrained systems
  - Embedded systems with limited resources
  - Low-level system programming

## Advantages and Disadvantages

### Advantages
- Dynamic size allocation
- Efficient insertions and deletions
- No need for contiguous memory
- Various specialized implementations for different use cases

### Disadvantages
- Higher memory usage due to storage of references
- No random access to elements
- More complex implementation than arrays
- Cache performance issues due to non-contiguous memory layout

## Implementation Notes

Each linked list variant in this repository is implemented as a standalone Python module with:

- A `Node` class representing individual elements
- A main list class with standard operations
- Comprehensive docstrings and type annotations
- Appropriate iterator implementations
- Unit tests covering all functionality

## Directory Structure

```
linked-list/
│
├── README.md              # This file
├── singly_linked_list/    # Singly linked list implementation
├── doubly_linked_list/    # Doubly linked list implementation
├── circular_linked_list/  # Circular linked list implementation
├── skip_list/             # Skip list implementation
└── xor_linked_list/       # XOR linked list implementation
```

Each subdirectory contains:
- Implementation file(s)
- README.md with specific details
- Unit tests
- Example usage
