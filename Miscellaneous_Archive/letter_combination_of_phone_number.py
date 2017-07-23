'''

Before advent of QWERTY keyboards, texts and numbers were placed on the same key. 
For example 2 has “ABC” if we wanted to write anything starting with ‘A’ we need to type key 2 once.
 If we wanted to type ‘B’, press key 2 twice and thrice for typing ‘C’

Given a keypad as shown in as dictionary, and a n digit number, list all words which are possible by pressing these numbers.
For example if input number is 234, possible words which can be formed are (Alphabetical order):
adg adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg cdh cdi ceg ceh cei cfg cfh cfi

'''

class Solution(object):
    def __init__(self):
        self.dec = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
        '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r', 's'], '8':['t','u','v'],
        '2':['w','x','y', 'z']}

    def letter_comb_util(num, curr, res, line):
        if len(line) == len(num):
            res.append(''.join([x for x in line]))
            return res
        for elem in self.dec[num[curr]]:
            line.append(elem)
            self.letter_comb_util(num, curr+1, res, line)
            line.pop()

    def letter_comb(self, num):
        if not num:
            return []
        #backtracking
        res = []
        line =[]
        self.letter_comb_util(num, 0, res, line)
        return res

# Time Complexity : O(2 ^n)
# Space Complexity : O(n)