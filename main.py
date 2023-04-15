import string


def addition(input: string):
    if input == '':
        return 0
    if len(input.split(',')) == 2:
        return int(input.split(',', 1)) + int(input.split(',', 2))
    if len(input.split(',')) == 1:
        return int(input)
