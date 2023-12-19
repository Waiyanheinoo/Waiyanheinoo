import sys
def main():
    num_lines = count_line()
    print(num_lines)

def count_line():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line argument")
        if len(sys.argv) < 2:
            sys.exit("Too few command-line argument")
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a python file")
        else:
            with open(sys.argv[1]) as file:
                lines = file.readlines()
                num_line = 0
                for line in lines:
                    line = line.lstrip()
                    if line and not line.startswith('#'):
                        num_line += 1
                return num_line


    except FileNotFoundError:
        sys.exit("File does not exit")

main()
