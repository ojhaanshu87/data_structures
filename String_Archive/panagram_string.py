#create empty list of 26 elem and assign False
#enter each entry ins tring and make crossponding True
#check if each entry is true then return yes else return no

class Solution(object):
  def __init__(self, string):
    self.string = string
    
  def check_panagram(self):
    list = []
    for elem in range(26):
      list.append(False)
      
    for char in self.string.lower(): 
      if not char == " ":
        list[ord(char) -ord('a')]=True
        
    for elem in list:
      if elem == False:
        return False
    return True

string = raw_input()

if (Solution(string).check_panagram()):
  print "pangram"
else:
  print "not pangram"
