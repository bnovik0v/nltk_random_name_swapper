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
    input_path = 'examples/test1.txt'
    text = read_file(input_path)

    rps = RandomPersonSwapper()

    new_text, pairs = rps.make_replacement(text)

    write_file(new_text, 'examples/test_out.txt')
    write_lines(pairs, 'examples/rules.txt')

    print(pairs)
    print(new_text)





