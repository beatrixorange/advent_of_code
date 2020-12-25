def main():
	f = open("/home/detmer/programming/aoc/2020/aoc_input/input_day4.txt", "r")
	for passport in f:
		a = passport.split(":")
		print(a)


if __name__ == '__main__':
	main()