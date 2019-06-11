class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value == None:
      self = BinarySearchTree(value)

    current = self
    while current.value is not None:

      if value < current.value:
        if current.left == None:
          current.left = BinarySearchTree(value)
          return
        current = current.left
      elif value > current.value:
        if current.right == None:
          current.right = BinarySearchTree(value)
          return
        current = current.right

    # 0. check current_node value
    # 1a. if new node is greater than root -> move down right side 
    # 1b. if new node is less than root -> move down left side 
    # 2. if no child exists (None), current_node.side = new_node.value
    #   2a. new_node.left = None
    #   2b. new_node.right = None
    # 3. continue (repeat)

  def contains(self, target):
    current = self

    while current.value is not None:
      if target == current.value:
        return True
      if target < current.value:
        if current.left == None:
          return False
        current = current.left
      elif target > current.value:
        if current.right == None:
          return False
        current = current.right

    # 0. while current_val is not None
    # 1. if val == current_val -> return True
    # 1a. if value is greater than current_val -> move down right side
    # 1b. if value is less than current_val -> move down left side
    # 2. return false

  def get_max(self):
    if self.value == None:
      return False
    current = self
    highest_val = current.value

    while current.value is not None:
      highest_val = current.value
      if current.right == None:
        return highest_val
      current = current.right
      
    # 0. if current.value == None -> return False
    # 1. if current.right == None -> return max_val
    # 2. if current.right is not None -> current = current.right

  def for_each(self, cb):
    pass