import re


def process(str=None):
    if str is None:
        return str
    regex = r'([0-1]\d|2[0-3]):([0-6]\d:[0-6]\d|[0-6]\d)'
    return re.sub(regex, "(TBD)", str)
