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
    arr = self.storage
    deleted = arr[0]

    # 0. "remove" first array element, store it in a variable
    arr[0] = arr.pop()
    parent = 0
    left, right = 1, 2

    # 1. while element has children:
    while arr[left]:
      # 1a. check & compare each child
      if arr[left] and arr[right]:
        if arr[left] > arr[right]:
          # 1b. swap priority child and parent
          arr[parent], arr[left] = arr[left], arr[parent]
          parent = left
        else:
          arr[parent], arr[right] = arr[right], arr[parent]
          parent = right
      elif arr[left]:
        arr[parent], arr[left] = arr[left], arr[parent]
        parent = left

      left = (parent*2) + 1
      right = (parent*2) + 2
      if left > len(arr):
        break

    # 2. return topmost value
    return deleted



  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    print(f'ARRAY: {self.storage}')
    if index == 0:
      return
    while index > 0:
      # index is 'right' child
      if index % 2 == 0:
        parent = (index - 2) / 2
      # index is 'left' child
      elif index % 2 == 1:
        parent = (index - 1) // 2
      if self.storage[index] > self.storage[parent]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
      elif self.storage[index] <= self.storage[parent]:
        print(f'BUBBLED UP: {self.storage}')
        return
      index = parent

  def _sift_down(self, index):
    arr = self.storage
    left = (index*2) + 1
    right = (index*2) + 2

    while left < len(arr):
      if arr[index] < arr[left] or arr[index] < arr[right]:
        if arr[left] >= arr[right]:
          arr[index], arr[left] = arr[left], arr[index]
          index = left
        else:
          arr[right], arr[index] = arr[index], arr[right]
          index = right
      else:
        return
      
      left = (index*2) + 1
      right = (index*2) + 2
    
    return