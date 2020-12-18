
def main():
	f = open("/home/detmer/programming/aoc/aoc_input/input_day1.txt", "r")
	expenses = []
	for line in f:
		expenses.append(int(line))

	for x in expenses:
		#print(x)
		for y in expenses:
			#print(y)
			if(x + y == 2020):
				print(x * y)
				return 0;



if __name__ == '__main__':
	main()




