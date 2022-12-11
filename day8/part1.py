from typing import List

with open ('input08.txt','r') as f:
    data = f.read().splitlines()

TREES = len(data)

def convert_grid_to_dict(data: List[str]) -> dict:
    
    # Prepare initial grid
    grid = {'Vertical':{}, 'Horizontal': {}}
    for i in range(TREES):
        grid['Vertical'][i] = ''
        grid['Horizontal'][i] = ''

    for i_data, line in enumerate(data):
        # Put each line in horizontal section
        grid['Horizontal'][i_data] = line
        
        for i_tree, tree in enumerate(list(line)):
            # For each line put the character of index i_tree in vertical section
            north = grid['Vertical'][i_tree]
            grid['Vertical'][i_tree] = f'{north}{tree}'

    return grid

grid = convert_grid_to_dict(data)

# Inicializate new grid
new_grid = {'North':{}, 'East': {}, 'South':{}, 'West':{}}
for i in range(TREES):
    new_grid['North'][i] = ''
    new_grid['East'][i] = ''
    new_grid['South'][i] = ''
    new_grid['West'][i] = ''


# Add to the new grid 1 (visible) or 0 (not visible) to each cardinal
for k,v in grid['Horizontal'].items():

    last_number = -1
    max_number = -1

    for nun in list(v):
        if last_number < int(nun) and int(nun) > max_number:
            new_grid['East'][k] += '1'
        else:
            new_grid['East'][k] += '0'
        
        last_number = int(nun)

        if int(nun) > max_number:
            max_number = int(nun)


for k,v in grid['Horizontal'].items():

    last_number = -1
    max_number = -1

    for nun in list(v[::-1]):
        if last_number < int(nun) and int(nun) > max_number:
            new_grid['West'][k] += '1'
        else:
            new_grid['West'][k] += '0'
        
        last_number = int(nun)
        if int(nun) > max_number:
            max_number = int(nun)
    new_grid['West'][k] = new_grid['West'][k][::-1]


for k,v in grid['Vertical'].items():

    last_number = -1
    max_number = -1

    for nun in list(v):
        if last_number < int(nun) and int(nun) > max_number:
            new_grid['North'][k] += '1'
        else:
            new_grid['North'][k] += '0'
        
        last_number = int(nun)
        if int(nun) > max_number:
            max_number = int(nun)


for k,v in grid['Vertical'].items():

    last_number = -1
    max_number = -1

    for nun in list(v[::-1]):
        if last_number < int(nun) and int(nun) > max_number:
            new_grid['South'][k] += '1'
        else:
            new_grid['South'][k] += '0'
        
        last_number = int(nun)
        if int(nun) > max_number:
            max_number = int(nun)
    new_grid['South'][k] = new_grid['South'][k][::-1]  


cardinal = {'Vertical': {},'Horizontal':{}}
for i in range(TREES):
    cardinal['Horizontal'][i] = ''
    cardinal['Vertical'][i] = ''

for k,v in new_grid['East'].items():
    for i,value in enumerate(list(v)):
        if value == '1' or new_grid['West'][k][i] == '1':
            cardinal['Horizontal'][k] += '1'
        else:
            cardinal['Horizontal'][k] += '0'


for k,v in new_grid['North'].items():
    for i,value in enumerate(list(v)):
        if value == '1' or new_grid['South'][k][i] == '1':
            cardinal['Vertical'][k] += '1'
        else:
            cardinal['Vertical'][k] += '0'


c = 0
for k,v in cardinal['Vertical'].items():

    for i, value in enumerate(list(v)):
        if value == '1' or cardinal['Horizontal'][i][k] == '1':
            c += 1
print(c)


