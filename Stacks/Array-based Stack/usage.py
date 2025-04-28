"""
Example usage of the Array-based Stack implementation.
"""

from stack import ArrayStack, EmptyStackError

def balanced_parentheses(expression: str) -> bool:
    """
    Check if an expression has balanced parentheses using a stack.
    
    Args:
        expression: A string containing parentheses, brackets, and braces.
        
    Returns:
        True if all opening brackets have matching closing brackets in the correct order,
        False otherwise.
    """
    stack = ArrayStack[str]()
    
    # Dictionary to store the matching pairs
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        # If it's an opening bracket, push to stack
        if char in '({[':
            stack.push(char)
        # If it's a closing bracket
        elif char in ')}]':
            # If stack is empty or brackets don't match
            if stack.is_empty() or stack.pop() != brackets[char]:
                return False
    
    # If stack is empty, all brackets were matched
    return stack.is_empty()

def reverse_string(input_str: str) -> str:
    """
    Reverse a string using a stack.
    
    Args:
        input_str: The string to reverse.
        
    Returns:
        The reversed string.
    """
    stack = ArrayStack[str]()
    
    # Push each character onto the stack
    for char in input_str:
        stack.push(char)
    
    # Pop characters from the stack to get the reversed string
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

def convert_decimal_to_binary(decimal_num: int) -> str:
    """
    Convert a decimal number to binary using a stack.
    
    Args:
        decimal_num: A non-negative integer in decimal.
        
    Returns:
        The binary representation as a string.
    """
    if decimal_num == 0:
        return "0"
    
    stack = ArrayStack[int]()
    
    # Process the decimal number
    while decimal_num > 0:
        remainder = decimal_num % 2
        stack.push(remainder)
        decimal_num //= 2
    
    # Construct the binary string
    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())
    
    return binary

def main():
    print("=== Stack Examples ===\n")
    
    # Example 1: Basic stack operations
    print("Example 1: Basic stack operations")
    stack = ArrayStack[int]()
    
    print(f"Is empty: {stack.is_empty()}")
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print(f"Stack after pushing 10, 20, 30: {stack}")
    print(f"Size: {len(stack)}")
    print(f"Top element: {stack.peek()}")
    
    popped = stack.pop()
    print(f"Popped: {popped}")
    print(f"Stack after popping: {stack}")
    
    stack.clear()
    print(f"Stack after clearing: {stack}")
    print()
    
    # Example 2: Checking balanced parentheses
    print("Example 2: Checking balanced parentheses")
    expressions = [
        "((()))",
        "{[()]}",
        "({[}])",
        "(((",
        "(){}[]"
    ]
    
    for expr in expressions:
        print(f"'{expr}' is balanced: {balanced_parentheses(expr)}")
    print()
    
    # Example 3: Reversing a string
    print("Example 3: Reversing a string")
    strings = ["hello", "Python", "stack"]
    
    for s in strings:
        print(f"'{s}' reversed is '{reverse_string(s)}'")
    print()
    
    # Example 4: Converting decimal to binary
    print("Example 4: Converting decimal to binary")
    numbers = [0, 2, 5, 10, 42, 255]
    
    for num in numbers:
        print(f"{num} in binary is {convert_decimal_to_binary(num)}")
    print()
    
    # Example 5: Iteration
    print("Example 5: Iteration")
    char_stack = ArrayStack[str]()
    chars = list("STACK")
    
    for char in chars:
        char_stack.push(char)
    
    print("Iterating through stack (top to bottom):")
    for char in char_stack:
        print(char, end=" ")
    print("\n")
    
    # Example 6: Error handling
    print("Example 6: Error handling")
    empty_stack = ArrayStack[float]()
    
    try:
        empty_stack.pop()
    except EmptyStackError as e:
        print(f"Error caught: {e}")
    
    try:
        empty_stack.peek()
    except EmptyStackError as e:
        print(f"Error caught: {e}")

if __name__ == "__main__":
    main()