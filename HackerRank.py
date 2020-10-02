"""s = input()
w = int(input())
for i in range(len(s)//w + 1):
    print(s[i*w:w*(i+1)])
"""
import textwrap
def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    x = ''
    for element in word_list:
        x += element+'\n'
    return x


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)