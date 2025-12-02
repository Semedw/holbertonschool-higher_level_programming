#!/usr/bin/python3

def common_elements(set1, set2):
    result = []
    for i in set1:
        if i in set2:
            result.append(i)
    return result
