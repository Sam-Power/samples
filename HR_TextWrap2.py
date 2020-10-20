"""You are given a string  and width .
Your task is to wrap the string into a paragraph of width .
Input Format
The first line contains a string, .
The second line contains the width, .
Constraints
Output Format
Print the text wrapped paragraph.
Sample Input 0
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ"""

def wrap(string, max_width):
    x=''
    for i in range(len(string) // max_width + 1):
        x += string[i * max_width:max_width * (i + 1)] + "\n"
    return x

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)