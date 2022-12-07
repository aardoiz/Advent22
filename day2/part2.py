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
            score = 0 + 3
        elif 'Y' in text:
            score = 3 + 1
        elif 'Z' in text:
            score = 6 + 2

    if 'B' in text:
        if 'X' in text:
            score = 0 + 1
        elif 'Y' in text:
            score = 3 + 2
        elif 'Z' in text:
            score = 6 + 3

    if 'C' in text:
        if 'X' in text:
            score = 0 + 2
        elif 'Y' in text:
            score = 3 + 3
        elif 'Z' in text:
            score = 6 + 1

    return score


response = sum([get_score(x) for x in text])
print(response)