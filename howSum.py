"""
Write a function 'howSum(targetSum, numbers)' that takes in a
targetSum and an array of numbers as arguments.

The function should return an array containing any combination of
elements that add up to exactl the targetSum. If there is no
combination that adds up to the targetSum, then return null.


If there are multiple combinations possible, you may return any single
one.

"""

def base_howSum(targetSum, numbers):
    if(targetSum == 0): return []
    if(targetSum < 0): return None

    for i in range(len(numbers)-1):
      for j in range(i + 1, len(numbers)):
       if numbers[i] + numbers[j] == targetSum:
         print("Pair with sum", targetSum,"is: (", numbers[i], ",", numbers[j],")")



def howSum(targetSum, numbers):
    sum = []
    memo = {}

    for i in range(len(numbers)):
      remainder = targetSum - numbers[i]
      if remainder in memo:
          print("Pair with sum", targetSum, "is: (", numbers[i],",",remainder,")")
      memo[numbers[i]] = numbers[i]


print(howSum(7, [2,3]))
print(howSum(7, [5,3,4,7]))
print(howSum(7, [2,4]))
print(howSum(8, [2,3,5]))
#print(howSum(300, [7,14]))
