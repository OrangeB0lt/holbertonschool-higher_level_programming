#!/usr/bin/python3
"""
    Indents text after speific character
    anotherline
    and anotherline!
"""
def text_indentation(text):
    """
        Indents text at specific characters . ? :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    temp = list(text)
    for idx in range(0, len(temp)):
        try:
            if temp[idx] == '.' or temp[idx] == '?' or temp[x] == ':':
                temp.insert(idx + 1, "\n")
        except:
            continue
    
    temp = "".join(temp).split('\n')
    for idx in temp:
        print(idx.strip())
        print()