"""
    Grid Traveller implementation

Say that you are a traveller on a 2D grid. You begin in the top-left
corner and your goal is to travel to the bottom-right corner. You may
only move down or right.

In how many ways can you travel to the goal on a grid with dimensions
m * n?

Write a function gridTraveller(m,n) that calculates this ex:

gridTraveler(2,3) -> 3
Because
1. right, right, down
2. right, down, right
3. down, right, right

gridTraveler(1,1) -> 1
(the start is the end)

gridTraveler(0,1) -> 0
gridTraveler(1,0) -> 0
(there is  no grids)


The recursive nature can be defined as such,
when travelling down, the function calls would reduce the amount of rows
when travelling  right, the function calls would reduce the amount of columns
"""



def gridTraveller_without_memoization(m, n):
   """
   See above for what this is solving.
   The run time of this function is O(2^m+n)
   The space complexity is O(m+n)
   """
   # Base case
   if (m == 1 and n == 1):
     return 1
   
   if (m == 0 or n == 0):
     return 0

   # down  - reduce rows, right - reduce columns
   return gridTraveller_without_memoization(m - 1,n) + gridTraveller_without_memoization(m, n-1)




def gridTraveller(m,n, memo={}):
    """
    See above for what this is solving.
    This version makes sense of memoization
    The run time of this function is O(m*n)
    The space complexity is O(m+n)
    """
   # Are the arguments in the memo
    key = str(m) + ',' + str(n)
    if key in memo:
      return memo[key]
    elif (m == 1 and n ==1):
      return 1
    elif (m == 0 or n == 0):
      return 0
    else:
      memo[key] = gridTraveller(m-1,n) + gridTraveller(m, n-1)
      return memo[key]

print(gridTraveller(0,1))
print(gridTraveller(1,1))
print(gridTraveller(2,3))
print(gridTraveller(3,2))
print(gridTraveller(3,4))
print(gridTraveller(18,18))

if __name__ == "__main__":
   testData = (2,3)
   expected = 3

   # if you running this with a large  grid , i.e . like an 18x18
   # The run time would be a lot higher
   got = gridTraveller_without_memoization(testData[0],testData[1])
   print(got)

   assert got == expected, "Values did not match"


   testMemo = (18,18)
   expectedMemo = 2333606220

   got = gridTraveller(testMemo[0], testMemo[1])
   print(got)

   assert expectedMemo == got, "Values did not match"

