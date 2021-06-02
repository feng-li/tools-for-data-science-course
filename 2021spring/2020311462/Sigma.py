import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import sympy
import datetime
import yagmail
from tkinter import *
from sympy import *
from PIL import Image, ImageTk

a, b, c = sympy.symbols('a, b, c')
s, t, d = sympy.symbols('s, t, d')
as_prove, as_cs, as_sc, as_pqr, as_ast = False, False, False, False, False
ast, _same_, check = True, False, True
OS, ver, time0 = 'Linux', '4.1', datetime.datetime.now()


def info():
    str0 = '\n 基于Python 3开发的 三元轮换对称不等式运算程序\n\n' \
           ' ----------------- Author ------------------\n' \
           ' Nova cx0222 Jinan, Shandong\n' \
           ' 2913026224@qq.com, 1929842479@qq.com\n\n' \
           ' ------------- Current Version -------------\n' \
           ' ver 4.1 [20210221]  Jinan, Shandong\n' \
           ' 该程序装载的最新算法版本为 Sigma_Core_2+ 等\n\n' \
           ' ------------- Historic Version ------------\n' \
           ' ver 4.0 [20210220]  Jinan, Shandong\n\n' \
           ' ver 3.5 [20210219]  Jinan, Shandong\n' \
           ' ver 3.4 [20210206]  Jinan, Shandong\n' \
           ' ver 3.3 [20210131]  Jinan, Shandong\n' \
           ' ver 3.2 [20210130]  Jinan, Shandong\n' \
           ' ver 3.1 [20210128]  Jinan, Shandong\n' \
           ' ver 3.0 [20210116]  Jinan, Shandong\n\n' \
           ' ver 2.7 [20210115]  Jinan, Shandong\n' \
           ' ver 2.6 [20210114]  Jinan, Shandong\n' \
           ' ver 2.5 [20210113]  Jinan, Shandong\n' \
           ' ver 2.4 [20210111]  Jinan, Shandong\n' \
           ' ver 2.3 [20210110]  Jinan, Shandong\n' \
           ' ver 2.2 [20210105]  Jinan, Shandong\n' \
           ' ver 2.1 [20210104]  Jinan, Shandong\n\n' \
           ' ver 1.6 [20201229]  Jinan, Shandong\n' \
           ' ver 1.5 [20201225]  Jinan, Shandong\n' \
           ' ver 1.4 [20201223]  Jinan, Shandong\n' \
           ' ver 1.3 [20201222]  Jinan, Shandong\n' \
           ' ver 1.2 [20201221]  Jinan, Shandong\n' \
           ' ver 1.1 [20201221]  Jinan, Shandong\n\n' \
           ' ver 0.1 [20201218]  Changping, Beijing\n\n' \
           ' ------ Recommended Version for Python -----\n' \
           ' Python 3.7.x or later with sympy\n\n'
    return str0


file8_0 = 'result.txt'
time1 = time0.strftime('%Y/%m/%d %H:%M:%S')
with open(file8_0, 'a') as file0:
    file0.write('Sigma 4.1 已启动！时间：')
    file0.write('{0}\n'.format(time1))
    file0.write('{0}\n'.format(info()))


def ex_0(expr):
    expr0 = [i for i in expr]
    expr1 = ''
    for i in range(0, expr0.__len__()):
        if expr0[i] == 'a':
            expr0[i] = 'b'
            continue
        if expr0[i] == 'b':
            expr0[i] = 'c'
            continue
        if expr0[i] == 'c':
            expr0[i] = 'a'
            continue
    for i in range(0, expr0.__len__()):
        expr1 += expr0[i]
    expr1 = str(expr1)
    return expr1


def ex_1(expr):
    expr0 = [i for i in expr]
    expr1 = ''
    for i in range(0, expr0.__len__()):
        if expr0[i] == 'a':
            expr0[i] = 'c'
            continue
        if expr0[i] == 'b':
            expr0[i] = 'a'
            continue
        if expr0[i] == 'c':
            expr0[i] = 'b'
            continue
    for i in range(0, expr0.__len__()):
        expr1 += expr0[i]
    expr1 = str(expr1)
    return expr1


def sigma(expr):
    expr0 = ex_0(expr) + ' + ' + ex_1(expr) + ' + ' + expr
    expr0 = str(expr0)
    return expr0


def pi(expr):
    expr0 = '(' + ex_0(expr) + ') * (' + ex_1(expr) + ') * (' + expr + ')'
    expr0 = str(expr0)
    return expr0


