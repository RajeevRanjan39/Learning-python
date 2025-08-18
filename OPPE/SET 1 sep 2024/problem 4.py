def sum_of_squares_of_even(nums: list) -> int:
    '''Return the sum of squares of all even numbers in the list.

    Args:
        nums : list - list of integers

    Returns:
        int - sum of squares of all even numbers
    '''
    ...
    sum = 0
    for i in nums:
        if(i % 2 == 0):
            sum += i ** 2
    return sum