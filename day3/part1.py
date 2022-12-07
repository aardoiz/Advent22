from enum import Enum, auto

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


def get_overlap_score(text: str) -> int:

    lenght = int(len(text)/2)

    part2 = list(text[lenght:])
    part1 = list(text[:lenght])

    inter = ''.join(set(part1).intersection(set(part2)))

    
    for letter in letter_value:
        if inter == letter.name:
            score = letter.value
        elif inter == letter.name.upper():
            score = letter.value + 26

    return score


final = sum([get_overlap_score(te) for te in text])
print(final)