# noinspection PyGlobalUndefined
def judge0(expr):
    global jud1, same0, sym0
    expr0 = sympy.simplify(numer(cancel(expr)))
    jud0, jud1 = 1, 1
    try:
        Poly(expr0, a, b, c)
    except sympy.polys.polyerrors.PolynomialError:
        jud0 = 0
    except NameError:
        jud1 = 0

    if jud0 == 1:
        deg0 = Poly(expr0, a, b, c).total_degree()
        expr1 = list(sympy.Poly(expr0, a, b, c).as_dict().keys())
        len0 = expr1.__len__()
        same0 = 1
        for i in range(0, len0):
            if sum(expr1[i]) != deg0:
                same0 = 0
                break

    cyc0 = 0
    if expr0.subs({(a, b, c): (b, c, a)}) == expr0:
        if expr0.subs({(a, b, c): (c, a, b)}) == expr0:
            cyc0 = 1
    if cyc0 == 1:
        sym0 = 0
        if expr0.subs({(a, b, c): (a, c, b)}) == expr0:
            if expr0.subs({(a, b, c): (c, b, a)}) == expr0:
                if expr0.subs({(a, b, c): (b, a, c)}) == expr0:
                    sym0 = 1
    return [jud0, jud1, same0, cyc0, sym0]


def judge1(expr):
    expr1 = sympy.simplify(numer(cancel(sigma(expr))))
    deg0 = Poly(expr1, a, b, c).total_degree()
    return deg0


def normal0(expr):
    expr0 = sympy.simplify(numer(cancel(sigma(expr))))
    return expr0


def normal1(expr):
    expr0 = sympy.simplify(numer(cancel(expr)))
    return expr0


def cs3_0(expr):
    if as_cs:
        out0 = '\n[整理] ' + str(normal0(expr))
        expr0 = str(numer(cancel(sigma(expr))))
        expr2 = numer(cancel(sigma(expr)))
    else:
        out0 = '\n[整理] ' + str(normal1(expr))
        expr0 = str(numer(cancel(expr)))
        expr2 = numer(cancel(expr))
    s_bc, s_ca, s_ab = (b - c) ** 2, (c - a) ** 2, (a - b) ** 2
    deg0 = judge1(expr0)
    fnum = dict1(deg0).__len__()
    varlistf = sympy.symbols('v:{}:a'.format(fnum))
    s_a, s_b, s_c = 0, 0, 0
    for i in range(0, fnum):
        s_a += varlistf[i] * dict1(deg0)[i]
        s_b += varlistf[i] * sympy.simplify(ex_0('{0}'.format(dict1(deg0)[i])))
        s_c += varlistf[i] * sympy.simplify(ex_1('{0}'.format(dict1(deg0)[i])))
    ineq = s_a * s_bc + s_b * s_ca + s_c * s_ab
    ineq0 = expand(s_a * s_bc + s_b * s_ca + s_c * s_ab)
    func0 = sympy.poly(ineq0 - expr2, a, b, c)
    equlist0 = []
    for i in range(0, dict0(deg0).__len__()):
        equlist0.append(func0.coeff_monomial(dict0(deg0)[i]))
    ans = solve(equlist0, varlistf)
    result0 = ineq.subs(ans)
    result2_a, result2_b, result2_c = s_a.subs(ans), s_b.subs(ans), s_c.subs(ans)
    result0 = str(result0)
    varlistf0 = [str(varlistf[i]) for i in range(0, fnum)]
    varlistf1, i = [], 0
    result2 = s_a.subs(ans)
    for j in range(0, fnum):
        if varlistf0[j] in result0:
            varlistf1.append(varlistf0[j])
    fnum0 = varlistf1.__len__()
    if fnum0 == 0:
        out0 += '\n[结果] ' + 'Σ (' + str(result2) + ') * (b - c) ** 2'
    else:
        out0 += '\n[通式] ' + 'Σ (' + str(result2) + ') * (b - c) ** 2'
        varlistf2 = [[] for _ in range(0, fnum0)]
        for k in range(0, fnum0):
            varlistf2[k] = sympy.symbols(varlistf1[k])
        varlistf3 = [varlistf2[i] for i in range(0, fnum0)]
        out0 += '\n[参数] ' + str(varlistf2)
        if judge1(expr0) == 4:
            add_a = sympy.poly(result2_a, a, b, c)
            equlist_4_1 = [add_a.coeff_monomial(c ** 2) - add_a.coeff_monomial(a ** 2)]
            equlist_4_2 = [add_a.coeff_monomial(a ** 2) - add_a.coeff_monomial(b ** 2)]
            add0_4 = solve(equlist_4_1 + equlist_4_2, varlistf3)
            result2 = numer(factor(add_a.subs(add0_4)))
            out0 += '\n[默认] ' + 'Σ (' + str(result2) + ') * (b - c) ** 2'
        if judge1(expr0) >= 5:
            add_a = sympy.poly(result2_a, a, b, c)
            add0_5 = {varlistf2[i]: 0 for i in range(0, fnum0)}
            result2 = numer(factor(add_a.subs(add0_5)))
            out0 += '\n[默认] ' + 'Σ (' + str(result2) + ') * (b - c) ** 2'
    return [out0, str(result2)]


