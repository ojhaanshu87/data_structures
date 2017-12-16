class Solution(object):
  def __init__(self, str1, str2):
    self.str1 = str1
    self.str2 = str2

  def is_anagram(self):
    idx1 = []
    idx2 = []
    for elem1 in self.str1:
      idx1.append(ord(elem1) - ord('a'))
    for elem2 in self.str2:
      idx2.append(ord(elem2) - ord('a'))
    if sum(idx1) == sum(idx2):
      return True
    else:
      return False
