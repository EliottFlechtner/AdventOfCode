import re
from collections import defaultdict, Counter
from itertools import product

def read_input(file):
    with open(file) as f:
        return f.read().splitlines()
    
def read_input_raw(file):
    with open(file) as f:
        return f.read()
    
def read_input_sep(file, sep):
    with open(file) as f:
        return f.read().split(sep)
    
def read_input_int(file):
    with open(file) as f:
        return [int(x) for x in f.read().splitlines()]
    
def read_input_int_sep(file, sep):
    with open(file) as f:
        return [int(x) for x in f.read().split(sep)]
    
def read_input_str(file):
    with open(file) as f:
        return f.read().splitlines()
    
def read_input_str_sep(file, sep):
    with open(file) as f:
        return f.read().split(sep)
    
def read_input_list(file):
    with open(file) as f:
        return [list(x) for x in f.read().splitlines()]
    
def read_input_list_sep(file, sep):
    with open(file) as f:
        return [list(x) for x in f.read().split(sep)]
    
def read_input_list_int(file):
    with open(file) as f:
        return [[int(i) for i in x] for x in f.read().splitlines()]
    
def read_input_list_int_sep(file, sep):
    with open(file) as f:
        return [[int(i) for i in x] for x in f.read().split(sep)]
    
def read_input_list_str(file):
    with open(file) as f:
        return [[str(i) for i in x] for x in f.read().splitlines()]
    
def read_input_list_str_sep(file, sep):
    with open(file) as f:
        return [[str(i) for i in x] for x in f.read().split(sep)]
    
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def manhattan_distance_3d(x1, y1, z1, x2, y2, z2):
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)

def manhattan_distance_4d(x1, y1, z1, w1, x2, y2, z2, w2):
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) + abs(w1 - w2)

def get_neighbors(x, y):
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def get_neighbors_3d(x, y, z):
    return [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]

def get_neighbors_8dir(x, y):
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)]

# collections helpers
def counter_dict(data):
    return dict(Counter(data))

def counter_list(data):
    return Counter(data)

def counter_dict_sorted(data):
    return dict(sorted(Counter(data).items(), key=lambda x: x[1], reverse=True))

def counter_list_sorted(data):
    return sorted(Counter(data).items(), key=lambda x: x[1], reverse=True)

def counter_dict_sorted_key(data):
    return dict(sorted(Counter(data).items(), key=lambda x: x[0]))

def counter_list_sorted_key(data):
    return sorted(Counter(data).items(), key=lambda x: x[0])

def counter_dict_sorted_key_rev(data):
    return dict(sorted(Counter(data).items(), key=lambda x: x[0], reverse=True))

def search_list(data, key):
    return [i for i, x in enumerate(data) if x == key]

def search_list_count(data, key):
    return len([i for i, x in enumerate(data) if x == key])

def search_list_count_range(data, key1, key2):
    return len([i for i, x in enumerate(data) if key1 <= x <= key2])

def search_list_count_range_excl(data, key1, key2):
    return len([i for i, x in enumerate(data) if key1 < x < key2])
