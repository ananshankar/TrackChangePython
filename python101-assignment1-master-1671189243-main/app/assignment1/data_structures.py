def min_max_value():
    """
    Get the keys of minimum and Max value from the below dictionary.
    :return: {'max_key': 'Sam', 'min_key': 'Andrew'}
    """
    dictionary = {"Kelly":25,"John":30,"Andrew":21,"Sam":32,"Suzane":22}
    youngest = min(dictionary, key=dictionary.get)
    oldest = max(dictionary, key=dictionary.get)
    result = {'min_key': youngest, 'max_key': oldest}
    return result

def replace_special_characters(str1):
    """
    Replace each special symbol with # in the following string
    :param str1:'/*Jon is @developer & musician!!'
    :return: ##Jon is #developer # musician##"
    """
    special_characters = "!@#$%^&*()_+[]{}|;':,.<>?`~/"
    for char in special_characters:
        str1 = str1.replace(char, '#')
    return str1

def extend_list():
    """
    You are given a nested list of characters, but few characters are missing in the list.
    Write a program to inject the missing characters at the right place maintaining the order and structure of the list.
    :return:['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
    """
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sub_list = ["h", "i", "j"]

    list1[2][1][2].extend(sub_list)
    return list1

def sort_tuples():
    """
    You are given unstructured data. Write a program to sort the tuples in ascending order based on the second position value
    :return: (('c', 11), ('a', 23), ('d', 29), ('b', 37))
    """
    tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))

    output = sorted(tuple1, key=lambda x: x[1])
    return tuple(output)

def calculate_number_of_days():
    """
    Tony wants to generate an account report between 2 dates and club them based on number of days.
    Write a program to calculate the number of days between two given dates so that Tony can easily club the reports
    :return: 854
    """
    date_1 = '25-01-2020'
    date_2 = '28-05-2022'
    d1, m1, y1 = map(int, date_1.split('-'))
    d2, m2, y2 = map(int, date_2.split('-'))
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # days remaining in date 1
    days_remaining_1 = month_days[m1-1] - d1 + 1
    days_in_months_1 = sum(month_days[m1:])
    total_days_1 = days_remaining_1 + days_in_months_1

    # days passed in date 2
    days_in_months_2 = sum(month_days[:m2-1])
    total_days_2 = d2 + days_in_months_2

    # days in years
    years = y2 - y1 - 1
    total_days_3 = years * 365

    # total days
    return total_days_1 + total_days_2 + total_days_3
    

def update_sets():
    """
    Tony is working on two different data sets and wants to merge them.
    He is stuck with the problem as the data sets have a lot of common/duplicate items.
    Write a program to merge given 2 sets keeping the occurrence of duplicate items to only one set.
    :return: {10, 20, 30, 40, 50, 60, 70}
    """
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

    return set1.union(set2)