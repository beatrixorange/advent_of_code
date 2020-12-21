def main():
	f = open("/home/detmer/programming/aoc/2020/aoc_input/input_day3.txt", "r")
	snowslope = []
	pos = 3
	started = False
	trees = 0
	print_first_tree = True
	
	for line in f:
		snowslope.append(line)

	for row in snowslope:
		if started:

			if row[pos] == '#':
				trees+=1

			if pos+3 > 30:
				pos+=3
				remainder = pos - 31
				pos = remainder
			else:
				pos+=3

		else:
			started = True

	print("Amount of trees:", trees)

if __name__ == '__main__':
	main()