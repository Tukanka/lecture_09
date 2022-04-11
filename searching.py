import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode='r') as json_file:
        data = json.load(json_file)
    if field not in set(data.keys()):
        return None
    return data[field]

def linear_search(prohledavana_sekvence, hledane_cislo):
    positions = []
    count = 0
    for idx, prvek in enumerate(prohledavana_sekvence):
        if prvek == hledane_cislo:
            positions.append(idx)
            count = count + 1
    return {'positions': positions, 'count': count}

def pattern_search(prohledavana_sekvence, vzor):
    pozice = set()
    index = 0
    while index < len(prohledavana_sekvence) - len(vzor):
        if prohledavana_sekvence[index:index + len(vzor)] == vzor:
            pozice.add(index)
        index = index + 1
    return pozice






def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')
    # print(sequential_data)
    results = linear_search(sequential_data, 0)
    # print(results)
    dna_sequence = read_data('sequential.json', 'dna_sequence')
    print(dna_sequence)
    print(pattern_search(dna_sequence, 'ATA'))


if __name__ == '__main__':
    main()