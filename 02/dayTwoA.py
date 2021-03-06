import re

def validatePasswords():
	results = []
	total = 0
	with open('input.txt') as report_file:
		lines = report_file.readlines()
		for line in lines:
			results.append(tuple(line.strip().split(" ")))
	
	for result in results:
		range = tuple(result[0].split("-"))
		required = result[1].strip(":")
		password = result[2]
		valid = ''.join(re.findall(required, password))
		if len(valid) >= int(range[0]) and len(valid) <= int(range[1]):
			total += 1
	print("Total Valid Passwords: ", total)

validatePasswords()
