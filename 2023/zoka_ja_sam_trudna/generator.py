#!/usr/bin/env python3
import os
import random
import string

ANSWER = "I've felt the hate rise up in me. Kneel down and clear the stone of leaves\n"
BASE_DIR = 'files'
NUMBER_OF_DIRS = 20
NUMBER_OF_FILES = 5000


def get_random_string(str_len):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=str_len))


def get_random_content():
    return ''.join(random.choices(string.ascii_lowercase + string.digits + ' ', k=len(ANSWER) + random.randint(1, 100)))


def write_file(dir_name):
    file_path = os.path.join(BASE_DIR, dir_name, get_random_string(5))
    with open(file_path, 'w') as f:
        f.write(get_random_content() + '\n')
    return file_path


def write_answer(file_path):
    with open(file_path, 'w') as f:
        f.write(ANSWER)


if __name__ == '__main__':
    if not os.path.exists(BASE_DIR):
        os.mkdir(BASE_DIR)
    directories = []
    files = []
    for _ in range(0, NUMBER_OF_DIRS):
        dir_name = get_random_string(10)
        os.mkdir(os.path.join(BASE_DIR, dir_name))
        directories.append(dir_name)
    for _ in range(0, NUMBER_OF_FILES):
        files.append(write_file(random.choice(directories)))
    write_answer(random.choice(files))
