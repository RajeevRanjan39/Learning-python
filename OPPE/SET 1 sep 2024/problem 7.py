'''
Print Pattern - V
Given an integer n (where n > 0), print a "V" shaped pattern with n rows. The pattern should use backslashes (\) and forward slashes (/) for each row, with the v character at the bottom. There should be no spaces to the right of the pattern.

NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

Input Format

    • A single integer n, representing the number of rows in the pattern.

Output Format

    • A "V" shaped pattern with n rows, as described.

Constraints

    • 1 <= n

Examples

Input:

1
Output:

v
Input:

2
Output:

\ /
 v
Input:

3
Output:

\   /
 \ /
  v

'''

n = int(input())
for i in range(n):
    spaces_before = " " * i
    if i == n-1:
            print(spaces_before + "v")
    else:
            inner_space = " " * ((n-i-1)*2-1)
            print(spaces_before + '\\' + inner_space + '/')


# Read input
n = int(input())

# Loop through each row
for i in range(n):
    spaces_before = ' ' * i
    if i == n - 1:
        # Last row, print 'v' at the correct position
        print(spaces_before + 'v')
    else:
        # Inner spaces between '\' and '/'
        spaces_between = ' ' * ((n - i - 1) * 2 - 1)
        print(spaces_before + '\\' + spaces_between + '/')
