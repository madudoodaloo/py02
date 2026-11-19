
"""
eval notes:
|| ex0/ft_command_quest.py
|| Authorized: import sys, sys.argv, len(), print() ||

questions:
how do you access cmdline params and in what data structure are they stored? 
through sys module - and they're stored in lists

what's a list?
a built-in data structure used to store an ordered collection of items. They are 
dynamic, resizable and capable of storing multiple data types. 

any notes on how we can access its elements?
the list's elements:
- are accessed using indexing, both zero-based indexing and negative indexing. 
- maintain the order in which they are inserted.
- can be changed, updated, added, or removed after the list is created

how can you create a list?
- Using Square Brackets
a = [1, 2, 3]

- Using list() Constructor: A list can also be created by passing an iterable 
(such as tuple, string or another list) to the list() constructor.
a = list((1, 2, 3, 'apple', 4.5)) = [1, 2, 3, 'apple', 4.5]
b = list("GFG") = ['G', 'F', 'G']

- Creating List with Repeated Elements: A list with repeated elements can be created using the multiplication (*) operator.
a = [2] * 5 = [2, 2, 2, 2, 2]

how do lists work behind the curtains?
through references to object, not the actual values directly.
- The list keeps memory addresses of objects -> the actual objects exist separately in memory.
- Modifying a mutable object inside a list changes the original object.
- Reassigning an immutable object creates a new object instead of changing the old one

list.methods
    append(): Adds an element at the end of the list.
    insert(index, element): Adds an element at a specific position.
    extend(): Adds multiple elements to the end of the list.
    remove(): Removes the first occurrence of an element.
    pop(): Removes the element at a specific index or the last element if no index is specified.
    clear(): Removes all items
    del statement: Deletes an element at a specified index. del a[1]

    
https://www.geeksforgeeks.org/python/python-lists/
https://www.w3schools.com/python/python_lists.asp

"""
