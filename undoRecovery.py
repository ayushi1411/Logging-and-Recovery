import sys
filename = sys.argv[1]
file = open(filename)
lines = file.readlines()
#print lines
for i in range(len(lines)):
	lines[i]=lines[i].split('\n')[0]
	if lines[i] == '':
		del lines[i]
		i-=1
#print lines

olddiskVal = {}
newdiskVal = {}
update = []
line = lines[0]
temp = line.split(' ')
for i in range(0,len(temp),2):
	olddiskVal[temp[i]]=int(temp[i+1])
	newdiskVal[temp[i]]=int(temp[i+1])

checkpointTransaction = []
committedTransaction = []
flag = False
for i in range(len(lines)-1,0,-1):
	if "end" in lines[i] and "ckpt" in lines[i]:
		flag=True
	if "start" in lines[i] and "ckpt" in lines[i] and flag==True:
		line = lines[i].split("<")[1]
		line = line.split(">")[0]
		pos = line.find("ckpt")
		line = line[pos+4:]
		line.replace(" ","")
		line = line.split(",")
		checkpointTransaction=checkpointTransaction+line
		break
for i in range(len(lines)-1,0,-1):
	line=lines[i]
	if "start" in line and "ckpt" in line and flag==False: 
		continue;

	if "start" in line and "ckpt" in line and flag==True : 
		break;

	if "start" in line:
		continue;

	line = line.split("<")[1]
	line = line.split(">")[0]
	line = line.split(",")
	if(len(line)==2):
		if(line[1]==" commit"):
			committedTransaction.append(line[0])
			continue;
	elif(len(line)==1):
		line = line[0].split(" ")
		for x in checkpointTransaction:
			committedTransaction.append(x)
		continue;
	trans = line[0]
	var = line[1].replace(" ","")
	val = int(line[2].replace(" ",""))
	if trans not in committedTransaction:
		newdiskVal[var]=val
		if var not in update:
			update.append(var)

#for i in olddiskVal.keys():
#	if olddiskVal[i] != newdiskVal[i]:
#		print i,newdiskVal[i]
update.sort()
for i in update:
	print i,newdiskVal[i],
