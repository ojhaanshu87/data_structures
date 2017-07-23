''' 
MS Excel columns has a pattern like A B C Z AA AB AC AZ BA BB ZZ AAA AAB etc 
In other words, column 1 is named as A column 2 as B, column 27 as AA.

Given a column number, find its corresponding Excel column name. Following are more examples.

Input          Output
 26             Z
 51             AY
 52             AZ
 80             CB
 676            YZ
 702            ZZ
 705            AAC

Algorithm :

Steps: (suppose n is the number given)

  A)  take an empty string (say result)
  B)  find rem = n % 26
  C)  if rem is non-zero then
        result += 'A' + (rem - 1)
        set n = n / 26
  D)  else if rem is zero
        result += 'Z'
        set n = (n / 26) - 1
  E)   if n > 0, goto step B
  F)  otherwise, output reverse(string)

'''
MAX = 100
class Solution(object):
	def __init__(self, num):
		self.num = num

	def get_excel_column(self):
		# declare empty string
		string = ['\0']*MAX
		#store a result
		result = 0
		#till given num greater than 0
		while (self.num > 0):
			#find Rermainder 
			rem = self.num % 26
			# remainder is equals to 0
			if rem == 0:
				string[result] +='Z'
				result +=1
				self.num = (self.num / 26)-1
			else:
				string[result] = chr((rem-1) + ord('A'))
				result += 1
				self.num = self.num/26
		string[result] = '\0'
		# else Reverse string
		string = string[::-1]
		print "".join(string)

if __name__ == '__main__':
	solution = Solution(705)
	solution.get_excel_column()
 
