with open('2.txt', 'r') as file:
	mat = []
	for line in file:
		mat.append([int(x) for x in line.split()])

# part 1
safe_reports = 0
for report in mat:
	prev = report[0]
	direction = None
	for curr in report[1:]:
		if curr > prev and 1 <= curr-prev <= 3:
			prev = curr
			if direction is None:
				direction = 'up'
			else:
				if direction != 'up':
					break
		elif curr < prev and 1 <= prev-curr <= 3:
			prev = curr
			if direction is None:
				direction = 'down'
			else:
				if direction != 'down':
					break
		else:
			break
	else:
		safe_reports += 1
print(safe_reports)


#part 2
safe_reports = 0
for report in mat:
	report_good = False
	for i in range(len(report)):
		report_aug = report[0:i] + report[i+1:]
		prev = report_aug[0]
		direction = None
		for curr in report_aug[1:]:
			if curr > prev and 1 <= curr-prev <= 3:
				prev = curr
				if direction is None:
					direction = 'up'
				else:
					if direction != 'up':
						break
			elif curr < prev and 1 <= prev-curr <= 3:
				prev = curr
				if direction is None:
					direction = 'down'
				else:
					if direction != 'down':
						break
			else:
				break
		else:
			report_good = True
	if report_good:
		safe_reports += 1
print(safe_reports)

