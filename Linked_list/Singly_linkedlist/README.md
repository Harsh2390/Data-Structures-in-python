# Singly Linked List Implementation in Python
## Introduction
This repository contains a Python implementation of a singly linked list, a fundamental data structure that consists of a sequence of elements, each contained in a node. The nodes are connected via pointers, with each node pointing to the next node in the sequence. This implementation provides a basic yet comprehensive understanding of how singly linked lists function, including operations such as insertion, deletion, and traversal.

## Features
*Node Creation: Define individual nodes containing data and a pointer to the next node.
*Add Front: Insert a new node at the beginning of the list.
*Append: Add a new node at the end of the list.
*Remove Front: Remove the node at the beginning of the list.
*Display: Print the entire list to show its contents.
*Length: Return the total number of nodes in the list.
*Get Index: Find the position of a node with specified data.
*Front and Back Access: Retrieve the first and last node of the list.

### Installation
No additional libraries are required to use this singly linked list implementation. Ensure you have Python installed on your system. Simply clone this repository or copy the linkedlist.py file into your project.

### Usage
To use this singly linked list in your project, import the Linkedlist class from the linkedlist.py file. Here's a quick example to get you started:
'''
from linkedlist import Linkedlist

# Create a new Linked List
my_list = Linkedlist()

# Add elements
my_list.append(10)
my_list.addFront(5)
my_list.append(15)

# Display the list
my_list.display()

# Remove the front element
my_list.removeFront()

# Display the list again
my_list.display()

# Print the length of the list
my_list.length()

# Get the index of a data item
my_list.getindex(15)
'''
