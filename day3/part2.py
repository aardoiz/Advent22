from enum import Enum, auto
from typing import List

with open ('input03.txt','r') as file:
    text = file.read().splitlines()


class letter_value(Enum):
    a = auto()
    b = auto()
    c = auto()
    d = auto()
    e = auto()
    f = auto()
    g = auto()
    h = auto()
    i = auto()
    j = auto()
    k = auto()
    l = auto()
    m = auto()
    n = auto()
    o = auto()
    p = auto()
    q = auto()
    r = auto()
    s = auto()
    t = auto()
    u = auto()
    v = auto()
    w = auto()
    x = auto()
    y = auto()
    z = auto()


def get_overlap_score(text_list: List[str]) -> int:

    text1 = text_list[0]
    text2 = text_list[1]
    text3 = text_list[2]

    inter = ''.join(set(list(text1)).intersection(set(list(text2))).intersection(set((text3))))
    
    for letter in letter_value:
        if inter == letter.name:
            score = letter.value
        elif inter == letter.name.upper():
            score = letter.value + 26

    return score

def filter_trios(original_list: list) -> list:

    final_list = []
    iter_list = []
    for i, group in enumerate(original_list):
        
        iter_list.append(group)
        if (i+1)%3 == 0:
                    final_list.append(iter_list)
                    iter_list = []
    return final_list


final = sum([get_overlap_score(te) for te in filter_trios(text)])
print(final)