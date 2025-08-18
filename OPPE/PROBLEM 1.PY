def deinterleave(s: str) -> str:
    """
    Deinterleave even and odd indices in a string.

    Args:
        s (str): The input string.

    Returns:
        str: The deinterleaved string.
    """
    even_chars = s[::2]  # Characters at even indices: 0, 2, 4, ...
    odd_chars = s[1::2]  # Characters at odd indices: 1, 3, 5, ...
    return even_chars + odd_chars
s=input()
new_string=deinterleave(s)
print(new_string)