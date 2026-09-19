# push() -> Adds a new element on the stack
# pop() -> Removes & returns the top element on the stack
# peek() -> Returns the top (last) element on the stack
# isEmpty() -> Check if the stack is empty
# size() -> Finds the number of elements in the stack


## Implementing Stack with Python List

stack = []

stack.append('A')
stack.append('B')
stack.append('C')
print('Stack: ', stack)

# Peek
topElement = stack[-1]
print('Peek: ', topElement)

# Pop
poppedElement = stack.pop()
print('Pop: ', poppedElement)

# Stack after pop
print('Stack after pop: ', stack)

# isEmpty

isEmpty = not bool(stack)
print('isEmpty: ', isEmpty)

# size
print('Size: ', len(stack))



