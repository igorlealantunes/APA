
m = int(input())
n = int(input())

pesos   = map(int, raw_input().split(" "))
valores = map(int, raw_input().split(" "))

peso_by_value = [ { "I" : i, "V" : valores[i]/pesos[i], "P" : pesos[i] } for i in range(0, n) ]
peso_by_value.sort(key=lambda k: k['V'], reverse = True)

na_mochila = []
for el in peso_by_value:

	if m >= el["P"]:
		m -= el["P"]
		na_mochila.append(el)


print "Peso restante: " + str(m)
print na_mochila