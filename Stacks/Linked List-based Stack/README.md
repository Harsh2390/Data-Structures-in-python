# Linked List-based Stack

## Definition and Overview

A stack is a fundamental abstract data type that follows the Last-In-First-Out (LIFO) principle. In a stack, the last element added is the first one to be removed. It is named "stack" as it resembles a physical stack of objects, where you can only add or remove items from the top.

A Linked List-based Stack uses a singly linked list as the underlying data structure to implement the stack operations. Each element in the stack points to the element beneath it, with the bottom element pointing to `None`.

```
ASCII Art Visualization:

   Top of Stack
       │
       ▼
    ┌─────┐
    │  A  │
    └─────┘
       │
       ▼
    ┌─────┐
    │  B  │
    └─────┘
       │
       ▼
    ┌─────┐
    │  C  │
    └─────┘
       │
       ▼
     None
```

## Mathematical/Theoretical Foundation

A stack is formally defined as a collection of elements with two main operations:
- **push**: Adds an element to the top of the stack
- **pop**: Removes the element from the top of the stack

A stack can be mathematically represented as a sequence of elements S = (a₁, a₂, ..., aₙ) where aₙ is the top of the stack. After a `push(x)` operation, the stack becomes S' = (a₁, a₂, ..., aₙ, x). After a `pop()` operation, the stack becomes S' = (a₁, a₂, ..., aₙ₋₁).

## Time and Space Complexity Analysis

### Operations

1. **push(element)** - Add an element to the top of the stack
   - Best, Average, Worst case: O(1)
   - This operation simply creates a new node and updates the reference to the top of the stack.

2. **pop()** - Remove and return the top element from the stack
   - Best, Average, Worst case: O(1)
   - This operation updates the reference to the top of the stack.

3. **peek()** - Return the top element without removing it
   - Best, Average, Worst case: O(1)
   - This operation just returns the value at the top of the stack.

4. **is_empty()** - Check if the stack is empty
   - Best, Average, Worst case: O(1)
   - This operation simply checks if the top reference is None.

5. **size()** - Return the number of elements in the stack
   - Best, Average, Worst case: O(1)
   - This operation returns the size counter that is maintained during push and pop operations.

### Space Complexity

- The space complexity for storing n elements in the stack is O(n).
- Each element in the linked list stack requires additional space for the reference to the next node, making it slightly less space-efficient than an array-based implementation.

## Real-world Applications and Example Use Cases

1. **Function Call Stack**: Programming languages use stacks to manage function calls and returns.
2. **Expression Evaluation**: Used in arithmetic expression evaluation and syntax parsing.
3. **Undo Mechanism**: Applications like text editors use stacks to implement undo functionality.
4. **Browser History**: Web browsers use stacks to navigate back through previously visited pages.
5. **Backtracking Algorithms**: Used in algorithms like maze solving, puzzle solving, and graph traversal.
6. **Parentheses Matching**: Used to check if parentheses are balanced in expressions.

## Advantages and Limitations

### Advantages
1. **Dynamic Size**: A linked list implementation allows the stack to grow and shrink as needed.
2. **Efficient Implementation**: All operations have constant time complexity O(1).
3. **No Overflow**: Unlike array-based implementations, a linked list stack won't overflow (unless memory is exhausted).
4. **Memory Efficiency**: Memory is allocated as needed.

### Limitations
1. **Extra Memory**: Each element requires additional memory for the reference (compared to array-based stacks).
2. **No Random Access**: Elements other than the top cannot be accessed directly.
3. **Cache Performance**: Linked list nodes may be scattered in memory, potentially resulting in more cache misses compared to contiguous array storage.

## Implementation Details and Design Decisions

1. **Node-based Structure**: Each element in the stack is represented by a node containing the data and a reference to the next node.
2. **Top Reference**: A reference to the top node is maintained to achieve O(1) time complexity for all operations.
3. **Size Tracking**: A counter is maintained to provide O(1) time complexity for the size operation.
4. **Type Hints**: Python's type hints are used throughout to improve code readability and developer experience.
5. **Iterator Implementation**: The stack implements iterator protocols for convenient traversal of elements from top to bottom.
6. **Exception Handling**: Custom exceptions are used for error conditions like popping from an empty stack.

## Code Sample: Typical Usage Patterns

```python
# Creating a new stack
stack = LinkedListStack()

# Pushing elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Checking the top element
top_element = stack.peek()  # Returns 30

# Checking the size
size = len(stack)  # Returns 3

# Popping elements from the stack
popped = stack.pop()  # Returns 30
popped = stack.pop()  # Returns 20

# Checking if the stack is empty
is_empty = stack.is_empty()  # Returns False

# Iterating through the stack (from top to bottom)
for item in stack:
    print(item)  # Prints 10

# String representation
print(stack)  # Prints "LinkedListStack([10])"
```
