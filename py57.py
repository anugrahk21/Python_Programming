#wrapping or split text after a specified index or number of characters


import textwrap

def wrap(string, max_width):
    j=textwrap.fill(string,max_width)
    k=textwrap.wrap(string,max_width)
    return k  #prints the list of splitted text  ["abc", "def"]
    return j #prints the splitted set of texts in each new line abc
                                                       #        def
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)   #("abcdef",3)
    print(result)