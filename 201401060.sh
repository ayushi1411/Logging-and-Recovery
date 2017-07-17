x=$#
if [ $x == 2 ];
then
    python 201401060_1.py $1 $2
elif [ $x == 1 ];
then
    python 201401060_2.py $1
fi