f = open("/home/detmer/programming/aoc/2020/aoc_input/input_day6.txt", "r")

all_forms = f.read()

total1 = 0
total2 = 0

forms = all_forms.split("\n\n")
for form in forms:
	#part two
	all_freq = {}
	m = form.split("\n")
	if m[len(m)-1] == '':
		m.pop(len(m)-1)
	for c in form:
		if c in all_freq:
			all_freq[c] += 1
		else:
			all_freq[c] = 1
		all_freq['\n'] = 0
	for f in all_freq.items():
		print(f)
		if f[1] == len(m):
			print(f[1])
			total2 += 1
	
	#part one
	u_form = form.replace("\n",'')
	s = set(u_form)
	total1 = total1 + len(s)


print(total1)
print(total2)