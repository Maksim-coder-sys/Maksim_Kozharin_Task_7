import os
import sys

size = {}


def scan_mem(project7_path):

    if not os.path.exists(project7_path):
        return
    with os.scandir(project7_path) as f:

        for node in f:

            if os.path.isfile(node):

                mem = 10 ** len(str(os.stat(node).st_size))
                size[mem] = size.get(mem, 0) + 1
            elif os.path.isdir(node):
                scan_mem(os.path.join(project7_path, node))


if __name__ == "__main__":

    if len(sys.argv) == 2:
        project7_path = sys.argv[1]
    else:
        project7_path = os.getcwd()

scan_mem('C:\\Users\\Катя-Ноут\\PycharmProjects\\pythonProject7')
print(size)