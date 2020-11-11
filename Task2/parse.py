import re


def process(data, lang="en"):
    if data is None:
        return None
    regex = r"[A-Z][A-z;:’—'\–\-\s]*,[A-z,;:’—'\–\-\s]*!"
    if lang == "ru":
        regex = r"[А-Я][А-я;:’—'\–\-\s]*,[А-я,;:’—'\–\-\s]*!"
    elif lang == "es":
        regex = r"¡[A-ZÑ][A-zÑñ;:’—'\–\-\s]*,[A-zÑñ,;:’—'\–\-\s]*!"
    elif lang == "de":
        regex = r"[A-ZÄÖÜß][A-zÄÖÜßäöüß;:’—'\–\-\s]*,[A-zÄÖÜßäöüß,;:’—'\–\-\s]*!"
    return re.findall(regex, data)


def test():
    text = "Look at what we’d kill: Mosquitos and flies. 'Cuz they’re pests. Lions and tigers. " \
               "'Cuz it’s fun! Chickens and pigs. 'Cuz we’re hungry. Pheasants and quails. 'Cuz it’s fun. " \
               "And we’re hungry. And people. We kill people… Cuz they’re pests, and it’s fun!"
    wanted = ["Cuz they’re pests, and it’s fun!"]
    print(text)
    print("________________")
    print(process(text))
    print("_________________")
    print(wanted)


if __name__=="__main__":
    test()