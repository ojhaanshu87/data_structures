def  all_prime_factors(number):
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

def power_set_from_prime_factors(number):
	seq_set = all_prime_factors(number)
	return [[seq_set[j] for j in range(len(seq_set)) if (i&(1<<j))] for i in range(1<<len(seq_set))]

def prod_within_list (complete_list):
	product =1
	for elem in complete_list:
		product = product*elem
	return product

def closet_multiplier_set_from_target (number, target):
	all_possible_combination = power_set_from_prime_factors(number)
	multiplication_val_with_diff = {}
	for elem in range (1, len (all_possible_combination)):

		multiplication_val = prod_within_list(all_possible_combination[elem])
		multiplication_val_with_diff[multiplication_val] = abs(target- multiplication_val)
	return min(multiplication_val_with_diff, key=multiplication_val_with_diff.get)
