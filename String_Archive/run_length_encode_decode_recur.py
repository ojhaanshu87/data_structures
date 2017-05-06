def run_len_encode(string):
	if not string:
		return ""
	else:
		last_char = string[0]
		max_index = len(string)
		elem = 1
		while elem < max_index and last_char == string[elem]:
			elem += 1
		return last_char + str(elem) + run_len_encode(string[elem:])


def run_len_decode(string):
	if not string:
		return ""
	else:
		char = string[0]
		quantity = string[1]
		return char * int(quantity) + run_len_decode(string[2:])