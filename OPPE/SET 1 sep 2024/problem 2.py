def is_odd_length_palindrome(s: str) -> bool:
    '''Check if a string is a palindrome with odd length.

    Args:
        s : str - input string

    Returns:
        bool - True if s is a palindrome with odd length, False otherwise.
    '''
    reverse = s[::-1]
    if(len(s)%2 == 0 ):
        return False
    return reverse==s