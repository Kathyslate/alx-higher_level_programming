#!/usr/bin/python3
"""
module for text_indentation function
Adds two new lines after a set of characters: ., ? and :.
"""


def text_indentation(text):
    """Prints text adding two newlines
    after each of these characters {'.', '?', ':'}.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Print the text with 2 new lines after ., , and :
    for char in text:
        if char in ['.', ',', ':']:
            print(char)
            print()
        else:
            print(char, end="")
    print()
