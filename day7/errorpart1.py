# THIS SCRIPT WOULD HAVE WORKED ON A UNIQUE FOLDER NAME PROBLEM

import re

with open ('input07.txt','r') as f:
    text = f.read()


storage = {}
# En primer lugar con regex dividimos el texto por grupos 'folder_name':'folder_content'
divided_raw_storage = re.findall(r'(?:\w+|\/)\n\$ ls\n(?:.+\n*)*?(?:\$ cd|\Z)', text)



def check_values(storage: dict) -> bool:
    """
    Check that neither of the values of any key is another key
    """
    for _,v in storage.items():
        for value in v:
            if value in storage.keys():
                return True
    return False


def update_storage_info(storage: dict) -> dict:
    while check_values(storage):
        for k,v in storage.items():
            for value in v:
                for key in storage.keys():
                    if value == key:
                        storage[k].extend(storage[key])
                        storage[k].remove(value)
    return storage


def compute_sum(storage: dict) -> dict:
    for k in storage.keys():
        if sum([int(v) for v in storage[k]]) <= 100000:
            storage[k] = sum([int(v) for v in storage[k]])
        else:
            storage[k] = 0
    return storage


def response(storage:dict) -> int:
    c = 0
    for v in storage.values():
        if v <= 100000:
            c += v
    return c


storage = update_storage_info(storage)
storage = compute_sum(storage)
solution = response(storage)
print(solution)