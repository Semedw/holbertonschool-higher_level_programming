#!/usr/bin/python3

def best_score(a_dict):
    if len(a_dict) == 0:
        return None
    result = []
    name = []
    for key, value in a_dict.items():
        result.append(value)
        name.append(key)
    if len(result) == 0:
        return None
    else:
        k = result.index(max(result))
        return name[k]
