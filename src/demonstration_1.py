"""
Given only a reference to a specific node in a linked list, delete that node from a 
singly-linked list.

Example:

The code below should first construct a linked list (x -> y -> z) and then delete `y` 
from the linked list by calling the function `delete_node`. It is your job to write 
the `delete_node` function.

```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)
```

*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
"""

"""
UNDERSTAND: 
- we do not have access to the head or tail in this situation, just the given node 

- since we only have access to the given item, we will want to look at the next item,
replace the given item with the next item, then remove the next item and remove 
the pointer 
    - we are able to do this since accessing the next node also gives us
    access to the pointer of the next node as well 

PLAN 
- set the value of the node_delete to the value of node_delete.next.value 
- set the pointer node_delete.next to node_delete.next.next

these have to be done in this order so that we do not mess up operations 

"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def delete_node(node_to_delete):
    # set the value of the next item to the value of the current item 
    node_to_delete.value = node_to_delete.next.value
    # set the pointer of the current item to point to the pointer of the 
    # next item
    node_to_delete.next = node_to_delete.next.next



x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)
