emacs line_countc.py

#! /usr/bin/env python3

import sys
import io

count = 0
# data = []
input_stream = io.TextIOWrapper(sys.stdin.buffer , encoding ='gbk')
for line in input_stream : # from stdin
	count += 1
	# data.append(line)
print(count) # print goes to sys.stdout

chmod +x line_countc.py

hadoop fs -put line_countc.py /00lifeng/haoliangzheng/

hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -input /00lifeng/haoliangzheng/600527.SH.CSV -output /00lifeng/haoliangzheng/output5/ -file "line_countc.py" -mapper "/usr/bin/cat" -reducer "python3 line_countc.py" -numReduceTasks 1

hadoop fs -ls line_countc.py /00lifeng/haoliangzheng/output5

hadoop fs -cat /00lifeng/haoliangzheng/output5/part-00000