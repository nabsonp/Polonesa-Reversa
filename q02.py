pos = input()
pilha = []
for i in range(len(pos)):
    if pos[i] == '*':
        x = int(pilha[len(pilha)-1])
        y = int(pilha[len(pilha)-2])
        del pilha[len(pilha)-1]
        del pilha[len(pilha)-1]
        pilha.append(x * y)
    elif pos[i] == '/':
        x = int(pilha[len(pilha)-1])
        y = int(pilha[len(pilha)-2])
        del pilha[len(pilha)-1]
        del pilha[len(pilha)-1]
        pilha.append(y / x)
    elif pos[i] == '-':
        x = int(pilha[len(pilha)-1])
        y = int(pilha[len(pilha)-2])
        del pilha[len(pilha)-1]
        del pilha[len(pilha)-1]
        pilha.append(y - x)
    elif pos[i] == '+':
        x = int(pilha[len(pilha)-1])
        y = int(pilha[len(pilha)-2])
        del pilha[len(pilha)-1]
        del pilha[len(pilha)-1]
        pilha.append(x + y)
    else:
        pilha.append(pos[i])
print(pilha[0])
