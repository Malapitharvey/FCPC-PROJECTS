name = input("enter your name :")

ceasar_cyper = ""

for x in range(len(name)):
    char = name[x]

    if char == "a" :
        ceasar_cyper += 'B'
    elif char == "b" :
        ceasar_cyper += 'C'
    elif char == "c":
        ceasar_cyper += 'D'
    elif char == "d" :
        ceasar_cyper += 'E'
    elif char == "e" :
        ceasar_cyper += 'F'
    elif char == "f" :
        ceasar_cyper += 'G'
    elif char == "g" :
        ceasar_cyper += 'H'
    elif char == "h" :
        ceasar_cyper += 'I'
    elif char == "i":
        ceasar_cyper += 'J'
    elif char == "j" :
        ceasar_cyper += 'K'
    elif char == "k" :
        ceasar_cyper += 'L'
    elif char == "l" :
        ceasar_cyper += 'M'
    elif char == "m" :
        ceasar_cyper += 'N'
    elif char == "n" :
        ceasar_cyper += 'O'
    elif char == "o" :
        ceasar_cyper += 'P'
    elif char == "p" :
        ceasar_cyper += 'Q'
    elif char == "q" :
        ceasar_cyper += 'R'
    elif char == "r" :
        ceasar_cyper += 'S'
    elif char == "s" :
        ceasar_cyper += 'T'
    elif char == "t" :
        ceasar_cyper += 'U'
    elif char == "u" :
        ceasar_cyper += 'V'
    elif char == "v":
        ceasar_cyper += 'W'
    elif char == "w" :
        ceasar_cyper += 'X'
    elif char == "x" :
        ceasar_cyper += 'Y'
    elif char == "y":
        ceasar_cyper += 'Z'
    elif char == "z":
        ceasar_cyper += A
    else:
        ceasar_cyper += char
print(ceasar_cyper)
