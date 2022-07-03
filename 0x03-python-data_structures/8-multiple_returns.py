#!/usr/bin/python3
def multiple_returns(sentence):
    ful_len = len(sentence)

    if (ful_len == 0):
        ful_tuple = (ful_len, None)
    else:
        ful_tuple = (ful_len, sentence[0])
    return (ful_tuple)
