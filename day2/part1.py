with open ('input02.txt','r') as f:
    text = f.readlines()

def get_score(text: str) -> int: 
    """
    A X -> Piedra
    B Y -> Papel
    C Z -> Tijeras
    """
    if 'A' in text:
        if 'X' in text:
            score = 1 + 3
        elif 'Y' in text:
            score = 2 + 6
        elif 'Z' in text:
            score = 3 + 0

    if 'B' in text:
        if 'X' in text:
            score = 1 + 0
        elif 'Y' in text:
            score = 2 + 3
        elif 'Z' in text:
            score = 3 + 6

    if 'C' in text:
        if 'X' in text:
            score = 1 + 6
        elif 'Y' in text:
            score = 2 + 0
        elif 'Z' in text:
            score = 3 + 3

    return score


response = sum([get_score(x) for x in text])
print(response)