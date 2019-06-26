# Login
ssh student@47.92.169.139

# Input password

# Remove previously failed files
hadoop fs -rm -r /00lifeng/mujiachen/output

# Import
hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -input /00lifeng/mujiachen/600880.SH.CSV -output /00lifeng/mujiachen/output/ -mapper "/usr/bin/cat" -reducer "/bin/wc"

# View
hadoop fs -cat /00lifeng/mujiachen/output/part*
