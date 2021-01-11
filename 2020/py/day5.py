
def get_num(indicator,number):
	half = int((number[1] - number[0]) / 2)
	middle = number[0] + half
	if indicator == 'F' or indicator == 'L':
		new_range = [number[0],middle]
		return new_range
	elif indicator == 'B' or indicator == 'R':
		new_range = [middle+1,number[1]]
		return new_range


f = open("/home/detmer/programming/aoc/2020/aoc_input/input_day5.txt", "r")
seatlist = []
for x in f:
	num_row_range = [0,127]
	num_col_range = [0,7]
	for y in x:
		if num_row_range[0] == num_row_range[1] and y == 'L' or y == 'R':
			row = num_row_range[0]
			num_col_range = get_num(y,num_col_range)
			if num_col_range[0] == num_col_range[1]:
				col = num_col_range[0]
				seat_id = row * 8 + col
				seatlist.append(seat_id)
		else:
			num_row_range = get_num(y,num_row_range)

print("Highest seat ID on a boarding pass is:",max(seatlist))
sorted_list = sorted(seatlist)

for x, val in enumerate(sorted_list):
	if val+1 < len(sorted_list):
		if sorted_list[val+1] - sorted_list[val] != 1:
			print("Your seat ID is:", sorted_list[val]+1)
