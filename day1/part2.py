import heapq

with open ('input01.txt','r') as f:
    text = f.read()

groups = text.split('\n\n')

# Bucle para sacar el valor de cada grupo:
cleaned = []
for group in groups:
    digits = [int(x) for x in group.split('\n') if x!= '']
    cleaned.append(sum(digits))

print(sum(heapq.nlargest(3, cleaned)))