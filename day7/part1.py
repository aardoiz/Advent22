import re

with open ('input07.txt','r') as f:
    text = f.read()


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
for i,division in enumerate(divided_raw_storage):
    name = re.findall(r'\A(\/|\w+)', division)[0]
    folders = re.findall(r'dir (\w+)', division)
    files = re.findall(r'(\d+)', division)
    storage[i] = {name:folders+files}



# Lo que tengo que hacer es recorrer el diccionario por el rango reverso de 197 a 0; e ir computando el peso de las carpetas una a una
ex_dict = {}
c = 0
for i in reversed(range(198)):
    
    n_sum = new_compute(storage[i], ex_dict)
    for k in storage[i].keys():
        ex_dict[k] = n_sum
    if n_sum <= 100000:
        c += n_sum
print(c)