def sc3_0(expr):
    if as_sc:
        out0 = '\n[整理] ' + str(normal0(expr))
        expr0 = str(numer(cancel(sigma(expr))))
        expr2 = numer(cancel(sigma(expr)))
    else:
        out0 = '\n[整理] ' + str(normal1(expr))
        expr0 = str(numer(cancel(expr)))
        expr2 = numer(cancel(expr))
    s_bc, s_ca, s_ab = (a - b) * (a - c), (b - c) * (b - a), (c - a) * (c - b)
    deg0 = judge1(expr0)
    fnum = dict1(deg0).__len__()
    varlistf = sympy.symbols('v:{}:a'.format(fnum))
    s_a, s_b, s_c = 0, 0, 0
    for i in range(0, fnum):
        s_a += varlistf[i] * dict1(deg0)[i]
        s_b += varlistf[i] * sympy.simplify(ex_0('{0}'.format(dict1(deg0)[i])))
        s_c += varlistf[i] * sympy.simplify(ex_1('{0}'.format(dict1(deg0)[i])))
    ineq = s_a * s_bc + s_b * s_ca + s_c * s_ab
    ineq0 = expand(s_a * s_bc + s_b * s_ca + s_c * s_ab)
    func0 = sympy.poly(ineq0 - expr2, a, b, c)
    equlist0 = []
    for i in range(0, dict0(deg0).__len__()):
        equlist0.append(func0.coeff_monomial(dict0(deg0)[i]))
    ans = solve(equlist0, varlistf)
    result0 = ineq.subs(ans)
    result2_a, result2_b, result2_c = s_a.subs(ans), s_b.subs(ans), s_c.subs(ans)
    result0 = str(result0)
    varlistf0 = [str(varlistf[i]) for i in range(0, fnum)]
    varlistf1, i = [], 0
    result2 = s_a.subs(ans)
    for j in range(0, fnum):
        if varlistf0[j] in result0:
            varlistf1.append(varlistf0[j])
    fnum0 = varlistf1.__len__()
    if fnum0 == 0:
        out0 += '\n[结果] ' + 'Σ (' + str(result2) + ') * (a - b) * (a - c)'
    else:
        out0 += '\n[通式] ' + 'Σ (' + str(result2) + ') * (a - b) * (a - c)'
        varlistf2 = [[] for _ in range(0, fnum0)]
        for k in range(0, fnum0):
            varlistf2[k] = sympy.symbols(varlistf1[k])
        varlistf3 = [varlistf2[i] for i in range(0, fnum0)]
        out0 += '\n[参数] ' + str(varlistf2)
        if judge1(expr0) == 4:
            add_a = sympy.poly(result2_a, a, b, c)
            equlist_4_1 = [add_a.coeff_monomial(c ** 2) - add_a.coeff_monomial(a ** 2)]
            equlist_4_2 = [add_a.coeff_monomial(a ** 2) - add_a.coeff_monomial(b ** 2)]
            add0_4 = solve(equlist_4_1 + equlist_4_2, varlistf3)
            result2 = numer(factor(add_a.subs(add0_4)))
            out0 += '\n[默认] ' + 'Σ (' + str(result2) + ') * (a - b) * (a - c)'
        if judge1(expr0) >= 5:
            add_a = sympy.poly(result2_a, a, b, c)
            add0_5 = {varlistf2[i]: 1 for i in range(0, fnum0)}
            result2 = numer(factor(add_a.subs(add0_5)))
            out0 += '\n[默认] ' + 'Σ (' + str(result2) + ') * (a - b) * (a - c)'
    return out0


def pqr2_6(expr):
    if _same_:
        result2_6_1 = pqr2_6_1(expr)
        return result2_6_1
    else:
        result2_6_2 = pqr2_6_2(expr)
        return result2_6_2


def pqr2_6_1(expr):
    if as_pqr:
        ineq0 = numer(cancel(sigma(expr)))
    else:
        ineq0 = numer(cancel(expr))
    a, b, c = sympy.symbols('a, b, c')
    p, q, r = sympy.symbols('p, q, r')
    list1, list2, equlist0 = [], dict0(judge1(expr)), []
    list0 = dict2(judge1(expr))[-1]
    fnum0, fnum1, result0, resultpqr = list0.__len__(), list2.__len__(), 0, 0
    varlistf = sympy.symbols('c:{}:a'.format(fnum0))
    for i in range(0, fnum0):
        list1.append(list0[i].subs({p: (a + b + c), q: a * b + b * c + c * a, r: a * b * c}))
        result0 += list1[i] * varlistf[i]
        resultpqr += list0[i] * varlistf[i]
    result1 = sympy.poly(sympy.simplify(result0) - ineq0, a, b, c)
    for i in range(0, fnum1):
        equlist0.append(result1.coeff_monomial(list2[i]))
    ans = solve(equlist0, varlistf)
    result2 = factor(resultpqr.subs(ans))
    return result2


