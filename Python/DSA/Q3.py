"""
WAP to calculate the sum of minimum and maximum element from input list.

Sample Input:
input_lst = [-2, 1, -4, 5, 3]

Sample Output:
1

"""


def findSum(input_lst, n):
    if n == 1:
        return input_lst[0]

    if input_lst[0] > input_lst[1]:
        maxi = input_lst[0]
        mini = input_lst[1]

    else:
        mini = input_lst[0]
        maxi = input_lst[1]

    for i in range(2, n):
        if input_lst[i] > maxi:
            maxi = input_lst[i]
        elif input_lst[i] < mini:
            mini = input_lst[i]

    return maxi + mini


input_lst = [1, 3, 4, 1]
n = len(input_lst)
result = findSum(input_lst, n)
print(f"Sum of max and min element = {result}")
