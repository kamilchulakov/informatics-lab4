import Parse


def main():
    in_put = "Input.txt"
    out_put = "Output.txt"
    with open(in_put, "r") as file:
        str = file.read()
        result = Parse.process(str)
    with open(out_put, "w") as file:
        file.write(result)


if __name__ == "__main__":
    main()
