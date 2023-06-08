#!/usr/bin/env python3
def first_with_given_key(iterable, key=repr):
    prev_keys = {}
    lamb_key = lambda item: key(item)
    for obj in iterable:
        obj_key = lamb_key(obj)
        if(obj_key) in prev_keys.keys():
            continue
        try:
            prev_keys[hash(obj_key)] = repr(obj)
        except TypeError:
            prev_keys[repr(obj_key)] = repr(obj)
        yield obj
    