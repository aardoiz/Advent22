import re

with open ('input07.txt','r') as f:
    text = f.read()


TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000


storage = {}
# En primer lugar con regex dividimos el texto por grupos 'folder_name'->'folder_content'
divided_raw_storage = re.findall(r'(?:\w+|\/)\n\$ ls\n(?:.+\n*)*?(?:\$ cd|\Z)', text)


def new_compute(storage: dict , external_dict: dict) -> int:        

    suuuum = 0
    for v in storage.values():
        for value in v:
            if value in external_dict.keys():
                suuuum += int(external_dict[value])
            else:
                suuuum += int(value)
    return suuuum


# Luego almacenamos esa info en un dict
byte = 0
for i,division in enumerate(divided_raw_storage):
    files = re.findall(r'(\d+)', division)
    for file in files:
        byte += int(file)
    name = re.findall(r'\A(\/|\w+)', division)[0]
    folders = re.findall(r'dir (\w+)', division)
    storage[i] = {name:folders+files}


space_not_used = TOTAL_SPACE - byte
space_needed = REQUIRED_SPACE - space_not_used


# Lo que tengo que hacer es recorrer el diccionario por el rango reverso de 197 a 0; e ir comparando el peso de las carpetas una a una
ex_dict = {}
minimun = TOTAL_SPACE
for i in reversed(range(198)):  
    n_sum = new_compute(storage[i], ex_dict)
    for k in storage[i].keys():
        ex_dict[k] = n_sum

for v in ex_dict.values():
    if v > space_needed and v < minimun:
        minimun = v

print(minimun)