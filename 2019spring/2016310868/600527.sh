hadoop fs -mkdir /00lifeng/haoliangzheng
cd 
cd data/
cd shanghai/
hadoop fs -put 600527.SH.CSV /00lifeng/haoliangzheng/
hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -input /00lifeng/haoliangzheng/600527.SH.CSV -output /00lifeng/haoliangzheng/output2/ -mapper "/usr/bin/cat" -reducer "/bin/wc"
hadoop fs -cat /00lifeng/haoliangzheng/output2/part*