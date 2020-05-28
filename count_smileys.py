"""
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
Rules for a smiling face:
-Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
-A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
-Every smiling face must have a smiling mouth that should be marked with either ) or D.
No additional characters are allowed except for those mentioned.
"""

def count_smileys(arr):
  count = 0
  if len(arr) == 0:
    count = 0
  for i in arr:
    if len(i) == 2:
      if (i[0] == ':' or i[0] == ";") and (i[1] == ')' or i[1] == 'D'): 
        count+=1
    if len(i) == 3:
      if (i[0] == ':' or i[0] == ";") and (i[1] == '~' or i[1] == '-') and (i[2] == ')' or i[2] == 'D'): 
        count+=1   
  return count  