def pqr2_6_2(expr):
    if as_pqr:
        ineq0 = numer(cancel(sigma(expr)))
    else:
        ineq0 = numer(cancel(expr))
    a, b, c = sympy.symbols('a, b, c')
    deg0 = judge1(expr)
    poly0 = sympy.poly(ineq0, a, b, c)
    polydict0 = poly0.as_dict()
    all0 = list(zip(list(polydict0.keys()), list(polydict0.values())))
    length0 = all0.__len__()
    listcy = [[] for _ in range(0, deg0 + 1)]
    listcy0 = [0 * a for _ in range(0, deg0 + 1)]
    for cy in range(1, deg0 + 1):
        for len in range(0, length0):
            if sum(all0[len][0]) == cy:
                listcy[cy].append(
                    (a ** all0[len][0][0] * b ** all0[len][0][1] * c ** all0[len][0][2]) * all0[len][1])
        count0 = listcy[cy].__len__()
        for i in range(0, count0):
            listcy0[cy] += listcy[cy][i]
        listcy0[cy] = sympy.simplify(listcy0[cy])
    for len in range(0, length0):
        if sum(all0[len][0]) == 0:
            listcy0[0] = all0[len][1]
    result3 = listcy0[0]
    for i in range(1, deg0 + 1):
        if as_pqr:
            result3 += pqr2_6_1(str(listcy0[i])) / 3
        else:
            result3 += pqr2_6_1(str(listcy0[i]))
    return result3


def ast3_0(expr):
    if as_ast:
        exprast = str(normal0(str(expr)))
    else:
        exprast = str(normal1(str(expr)))
    expr0, expr1 = [i for i in exprast], ''
    for i in range(0, expr0.__len__()):
        if expr0[i] == 'b':
            expr0[i] = '(a+s)'
            continue
        if expr0[i] == 'c':
            if ast:
                expr0[i] = '(a+t)'
                continue
            else:
                expr0[i] = '(a+s+t)'
    for i in range(0, expr0.__len__()):
        expr1 += expr0[i]
    expr1 = sympy.poly(sympy.simplify(expand(expr1)), a)
    deg0 = expr1.total_degree()
    expr2, expr3 = '', []
    for n in range(0, deg0):
        expr_temp = factor(expr1.coeff_monomial(a ** (deg0 - n)))
        expr2 += str(expr_temp * a ** (deg0 - n)) + ' + '
        expr3.append(expr_temp)
    constant0 = str(factor(expr1.coeff_monomial(a ** 0)))
    expr2 += constant0
    expr3.append(constant0)
    return [expr2, expr3]


def dict0(jud0):
    termlist0 = []
    for i in range(0, jud0 + 1):
        for j in range(0, jud0 + 1):
            for k in range(0, jud0 + 1):
                if i + j + k == jud0:
                    termlist0.append(a ** i * b ** j * c ** k)
    return termlist0


def dict1(jud1):
    termlist1 = []
    for i in range(0, jud1 - 1):
        for j in range(0, jud1 - 1):
            for k in range(0, jud1 - 1):
                if i + j + k == jud1 - 2:
                    termlist1.append(a ** i * b ** j * c ** k)
    return termlist1


def dict2(deg0):
    pqrdict = [[] for _ in range(0, deg0 + 1)]
    p, q, r = sympy.symbols('p, q, r')
    for d in range(0, deg0 + 1):
        for p0 in range(0, d + 1):
            for q0 in range(0, d + 1):
                for r0 in range(0, d + 1):
                    if p0 + 2 * q0 + 3 * r0 == d:
                        pqrdict[d].append(p ** p0 * q ** q0 * r ** r0)
    return pqrdict


def _get_(func):
    exp0 = entry0.get()
    out0 = '\n[输入] ' + str(exp0)
    if func == 1:
        listcs = cs3_0(exp0)
        out0 += listcs[0]
        outcut = listcs[1]
        window3 = tk.Toplevel()
        window3.title('三元轮换对称不等式运算程序  ver 4.1  SOS分拆结果')
        window3.geometry('800x400')
        window3.resizable(True, False)
        result3 = tk.Text(window3, width=400, height=28, borderwidth=1)
        result3.pack()
        result3.insert(END, out0)
        if judge1(entry0.get()) != 3:
            cs = tk.Button(window3, text='进一步运算', command=lambda: _further_(outcut))
            cs.pack()
        window3.mainloop()
    if func == 2:
        window4 = tk.Toplevel()
        out0 += sc3_0(exp0)
        window4.title('三元轮换对称不等式运算程序  ver 4.1  Schur分拆结果')
        title4 = tk.Text(window4, width=800, height=500)
        title4.pack(side=tkinter.LEFT, fill=tkinter.Y)
        window4.geometry('800x500')
        window4.resizable(True, True)
        title4.insert(tkinter.INSERT, out0)
        window4.mainloop()


