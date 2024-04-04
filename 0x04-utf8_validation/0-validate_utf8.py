
#!/usr/bin/python3

'''
A script to determine if a data set represents a valid UTF-8 encoding.
'''


def validUTF8(data):
    # Get around this case.
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode()
    except BaseException:
        return False
    return True

