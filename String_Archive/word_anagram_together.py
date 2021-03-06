class Solutions():
  def __init__(self, list_of_str):
    self.str_list = list_of_str

  def word_anagram_together(self):
    dict_str_ascii, new_dict, result = {}, {}, []
    for word in self.str_list:
      sum_char = 0
      for elem in word:
        char_ascii = ord(elem) - ord("a")
        sum_char += char_ascii
      dict_str_ascii[word] = sum_char
    for ascii, word_list in dict_str_ascii.iteritems():
      new_dict.setdefault(word_list, []).append(ascii)

    for key, value in new_dict.iteritems():
      if len(value) > 1:
        result.append(value)
    return result

#[['ngi', 'ing'], ['cba', 'bca', 'cab']]
print Solutions(['cab', 'nye', 'ing', 'bca', 'zyx', 'cba', 'ngi', 'nyee']).word_anagram_together()
