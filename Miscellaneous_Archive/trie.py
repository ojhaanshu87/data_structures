class TrieNode(object):
	def __init__(self):
		self.is_leaf = False
		self.children = [None]*26

class Trie(object):
	def __init__(self):
		self.root = self.get_node()

	def get_node(self):
		return TrieNode()

	def _char_to_idx (self, char):
		return ord(char)-ord('a')

	def insert_char(self, char):
		length = len (char)
		for elem in range(length):
			idx = self._char_to_idx(char[elem])
			if not self.root.children[idx]:
				self.root.children[idx] = self.get_node()
			self.root = self.root.children[idx]

		#mark last node as leaf	
		self.root.is_leaf = True

	def search_elem(self, char):
		length = len(char)
		for elem in range(length):
			idx = self._char_to_idx(char[elem])
			if not self.root.children[idx]:
				return False
			self.root = self.root.children[idx]

		return self.root != None and self.root.is_leaf()


# TIME COMPLEXITY -> INSERT :  O(average length of words * total number of words)
# TIME COMPLEXITY -> INSERT :  O(length of words)

# if __name__ == '__main__':
# 	keys = ["the","a","there","anaswe","any","by","their"]
# 	output = ["Not present in trie", "Present in trie"]
# 	trie_obj = Trie()
# 	for key in keys:
# 		trie_obj.insert_char(key)
# 	print("{} ---- {}".format("the",output[trie_obj.search_elem("the")]))
# 	print("{} ---- {}".format("the",output[trie_obj.search_elem("this")]))
 