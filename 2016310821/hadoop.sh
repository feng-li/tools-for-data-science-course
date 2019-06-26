#! /bin/sh
hadoop fs -mkdir /00lifeng/Luo
hadoop fs -put /data/shanghai/600782.SH.CSV /00lifeng/Luo
hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -input /00lifeng/Luo/600782.SH.CSV -output /00lifeng/Luo/output/ -mapper "/usr/bin/cat" -reducer "/bin/wc"
hadoop fs -cat /00lifeng/Luo/output/part*
