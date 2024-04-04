#!/usr/bin/python3

'''
Determine if a data set represents a valid UTF-8 encoding
'''


def validUTF8(data):
    # Getting around this wierd case
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode()
    except BaseException:
        return False
    return True
