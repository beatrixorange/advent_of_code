import re

def main():
	f = open("/home/detmer/programming/aoc/2020/aoc_input/input_day4.txt", "r")
	#a = re.split(':| ', passport)
	#put entire input in a string
	all_passports = f.read()
	#split string on two new lines to get individual passports
	passports = all_passports.split("\n\n")
	#make two sorted lists one with all required fields for legit passport and another one with CID prop missing
	#then mutate x so that you get the fields and add those fields to a list. Sort the list and check if it is 
	#the same as either one of the aforementioned lists. Increment valid pass by 1.
	valid_pass = 0
	check_pass = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
	for x in passports:
		mut = re.split(':| |\n', x)
		l_pass = []
		for passport in mut:
			if passport in check_pass:
				l_pass.append(passport)
				l_pass.sort()
				if l_pass == check_pass:
					valid_pass+=1

	print(valid_pass)


if __name__ == '__main__':
	main()