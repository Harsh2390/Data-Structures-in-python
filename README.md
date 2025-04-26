# Data Structures in python
## Overview
This repository contains Python implementations of common data structures with comprehensive documentation and unit tests. Each data structure is thoroughly explained with time and space complexity analysis, real-world applications, advantages, disadvantages, and visual representations where applicable.

## Purpose
This repository serves as:

* A learning resource for understanding fundamental data structures
* A reference for Python implementations with proper type hints and docstrings
* A showcase of clean, well-documented code following best practices
* A practical guide to data structure selection based on operational requirements

## Repository Structure
```
data-structures-python/
│
├── README.md                 # This file
├── .gitignore                # Standard Python gitignore
│
├── arrays/                   # Array-based structures
│   ├── README.md             # Overview of array structures
│   ├── static_array/
│   │   ├── README.md         # Documentation for static arrays
│   │   ├── static_array.py   # Implementation
│   │   └── test_static_array.py  # Unit tests
│   └── dynamic_array/
│       ├── ...
│
├── linked_structures/        # Linked structures
│   ├── README.md
│   ├── singly_linked_list/
│   │   ├── ...
│   └── ...
│
└── ...
```
## Each Structure Features
For each data structure, you'll find:

1. Comprehensive README:

    * Definition and conceptual explanations
    * Visual representations
    * Real-world applications
    * Advantages and disadvantages
    * Time complexity analysis for all operations
    * Space complexity analysis
    * Comparisons with similar structures


2. Clean Implementation:

    * Well-documented Python code with type hints
    * Comprehensive docstrings
    * Error handling
    * Usage examples


3. Unit Tests:

    * Tests for all operations
    * Edge case coverage

## Installation

```
# Clone the repository
git clone https://github.com/Harsh2390/Data-Structures-in-python.git

# Navigate to the repository directory
cd data-structures-python

# Optional: Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install any dependencies (if applicable)
pip install -r requirements.txt
```

## Usage
Each data structure can be imported and used independently:
```
# Example: Using a singly linked list
from linked_structures.singly_linked_list.singly_linked_list import SinglyLinkedList

# Create a new list
my_list = SinglyLinkedList()

# Add elements
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Display the list
print(my_list)  # Output: 1 -> 2 -> 3 -> None

# Get the length
print(len(my_list))  # Output: 3
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.