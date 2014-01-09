#!/bin/bash
#c3po- robot protocol droid
#this script with create a daily report of projects
FILES="dru/*.txt"
echo "C3P0 report:"
echo "============"
for f in $FILES
do
	PROJ=$(echo "$f"|cut -d '/' -f2| cut -d '.' -f1)
	OWNR=$(echo "$f"|cut -d '/' -f1)
	TODO=$(grep -F "[ ]" $f |wc -l)
	DONE=$(grep -F "[x]" $f |wc -l)
	DUED=$(grep -F "#due_date" $f |cut -d ':' -f2)
	TOTL=$(echo "$TODO + $DONE"|bc)
	PERT=$(echo "$DONE*100/$TOTL"| bc)
	PWNR=$(echo "$f"|cut -d '/' -f1)
	echo "$PROJ:"
	echo "--------------------"
	echo "Owner:$PWNR"
	echo "Due Date:$DUED"
	echo "Action Steps Left:$TODO"
if [ "$PERT" -lt "5" ] && [ "$PERT" -ge "0" ];then
	echo "[>..................]$PERT%"
elif [ "$PERT" -lt "10" ] && [ "$PERT" -ge "5" ];then
        echo "[=>.................]$PERT%"
elif [ "$PERT" -lt "15" ] && [ "$PERT" -ge "10" ];then
        echo "[==>................]$PERT%"
elif [ "$PERT" -lt "20" ] && [ "$PERT" -ge "15" ];then
        echo "[==>................]$PERT%"
elif [ "$PERT" -lt "25" ] && [ "$PERT" -ge "20" ];then
        echo "[===>...............]$PERT%"
elif [ "$PERT" -lt "30" ] && [ "$PERT" -ge "25" ];then
        echo "[====>..............]$PERT%"
elif [ "$PERT" -lt "35" ] && [ "$PERT" -ge "30" ];then
        echo "[=====>.............]$PERT%"
elif [ "$PERT" -lt "40" ] && [ "$PERT" -ge "35" ];then
        echo "[======>............]$PERT%"
elif [ "$PERT" -lt "45" ] && [ "$PERT" -ge "40" ];then
        echo "[=======>...........]$PERT%"
elif [ "$PERT" -lt "50" ] && [ "$PERT" -ge "45" ]; then
	echo "[========>..........]$PERT%"
elif [ "$PERT" -lt "55" ] && [ "$PERT" -ge "50" ];then
        echo "[=========>.........]$PERT%"
elif [ "$PERT" -lt "60" ] && [ "$PERT" -ge "55" ];then
        echo "[==========>........]$PERT%"
elif [ "$PERT" -lt "65" ] && [ "$PERT" -ge "60" ];then
        echo "[===========>.......]$PERT%"
elif [ "$PERT" -lt "70" ] && [ "$PERT" -ge "65" ];then
        echo "[============>......]$PERT%"
elif [ "$PERT" -lt "75" ] && [ "$PERT" -ge "70" ];then
        echo "[=============>.....]$PERT%"
elif [ "$PERT" -lt "80" ] && [ "$PERT" -ge "75" ];then
        echo "[==============>....]$PERT%"
elif [ "$PERT" -lt "85" ] && [ "$PERT" -ge "80" ];then
        echo "[===============>...]$PERT%"
elif [ "$PERT" -lt "90" ] && [ "$PERT" -ge "85" ];then
        echo "[================>..]$PERT%"
elif [ "$PERT" -lt "95" ] && [ "$PERT" -ge "90" ]; then
        echo "[=================>.]$PERT%"
elif [ "$PERT" -lt "100" ] && [ "$PERT" -ge "95" ]; then
	echo "[==================>]$PERT%"
else
	echo "[===================]Done"
fi	
	echo ""
