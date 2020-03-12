hadoop fs -rm -r /00lifeng/lixiaogao/output/

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
       -input /00lifeng/lixiaogao/600779.SH.CSV \
       -output /00lifeng/lixiaogao/output/ \
       -mapper "/usr/bin/cat" \
       -reducer "/bin/wc"

hadoop fs -cat /00lifeng/lixiaogao/output/*