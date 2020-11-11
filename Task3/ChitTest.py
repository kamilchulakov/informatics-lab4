from Parse import parse_all

text = "Петров П.П. P000\n" \
       "Анищенко А.А. P33113\n" \
       "Балаквин П.В. P000\n" \
       "Иванов И.И. P000"

print(parse_all(text, "P000"))
