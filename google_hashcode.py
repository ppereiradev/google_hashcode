total_slices = 0
maximum = 0
type_pizza = []

def printCombination(array, p):
	data = [0]*p
	combinationUtil(array, data, 0, len(array)-1, 0, p)


def combinationUtil(array, data, start, end, index, p):
	global total_slices
	global maximum
	global type_pizza
	if index == p:
		s = 0
		aux_array = []
		for j in range(0,p):
			s += data[j]
			aux_array.append(array.index(data[j]))

		if total_slices <= s and s <= maximum:
			total_slices = s
			type_pizza = aux_array
		return

	i = start
	while i <= end and (end - i + 1) >= (p - index):
		if total_slices == maximum:
			break

		data[index] = array[i]
		combinationUtil(array, data, i+1, end, index+1, p)
		i += 1





f = open("c_medium.in", "r")
first_line = f.readline().split()

maximum = int(first_line[0])
pizzas_slices_amount = f.readline().split()
f.close()

pizzas_slices_amount = [int(i) for i in pizzas_slices_amount]

aux = len(pizzas_slices_amount)+1
while aux > 0:
	printCombination(pizzas_slices_amount, aux)
	aux -= 1
	if total_slices == maximum:
			break

print("total slices: " + str(total_slices))
print("types of pizza: " + str(len(type_pizza)))
print("pizzas: " + str(type_pizza))

f = open("c_medium.out","w+")
f.write(str(len(type_pizza)) + "\n")

for i in range(0, len(type_pizza)):
	f.write(str(type_pizza[i]) + " ")
f.close()
