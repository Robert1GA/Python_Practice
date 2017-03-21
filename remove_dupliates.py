num1 = [2,4,7,9,3,4,3,9,9,8]
num2 = [5,5,-2,2]
num3 = [2,-2,0,0,5]
num4 = [2.4,2.5,2.6,2.7,2.4]
num5 = []
num6 = ['a', 0, 'a']

def remove_dupes(numbers):
  # empty list to put the results into
  results = []
  for num in numbers:
    # check to make sure it is a number
    if type(num) != int and type(num) != float:
      # immediately return error if it comes across one non-number
      return('Not a list of numbers')
    if num not in results:
      # if the number doesn't already exist in results, then append it
      results.append(num)
  return results

print(remove_dupes(num1))
print(remove_dupes(num2))
print(remove_dupes(num3))
print(remove_dupes(num4))
print(remove_dupes(num5))
print(remove_dupes(num6))