def _catch_(func):
    exp0 = entry0.get()
    out0 = '\n[输入] {0}'.format(str(exp0))
    window5 = tk.Toplevel()
    if func == 1:
        if as_pqr:
            out0 += '\n[整理] ' + str(normal0(exp0))
        else:
            out0 += '\n[整理] ' + str(normal1(exp0))
        out0 += '\n[换元] (a + b + c, a*b + b*c + c*a, a*b*c) ⬅ (p, q, r)'
        out0 += '\n[结果] ' + str(pqr2_6(exp0))
        window5.title('三元轮换对称不等式运算程序  ver 4.1  pqr分拆结果')
    if func == 2:
        if as_ast:
            out0 += '\n[整理] ' + str(normal0(exp0))
        else:
            out0 += '\n[整理] ' + str(normal1(exp0))
        if ast:
            out0 += '\n[换元] (a, a + s, a + t) ⬅ (a, b, c)'
        else:
            out0 += '\n[换元] (a, a + s, a + s + t) ⬅ (a, b, c)'
        listast = ast3_0(exp0)
        out0 += '\n[结果] ' + listast[0]
        window5.title('三元轮换对称不等式运算程序  ver 4.1  差分代换结果')
        cs = tk.Button(window5, text='机器证明', command=lambda: _more_(listast[1]))
        cs.pack()
    title = tk.Text(window5, width=800, height=500)
    title.pack(side=tkinter.LEFT, fill=tkinter.Y)
    window5.geometry('800x500')
    window5.resizable(True, True)
    title.insert(tkinter.INSERT, out0)
    file8_0 = 'result.txt'
    with open(file8_0, 'a') as file0:
        file0.write('{0}\n'.format(out0))
    window5.mainloop()


def _zero_(deg0):
    a, b, c, co = sympy.symbols('a, b, c, co')
    if deg0 == 4:
        expr_a = 2 * a ** 2 + a * b + a * c + 2 * b * c
        return expr_a


def _further_(out):
    window7 = tk.Toplevel()
    window7.geometry('800x520')
    window7.resizable(True, True)
    window7.title('三元轮换对称不等式运算程序  ver 4.1  进一步运算')
    title7_0_0 = tk.Label(window7, text='初步结果：')
    title7_0_1 = tk.Label(window7, text='Sa = ' + out)
    title7_0_2 = tk.Label(window7, text='Sb = ' + ex_0(out))
    title7_0_3 = tk.Label(window7, text='Sc = ' + ex_0(ex_0(out)))
    title7_0_0.pack(), title7_0_1.pack(), title7_0_2.pack(), title7_0_3.pack()
    deg0 = judge1(entry0.get())
    if deg0 == 4:
        title7_1_0 = tk.Label(window7, text='请配置零因式：')
        title7_1_1 = tk.Label(window7, text='Ta = ' + str(_zero_(deg0)))
        title7_1_0.pack(), title7_1_1.pack()
        entry7_4_1, entry7_4_0 = tk.Entry(window7, width=8), tk.Entry(window7, width=8)
        input7_4_1 = tk.Label(window7, text='请输入零因式所乘系数：')
        input7_4_0 = tk.Label(window7, text='请输入原式所乘系数：')
        input7_4_1.pack(), entry7_4_1.pack(), input7_4_0.pack(), entry7_4_0.pack()

        def add_4():
            k1, k0 = entry7_4_1.get(), entry7_4_0.get()
            out7_4 = sympy.simplify(_zero_(deg0)) * int(k1) + sympy.simplify(out) * int(k0)
            out_4 = '[调整] ' + 'Σ (' + str(out7_4) + ') * (b - c) ** 2'
            title7_5 = tk.Text(window7, height=10)
            title7_5.pack()
            title7_5.insert(tkinter.INSERT, out_4)
            return out_4

        button7_6 = tk.Button(window7, text='确定', command=add_4)
        button7_6.pack()
    window7.mainloop()


def _more_(list0):
    num0 = list0.__len__()
    window8 = tk.Toplevel()
    window8.geometry('1000x520')
    window8.resizable(True, True)
    window8.title('三元轮换对称不等式运算程序  ver 4.1  进一步运算')
    title8_0 = tk.Label(window8, text='初步结果：')
    title8_0.pack()
    file8_0 = 'result.txt'
    with open(file8_0, 'a') as file0:
        file0.write('初步结果：\n')
    for i in range(0, num0):
        text8 = Text(window8, width=100, height=2, bd=0)
        text8.pack()
        text8.insert(END, list0[i])
        with open(file8_0, 'a') as file0:
            file0.write('{0}\n'.format(list0[i]))

    def auto_prove_0(n, l_0):
        l_1, l_2, l_3, result1, result2, result3 = [], [], [], [], [], []
        for i in range(0, n):
            result1.append(factor_list(l_0[i])[1])
            len1 = result1[i].__len__()
            for j in range(0, len1):
                if result1[i][j][1] % 2 == 1:
                    l_1.append(result1[i][j][0])
        len2 = l_1.__len__()
        for k in range(0, len2):
            l_2.append(Poly(l_1[k], s, t))
            result2.append(list(l_2[k].as_dict().values()))
            len3 = result2[k].__len__()
            for m_0 in range(0, len3):
                if result2[k][m_0] < 0:
                    l_3.append(result2[k][m_0])
                if l_3.__len__() != 0:
                    if result3.__len__() != 0:
                        temp = 0
                        for m_1 in range(0, result3.__len__()):
                            if l_1[k] != result3[m_1]:
                                temp += 1
                        if temp == result3.__len__():
                            result3.append(l_1[k])
                    else:
                        result3.append(l_1[k])
            l_3 = []
        return result3

    def poly_cut(poly0):
        poly_0 = Poly(poly0, s, t)
        poly_1 = list(poly_0.as_dict().keys())
        poly_mono = [poly_1[i] for i in range(0, poly_1.__len__())]
        poly_coeff = list(poly_0.as_dict().values())
        max0 = poly_mono[-1][0]
        coeff0 = poly_coeff[-1]
        poly_2 = factor(sympy.simplify(poly0) - sympy.simplify(coeff0 * sympy.simplify(s - t) ** max0))
        return poly_2

    result4 = auto_prove_0(num0, list0)
    while True:
        if result4.__len__() != 0:
            title8_1 = tk.Label(window8, text='进一步结果：')
            title8_1.pack()
            with open(file8_0, 'a') as file0:
                file0.write('进一步结果:\n')
            for i in range(0, result4.__len__()):
                text8 = Text(window8, width=100, height=2, bd=0)
                text8.pack()
                text8.insert(END, result4[i])
                with open(file8_0, 'a') as file0:
                    file0.write('{0}\n'.format(result4[i]))
            title8_2 = tk.Label(window8, text='只需要证明上述多项式非负！')
            title8_2.pack()
            with open(file8_0, 'a') as file0:
                file0.write('只需要证明上述多项式非负！\n')
            result5 = [poly_cut(result4[i]) for i in range(0, result4.__len__())]
            result4 = auto_prove_0(result5.__len__(), result5)
        else:
            title8_3 = tk.Label(window8, text='显然！证毕！')
            title8_3.pack()
            with open(file8_0, 'a') as file0:
                file0.write('显然！证毕！\n')
            break
    window8.mainloop()


