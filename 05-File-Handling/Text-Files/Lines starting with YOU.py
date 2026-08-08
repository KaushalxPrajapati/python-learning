def read_from_alpha():
    try:
        with open("Alpha.txt", "r") as f:
            for line in f:
                if line.startswith("You"):
                    print(line.strip())
    except FileNotFoundError:
        print("File not found.")

read_from_alpha()
