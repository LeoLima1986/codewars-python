"""
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case 

"""

def countBits(n):
  binary_num = ""
  count = 0
  ans = []
  
  while n != 0:
    binary_num = str(n%2) + binary_num
    n = n // 2
  ans = list(binary_num)

  for i in ans:
   count+= int(i)
  return count
     
print(countBits(1234)) # 5
