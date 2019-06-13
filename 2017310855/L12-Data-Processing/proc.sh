#! /usr/bin/sh

# Map reduce
hadoop jar /usr/lib/hadoop-curr ent/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -input /00lifeng/mujiachen/600880.SH.CSV -output /00lifeng/mujiachen/output -file "data_proc.py" -mapper "/usr/bin/cat" -reducer "python3 data_proc.py" -numReduceTasks 1
