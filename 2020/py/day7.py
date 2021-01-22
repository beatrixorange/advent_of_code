f = open("/home/detmer/programming/aoc/2020/aoc_input/input_day7.txt", "r")

bags_rules = {}

bags_list = []

def check_bag(bag,bags):
	for key in bags:
		for x in bags[key]:
			if bag[:-2] in x:
				if key[:-2] not in bags_list:
					bags_list.append(key[:-2])
				check_bag(key[:-2],bags)


for line in f:
	main_bag = line.split("contain")
	nested_bags = main_bag[1].replace("\n","").split(",")
	bags_rules[main_bag[0]] = nested_bags


check_bag("shiny gold bag",bags_rules)
print(len(bags_list))
