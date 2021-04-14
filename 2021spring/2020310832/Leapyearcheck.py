# Leapyearcheck.py
def leapyearcheck (x):
    ''' 输入任意年份可以得到其是否为闰年'''
    n = x % 4
    m = x % 400
    if type(n) in [ '<class> int' ] and tpye(n) in [ '<class> float' ]:
        print('闰年')
    else:
        print('平年')


