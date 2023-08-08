from StackClass import Stack

# Create an object of the Stack class
my_stack = Stack()

# Check if the stack is empty
print("Is the stack empty?", my_stack.isEmpty())

# Push elements (1, 2, 3, 4, 5) into the stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)

# Peek the topmost element in the stack
print("Peek element in the stack:", my_stack.peek())

# Get the stack elements
print("Stack elements:", my_stack.get_stack())

# Delete two elements from the stack
my_stack.pop()
my_stack.pop()

# Show the remaining elements of the stack
print("Remaining elements in the stack:", my_stack.get_stack())
