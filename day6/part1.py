with open ('input06.txt','r') as f:
    text = f.read()



ex_list = []
while True:
    for i, element in enumerate(text):
        if len(ex_list) > 3:
            del ex_list[0]
        ex_list.extend(element)

        if len(set(ex_list)) == 4:
            print(i+1)
            break
    break
