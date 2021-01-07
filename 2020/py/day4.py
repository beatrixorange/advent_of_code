import re


def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def main():
	f = open("/home/detmer/programming/aoc/2020/aoc_input/input_day4.txt", "r")
	#put entire input in a string
	all_passports = f.read()
	#split string on two new lines to get individual passports
	passports = all_passports.split("\n\n")
	#passports get split into lists where each list is a paspport. This gets looped over to put the values in a dict.
	#values are checked according to the constraints set on the passports in a long nests of if statements.
	#if all values are correct valid_pass is incremented with 1.
	valid_pass = 0
	check_pass = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid', 'cid']
	for x in passports:
		mutate = re.split(':| |\n', x)
		l_pass = []
		i = 1
		check_passd = {'byr': '', 'ecl': '', 'eyr': '', 'hcl': '', 'hgt': '', 'iyr': '', 'pid': '', 'cid': ''}
		for passport in mutate:
			if i < len(mutate):
				if passport in check_pass:
					#putt values in the dict
					check_passd[passport] = mutate[i]
					if i+1 == len(mutate):
						#check if all values present
						if check_passd['byr'] != '' and check_passd['ecl'] != ''  and check_passd['eyr'] != ''  and check_passd['hcl'] != ''  and check_passd['hgt'] != ''  and check_passd['iyr'] != ''  and check_passd['pid'] != '':
							#check if birthyear is legit
							if int(check_passd['byr']) >= 1920 and int(check_passd['byr']) <= 2002:
								#check if expiration year is legit
								if int(check_passd['eyr']) >= 2020 and int(check_passd['eyr']) <= 2030:
									#check if issue year is legit
									if int(check_passd['iyr']) >= 2010 and int(check_passd['iyr']) <= 2020:
										#check if eyecolor is legit
										if check_passd['ecl'] == 'amb' or check_passd['ecl'] == 'blu' or check_passd['ecl'] == 'brn' or check_passd['ecl'] == 'gry' or check_passd['ecl'] == 'grn' or check_passd['ecl'] == 'hzl' or check_passd['ecl'] == 'oth':			
												#check if haircolor is legit
												if is_hex(check_passd['hcl'][1:]) and check_passd['hcl'][:1] == '#' and len(check_passd['hcl']) == 7:
													#check if passport ID is legit
													if len(check_passd['pid']) == 9:
														#check if height is legit
														if check_passd['hgt'][-2:] == 'cm':
															if int(check_passd['hgt'][:-2]) >= 150 and int(check_passd['hgt'][:-2]) <= 193:
																valid_pass+=1
														if check_passd['hgt'][-2:] == 'in':
															if int(check_passd['hgt'][:-2]) >= 59 and int(check_passd['hgt'][:-2]) <= 76:
																valid_pass+=1									
				i+=1
	print(valid_pass)


if __name__ == '__main__':
	main()