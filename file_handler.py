def read_from_file(input_file_path):
    file = open(input_file_path, "r")

    # X,Y from first line ignored
    file.readline()
    input_dots = []
    for line in file:
        print([float(line.split(',')[0]),float(line.split(',')[1])])
        input_dots.append([float(line.split(',')[0]),float(line.split(',')[1])])
    return input_dots