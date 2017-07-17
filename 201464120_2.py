import sys
oldDiskVal = {};
newDiskVal = {};
com_tran = [];
ckpt_tran = [];

endFlag = False;

filename = sys.argv[1]
file = open(filename)


for line in reversed(file.readlines()):

    if "end" in line and "ckpt" in line :
        endFlag = True;

    if "start" in line and "ckpt" in line and endFlag==True:
        temp = line.split("<");
        temp = temp[1].split(">")[0];
        temp = temp.replace("\n","");
        Pos = temp.find("ckpt");
        trans = temp[Pos+4:];
        trans = trans.replace(" ","");
        ckpt_tran = trans.split(",");
        print ckpt_tran;
        break;


i = 0;
for line in file:
    i = i+1;
    if line != '\n':    
        line = line.split("\n")[0];
        var = line.split(" ");
        for j in range(0,len(var),2):
            oldDiskVal[var[j]] = int(var[j+1]);
            newDiskVal[var[j]] = int(var[j+1]);
        break;



line_list = file.read().splitlines();
#print line_list
line_list = line_list[i+1:];

for i in range(len(line_list)-1,0,-1):

    line = line_list[i];

    if not line.strip():
        continue;

    if "start" in line and "ckpt" in line and endFlag==False: # start ckpt without and end .
        continue;

    if "start" in line and "ckpt" in line and endFlag==True : # no need to see logs before the starting ckpt with an end ;
        break;

    if "start" in line :
        continue;

    if "end" in line:
        endFlag = 1;
        for t in ckpt_tran:
            com_tran.append(t);
        continue;
    if "commit" in line:
        line = line.replace("<","");
        line = line.replace(">","");
        trans = line.split(',')[0];
        com_tran.append(trans);
        continue;

    

    temp = line ;
    temp = temp.replace("\n","");
    temp = temp.split("<")[1]
    temp = temp.split(">")[0];
    temp = temp.replace(" ","");
    temp = temp.split(",");
    t_name = temp[0];
    data = temp[1];
    val = int(temp[2]);

    if t_name in com_tran:
        continue;

    newDiskVal[data]=val;

print newDiskVal;
print oldDiskVal;
