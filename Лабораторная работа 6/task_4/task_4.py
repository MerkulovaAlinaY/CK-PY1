import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, new_line="\n", delimiter=","):
    with open(filename, 'r') as f:
        dict_ = []
        for i, j in enumerate(f):
            column = j.strip(new_line).split(delimiter)
            if i == 0:
                value = column
                continue
            dict_.append({})
            for a, b in enumerate(value):
                dict_[-1][value[a]] = column[a]
    return dict_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
