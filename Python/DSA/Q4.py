"""
WAP to seprate the digits from the given string.

Sample Input:
input = "a1 b2 c3"

Sample Output:
1 2 3

"""

x = "a1 b2 c3"
n1, n2, n3 = list(map(lambda s: int(s[-1]), x.split()))
print(n1)
print(n2)
print(n3)
