import sys
def makeGlobal(str_name,val): # set variable with str_name with value val

	if str_name in globals() : # already a global variable
	    exec (str_name + "=" + str(val));
	    globals()[str_name]=eval(str_name);

	if str_name not in globals(): # not a global variable
	    exec ("global "+str_name+"; "+ str_name+"="+str(val));


file = sys.argv[1]
x = int(sys.argv[2])
filename = open(file)
flagfirst = True
transaction = {}
transName = []
diskVal = {}
memVal = {}
var = {}
for line in filename:
	if flagfirst == True:
		temp = line.split(' ')
		flagfirst = False
		for i in range(0,len(temp),2):
			num = temp[i+1]
			num = num.split('\n')[0]
			diskVal[temp[i]] = int(num)
			memVal[temp[i]] = int(num)
		continue;
	if not line.strip():
	    continue;
	temp = line.split(' ')
	name = temp[0]
	transName.append(name)
	cnt = int(temp[1])
	transaction[name] = []
	it = 1
	for line in filename:
		t = line.replace('\n','')
		transaction[name].append(t)
		it +=1
		if cnt<i:
			break

flag = True

while len(transName) != 0:
	delelem = []
	for i in transName:
		if flag == True:
			print "<"+ i +", start>"
			for val in sorted(memVal):
				print val,memVal[val],
			print
		for j in range(0,x):
			command = transaction[i][0]
			cmd = command.replace('(','')
			print cmd
			if "read" in cmd:
				cmd = cmd.replace(')','')
				xt = cmd.split(',')[0]
				xt = xt[4:]
			#	x=x.split(' ')[1]
				y = cmd.split(',')[1]
				makeGlobal(y,memVal[xt])
			elif "output" in cmd:
				source = cmd.replace(')','')
				source=source[6:]
				diskVal[source] = memVal[source]
				if len(transaction[i])==1:
					print "<"+str(i)+", commit>"
					for val in sorted(memVal):
						print val,memVal[val],
					print
			elif "write" in cmd:
				cmd = cmd.replace(')','')
				xt = cmd.split(',')[1]
				y = cmd.split(',')[0]
				y=y[5:]
				temp = memVal[y]
				exec("memVal[y]="+xt)
				print "<"+str(i)+", "+str(y)+ ", "+str(temp) +">"
				for val in sorted(memVal):
					print val,memVal[val],
				print
			
			else:
				cmd = cmd.replace(":","")
				print cmd
				exec(cmd)
				
			del transaction[i][0]
			if(transaction[i]==[]):
				break;
		if(transaction[i]==[]):
			delelem.append(i)

	for i in delelem:
		transName.remove(i)

	flag=False	
					