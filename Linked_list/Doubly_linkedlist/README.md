# Doubly Linked List

A robust, type-hinted Python implementation of the Doubly Linked List data structure.

## Table of Contents
1. [Definition and Visualization](#definition-and-visualization)
2. [Mathematical Foundation](#mathematical-foundation)
3. [Operations and Complexity](#operations-and-complexity)
4. [Real-world Applications](#real-world-applications)
5. [Advantages and Limitations](#advantages-and-limitations)
6. [Implementation Details](#implementation-details)
7. [Usage Examples](#usage-examples)
8. [References](#references)

## Definition and Visualization

A Doubly Linked List is a linear data structure consisting of nodes, where each node contains:
- Data (the value stored in the node)
- A reference (pointer) to the next node in the sequence
- A reference (pointer) to the previous node in the sequence

The list maintains references to both the head (first) and tail (last) nodes for efficient operations at both ends.

### Visualization:

```
  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
  │   Node 1    │    │   Node 2    │    │   Node 3    │
  │ ┌─────────┐ │    │ ┌─────────┐ │    │ ┌─────────┐ │
  │ │  Data   │ │    │ │  Data   │ │    │ │  Data   │ │
┌─┼─┤ Prev=None│◄┼────┼─┤ Prev    │◄┼────┼─┤ Prev    │ │
│ │ │  Next   │─┼────►│ │  Next   │─┼────►│ │Next=None│ │
│ │ └─────────┘ │    │ └─────────┘ │    │ └─────────┘ │
│ └─────────────┘    └─────────────┘    └─────────────┘
│                                                      │
│                                                      │
└──────────────────────────────────────────────────────┘
Head                                                 Tail
```

## Mathematical Foundation

Formally, a doubly linked list can be defined as an ordered set of elements (nodes) in which:

- Each node contains an element of data and two pointers/references
- If we denote a node as `N`, then `N.prev` points to the previous node in the sequence (or `None` if it's the first node)
- Similarly, `N.next` points to the next node in the sequence (or `None` if it's the last node)
- The list maintains references to the head (first) and tail (last) nodes

Mathematically, we can represent a doubly linked list with n nodes as:

$L = \{N_1, N_2, ..., N_n\}$ where:
- $N_i.prev = N_{i-1}$ for $2 \leq i \leq n$
- $N_i.next = N_{i+1}$ for $1 \leq i \leq n-1$
- $N_1.prev = None$
- $N_n.next = None$

## Operations and Complexity

| Operation | Description | Best Case | Average Case | Worst Case | Space Complexity |
|-----------|-------------|-----------|--------------|------------|------------------|
| append(value) | Add element at the end | O(1) | O(1) | O(1) | O(1) |
| prepend(value) | Add element at the beginning | O(1) | O(1) | O(1) | O(1) |
| insert_after(node, value) | Insert after a specific node | O(1) | O(1) | O(1) | O(1) |
| insert_before(node, value) | Insert before a specific node | O(1) | O(1) | O(1) | O(1) |
| insert_at(index, value) | Insert at a specific index | O(1)* | O(n/2) | O(n) | O(1) |
| remove_first() | Remove the first node | O(1) | O(1) | O(1) | O(1) |
| remove_last() | Remove the last node | O(1) | O(1) | O(1) | O(1) |
| remove(node) | Remove a specific node | O(1) | O(1) | O(1) | O(1) |
| remove_at(index) | Remove at a specific index | O(1)* | O(n/2) | O(n) | O(1) |
| find(value) | Find first node with value | O(1) | O(n/2) | O(n) | O(1) |
| get_at(index) | Get node at index | O(1)* | O(n/2) | O(n) | O(1) |
| clear() | Remove all elements | O(1) | O(1) | O(1) | O(1) |
| __len__() | Size/length of the list | O(1) | O(1) | O(1) | O(1) |
| __iter__() | Iterate through the list | O(1) | O(n) | O(n) | O(1) |
| __contains__(value) | Check if value exists | O(1) | O(n/2) | O(n) | O(1) |
| __getitem__(index) | Access via index | O(1)* | O(n/2) | O(n) | O(1) |
| __setitem__(index, value) | Set value at index | O(1)* | O(n/2) | O(n) | O(1) |
| __str__() | String representation | O(n) | O(n) | O(n) | O(n) |
| __repr__() | Detailed string representation | O(n) | O(n) | O(n) | O(n) |

*O(1) for first or last index

### Explanation:

- **Access operations** (`get_at`, `__getitem__`): O(n) worst case as we may need to traverse the entire list
  - However, our implementation is optimized to start from the closest end (head or tail)
  - This reduces average-case complexity to O(n/2)
  
- **Insertion/Deletion at ends** (`append`, `prepend`, `remove_first`, `remove_last`): O(1) because we maintain references to both head and tail

- **Insertion/Deletion at a known node** (`insert_after`, `insert_before`, `remove`): O(1) because we only need to update a few pointers

- **Insertion/Deletion at index** (`insert_at`, `remove_at`): O(n) worst case as we might need to traverse to the position
  - Optimized to O(n/2) by starting from the closer end

- **Search operations** (`find`, `__contains__`): O(n) worst case as we may need to check every node

- **Size operation** (`__len__`): O(1) as we maintain a size counter

## Real-world Applications

Doubly Linked Lists are extensively used in various applications:

1. **Browser History**: The forward and backward navigation in web browsers is often implemented using a doubly linked list, where each node represents a webpage.

2. **Music Player Application**: For implementing features like next and previous song, where each node contains song information.

3. **Undo/Redo Operations**: In applications like text editors and graphic design tools for implementing undo and redo functionality.

4. **LRU (Least Recently Used) Cache**: Combined with a hash map, doubly linked lists help implement efficient caching mechanisms.

5. **Image Viewers**: For navigating between images in forward and backward directions.

6. **Text Editors**: For efficient insertions and deletions of characters or lines.

7. **Task Schedulers**: In operating systems for maintaining lists of processes.

8. **Deck of Cards in Card Games**: For easy reshuffling and dealing operations.

## Advantages and Limitations

### Advantages

1. **Bidirectional Traversal**: Can be traversed in both forward and backward directions.

2. **Efficient Insertions and Deletions**: O(1) time complexity for insertions and deletions at known positions, including both ends.

3. **Dynamic Size**: Can grow or shrink as needed during execution.

4. **No Reallocation**: Unlike arrays, no need to reallocate the entire data structure when adding elements.

5. **Efficient Implementation of Various Algorithms**: Such as LRU cache, undo/redo functionality, etc.

### Limitations

1. **Extra Memory Overhead**: Each node requires additional memory for storing previous and next pointers.

2. **Random Access Inefficiency**: O(n) worst-case time complexity for accessing arbitrary elements, unlike arrays with O(1).

3. **Cache Unfriendliness**: Nodes may be scattered in memory, which can lead to cache misses.

4. **Reverse Traversal Overhead**: While traversal is bidirectional, maintaining the previous pointers adds complexity.

5. **Complex Implementation**: More complex to implement and maintain than singly linked lists or arrays.

## Implementation Details

Our implementation follows a domain-driven design approach with clear separation of concerns:

1. **Node Class**: Represents a single node in the doubly linked list, containing:
   - Data (value stored)
   - Next pointer (reference to the next node)
   - Previous pointer (reference to the previous node)

2. **DoublyLinkedList Class**: The main data structure class with:
   - Head and tail references
   - Size counter
   - Methods for all standard operations
   - Iterator implementation for traversal
   - Magic methods for Python-idiomatic usage

### Design Decisions

1. **Type Hints**: Full type annotation using Python's typing module for better IDE support and code clarity.

2. **Generic Type Parameter**: The list is implemented as a generic container that can store any type.

3. **Optimized Traversal**: For index-based operations, traversal starts from the closest end (head or tail) to reduce average-case complexity to O(n/2).

4. **Python Idioms**: Implementation of magic methods (`__len__`, `__iter__`, `__getitem__`, etc.) for intuitive Pythonic usage.

5. **Comprehensive Error Handling**: Proper checks for empty lists, invalid indices, and other edge cases.

6. **Automatic Cleanup**: The `clear` method helps in proper garbage collection.

7. **Bidirectional Iterator**: Implementation allows for efficient bidirectional iteration.

## Usage Examples

```python
# Basic operations
dll = DoublyLinkedList[int]()
dll.append(10)
dll.append(20)
dll.prepend(5)
print(dll)  # Output: [5, 10, 20]

# Insertion at specific positions
dll.insert_at(1, 7)
print(dll)  # Output: [5, 7, 10, 20]

# Removal operations
dll.remove_first()
dll.remove_last()
print(dll)  # Output: [7, 10]

# Searching
node = dll.find(10)
dll.insert_after(node, 15)
print(dll)  # Output: [7, 10, 15]

# Iteration
for value in dll:
    print(value)  # Outputs: 7, 10, 15

# Using indexing
print(dll[1])  # Output: 10
dll[1] = 12
print(dll)  # Output: [7, 12, 15]

# Check membership
print(12 in dll)  # Output: True
print(10 in dll)  # Output: False
```

### Practical Example: LRU Cache Implementation

```python
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map for O(1) lookup
        self.list = DoublyLinkedList[tuple[Any, Any]]()  # Stores (key, value) pairs
        
    def get(self, key: Any) -> Any:
        if key not in self.cache:
            return -1
        
        # Move accessed item to the end (most recently used)
        node = self.cache[key]
        value = node.data[1]
        self.list.remove(node)
        new_node = self.list.append((key, value))
        self.cache[key] = new_node
        return value
        
    def put(self, key: Any, value: Any) -> None:
        if key in self.cache:
            # Remove existing item
            self.list.remove(self.cache[key])
            
        elif len(self.list) >= self.capacity:
            # Remove least recently used item (front of the list)
            lru_key = self.list.head.data[0]
            self.list.remove_first()
            del self.cache[lru_key]
            
        # Add new item to the end (most recently used)
        new_node = self.list.append((key, value))
        self.cache[key] = new_node
```

