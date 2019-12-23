def read_in_text_file(filename):
    with open(filename, "r") as file:
        return file.read()