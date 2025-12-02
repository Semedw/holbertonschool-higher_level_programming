#!/usr/bin/python3

def best_score(a_dict):
    result = []
    for value in a_dict.values():
        result.append(value)
    return max(result) if len(result) > 0 else None
