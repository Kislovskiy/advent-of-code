def read_input_file(file_path):
    with open(file_path, "r") as fi:
        return [number.strip() for number in fi.readlines()]
