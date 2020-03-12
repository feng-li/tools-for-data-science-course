#！/bin/sh
cd data/shanghai
hadoop fs -mkdir /00lifeng/Yuxiao 
hadoop fs -put 600767.SH.CSV  /00lifeng/Yuxiao/    
hadoop fs -get /00lifeng/Yuxiao/600767.SH.CSV  ./2016310823
hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -input /00lifeng/Yuxiao/600767.SH.CSV -output /00lifeng/Yuxiao/output/ -mapper "/usr/bin/cat" -reducer "/bin/wc"
hadoop fs -ls /00lifeng/Yuxiao/output
hadoop fs -cat /00lifeng/Yuxiao/output/part*