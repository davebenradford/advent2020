def expenseReport():
	results = []
	with open('input.txt') as report_file:
		lines = report_file.readlines()
		for line in lines:
			results.append(int(line.strip()))
	sum = 0
	product = 0
	for result in results:
		for outer in results:
			if result == outer or result > 2020 or outer > 2020:
				pass
			for inner in results:
				sum = 0
				if result == inner and result == outer:
					break
				elif result == inner or result == outer or outer == inner or result > 2020 or outer > 2020 or inner > 2020:
					pass
				else:
					sum = result + outer + inner
					if sum == 2020:
						print("Result: ", result, "; Outer: ", outer,  "; Inner: ", inner)
						print("Sum: ", sum)
						product = result * outer * inner
						break
			if product > 0:
				break
	print("Product: ", product)
	
	input("Press any key to continue...")
	
expenseReport()