print('请输入意愿储存的年数：')
n=int(input(''))
print('请输入每月初储存的金额：')
X=int(input(''))
print('')

a=((1+0.03)**n)-1
b=12*(((1+0.03)**(1/12))-1)
S=12*X*(a/b)
S='%.2f' % S
result='每月存储{a}元，{b}年后，您将获得{c}元。'.format(a=X,b=n,c=S)
print(result)
