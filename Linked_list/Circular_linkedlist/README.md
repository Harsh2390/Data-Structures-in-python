# Circular Linked List

## Table of Contents
- [Overview](#overview)
- [Visual Representation](#visual-representation)
- [Mathematical Foundation](#mathematical-foundation)
- [Operations and Complexity Analysis](#operations-and-complexity-analysis)
- [Real-world Applications](#real-world-applications)
- [Advantages and Limitations](#advantages-and-limitations)
- [Implementation Details](#implementation-details)
- [Usage Examples](#usage-examples)
- [References](#references)

## Overview
A Circular Linked List is a variation of a linked list data structure where the last node points back to the first node, forming a closed loop. Unlike a standard linked list that has a distinct beginning and end, a circular linked list has no clear termination point. This cyclic nature gives circular linked lists unique properties that are advantageous for certain applications.

This implementation provides a Python class for a singly circular linked list with comprehensive functionality while adhering to Pythonic design principles.

## Visual Representation

### Singly Circular Linked List
```
    ┌─────────────────────────────────────────────┐
    │                                             │
    ▼                                             │
┌───────┐     ┌───────┐     ┌───────┐     ┌───────┐
│ Node1 │ ──► │ Node2 │ ──► │ Node3 │ ──► │ Node4 │
└───────┘     └───────┘     └───────┘     └───────┘
```

## Mathematical Foundation
Formally, a circular linked list can be represented as a directed cyclic graph G = (V, E) where:
- V is a set of vertices (nodes)
- E is a set of ordered pairs (directed edges)

For a singly circular linked list with n nodes, V = {v₁, v₂, ..., vₙ}, and E = {(v₁, v₂), (v₂, v₃), ..., (vₙ₋₁, vₙ), (vₙ, v₁)}.

The circular nature means there exists a path from any node to any other node, and for any node v, there exists a cycle of length n starting and ending at v.

## Operations and Complexity Analysis

| Operation        | Description                                  | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
|------------------|----------------------------------------------|------------------------|---------------------------|-------------------------|-----------------|
| `append`         | Add node at the end                          | O(1)¹                  | O(1)¹                     | O(1)¹                   | O(1)            |
| `prepend`        | Add node at the beginning                    | O(1)                   | O(1)                      | O(1)                    | O(1)            |
| `insert_after`   | Insert after a specific node                 | O(1)                   | O(1)                      | O(1)                    | O(1)            |
| `insert_at`      | Insert at a specific position                | O(1)²                  | O(n)                      | O(n)                    | O(1)            |
| `remove`         | Remove a specific node by value              | O(1)³                  | O(n)                      | O(n)                    | O(1)            |
| `remove_at`      | Remove at a specific position                | O(1)²                  | O(n)                      | O(n)                    | O(1)            |
| `find`           | Find a node by value                         | O(1)                   | O(n)                      | O(n)                    | O(1)            |
| `get_at`         | Get node at a specific position              | O(1)²                  | O(n)                      | O(n)                    | O(1)            |
| `clear`          | Remove all nodes                             | O(1)                   | O(1)                      | O(1)                    | O(1)            |
| `size`/`__len__` | Get list size                                | O(1)                   | O(1)                      | O(1)                    | O(1)            |
| `is_empty`       | Check if list is empty                       | O(1)                   | O(1)                      | O(1)                    | O(1)            |
| `to_list`        | Convert to Python list                       | O(n)                   | O(n)                      | O(n)                    | O(n)            |
| `from_list`      | Create from Python list                      | O(n)                   | O(n)                      | O(n)                    | O(n)            |
| `__iter__`       | Get iterator                                 | O(1)                   | O(1)                      | O(1)                    | O(1)            |
| `__next__`       | Get next element                             | O(1)                   | O(1)                      | O(1)                    | O(1)            |
| `rotate`         | Rotate the list by k positions               | O(1)²                  | O(n)                      | O(n)                    | O(1)            |
| `__str__`        | String representation                        | O(n)                   | O(n)                      | O(n)                    | O(n)            |
| `__repr__`       | Official string representation               | O(n)                   | O(n)                      | O(n)                    | O(n)            |

¹ With tail pointer, otherwise O(n)  
² For first or last position, otherwise O(n)  
³ When the node to remove is known directly, otherwise O(n)  

## Real-world Applications

1. **Round-Robin Scheduling**: Operating systems use circular linked lists for round-robin scheduling of processes, where each process gets a fixed time slice in rotation.

2. **Media Playlists**: Music or video players use circular linked lists for continuous playback of playlists.

3. **Turn-based Games**: Games where players take turns in a fixed order can use circular linked lists to manage player rotation.

4. **Circular Buffers**: Implementing circular buffers for streaming data or managing limited resources.

5. **Josephus Problem**: Solving the Josephus problem, a counting-out game where people stand in a circle and are eliminated at regular intervals.

6. **Traffic Light Systems**: Managing the cyclic nature of traffic light sequences.

7. **Browser Tab Navigation**: Implementing wrapping behavior in browser tab navigation (cycling from last to first tab).

## Advantages and Limitations

### Advantages
1. **Continuous Traversal**: Allows for continuous traversal through all nodes without having to check for the end of the list.
2. **No Null Checking**: No need to check for null pointers when traversing.
3. **Efficient Rotation**: Rotation operations can be performed in O(1) time.
4. **Memory Efficiency**: No need to store end-of-list markers.
5. **Simplified Implementation**: Some operations are simpler compared to doubly linked lists.

### Limitations
1. **Risk of Infinite Loops**: If not implemented carefully, traversal can lead to infinite loops.
2. **Additional Complexity**: More complex to implement correctly than standard linked lists.
3. **No Direct End Access**: Without a tail pointer, finding the end requires O(n) traversal.
4. **No Backward Traversal**: In singly circular linked lists, backward traversal is inefficient.
5. **Deletion Complexity**: Deleting a node requires tracking the previous node.

## Implementation Details

Our implementation employs a singly circular linked list with the following design decisions:

1. **Tail Pointer**: Maintains a reference to the last node for O(1) append operations.
2. **Size Tracking**: Keeps track of size for O(1) length operations.
3. **Node Class**: Uses a separate Node class for clean encapsulation.
4. **Iteration Support**: Implements Python's iterator protocol for seamless iteration.
5. **Type Hints**: Employs type hints throughout for better code documentation and IDE support.
6. **Pythonic Interface**: Follows Python conventions with magic methods like `__len__`, `__iter__`, etc.
7. **Error Handling**: Comprehensive error handling for edge cases.
8. **Method Naming**: Uses consistent method naming that aligns with Python's built-in collections.

## Usage Examples

Here's a simple example demonstrating the basic operations:

```python
from circular_linked_list import CircularLinkedList

# Create a new circular linked list
cll = CircularLinkedList()

# Add elements
cll.append(1)
cll.append(2)
cll.append(3)
print(cll)  # Output: CircularLinkedList([1, 2, 3])

# Prepend an element
cll.prepend(0)
print(cll)  # Output: CircularLinkedList([0, 1, 2, 3])

# Insert at a specific position
cll.insert_at(2, 1.5)
print(cll)  # Output: CircularLinkedList([0, 1, 1.5, 2, 3])

# Remove an element
cll.remove(1.5)
print(cll)  # Output: CircularLinkedList([0, 1, 2, 3])

# Iterate through the list
print("Iterating through the list:")
for item in cll:
    print(item)

# Rotate the list
cll.rotate(2)
print(cll)  # Output: CircularLinkedList([2, 3, 0, 1])

# Get the size of the list
print(f"Size: {len(cll)}")  # Output: Size: 4

# Check if an element exists
print(f"Contains 2: {2 in cll}")  # Output: Contains 2: True
print(f"Contains 5: {5 in cll}")  # Output: Contains 5: False

# Clear the list
cll.clear()
print(cll)  # Output: CircularLinkedList([])
```

A more advanced example showing a round-robin scheduler:

```python
def round_robin_scheduler(tasks, time_quantum):
    """
    A simple round-robin task scheduler using a circular linked list.
    Each task gets a fixed time slice (quantum) before moving to the next.
    
    Args:
        tasks: List of task names
        time_quantum: Time slice for each task
    """
    from circular_linked_list import CircularLinkedList
    
    # Initialize tasks with their remaining time
    task_list = CircularLinkedList()
    for task in tasks:
        task_list.append({"name": task, "remaining_time": 10})  # Assume each task needs 10 time units
    
    current_time = 0
    
    # Process until all tasks are completed
    while not task_list.is_empty():
        current_task = next(iter(task_list))
        
        # Execute the task for the time quantum or until completion
        execution_time = min(time_quantum, current_task["remaining_time"])
        current_task["remaining_time"] -= execution_time
        current_time += execution_time
        
        print(f"Time {current_time}: Executed task '{current_task['name']}' for {execution_time} units")
        
        # If the task is completed, remove it from the list
        if current_task["remaining_time"] <= 0:
            task_list.remove(current_task)
            print(f"Task '{current_task['name']}' completed")
        else:
            # Rotate to the next task
            task_list.rotate(1)
```
