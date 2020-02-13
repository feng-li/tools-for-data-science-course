cd
cd 00lifeng/
mkdir 00lifeng/dengxuanjie/
cd dengxuanjie/
hadoop fs -mkdir /00lifeng/dengxuanjie
hadoop fs -ls /00lifeng/dengxuanjie
cd
cd data
cd shanghai
hadoop fs -put 600782.SH.CSV /00lifeng/dengxuanjie
cd 
cd 00lifeng/dengxuanjie/
hadoop fs -get /00lifeng/dengxuanjie/600782.SH.CSV
hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -input /00lifeng/dengxuanjie/600782.SH.CSV -output /00lifeng/dengxuanjie/output/ -mapper "/usr/bin/cat" -reducer "/bin/wc/"
hadoop fs -cat /00lifeng/dengxuanjie/output/part*