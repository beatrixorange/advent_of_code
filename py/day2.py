
def main():
	f = open("/home/detmer/programming/aoc/aoc_input/input_day2.txt", "r")
	valid_pass = 0
	for line in f:

		#splitting the strings into workable parts

		pass_split = line.split(":")
		pol_split = pass_split[0].split(" ")
		polnum_split = pol_split[0].split("-")
		
		#naming vars for readability

		minimum = int(polnum_split[0])
		maximum = int(polnum_split[1])
		letter = pol_split[1]
		password = pass_split[1]

		#count occurences of letter in password

		amount = 0

		for i in password:
			if i == letter:
				amount+=1

		#check if password is valid according to the password policy

		if(amount >= minimum and amount <= maximum):
			valid_pass+=1

	print(valid_pass)


if __name__ == '__main__':
	main()

