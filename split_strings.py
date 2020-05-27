"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of 
characters then it should replace the missing second character of the final pair with an underscore ('_').
"""
def solution(n):
  newlist = []
  if len(n) % 2 != 0:
    n+="_"
  for i in range(0,len(n),2):
    newlist.append(n[i:i+2])
  return newlist
  
print(split_pairs("abcd"))  # == ['ab', 'cd']
print(split_pairs("abc"))  # == ['ab', 'c_']
print(split_pairs("abcdf"))  # == ['ab', 'cd', 'f_']
print(split_pairs("a"))  # == ['a_']
print(split_pairs(""))  # == []
