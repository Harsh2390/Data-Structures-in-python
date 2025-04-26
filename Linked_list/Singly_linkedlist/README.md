# Singly Linked List

## Definition
A Singly Linked List is a linear data structure consisting of a sequence of elements, where each element points to the next element in the sequence. Each element (node) contains:
- Data: The value stored in the node
- Next: A reference to the next node in the sequence

The list is accessed through a 'head' reference pointing to the first node. The last node points to `None` indicating the end of the list.

### Visual Representation

```
head
 |
 v
+------+------+    +------+------+    +------+------+
| Data | Next |--->| Data | Next |--->| Data | Next |---> None
+------+------+    +------+------+    +------+------+
   Node 1              Node 2              Node 3
```

## Mathematical/Theoretical Foundation
A Singly Linked List can be represented mathematically as a tuple L = (N, head, next), where:
- N is a set of nodes
- head ∈ N ∪ {None} is the first node (or None for an empty list)
- next: N → N ∪ {None} is a function mapping each node to its successor (or None for the last node)

This forms a connected structure where node traversal always moves forward following the next pointers.

## Time and Space Complexity Analysis

| Operation           | Best Case | Average Case | Worst Case | Space Complexity |
|---------------------|-----------|--------------|------------|------------------|
| Access (get)        | O(1)      | O(n)         | O(n)       | O(1)             |
| Search              | O(1)      | O(n)         | O(n)       | O(1)             |
| Insert at head      | O(1)      | O(1)         | O(1)       | O(1)             |
| Insert at tail      | O(1)*     | O(n)         | O(n)       | O(1)             |
| Insert at position  | O(1)**    | O(n)         | O(n)       | O(1)             |
| Delete at head      | O(1)      | O(1)         | O(1)       | O(1)             |
| Delete at tail      | O(n)      | O(n)         | O(n)       | O(1)             |
| Delete at position  | O(1)**    | O(n)         | O(n)       | O(1)             |
| Space requirement   | -         | -            | -          | O(n)             |

*O(1) if we maintain a tail pointer
**O(1) if we already have a reference to the node before the insertion/deletion point

### Explanation:
- **Access/Search**: Requires traversing the list from the head, with worst-case O(n) when the element is at the end
- **Insert at head**: Always O(1) since we just update the head pointer
- **Insert at tail**: O(n) since we need to traverse to the end unless we maintain a tail pointer
- **Insert at position**: O(n) for finding the position, then O(1) for the actual insertion
- **Delete operations**: Similar to insertion, with head deletion being O(1) and others requiring list traversal

## Real-world Applications

1. **Implementation of other data structures**: 
   - Stacks and queues
   - Symbol tables in compilers and interpreters
   - Components of hash tables for collision resolution

2. **Memory management**:
   - Managing dynamic memory allocation in operating systems
   - Implementing memory pools

3. **Application scenarios**:
   - Browser's back and forward navigation
   - Undo functionality in applications
   - Music playlist management
   - Transaction histories

## Advantages and Limitations

### Advantages:
1. **Dynamic size**: Can grow and shrink as needed at runtime
2. **Efficient insertions/deletions**: Especially at the beginning (O(1))
3. **Memory efficiency**: Only allocates what it needs
4. **No pre-allocation needed**: Unlike arrays, doesn't require size specification upfront
5. **Simplicity**: Conceptually straightforward compared to other dynamic data structures

### Limitations:
1. **Sequential access only**: No direct/random access to elements (O(n) access time)
2. **Extra memory**: Additional memory for storing references
3. **No backward traversal**: Cannot easily move backwards without a doubly-linked version
4. **Cache performance**: Poor cache locality compared to contiguous structures like arrays
5. **No index-based access**: Cannot use integer indices efficiently

## Implementation Details and Design Decisions

1. **Two-class design**: Separating the `Node` (internal implementation) from the `SinglyLinkedList` (user interface)
2. **Iterator support**: Implementing Python's iterator protocol for natural list traversal
3. **Sentinel nodes**: Not used to keep implementation cleaner, but head/tail management is explicit
4. **Type hints**: Used throughout for better IDE support and code clarity
5. **Full Python collections interface**: Implementing standard Python behavior where appropriate
6. **Error handling**: Comprehensive error handling for edge cases like empty lists
7. **Position validation**: Methods that operate on positions validate inputs to prevent errors

## Basic Usage

```python
# Create a new linked list
llist = SinglyLinkedList()

# Add elements
llist.append(1)
llist.append(2)
llist.append(3)

# Insert at beginning
llist.prepend(0)

# Insert at specific position
llist.insert_at(2, 1.5)  # Insert 1.5 at position 2

# Access elements
head_value = llist.head_value  # Get value at head
value_at_2 = llist.get(2)      # Get value at position 2

# Remove elements
llist.remove_head()  # Remove first element
llist.remove(2)      # Remove element at position 2

# Check size and emptiness
size = len(llist)
is_empty = llist.is_empty()

# Iteration
for value in llist:
    print(value)

# Convert to list
values = list(llist)

# String representation
print(llist)  # Shows something like: [1, 2, 3]
```
