"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if not self.head:
      self.head = ListNode(value)
      self.tail = self.head
      self.length = 1
      return
    
    # self.old_head = self.head
    # self.new_head = ListNode(value)
    # self.new_head.next = self.old_head
    # self.old_head.prev = self.new_head
    # self.head = self.new_head

    self.head.insert_before(value)
    self.head = self.head.prev
    self.length += 1

  def remove_from_head(self):
    if not self.head and not self.tail:
      return False
    if self.length == 1:
      old_head = self.head
      self.head = None
      self.tail = None
      self.length = 0
      return old_head.value
    if self.length == 2:
      old_head = self.head
      self.head = self.tail
      self.length = 1
      return old_head.value
    else:
      self.old_head = self.head
      self.head = self.head.next
      self.length -= 1
      return self.old_head.value


  def add_to_tail(self, value):
    if not self.head and not self.tail:
      self.head = ListNode(value)
      self.tail = self.head
      self.length = 1
      return 

    # self.old_tail = self.tail
    # self.new_tail = ListNode(value)
    # self.new_tail.prev = self.old_tail
    # self.old_tail.next = self.new_tail
    # self.tail = self.new_tail

    self.tail.insert_after(value)
    self.tail = self.tail.next
    self.length += 1

  def remove_from_tail(self):
    if not self.head and not self.tail:
      return False
    if self.length == 1:
      old_tail = self.tail
      self.tail = None
      self.head = None
      self.length = 0
      return old_tail.value
    if self.length == 2:
      old_tail = self.tail
      self.tail = self.head
      self.length = 1
      return old_tail.value
    else:
      old_tail = self.tail
      self.tail = self.tail.prev
      self.length -= 1
      return old_tail.value

  def move_to_front(self, node):
    if self.tail == node:
      self.remove_from_tail()
      self.add_to_head(node.value)
    else:
      node.delete()
      self.length -= 1
      self.add_to_head(node.value)

  def move_to_end(self, node):
    if self.head == node:
      self.remove_from_head()
      self.add_to_tail(node.value)
    else:
      node.delete()
      self.length -= 1
      self.add_to_tail(node.value)

  def delete(self, node):
    if not self.head and not self.tail:
      return False
    if self.head == node:
      self.remove_from_head()
      node.delete()
      return
    if self.tail == node:
      self.remove_from_tail()
      node.delete()
      return
    node.delete()
    self.length -= 1
    
  def get_max(self):
    highest = 0
    current = self.head

    while current is not None:
      if current.value > highest:
        highest = current.value
      current = current.next
    return highest
