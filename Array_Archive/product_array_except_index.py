#return product element inside list except index

def prod_array(arr):
	prod = 1
	for elem in arr:
		prod *=elem
	final_prod = [prod/elem for elem in arr]
	return final_prod