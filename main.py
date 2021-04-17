F = []
print("==================Retorna ordem inversa===============")

for c in range (0,10):
	print("Qual o nome do",c+1,"° funcionário?")
	F.append(input())
print("_________________________________________________")

print("Os nomes dos funcionários em ordem alfabetica inversa são:")

F.sort(reverse=True)
print(F)