import os
import sys
from random_person_swapper import RandomPersonSwapper


def read_file(name):
    """Read the content of file"""
    f = open(name)
    fd = f.read()
    f.close()
    return fd

def write_file(src, name):
    """Write the content in file"""
    f = open(name, 'w')
    f.write(str(src))
    f.close()


if __name__ == '__main__':
    # Get input file name from command arg
    file_name = sys.argv[1]

    # Set inout path
    inout_path = 'inout/'

    # Read text from input file
    input_path = inout_path + file_name
    text = read_file(input_path)

    # Use RandomPersonSwapper to get transformed text and rules
    rps = RandomPersonSwapper()
    new_text, rules = rps.make_replacement(text)

    # Write the results in output files
    write_file(new_text, f'{inout_path}out_{file_name}')
    write_file(rules, f'{inout_path}rules_{file_name}')

    # Output the results on screen
    print(rules)
    print(new_text)





