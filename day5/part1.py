import re
from typing import Tuple

with open ('input05.txt','r') as file:
    data = file.readlines()
    cargo = data[:8]
    instructions = data[10:]


def update_array(data_line: list, data_array:dict) -> dict:

    for i, element in enumerate(data_line):
        element = element.replace(' ', '').replace('[','').replace(']','').replace('\n','')
        if len(element) > 0:
            data_array[i+1].append(element)

    return data_array


def convert_cargo_to_dicts(text_list: list) -> dict:

    data_array = {}
    docks = [1,2,3,4,5,6,7,8,9]
    for x in docks:
        data_array[x] = []

    for line in text_list:
        all_groups = re.findall(r'(...[ \n])', line) 
        data_array = update_array(all_groups ,data_array)
        
    return data_array
   

def move_cargo(data: dict, n_items: int, init: int, end: int) -> dict:
    for _ in range(n_items):
        data[end].insert(0, data[init][0])
        del(data[init][0])
    
    return data


def process_instructions(text: str) -> Tuple[int, int, int]:
    n_items, init, end = re.findall('\d+', text)
    return int(n_items), int(init), int(end)


def get_solution(data:dict):
    inter_list = []
    for k,v in data.items():
        inter_list.append(v[0])
    print(''.join(inter_list))


def main(text: str, data: dict) -> None:
    for line in text:
        n_items, init, end =  process_instructions(line)
        data = move_cargo(data, n_items, init, end)
    get_solution(data)


array = convert_cargo_to_dicts(cargo)
main(instructions, array)
