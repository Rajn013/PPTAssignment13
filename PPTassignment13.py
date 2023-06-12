#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Answer 1 .

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def Newlist(list1, list2):
    head = None
    Curr = None
     
    while list1 and list2:
        if list1.val >= list2.val:
            Node = list1
            list1 = list1.next
        else:
            Node = list2
            list2 = list2.next
            
            Node = Node.next
            
    Node = list1 or list2
    
    return head


# In[ ]:


def LinkedList(head):
    curr = head
    while curr:
        print(curr.val, end =" ")
        curr = curr.next
    print()
    
list1 = Node(5)
list1.next = Node(2)
list1.next.next = Node(3)
list1.next.next.next = Node(8)



list2 = Node(1)
list2.next = Node(7)
list2.next.next = Node(4)
list2.next.next.next = Node(5)


print("Linked List 1:")
LinkedList(list1)

print("Linked List 2:")
LinkedList(list2)

new_list = Newlist(list1, list2)

print("New Linked List:")
LinkedList(new_list)


# In[ ]:


list1 = Node(2)
list1.next = Node(8)
list1.next.next = Node(9)
list1.next.next.next = Node(4)



list2 = Node(5)
list2.next = Node(8)
list2.next.next = Node(9)
list2.next.next.next = Node(4)


print("Linked List 1:")
LinkedList(list1)

print("Linked List 2:")
LinkedList(list2)

new_list = Newlist(list1, list2)

print("New Linked List:")
LinkedList(new_list)


# In[ ]:


#Answer 2.

def Duplicate(head):
    if head is None:
        return head
    
    curr = head
    while curr.next is not None:
        if curr.val == curr.next.val:
            curr.next =curr.next.next
        else:
            curr = curr.next
            
    return head


# In[ ]:


def linkedlist(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()
    
    
head = Node(11)
head.next = Node(11)
head.next.next = Node(11)
head.next.next.next = Node(21)
head.next.next.next.next = Node(43)
head.next.next.next.next.next = Node(43)
head.next.next.next.next.next.next = Node(60)

print("Linked List before  removing duplicates:")
linkedlist(head)

new_head = Duplicate(head)

print("Linked List after removing duplicates:")
linkedlist(new_head)


# In[ ]:



head = Node(10)
head.next = Node(12)
head.next.next = Node(12)
head.next.next.next = Node(25)
head.next.next.next.next = Node(25)
head.next.next.next.next.next = Node(25)
head.next.next.next.next.next.next = Node(35)

print("Linked List before  removing duplicates:")
linkedlist(head)

new_head = Duplicate(head)

print("Linked List after removing duplicates:")
linkedlist(new_head)


# In[ ]:


#Answer 3.

def reverse_k_nodes(head, k):
    curr = head
    next_node = None
    prev = None
    count = 0

    while curr and count < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count += 1

    if next_node:
        head.next = reverse_k_nodes(next_node, k)

    return prev


# In[ ]:


head = Node(1)
node2 = Node(2)
node3 = Node(2)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

k = 4

print("original")
curr_node = head
while curr_node:
    print(curr_node.val, end=" -> ")
    curr_node = curr_node.next
print("None")


head = reverse_k_nodes(head, k)

print("modified")
curr_node =head
while curr_node:
    print(curr_node.val, end="")
    curr_node = curr_node.next


# In[ ]:


head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

k = 3

print("Original")
curr_node = head
while curr_node:
    print(curr_node.val, end=" -> ")
    curr_node = curr_node.next
print("None")

head = reverse_k_nodes(head, k)

print("Modified ")
curr_node = head
while curr_node:
    print(curr_node.val, end=" ")
    curr_node = curr_node.next


# In[ ]:


#Answer 4.

def reverse_alternate_k_nodes(head, k):
    curr = head
    prev = None
    next_node = None
    count = 0
    is_reverse = True

    while curr and count < k:
        next_node = curr.next

        if is_reverse:
            curr.next = prev
            prev = curr
        else:
            prev = curr

        curr = next_node
        count += 1

    
    if is_reverse and next_node:
        head.next = reverse_alternate_k_nodes(next_node, k)

    if prev and not is_reverse:
        prev.next = reverse_alternate_k_nodes(next_node, k)

    return prev if is_reverse else head


# In[ ]:


head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9

k = 3

print("Original")
current_node = head
while current_node:
    print(current_node.val, end=" -> ")
    current_node = current_node.next
print("None")

head = reverse_alternate_k_nodes(head, k)

print("Modified ")
current_node = head
while current_node:
    print(current_node.val, end=" -> ")
    current_node = current_node.next
print("None")


# In[ ]:


#Answer 5.

def deleteLastOccurrence(head, key):
    if not head:
        return None

    last = None
    prev_last = None

    prev = None
    curr = head

    while curr:
        if curr.val == key:
            last = curr
            prev_last = prev
        prev = curr
        curr = curr.next

    if last:
        if prev_last is None:
            head = last.next
        else:
            prev_last.next = last.next
        del last

    return head


# In[ ]:




head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(5)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(10)

key = 2
new_head = deleteLastOccurrence(head, key)

while new_head:
    print(new_head.val, end="->")
    new_head = new_head.next
print("None")


# In[ ]:


#Answer 6.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(a, b):
    dummy = Node()
    curr = dummy
    
    while a and b:
        if a.val <= b.val:
            curr.next = a
            a = a.next
        else:
            curr.next = b
            b = b.next
        curr = curr.next
        
    if a :
        curr.next = a
    if b :
        curr.next = b
        
    return dummy.next


# In[ ]:


a = Node(5)
a.next = Node(10)
a.next.next = Node(15)

b = Node(2)
b.next = Node(3)
b.next.next = Node(20)

merged = merge(a, b)

while merged:
    print(merged.val, end="->")
    merged = merged.next
print("None")


# In[ ]:


a = Node(1)
a.next = Node(1)

b = Node(2)
b.next = Node(4)

merged = merge(a, b)

while merged:
    print(merged.val, end="->")
    merged = merged.next
print("None")


# In[2]:


#Answer 7 .
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def reverse(head):
    if head is None or head.next is None:
        return head

    curr = head
    prev = None
    while curr:
        curr.next, curr.prev = curr.prev, curr.next
        prev = curr
        curr = curr.prev

    head = prev

    return head


# In[3]:


head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.next.next.next = Node(4)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(5)
head.next.next.next.next.prev = head.next.next.next

reversed_head = reverse(head)

while reversed_head:
    print(reversed_head.data, end=" <-> ")
    reversed_head = reversed_head.next
print("None")


# In[12]:


#Answer 8.

def deleteNode(head, position):
      if head is None:
        return None

      if position == 0:
        if head.next:
            head.next.prev = None
        return head.next

      curr = head
      
      for _ in range(position):
        curr = curr.next
        if curr is None:
            return head

 
      if curr.prev:
        curr.prev.next = curr.next
    
      if curr.next:
        curr.next.prev = curr.prev

       
      return head


# In[13]:


head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.next.next.next = Node(4)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(5)
head.next.next.next.next.prev = head.next.next.next

position = 2
new_head = deleteNode(head, position)

while new_head:
    print(new_head.data, end=" <-> ")
    new_head = new_head.next
print("None")


# In[14]:


head = Node(1)
node2 = Node(5)
node3 = Node(2)
node4 = Node(9)

head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

x = 1

new_head = deleteNode(head, x)

while new_head:
    print(new_head.data, end=" <-> ")
    new_head = new_head.next
print("None")


# In[ ]:




