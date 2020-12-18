
def main():
	f = open("/home/detmer/programming/aoc/2020/aoc_input/input_day2.txt", "r")
	valid_pass_part1 = 0
	valid_pass_part2 = 0

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
			valid_pass_part1+=1

		#part two
		#checking if the character is at specific location according to the password policy
		if password[minimum] == letter and password[maximum] != letter or password[minimum] != letter and password[maximum] == letter:
			valid_pass_part2+=1

	print("Valid passwords part one: " + str(valid_pass_part1))
	print("Valid passwords part two: " + str(valid_pass_part2))


if __name__ == '__main__':
	main()

