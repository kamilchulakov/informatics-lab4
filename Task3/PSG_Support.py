import re


def main():
    group = "P311[0-5]"
    with open("Example.txt", "r") as file:
        data = file.read()
        result = get_fio(data, group).split("\n")
        # print(result)
        for i in range(len(result)):
            if result[i] == "":
                continue
            filename = "PSGes/ПСЖ{}.txt".format(i + 1)
            with open(filename, "w") as file2:
                file2.write(
                    "В приказ №{0}                       Ректору Университета ИТМО        \n\
____________________              член-корреспонденту РАН          \n\
(подпись)                         д.т.н., профессору В.Н. Васильеву\n\
«____» ________ 20____ г.\n\n\n\n"
                    "\t\t\t\t\t\tЗАЯВЛЕНИЕ\n\n\n\n\
Прошу отчислить меня из университета по собственному желанию.\n\n\
«____» ________ 20____ г.		_______________		{1}\n \
(дата)				            (личная подпись)	(ФИО)".format(i+1, " ".join(result[i].split()[:-1])))


def get_fio(data, group):
    regex = r"([А-Я])[а-я]* \1\.\1\. " + group + "(\n|$)"
    result = re.sub(regex, "", data)
    return result


if __name__ == "__main__":
    main()
