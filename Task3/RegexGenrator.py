import re

alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУЙФХЦЧШЩЪЫЬЭЮЯ"
text = "Петров П.П. P000\n" \
       "Анищенко А.А. P33113\n" \
       "Балаквин П.В. P000\n" \
       "Иванов И.И. P000"
group = "P000"
for i in alphabet:
    regex = r"({0}[а-я]* {0}\.{0}\. {1}($|\n))".format(i, group)

    text = re.sub(regex, "", text)

print(text)
