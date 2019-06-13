class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # 0. append value to array:
    index = len(self.storage)
    self.storage.append(value)

    while index > 0:
      # 1. compare value to parent:
      parent = (index-1)//2
      # 2. if value > parent -> swap values 
      if self.storage[index] > self.storage[parent]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = (index-1)//2
      # 3. if value <= parent -> return 
      elif self.storage[index] <= self.storage[parent]:
        break


  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass
