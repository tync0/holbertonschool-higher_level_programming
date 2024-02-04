#!/usr/bin/python3

"""
Text
"""


def text_indentation(text):
    """
    Print a text indentation
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    txt = list(text)
    for i in range(len(txt)):
        if txt[i] in [".", "?", ":"]:
            print(txt[i])
            print()
            j = i + 1
            while j != len(txt) and txt[j] == " ":
                txt[j] = ""
                j += 1
            continue
        print(txt[i], end="")
