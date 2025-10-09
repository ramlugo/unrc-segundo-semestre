a, b, c, d, e, f = 8, 24, 30, 10, 15, 5
ordenada = sorted([a, b, c, d, e, f], reverse=True)
print(ordenada)

if len(ordenada) % 2 == 0:
	while len(ordenada) > 2:
		ordenada.pop() and ordenada.pop(0)
		print(ordenada)
else:
	while len(ordenada) > 1:
		ordenada.pop() and ordenada.pop(0)
		print(ordenada)
