#！/usr/bin/env sh
hadoop
hadoop fs
cd 00lifeng
hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -input /00lifeng/gaosiqin/600863.SH.CSV -output /00lifeng/gaosiqin/output/ -mapper "/usr/bin/cat" reducer "/bin/wc"
hadoop fs -ls /00lifeng/gaosiqin/output/part*