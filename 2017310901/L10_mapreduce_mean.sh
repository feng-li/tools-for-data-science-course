screen -DR 2017310901
cd 00lifeng/dengxuanjie/
touch mean.py
emacs -Q mean.py
----------------------
#! /usr/bin/env python3
import sys
import io
s=0
l=0
input_stream=io.TextIOWrapper(sys.stdin.buffer, encoding='gbk')
for line in input_stream:
	inp=line.split(",")
	s+=eval(inp[5])
	l+=1
mean=s/l
print(mean)
----------------------
chmod +x mean.py
cat 600782.SH.CSV | mean.py
hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -input /00lifeng/dengxuanjie/600782.SH.CSV -output /00lifeng/dengxuanjie/output5/ -file "mean.py" -mapper "/usr/bin/cat" -reducer "python3 mean.py" -numReduceTasks 5
hadoop fs -cat /00lifeng/dengxuanjie/output5/part*
exit