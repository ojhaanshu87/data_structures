class Solution(object):
  def __init__(self):
     self.val = None
     
  def print_anagram(self, word_list):
    word_dict ={}
    for word in word_list:
      word_dict.setdefault(''.join(sorted(word)), []).append(word)
    for k, v in word_dict.items():
      if len(v) >1:
        print v[0],

#cab ing
obj = Solution().print_anagram(['cab', 'nye', 'ing', 'bca', 'zyx', 'cba', 'ngi', 'nyee'])
