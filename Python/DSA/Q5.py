"""
Given an array arr of n non-negative integers, WAP to find a non-negative
integer that is not in the array.

Sample Input:
lst = [0, 1, 2, 3, 4, 5, 7, 8, 9]
Output:
6

lst = [0, 1, 6, 2, 7, 5, 4]
Output:
3

"""


def find_missing_number(lst):
    ans = {}
    for element in lst:
        ans[element] = True

    for val in range(len(ans) + 1):
        if not ans.get(val):
            return val

    return None


lst = [0, 1, 2, 3, 4, 5, 7, 8, 9]
result = find_missing_number(lst)
print(f"The missing number in the given list {lst} = {result}.")
