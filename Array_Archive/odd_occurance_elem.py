class Solution(object):
  def __init__(self, arr):
    self.arr = arr
  
  def odd_occourance(self):
    dict = {}
    for elem in self.arr:
      if elem in dict:
        dict[elem] +=1
      else:
        dict[elem] = 1
    for elem in zip(dict.keys(), dict.values()):
      if elem[1] %2 != 0:
        print elem[0]
