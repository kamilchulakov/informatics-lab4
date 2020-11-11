from parse import process


def main(infile="RomeoAndJuliet.txt", output="Output.txt"):
    file = open(infile, "r")

    data = file.read()
    result = process(data)
    file.close()
    with open(output, "w") as out:
        for i in result:
            out.write(i + '\n')


if __name__ == "__main__":
    main()