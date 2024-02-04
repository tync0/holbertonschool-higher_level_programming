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
            if txt[i + 1] == " ":
                txt[i + 1] = ""
            print()
            continue
        print(txt[i], end="")
