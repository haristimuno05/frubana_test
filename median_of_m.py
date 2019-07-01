

def median(numbers_array):
    """
    Method to calculate the median

    :param numbers_array: array of numbers
    :return: median
    """
    n = len(numbers_array)
    numbers_array = sorted(numbers_array)

    # check for even case
    if n % 2 != 0:
        return numbers_array[int(n / 2)]

    return float((numbers_array[int((n - 1) / 2)] + numbers_array[int(n / 2)]) / 2.0)


if __name__ == '__main__':
    """Principal method"""
    numbers = list()
    n = int(input())  # number of operations
    i = 0

    while i < n:  # while exists operations
        line = input()
        operation, num = line.split(' ')  # assign operation and num
        num = int(num)

        if operation == 'r' and num in numbers:
            numbers.remove(num)

            if len(numbers) == 0:
                print('Wrong!')
            else:
                print(median(numbers))
        elif operation == 'a':
            numbers.append(num)
            print(median(numbers))
        else:
            print('Wrong!')
        i += 1
