def sum_squares_abs_diff_squares(a:int, b:int) -> tuple:
    '''Return the sum of squares and the absolute difference of squares.

    Args:
        a, b : int - input numbers

    Returns:
        tuple - tuple with sum of squares and absolute difference of squares.

    '''
    sum_of_square = a**2 + b**2
    abs_diff_of_square = abs(a**2 - b**2)
    return (sum_of_square, abs_diff_of_square)
