class Solution(object):
  def __init__(self, str1, str2):
    self.str1 = str1
    self.str2 = str2

  def is_anagram(self):
    idx1 = []
    idx2 = []
    sorted_str1, sorted_str2 = sorted(self.str1.lower()), sorted(self.str2.lower())
    #base case1
    if len(sorted_str1) <> len(sorted_str2):
      return False
    #base case2
    elif len(sorted_str1) is None or len(sorted_str2) is None:
      return False
    #convert into ord(sets) and compare sum of array
    else:
      for elem1 in sorted_str1:
        idx1.append(ord(elem1) - ord('a'))
      for elem2 in sorted_str2:
        idx2.append(ord(elem2) - ord('a'))
    if sum(idx1) == sum(idx2):
      return True
