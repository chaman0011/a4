try:
    with open('sample.txt', 'r') as file:
        line_num = 1
        print("Reading file content :")
        for line in file:
            print(f"Line {line_num}: {line}", end='')
            line_num += 1
except FileNotFoundError:
    print("Error: The file was not found.")

