# Your goal in this kata is to implement an difference function, which subtracts one list from another.
#
# It should remove all values from list a, which are present in list b.
#
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
#
# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    #your code here
    diff = []
    for i in a:
      if i not in b:
        diff.append(i)
    return diff

a = [1,2,3,4,9,6]
b = [2,4,4,6,7,8]
print(array_diff(a,b))
