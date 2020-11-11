from Parse import parse_all


def main(filename1="DefaultInput.txt", group="P000", filename2="Output.txt"):
    with open(filename1, "r", encoding="UTF-8") as file:
        data = file.read()
        result = parse_all(data, group)
        output = open(filename2, "w", encoding="UTF-8")
        output.write(result)
        output.close()


if __name__ == "__main__":
    main()
