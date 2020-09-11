class Solution():
  def init(self):
    self.val = None

  def closing_parenthesis_indices(self, sentence, open_paren_idx): 
    open_parenthesis_indices = 0
    pos_close_parenthesis = open_paren_idx + 1
    while pos_close_parenthesis <= len(sentence) - 1:
      char = sentence[pos_close_parenthesis]
      if char == '[':
        open_parenthesis_indices += 1
      elif char == ']':
        if open_parenthesis_indices == 0:
          return pos_close_parenthesis
        else: open_parenthesis_indices -= 1
      pos_close_parenthesis += 1
    return pos_close_parenthesis
  
print Solution().closing_parenthesis_indices("[ABC[23]][89]", 0)
