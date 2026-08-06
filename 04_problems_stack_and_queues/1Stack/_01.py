# Declaration: we will just use a list
stack = []

# Pushing elements:
stack.append(1)
stack.append(2)
stack.append(3)

# Popping elements:
stack.pop() # 3
stack.pop() # 2

# Check if empty
not stack # False

# Check element at top
stack[-1] # 1

# Get size
len(stack) # 1

"""
A stack is an ordered collection of elements where elements are only added and removed from the same end.
In the physical world, an example of a stack would be a stack of plates in a kitchen - 
you add plates or remove plates from the top of the pile.

Another term used to describe stacks is LIFO, which stands for last in, first out. 
The last (most recent) element placed inside is the first element to come out.

Stacks and recursion are very similar. This is because recursion is actually done using a stack. 
Function calls are pushed on a stack. The call at the top of the stack at any given moment is the 
"active" call. On a return statement or the end of the function being reached, the current call 
is popped off the stack.
"""