def _core_2_():
    expr = entry0.get()
    if as_prove:
        exprast = str(normal0(str(expr)))
    else:
        exprast = str(normal1(str(expr)))
    expr0, expr1 = [i for i in exprast], ''
    for i in range(0, expr0.__len__()):
        if expr0[i] == 'b':
            expr0[i] = '(a+s)'
            continue
        if expr0[i] == 'c':
            expr0[i] = '(a+t)'
            continue
    for i in range(0, expr0.__len__()):
        expr1 += expr0[i]
    expr1 = sympy.poly(sympy.simplify(expand(expr1)), a)
    deg0 = expr1.total_degree()
    list0 = []
    for n in range(0, deg0):
        list0.append(expr1.coeff_monomial(a ** (deg0 - n)))
    list0.append(expr1.coeff_monomial(a ** 0))
    len0 = list0.__len__()

    def _core_(coefflist):
        global TypeError
        error = 0
        errortype = ''
        for i in range(0, len0):
            current0 = coefflist[i]
            s_gt_t = sympy.simplify(expand(current0.subs({s: (t + 1)}), t))
            if not s_gt_t.is_Add:
                s_gt_t_list = [s_gt_t]
            else:
                try:
                    list(((sympy.Poly(s_gt_t, t)).as_dict()).values())
                except TypeError:
                    error += 1
                    errortype += 'TypeError'
                    break
                else:
                    s_gt_t_list = list(((sympy.Poly(s_gt_t, t)).as_dict()).values())
            len1 = s_gt_t_list.__len__()
            for j in range(0, len1):
                if s_gt_t_list[j] < 0:
                    error += 1
                    break
            if error != 0:
                break

            s_lt_t = sympy.simplify(expand(current0.subs({t: (s + 1)}), s))
            if not s_lt_t.is_Add:
                s_lt_t_list = [s_lt_t]
            else:
                try:
                    list(((sympy.Poly(s_lt_t, s)).as_dict()).values())
                except TypeError:
                    error += 1
                    errortype += 'TypeError'
                    break
                else:
                    s_lt_t_list = list(((sympy.Poly(s_lt_t, s)).as_dict()).values())
            len2 = s_lt_t_list.__len__()
            for j in range(0, len2):
                if s_lt_t_list[j] < 0:
                    error += 1
                    break
            if error != 0:
                break
        if error != 0:
            print('Error!')
            tkinter.messagebox.showinfo(title='检查到有错误发生！',
                                        message='该不等式不成立，或者本软件未能达成您的请求。\n'
                                                '请您检查键入的不等式，或重新输入一个三元轮换齐次轮换对称的有理不等式。\n'
                                                '注意：变量为a, b, c；并且保证定义域为正实数集。')
            report0 = tkinter.messagebox.askokcancel(title='是否发送一份错误报告？',
                                                     message='仅为改进我们的产品，一份错误报告在您的许可下可能将被发送。\n'
                                                             '错误报告仅存贮您的基本操作信息，与您的任何隐私信息均无关。')
            if report0:
                yag = yagmail.SMTP('gdsb7770002@163.com', 'QMMYHEMPBVPHYAII', 'smtp.163.com')
                yag.send(['2913026224@qq.com', '1929842479@qq.com'], '错误报告',
                         ['错误个数：{0}\n'.format(error),
                          '键入信息：{0}\n'.format([expr, as_prove, as_cs, as_sc, as_pqr, as_ast, ast, _same_, check]),
                          '启动时间：{0}\n'.format(time0.strftime('%Y/%m/%d %H:%M:%S')),
                          '版本信息：{0} based on {1}\n'.format(ver, OS)])

        else:
            print('OK!')
            tkinter.messagebox.showinfo(title='Success！',
                                        message='原不等式成立！其中，a, b, c > 0.')

    _core_(list0)


