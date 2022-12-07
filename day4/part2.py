from pydantic import BaseModel

with open ('input04.txt','r') as file:
    data = file.read().splitlines()


class CleaningZone(BaseModel):
    start: int
    end: int


def text_to_CZ(text: str) -> CleaningZone:
    numbers = text.split('-')
    return CleaningZone(start=numbers[0], end=numbers[1])


def is_overlap(text: str) -> bool:
    
    pair = text.split(',')
    pair1 = text_to_CZ(pair[0])
    pair2 = text_to_CZ(pair[1])

    if pair1.start <= pair2.start <= pair1.end:
        return True

    if pair2.start <= pair1.start <= pair2.end:
        return True
    
    return False


c = 0
for d in data:
    if is_overlap(d):
        c += 1

print(c)