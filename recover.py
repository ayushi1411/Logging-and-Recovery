old_disk_values = {};
new_disk_values = {};
commited_trans = [];
checkpoint_trans = [];

end_ckpt_flag = 0;


# finding out the transactions of the last checkpoint with an end .

for line in reversed(open("log.txt","r").readlines()):

    if "end" in line.lower() and "ckpt" in line.lower() :
        end_ckpt_flag = 1;

    if "start" in line.lower() and "ckpt" in line.lower() and end_ckpt_flag==1:
        temp = line.replace("<","");
        temp = temp.replace(">","");
        temp = temp.replace("\n","");
        ckpt_pos = temp.find("ckpt");
        temp = temp[4+ckpt_pos:];
        temp = temp.replace(" ","");
        checkpoint_trans = temp.split(",");
        print checkpoint_trans;
        break;


# getting initial disk values
pos = 0;
for line in open("log.txt","r").readlines():

    pos = pos+1;
    if not line.strip():
        continue;

    line = line.replace("\n","");
    lis = line.split(" ");
    for i in range(0,len(lis),2):
        old_disk_values[lis[i]] = int(lis[i+1]);
        new_disk_values[lis[i]] = int(lis[i+1]);
    break;



line_list = open("log.txt","r").read().splitlines();
line_list = line_list[pos+1:];

#traversing log in reverse order after removing the initial disk line
for i in range(len(line_list)-1,0,-1):

    line = line_list[i];

    if not line.strip():
        continue;

    if "start" in line and "ckpt" in line and end_ckpt_flag==0: # start ckpt without and end .
        continue;

    if "start" in line and "ckpt" in line and end_ckpt_flag==1 : # no need to see logs before the starting ckpt with an end ;
        break;

    if "start" in line :
        continue;

    if "commit" in line:
        line = line.replace("<","");
        line = line.replace(">","");
        t_name = line.split(',')[0];
        commited_trans.append(t_name);
        print commited_trans;
        continue;

    if "end" in line:
        end_ckpt_flag = 1;
        for t in checkpoint_trans:
            commited_trans.append(t);
        continue;

    print line
    temp = line ;
    temp = temp.replace("\n","");
    temp = temp.replace("<","");
    temp = temp.replace(">","");
    temp = temp.replace(" ","");
    temp = temp.split(",");
    t_name = temp[0];
    data_elem = temp[1];
    val = int(temp[2]);

    if t_name in commited_trans:
        continue;

    new_disk_values[data_elem]=val;

print new_disk_values;
print old_disk_values;
