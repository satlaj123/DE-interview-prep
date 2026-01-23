"""
WAP to transform the month number in the input list to month name as shown in the output list.

Sample Input:
lst_data = ['01-01-2020', '21-03-2022','11-06-2023','12-12-2020']

Sample Output:
['01-Jan-2020', '21-Mar-2022','11-Jun-2023','12-Dec-2020']

"""


def repplaceMonth(input_lst):
    dict_month = {"01": "Jan", "02": "Feb", "03": "Mar", "06": "Jun", "12": "Dec"}
    result_lst = []
    for date_ in input_lst:
        month_number = date_.split("-")
        month_name = dict_month[month_number[1]]
        result_lst.append(month_number[0] + "-" + month_name + "-" + month_number[2])
    return result_lst


lst_data = ["01-01-2020", "21-03-2022", "11-06-2023", "12-12-2020"]
print(repplaceMonth(lst_data))
