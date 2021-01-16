f = open("/home/detmer/programming/aoc/2020/aoc_input/input_day6.txt", "r")

all_forms = f.read()

total = 0

forms = all_forms.split("\n\n")
for form in forms:
	u_form= form.replace("\n",'')
	s = set(u_form)
	total = a + len(s)
	print()
print(total)