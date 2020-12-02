def validatePasswords():
	results = []
	with open('input.txt') as report_file:
		lines = report_file.readlines()
		for line in lines:
			results.append(list(line.strip().split(" ")))
	
	for result in results:
		
validatePasswords()
