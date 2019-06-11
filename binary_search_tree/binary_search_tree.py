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


    # self.value = value
    # self.left = None
    # self.right = None

    # 1. check current_node value
    # 2. if new node is greater than root -> move down right side 
    # 3. if new node is less than root -> move down left side 
    # 4. if no child exists (None), current_node.side = new_node.value
    #   4a. new_node.left = None
    #   4b. new_node.right = None
    # 5. continue (repeat)

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass