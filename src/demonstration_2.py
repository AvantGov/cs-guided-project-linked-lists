"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""


"""
UNDERSTAND: 
given the refernce to the head of a linked list, we want to reverse the list 
and return the new head 
    - this involves swapping the position of the tail and head 
    - and changing all of the pointers in the list 
    - we cannot just reverse the order, since it isn't really an "order" inherently 

PLAN 
# Simple and tail recursive Python program to 
# reverse a linked list 

# Node class 
class Node: 
	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 
	# Function to initialize head 

	def reverseUtil(self, curr, prev): 
		
		# If last node mark it head 			
			# Update next to prev node 

		
		# Save curr.next node for recursive call 


		# And update next 


	# This function mainly calls reverseUtil() 
	# with previous as None 



	# Function to insert a new node at the beginning 


	# Utility function to print the linked LinkedList 


"""

class LinkedListNode():
    # inits node object 
    def __init__(self, value):
        self.value = value
        self.next  = None

    def reverseUtil(self, current, previous):
        # if the current node in focus in the tail (.next is None), make that node the head
        # then update the previous node  
        if current.next is None:
            self.head = current
            current.next = previous 
            return 
        
        # create holder for the current node in focus's next item for use later 
        cur_nxt = current.next

        # change the current next to the previous item 
        current.next = previous

        
    # This function mainly calls reverseUtil() with previous as None 
    def reverse(self): 
        if self.head is None: 
            return 
        self.reverseUtil(self.head, None) 
  
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  

def reverse(head_of_list):
