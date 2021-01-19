#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""

def get_greatest(number_list):
    """
    주어진 리스트에서 가장 큰 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            greatest_6'6number (int): parameter number_list 중 가장 큰 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_greatest(number_list)
            99
    """
    greatest_number = -9999999
    for i in range (len(number_list)):
        if(number_list[i] > greatest_number):
            greatest_number = number_list[i]
    return greatest_number


def get_smallest(number_list):
    """
    주어진 리스트에서 제일 작은 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            smallest_number (int): parameter number_list 중 가장 작은 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_smallest(number_list)
            11
    """
    smallest_number = 999999999
    for i in range (len(number_list)):
        if(number_list[i] < smallest_number):
            smallest_number=number_list[i]
    return smallest_number


def get_mean(number_list):
    """
    주어진 리스트 숫자들의 평균을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            mean (int): parameter number_list 숫자들의 평균

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_mean(number_list)
            47
    """
    mean = 0
    for i in number_list:
        mean = mean + i
    mean /= len(number_list)
    mean = round(mean,1)
    return mean


def get_median(number_list):
    """
    주어진 리스트 숫자들의 중간값을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            median (int): parameter number_list 숫자들의 중간값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_median(number_list)
            39
            >>> number_list2 = [39, 54, 32, 11, 99, 5]
            >>> bm.get_median(number_list2)
            35.5
    """
    median = 0
    number_list.sort()
    l = len(number_list)
    if(l%2 == 0):
        median = (number_list[l//2-1]+number_list[l//2])/2
    else:
        median = number_list[l//2]
    median = round(median, 1)
    return median


li = [72, 51, 10, 48, 58, 62, 92, 90, 11, 16]
print(get_greatest(li))
print(get_smallest(li))
print(get_median(li))
print(get_mean(li))