def _pre_(n):
    if n == 3:
        str0 = '轮换对称'
    else:
        str0 = '全对称'
    if as_prove:
        expr0 = sigma(entry0.get())
    else:
        expr0 = entry0.get()
    if judge0(expr0)[0] * judge0(expr0)[1] * judge0(expr0)[2] * judge0(expr0)[3] == 1:
        _core_2_()
    else:
        tkinter.messagebox.showinfo(title='检查到有错误发生！',
                                    message='该版本的此软件不能达成您的请求。\n'
                                            '请您检查键入的不等式，或重新输入一个三元轮换齐次{0}有理不等式。\n'
                                            '注意：变量为a, b, c；并且保证定义域为正实数集。'.format(str0))


def _true_(func):
    global as_prove, as_cs, as_sc, as_pqr, as_ast, ast, _same_, check
    if func == 0:
        as_prove = not as_prove
    if func == 1:
        as_cs = not as_cs
    if func == 2:
        as_sc = not as_sc
    if func == 3:
        as_pqr = not as_pqr
    if func == 4:
        as_ast = not as_ast
    if func == 5:
        ast = not ast
    if func == 6:
        _same_ = not _same_
    if func == 7:
        check = not check


def _exit_():
    file_8 = 'result.txt'
    time2 = time0.strftime('%Y/%m/%d %H:%M:%S')
    with open(file_8, 'a') as file_8_0:
        file_8_0.write('Sigma 4.1 正常关闭！时间：')
        file_8_0.write('{0}\n\n\n'.format(time2))
    window0.quit()
    window0.destroy()
    exit()


def _all_():
    window1 = tk.Toplevel()
    window1.geometry('800x720')
    window1.resizable(True, True)
    title2 = tk.Label(window1, text=info())
    title2.pack()
    window1.mainloop()


def _about_():
    window2 = tk.Toplevel()
    window2.geometry('800x400')
    window2.resizable(False, False)
    bg0 = ImageTk.PhotoImage(Image.open('ver4_1.gif'))
    canvas0 = tk.Canvas(window2, width=800, height=400, bg='white')
    canvas0.create_image(400, 200, image=bg0)
    canvas0.pack()
    window2.mainloop()


def _report_():
    window9 = tk.Toplevel()
    window9.title('三元轮换对称不等式运算程序  ver 4.1 [20210221] 反馈系统')
    window9.geometry('800x570')
    window9.resizable(False, False)
    bg0 = ImageTk.PhotoImage(Image.open('ver4_1_1.gif'))
    canvas0 = tk.Canvas(window9, width=800, height=400, bg='white')
    canvas0.create_image(400, 200, image=bg0)
    title9_1 = tk.Label(window9,
                        text='请输入您遇到的问题，开发商将认真考虑您的意见与建议！',
                        font=('KaiTi', 15))
    entry1 = tk.Entry(window9, width=80)
    title2 = tk.Label(window9,
                      text='如果您愿意，请您留下您的联系方式，开发商将会与您联系。',
                      font=('KaiTi', 15))
    entry2 = tk.Entry(window9, width=80)
    report1 = tk.Button(window9, text='发送至官方邮箱', command=lambda: _sent_(entry1.get(), entry2.get()))

    canvas0.pack(), title9_1.pack(), entry1.pack(), title2.pack(), entry2.pack()
    report1.place(relheight=0.05, relwidth=0.15, relx=0.425, rely=0.92)
    window9.mainloop()


def _sent_(str0, str1):
    report2 = tkinter.messagebox.askokcancel(title='请问您确定发送吗？',
                                             message='它仅存贮您的基本操作信息以及您的反馈意见、建议，与您的其他任何信息均无关。')
    if report2:
        yag = yagmail.SMTP('gdsb7770002@163.com', 'QMMYHEMPBVPHYAII', 'smtp.163.com')
        yag.send(['2913026224@qq.com', '1929842479@qq.com'], '反馈',
                 ['意见建议：{0}\n'.format(str0),
                  '联系方式：{0}\n'.format(str1),
                  '配置信息：{0}\n'.format([as_prove, as_cs, as_sc, as_pqr, as_ast, ast, _same_, check]),
                  '启动时间：{0}\n'.format(time0.strftime('%Y/%m/%d %H:%M:%S')),
                  '版本信息：{0} based on {1}\n'.format(ver, OS)])
        tkinter.messagebox.showinfo(title='请问您确定提交吗？',
                                    message='您已发出，感谢您的反馈！')
    else:
        tkinter.messagebox.showinfo(title='请问您确定发送吗？',
                                    message='您已取消发送。')


