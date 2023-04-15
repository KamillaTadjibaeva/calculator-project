import string

def addition(input: string):
    if input == '':
        return 0
    if len(input.split(',')) == 2:
        arr = input.split(',')
        return int(arr[0]) + int(arr[1])
    if len(input.split(',')) == 1:
        return int(input)
