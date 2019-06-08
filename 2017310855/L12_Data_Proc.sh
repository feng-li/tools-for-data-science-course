#! /usr/bin/sh

# Login
ssh student@47.92.169.139

# Input password

# Remove wc output
hadoop fs -rm -r /00lifeng/mujiachen/output

# View
hadoop fs -ls /00lifeng/mujiachen

# Switch work dic
cd 00lifeng/mujiachen

touch 00lifeng/mujiachen/data_proc.py
emacs -Q data_proc.py

#! /usr/bin/env python3

import sys
import io

input = io.TextIOWrapper(sys.stdin.buffer, encoding = 'gbk')

for line in input:

    # Split
    field = line.split(sep = ',')
    
    # Process
    date = field[2]
    max = max(float(field[4]), float(field[5]), float(field[6]), float(field[7]))
    min = min(float(field[4]), float(field[5]), float(field[6]), float(field[7]))
    range = max - min
    mean = (max + min)/2

    data = (date, max, min, range, mean)
    print(data) 

# Quit emacs
ctrl + x
ctrl + c

# Save
y

# Grant authority
chmod +x data_proc.py

# View
cat 600880.SH.CSV

# Try
cat 600880.SH.CSV | python3 data_proc.py

# Map reduce
hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -input /00lifeng/mujiachen/600880.SH.CSV -output /00lifeng/mujiachen/output -file "data_proc.py" -mapper "/usr/bin/cat" -reducer "python3 data_proc.py" -numReduceTasks 1

# View
hadoop fs -cat /00lifeng/mujiachen/output/* 
