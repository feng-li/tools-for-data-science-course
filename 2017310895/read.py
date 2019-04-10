import re
starts_with_hash = 0
with open("D:/learnfiles/商务分析/情感分析/senti_analysis-master/senti_analysis-master/1_process.py","r") as f:
    for line in f:
        if re.match("^#",line):
            starts_with_hash +=1
print(starts_with_hash)
