#!/usr/bin/python3

def delete_at(mylist, idx):
    if idx >= len(mylist) or idx < 0:
        return mylist
    del mylist[idx]
    return mylist
