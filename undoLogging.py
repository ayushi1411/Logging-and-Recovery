inputfile = open("input.txt")
firstLine = True
transaction = {}
transName = []
diskDict = {}
memDict = {}
for line in inputfile:
	if firstLine == True:
		temp = line.split(' ')
		firstLine = False
		for i in range(0,len(temp),2):
			num = temp[i+1]
			num = num.split('\n')[0]
			diskDict[temp[i]] = int(num)
			memDict[temp[i]] = int(num)
	else:

		temp = line.split(' ')
		name = temp[0]
		transName.append(name)
		cnt = int(temp[1])
		transaction[name] = []
		i = 1
		for line in inputfile:
			transaction[name].append(line.split('\n')[0])
			i = i + 1
			if i>cnt:
				break

print transaction
print memDict


	