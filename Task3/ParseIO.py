import re
# for imya and otchestvo only filter
for i in range(6):
    group = "P312" + str(i)
    with open("StudentsList.txt", "r") as file:
        text = file.read()
        regex = r"([А-Я])[а-я]{1.} \w\. \w\. " + group + "(\n|$)"
        print("==============>{}<==============".format(group))
        print(re.findall(regex, text))
        result = re.sub(regex, "", text)
        # print(result)
