#!/usr/bin/python3
def new_in_list(mylist, idx, element):
    if idx < 0 and idx >= len(mylist):
        return mylist
    new_list = mylist.copy()
    new_list[idx] = element
    return new_list
