def multipy(n1,n2):
    print(n1)
    print(n2)
    n1.reverse()
    n2.reverse()
    #n3存储结果，长为len(n1) + len(n2)
    n3=[]
    for i0 in range(len(n1)+len(n2)):
        n3.append(0)

    for i1 in range(len(n1)):
        for i2 in range(len(n2)):
            n3[i1+i2] += n1[i1]*n2[i2]
    for i3 in range(len(n3)):
        if(n3[i3]>9):
            n3[i3+1] += n3[i3] // 10
            n3[i3] = n3[i3] % 10
    n3.reverse()
    
    flag = ''
    for i in range(len(n3)):
        flag += str(n3[i])
    return int(flag)
