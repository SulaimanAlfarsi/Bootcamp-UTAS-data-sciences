# Import the Stack class from the StackClass module
from StackClass1 import Stack

def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)

    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

# Test the reverse_string function with an input string
input_word = input("Enter any word: ")
reversed_word = reverse_string(input_word)
print("Reversed word:", reversed_word)
