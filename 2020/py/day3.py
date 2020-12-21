def main():
	f = open("/home/detmer/programming/aoc/2020/aoc_input/input_day3.txt", "r")
	snowslope = []
	
	for line in f:
		snowslope.append(line)

	print("Product of amount of trees of all slopes:", traverse(1,1,snowslope) * traverse(3,1,snowslope) * traverse(5,1,snowslope) * traverse(7,1,snowslope) * traverse(1,2,snowslope))

def traverse(step,jump,snowslope):

	snowslope = snowslope
	pos = step
	step = step
	jump = jump
	started = False
	trees = 0
	start = 0

	for row in snowslope:
		if started:	
			if row[pos] == '#':
				trees+=1
				
			if pos+step > 30:
				pos+=step
				remainder = pos - 31
				pos = remainder
			else:
				pos+=step
			if jump == 2:
				started = False

		elif jump == 1:
			started = True
		elif jump == 2:
			if start == 1:
				started = True;
				start = 0
			start+=1
		

	print("Amount of trees:", trees)
	return trees



if __name__ == '__main__':
	main()