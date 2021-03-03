import os
import sys
from random_person_swapper import RandomPersonSwapper


def read_file(name):
    f = open(name)
    fd = f.read()
    f.close()

    return fd

def write_file(src, name):
    f = open(name, 'w')
    f.write(src)
    f.close()

def write_lines(src, name):
    f = open(name, 'w')
    f.writelines(str(line) + '\n' for line in src)
    f.close()


if __name__ == '__main__':
    input_path = 'inout/' + sys.argv[1]

    text = read_file(input_path)

    rps = RandomPersonSwapper()

    new_text, pairs = rps.make_replacement(text)

    write_file(new_text, f'inout/{sys.argv[1]}_out.txt')
    write_lines(pairs, f'inout/{sys.argv[1]}_rules.txt')

    print(pairs)
    print(new_text)





