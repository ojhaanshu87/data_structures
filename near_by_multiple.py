def  all_multiples(number):
    elem = 2
    factors = []
    while elem * elem <= number:
        if number % elem:
            elem += 1
        else:
            number //= elem #divide with integral result (discard remainder)
            factors.append(elem)
    if number > 1:
        factors.append(number)
    return factors

#https://math.stackexchange.com/questions/910716/how-many-ways-to-generate-unique-multiplication-result-from-given-set

def possible_combination(number):
	seq_set = all_multiples(number)
	return [[seq_set[j] for j in range(len(seq_set)) if (i&(1<<j))] for i in range(1<<len(seq_set))]

def prod_within_list (complete_list):
	product =1
	for elem in complete_list:
		product = product*elem
	return product

def closet_multiplier_set_from_target (number, target):
	all_possible_combination = possible_combination(number)
	multiplication_val_with_diff = {}
	for elem in range (1, len (all_possible_combination)):

		multiplication_val = prod_within_list(all_possible_combination[elem])
		multiplication_val_with_diff[multiplication_val] = abs(target- multiplication_val)
	return min(multiplication_val_with_diff, key=multiplication_val_with_diff.get)


# obj = closet_multiplier_set_from_target(13148, 100)
obj = all_multiples(13148)
print obj
