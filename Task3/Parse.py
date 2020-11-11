import re


def parse_all(text, group="P000"):
    if text is None:
        return None
    text = parse_fio(text, group)
    text = parse_fi(text, group)
    return text


def parse_fio(text, group):
    regex = r"([А-ЯA-Z])[а-яa-z]* \1.\1. " + group + "(\n|$)"
    # print(re.findall(regex, text))
    return re.sub(regex, "", text)


def parse_fi(text, group):
    regex = r"([А-ЯA-Z])[а-яa-z]* \1. " + group + "(\n|$)"
    # print(re.findall(regex, text))
    return re.sub(regex, "", text)
