# Linked List Overview

## Introduction
A linked list is a linear data structure where elements are not stored at contiguous memory locations. Instead, each element (known as a node) contains data and a reference (or link) to the next node in the sequence. Linked lists allow for efficient insertion and deletion of elements as these operations do not require the reorganization of the entire data structure.

## Types of Linked Lists
There are three main types of linked lists:
1. **Singly Linked Lists**
2. **Doubly Linked Lists**
3. **Circular Linked Lists**

### Singly Linked List
A singly linked list is a collection of nodes that together form a linear sequence. Each node stores a reference to an object that is an element of the sequence, as well as a reference to the next node of the list. The first node has a reference from an external source (head), and the last node points to `None`.

**Time Complexity:**
- Access: O(n)
- Search: O(n)
- Insertion: O(1) at the beginning, O(n) at the end
- Deletion: O(1) at the beginning, O(n) to remove a specific element

### Doubly Linked List
A doubly linked list is similar to a singly linked list, but each node contains two links: the first links to the previous node, and the second links to the next node in the sequence. This allows for a bidirectional traversal of the list.

**Time Complexity:**
- Access: O(n)
- Search: O(n)
- Insertion: O(1) for inserting at the beginning or end
- Deletion: O(1) for deleting at the beginning or end

### Circular Linked List
A circular linked list is either singly or doubly linked where the last node, instead of pointing to `None`, points back to the first node. This forms a circular loop. A circular linked list can be either singly circular or doubly circular.

**Time Complexity:**
- Access: O(n)
- Search: O(n)
- Insertion: O(1) if the tail is known, otherwise O(n)
- Deletion: O(1) to remove from the beginning, O(n) to remove a specific element if the tail is not directly accessible

## Advantages of Linked Lists
- Dynamic data structure: Linked lists are dynamic and can grow and shrink in size without the need for reallocation or reorganization of the entire structure.
- Efficient Insertions/Deletions: Adding or removing elements from a linked list is more efficient in terms of time complexity compared to arrays or other linear data structures.

## Disadvantages of Linked Lists
- Memory Usage: Each element in a linked list requires extra storage for the reference/link part.
- Sequential Access: Elements in a linked list must be accessed sequentially starting from the first node. Hence, direct access by position is not as efficient as in arrays.

Linked lists serve as a foundational data structure for building more complex structures like stacks, queues, and graphs, and understanding them is crucial for efficient algorithm implementation and optimization.

