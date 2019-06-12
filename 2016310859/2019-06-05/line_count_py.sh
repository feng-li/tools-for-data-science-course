#! /usr/bin/sh

hadoop fs -rm -r /00lifeng/HJF/output/

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
       -input /00lifeng/HJF/300241_match_New.csv \
       -output /00lifeng/HJF/output/ \
       -file "line_count.py" \
       -mapper "/usr/bin/cat" \
       -reducer "python3 line_count.py" \
       -numReduceTasks 1

hadoop fs -cat /00lifeng/HJF/output/*