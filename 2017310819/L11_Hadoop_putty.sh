#£°/usr/bin/env sh
cd 00lifeng
mkdir 2017310819
ls
hadoop
haddoop version
echo $HADOOP_HOME 
hadoop ls 
hadoop fs -ls
hadoop fs -mkdir /00lifeng/zhangyunwen
hadoop fs -ls /00lifeng/
hadoop fs -rm -r /00lifeng/zhangyunwen/
cd 
cd data
cd shanghai
emacs -Q 600782.SH.CSV
revert buffer-with-coding-system
yes

hadoop fs -put 600782.SH.CSV /00lifeng/zhangyunwen/  
hadoop fs -ls

hadoop fs -get /00lifeng/zhangyunwen/600782.SH.CSV 

hadoop fs 

copy from local

cat 600893.SH.CSV | wc 
#mapreducer‘À––
Cd Workshop+00lifeng]$ 
 Workshop+00lifeng]$ 
Echo $HADOOP_HOME
Hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-s
Hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -input /00lifeng/lifeng/600863.SH.CSV -output /00lifeng/lifeng/output/ -m

Hadoop fs -ls /00lifeng/lifeng/output/part*
Hadoop fs -cat /00lifeng/lifeng/output/part*