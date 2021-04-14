cd 
cd data/
cd shanghai/
hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -input /00lifeng/lijinyang/600780.SH.CSV -output /00lifeng/lijinyang/output/ -mapper "/usr/bin/cat" -reducer "/bin/wc"
hadoop fs -cat /00lifeng/lijinyang/ouput/part*