window0 = Tk()
window0.title('三元轮换对称不等式运算程序  ver 4.1 [20210221]')
window0.geometry('800x500')
window0.resizable(True, True)
canvas1 = tk.Canvas(window0, highlightthickness=0, width=800, height=500, bg='Gainsboro')
canvas1.pack(fill=BOTH, expand=YES)

title0 = tk.Label(canvas1,
                  text='\n基于Python 3开发的 三元轮换对称不等式运算程序（发行版）'
                       '\n ver 4.1 [20210221]  cx0222 Jinan, Shandong',
                  font=('KaiTi', 16))
title0.place(relheight=0.2, relwidth=0.90, relx=0.1, rely=-0.0625)
title1 = tk.Label(canvas1,
                  text='请输入不等式，并以a, b, c作为不等式的变量',
                  font=('KaiTi', 13))
title1.place(relheight=0.15, relwidth=0.8, relx=0.1, rely=0.25)

menu0 = tk.Menu(window0)
window0.config(menu=menu0)
menu_operate = tk.Menu(menu0, tearoff=False)
menu_operate.add_command(label='SOS分拆', command=lambda: _get_(1))
menu_operate.add_command(label='Schur分拆', command=lambda: _get_(2))
menu_operate.add_command(label='pqr分拆', command=lambda: _catch_(1))
menu0.add_cascade(label='配方与分拆', menu=menu_operate)
menu_2 = tk.Menu(menu0, tearoff=False)
menu_2.add_command(label='差分代换', command=lambda: _catch_(2))
menu_2.add_separator()
menu_2.add_command(label='预先检测并机器证明', command=lambda: _pre_(3))
menu0.add_cascade(label='代换与证明', menu=menu_2)
menu_1 = tk.Menu(menu0, tearoff=False)
menu_1.add_command(label='关于Sigma 4.1', command=_about_)
menu_1.add_command(label='发行说明及开发信息', command=_all_)
menu_1.add_command(label='反馈给开发者', command=_report_)
menu_1.add_separator()
menu_1.add_command(label='退出Sigma 4.1', command=_exit_)
menu0.add_cascade(label='说明与反馈', menu=menu_1)

about0 = tk.Button(canvas1, text='关  于', command=_about_)
about0.place(relheight=0.07, relwidth=0.15, relx=0.3, rely=0.14)
note0 = tk.Button(canvas1, text='说  明', command=_all_)
note0.place(relheight=0.07, relwidth=0.15, relx=0.55, rely=0.14)
report0 = tk.Button(canvas1, text='反  馈', command=_report_)
report0.place(relheight=0.07, relwidth=0.15, relx=0.3, rely=0.87)
exit0 = tk.Button(canvas1, text='退  出', command=_exit_)
exit0.place(relheight=0.07, relwidth=0.15, relx=0.55, rely=0.87)

entry0 = tk.Entry(canvas1)
entry0.place(relheight=0.07, relwidth=0.80, relx=0.1, rely=0.23)
cs0 = tk.Button(canvas1, text='SOS分拆', command=lambda: _get_(1))
cs0.place(relheight=0.07, relwidth=0.15, relx=0.3, rely=0.37)
sc0 = tk.Button(canvas1, text='Schur分拆', command=lambda: _get_(2))
sc0.place(relheight=0.07, relwidth=0.15, relx=0.3, rely=0.47)
pqr0 = tk.Button(canvas1, text='pqr分拆', command=lambda: _catch_(1))
pqr0.place(relheight=0.07, relwidth=0.15, relx=0.3, rely=0.57)
ast0 = tk.Button(canvas1, text='差分代换', command=lambda: _catch_(2))
ast0.place(relheight=0.07, relwidth=0.15, relx=0.3, rely=0.67)
prove0 = tk.Button(canvas1, text='机器证明', command=lambda: _pre_(3))
prove0.place(relheight=0.07, relwidth=0.15, relx=0.3, rely=0.77)

cs1 = tk.Checkbutton(canvas1, text='自动求和', command=lambda: _true_(1))
cs1.place(relheight=0.07, relwidth=0.11, relx=0.57, rely=0.37)
sc1 = tk.Checkbutton(canvas1, text='自动求和', command=lambda: _true_(2))
sc1.place(relheight=0.07, relwidth=0.11, relx=0.57, rely=0.47)
pqr1 = tk.Checkbutton(canvas1, text='自动求和', command=lambda: _true_(3))
pqr1.place(relheight=0.07, relwidth=0.11, relx=0.57, rely=0.57)
ast1 = tk.Checkbutton(canvas1, text='自动求和', command=lambda: _true_(4))
ast1.place(relheight=0.07, relwidth=0.11, relx=0.57, rely=0.646)
ast2 = tk.Checkbutton(canvas1, text='(a, a + s, a + s + t)', command=lambda: _true_(5))
ast2.place(relheight=0.07, relwidth=0.20, relx=0.53, rely=0.695)
prove1 = tk.Checkbutton(canvas1, text='自动求和', command=lambda: _true_(0))
prove1.place(relheight=0.07, relwidth=0.11, relx=0.57, rely=0.77)

window0.mainloop()
