"""
WAP to count the occurance of each element in input list.

Sample Input:
input_lst = [[1,2],[3,4],[2,3],[5,1],[7,1,2]]

Sample Output:
{1:3, 2:3, 3:2, 4:1, 5:1, 7:1}

"""
def countOccurance(input_lst):
    dict = {}
    for lst in input_lst:
        for element in lst:
            if element in dict:
                dict[element] += 1
            else:
                dict[element] = 1

    return dict

input_lst = [[1,2],[3,4],[2,3],[5,1],[7,1,2]]
print(countOccurance(input_lst))