
import sys

def func(str_name,val): # set variable with str_name with value val

    if str_name in globals() : # already a global variable
        exec (str_name + "=" + str(val));
        globals()[str_name]=eval(str_name);

    if str_name not in globals(): # not a global variable
        exec ("global "+str_name+"; "+ str_name+"="+str(val));


file = sys.argv[1]
x = int(sys.argv[2])
inputfile = open(file)
firstLine = True
transaction = {}
transName = []
diskDict = {}
memDict = {}
var = {}
for line in inputfile:
	if firstLine == True:
		temp = line.split(' ')
		firstLine = False
		for i in range(0,len(temp),2):
			num = temp[i+1]
			num = num.split('\n')[0]
			diskDict[temp[i]] = int(num)
			memDict[temp[i]] = int(num)
	elif line!='\n':

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

flag = True

while len(transName) != 0:
	delTrans = []
	for i in transName:
		if flag == True:
			print "<"+ i +", start>"
			for val in sorted(memDict):
				print val,memDict[val],
			print
		for j in range(0,x):
			command = transaction[i][0]
			cmd = command.split('(')
			if cmd[0] == "read":
				cmd = cmd[1].split(')')[0]
				source = cmd.split(',')[0]
				dest = cmd.split(',')[1]
				func(dest,memDict[source])
			elif cmd[0] == "write":
				cmd = cmd[1].split(')')[0]
				source = cmd.split(',')[1]
				dest = cmd.split(',')[0]
				temp = memDict[dest]
				exec("memDict[dest]="+source)
				print "<"+str(i)+", "+str(dest)+ ", "+str(temp) +">"
				for val in sorted(memDict):
					print val,memDict[val],
				print
			elif cmd[0] == "output":
				source = cmd[1].split(')')[0]
				diskDict[source] = memDict[source]
				if len(transaction[i])==1:
					print "<"+str(i)+", commit>"
					for val in sorted(memDict):
						print val,memDict[val],
					print
			else:
				cmd = cmd[0].replace(":","")
				exec(cmd)
				
			del transaction[i][0]
			if(len(transaction[i])==0):
				break;
		if(len(transaction[i])==0):
			delTrans.append(i)

	for i in delTrans:
		transName.remove(i)

	flag=False	
					