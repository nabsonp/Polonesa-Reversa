oper = input().split()
for i in range(len(oper)-1):
	if (oper[i] == '+' or oper[i] == '-') and (oper[i+1] != '+' and
	 oper[i+1] != '-' and oper[i+1] != '*' and oper[i+1] != '/'):
		aux = oper[i+1]
		oper[i+1] = oper[i]
		oper[i] = aux
	elif (oper[i] == '*' or oper[i] == '/') and (oper[i+1] != '+' and
	oper[i+1] != '-' and oper[i+1] != '*' and oper[i+1] != '/'):
		if oper[i-1] == '+' or oper[i-1] == '-':
			aux = oper[i-1]
			oper[i-1] = oper[i+1]
			oper[i+1] = aux
		else:
			aux = oper[i+1]
			oper[i+1] = oper[i]
			oper[i] = aux
for j in range(len(oper)):
	print(oper[j],end=" ")
print()
