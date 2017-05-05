import sys
import random

def sort_nuts_and_bolts(nuts, bolts):
    if(len(nuts) <= 0 or len(bolts) <= 0):
        # base case
        return [],[]
    
    pivot_nut = nuts[0]
    less_than_pivot_nut_pile = []
    greater_than_pivot_nut_pile = []
    bolt_equal_to_nut = None

    for bolt in bolts:
        if bolt > pivot_nut:
            greater_than_pivot_nut_pile.append(bolt)
        elif bolt < pivot_nut:
            less_than_pivot_nut_pile.append(bolt)
        else:
            bolt_equal_to_nut = bolt
    
    pivot_bolt = bolt_equal_to_nut
    less_than_pivot_bolts_pile = []
    greater_than_pivot_bolts_pile = []
    
    for nut in nuts:
        if nut > pivot_bolt:
            greater_than_pivot_bolts_pile.append(nut)
        elif nut < pivot_bolt:
            less_than_pivot_bolts_pile.append(nut)

    nuts_arr = []
    bolts_arr = []

    lower_nuts, lower_bolts = sort_nuts_and_bolts(less_than_pivot_nut_pile, less_than_pivot_bolts_pile)
    if(len(lower_nuts) > 0):
        for (n, b) in zip(lower_nuts, lower_bolts):
            nuts_arr.append(n)
            bolts_arr.append(b)
    
    nuts_arr.append(pivot_nut)
    bolts_arr.append(bolt_equal_to_nut) 

    upper_nuts, upper_bolts = sort_nuts_and_bolts(greater_than_pivot_nut_pile, greater_than_pivot_bolts_pile)
    if(len(upper_nuts) > 0):
        for (n, b) in zip(upper_nuts, upper_bolts):
            nuts_arr.append(n)
            bolts_arr.append(b)
    

    return nuts_arr, bolts_arr

