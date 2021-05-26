import time
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import sympy
import datetime
import yagmail
from tkinter import *
from tkinter import ttk
from sympy import *
from PIL import Image, ImageTk

time_0 = time.time()
a, b, c = sympy.symbols('a, b, c')
a1, b1, c1 = sympy.symbols('a1, b1, c1')
s, t, d = sympy.symbols('s, t, d')
p, q, r = sympy.symbols('p, q, r')
sum_auto = True
OS, ver, time0 = 'macOS', '4.3', datetime.datetime.now()


def info():
    str0 = '\n 基于Python 3开发的 三元轮换对称不等式运算程序\n\n' \
           ' ----------------- Author ------------------\n' \
           ' Nova cx0222 Jinan, Shandong\n' \
           ' 2913026224@qq.com, 1929842479@qq.com\n\n' \
           ' ------------- Current Version -------------\n' \
           ' ver 4.5 [20210322]  Jinan, Shandong\n' \
           ' 该程序装载的最新算法版本为 Sigma_Core_2+ 等\n\n' \
           ' ------------- Historic Version ------------\n' \
           ' ver 4.4 [20210319]  Jinan, Shandong\n' \
           ' ver 4.3 [20210313]  Jinan, Shandong\n' \
           ' ver 4.2 [20210311]  Jinan, Shandong\n' \
           ' ver 4.1 [20210221]  Jinan, Shandong\n' \
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


def auto_sum(expr):
    # If this function runs, the input expression will be summed up automatically:
    F0 = sympy.simplify(expr)
    F1 = (F0.subs({a: a1, b: b1, c: c1})).subs({a1: b, b1: c, c1: a})
    F2 = (F1.subs({a: a1, b: b1, c: c1})).subs({a1: b, b1: c, c1: a})
    F = F0 + F1 + F2
    # return type = <class 'sympy.core.*.*'>
    return [F, F0, F1, F2]


def super_subs(expr, expr1, expr2, expr3):
    if sum_auto:
        expr = auto_sum(expr)[0]
    return sympy.simplify(expr.subs({a: expr1, b: expr2, c: expr3}))


# noinspection PyGlobalUndefined
def judge0(expr):
    global jud1, same0, deg0
    # Check whether the input expression is a polynomial:
    # Notice: it is assumed that "expr" has already been summed up if "sum_auto" is enabled.
    expr0 = sympy.simplify(numer(cancel(expr)))
    expr1 = sympy.simplify(denom(cancel(expr)))
    jud0, jud1 = 1, 1
    try:
        Poly(expr0, a, b, c)
        Poly(expr1, a, b, c)
    except sympy.polys.polyerrors.PolynomialError:
        jud0 = 0
    except NameError:
        jud1 = 0
    # Check homogeneity:
    if jud0 == 1 and jud1 == 1:
        deg0 = Poly(expr0, a, b, c).total_degree()
        expr1 = list(sympy.Poly(expr0, a, b, c).as_dict().keys())
        len0 = expr1.__len__()
        same0 = 1
        for i in range(0, len0):
            if sum(expr1[i]) != deg0:
                same0 = 0
                break
    else:
        same0, deg0 = 0, 0
    # jud0: like "is.polynomial()", return only 1 (True) or 0 (False);
    # jud1: whether the variables are a, b, c;
    # same0: if jud0 == 1 and jud1 == 1, return "is.homogenous()";
    # deg0: assume same0 == 1, return the degree of the expression;
    # Notice that if jud0 == 0 or if jud1 == 0, which means the input is valid or,
    #   at least, cannot be operated in the current version of this app,
    #   the return of same0 and deg0 still exists and the error may not be detected.
    #   So, notice that these values can be wrong or meaningless sometimes.
    return [jud0, jud1, same0, deg0]


# noinspection PyGlobalUndefined
def judge1(expr):
    global sym0
    cyc0 = 0
    expr0 = sympy.simplify(numer(cancel(expr)))
    # Check whether it is cyclic:
    # To-do list: for the expression which has been summed up automatically, this step is redundant.
    if (expr0.subs({a: a1, b: b1, c: c1})).subs({a1: b, b1: c, c1: a}) == expr0:
        if (expr0.subs({a: a1, b: b1, c: c1})).subs({a1: c, b1: a, c1: b}) == expr0:
            cyc0 = 1
    # If true, check whether it is symmetric:
    if cyc0 == 1:
        sym0 = 0
        if (expr0.subs({a: a1, b: b1, c: c1})).subs({a1: a, b1: c, c1: b}) == expr0:
            if (expr0.subs({a: a1, b: b1, c: c1})).subs({a1: c, b1: b, c1: a}) == expr0:
                if (expr0.subs({a: a1, b: b1, c: c1})).subs({a1: b, b1: a, c1: c}) == expr0:
                    sym0 = 1
    # expr0: return the standardized form of the expression
    # jud0: return whether the expression is cyclic;
    # jud1: return whether the expression is symmetric.
    return [expr0, cyc0, sym0]


def terms(deg0):
    term0 = []
    for i in range(0, deg0 + 1):
        for j in range(0, deg0 + 1):
            for k in range(0, deg0 + 1):
                if i + j + k == deg0:
                    term0.append(a ** i * b ** j * c ** k)
    return term0


def pqr_terms(deg0):
    term0 = []
    for i in range(0, deg0 + 1):
        for j in range(0, deg0 + 1):
            for k in range(0, deg0 + 1):
                if i + 2 * j + 3 * k == deg0:
                    term0.append(p ** i * q ** j * r ** k)
    return term0


# noinspection PyGlobalUndefined


def square(expr):
    # [Step 1] Sum up if enabled:
    global j1
    if sum_auto:
        expr1 = auto_sum(expr)
    else:
        expr1 = [expr]
    # [Step 2] Check the basic information of the expression:
    pre_check, error = 0, []
    j0 = judge0(expr1[0])
    if j0[0] == 1 and j0[1] == 1:
        j1 = judge1(expr1[0])
        if j1[1] == 1:
            pre_check = 1
        else:
            error.append([1, 1])
    elif j0[0] == 1 and j0[1] == 1 and j0[2] == 0:
        error.append([1, 2])
    else:
        error.append([1, 3])
    # [Step 3] Main Process:
    if pre_check == 0:
        return error
    else:
        deg0, expr2, equlist = j0[3], j1[0], []
        s_bc, s_ca, s_ab, s_a, s_b, s_c = (b - c) ** 2, (c - a) ** 2, (a - b) ** 2, 0, 0, 0
        term, total = terms(deg0 - 2), terms(deg0)
        term_count, total_count = term.__len__(), total.__len__()
        coeffs = sympy.symbols('v:{}:a'.format(term_count))
        for i in range(0, term_count):
            s_a += coeffs[i] * term[i]
            s_b += (coeffs[i] * term[i]).subs({a: a1, b: b1, c: c1}).subs({a1: b, b1: c, c1: a})
            s_c += (coeffs[i] * term[i]).subs({a: a1, b: b1, c: c1}).subs({a1: c, b1: a, c1: b})
        ineq = s_a * s_bc + s_b * s_ca + s_c * s_ab
        func = sympy.poly(expr2 - ineq, a, b, c)
        for i in range(0, total_count):
            equlist.append(func.coeff_monomial(total[i]))
        ans = solve(equlist, coeffs)
        result0_a, result0_b, result0_c = s_a.subs(ans), s_b.subs(ans), s_c.subs(ans)
        ans_list = list(ans)
        rest_list = [i for i in coeffs if i not in ans_list]
        rest_count = rest_list.__len__()
        output0 = [result0_a, result0_b, result0_c]
        if rest_count == 0:
            return [output0]
        else:
            for i in range(0, rest_count):
                rest_dict = dict(zip(rest_list, [0 for _ in range(0, rest_count)]))
                result1_a, result1_b, result1_c = result0_a.subs(rest_dict), result0_b.subs(rest_dict), result0_c.subs(
                    rest_dict)
                output1 = [result1_a, result1_b, result1_c]
                return [output0, output1]


# noinspection PyGlobalUndefined
def schur(expr):
    # [Step 1] Sum up if enabled:
    global j1
    if sum_auto:
        expr1 = auto_sum(expr)
    else:
        expr1 = [expr]
    # [Step 2] Check the basic information of the expression:
    pre_check, error = 0, []
    j0 = judge0(expr1[0])
    if j0[0] == 1 and j0[1] == 1 and j0[2] == 1:
        j1 = judge1(expr1[0])
        if j1[1] == 1:
            pre_check = 1
        else:
            error.append([2, 1])
    elif j0[0] == 1 and j0[1] == 1 and j0[2] == 0:
        error.append([2, 2])
    else:
        error.append([2, 3])
    # [Step 3] Main Process:
    if pre_check == 0:
        return error
    else:
        deg0, expr2, equlist = j0[3], j1[0], []
        s_bc, s_ca, s_ab, s_a, s_b, s_c = (a - b) * (a - c), (b - c) * (b - a), (c - a) * (c - b), 0, 0, 0
        term, total = terms(deg0 - 2), terms(deg0)
        term_count, total_count = term.__len__(), total.__len__()
        coeffs = sympy.symbols('v:{}:a'.format(term_count))
        for i in range(0, term_count):
            s_a += coeffs[i] * term[i]
            s_b += (coeffs[i] * term[i]).subs({a: a1, b: b1, c: c1}).subs({a1: b, b1: c, c1: a})
            s_c += (coeffs[i] * term[i]).subs({a: a1, b: b1, c: c1}).subs({a1: c, b1: a, c1: b})
        ineq = s_a * s_bc + s_b * s_ca + s_c * s_ab
        func = sympy.poly(expr2 - ineq, a, b, c)
        for i in range(0, total_count):
            equlist.append(func.coeff_monomial(total[i]))
        ans = solve(equlist, coeffs)
        result0_a, result0_b, result0_c = s_a.subs(ans), s_b.subs(ans), s_c.subs(ans)
        ans_list = list(ans)
        rest_list = [i for i in coeffs if i not in ans_list]
        rest_count = rest_list.__len__()
        output0 = [result0_a, result0_b, result0_c]
        if rest_count == 0:
            return [output0]
        else:
            for i in range(0, rest_count):
                rest_dict = dict(zip(rest_list, [0 for _ in range(0, rest_count)]))
                result1_a, result1_b, result1_c = result0_a.subs(rest_dict), result0_b.subs(rest_dict), result0_c.subs(
                    rest_dict)
                output1 = [result1_a, result1_b, result1_c]
                return [output0, output1]


# noinspection PyGlobalUndefined
def pqr(expr):
    # [Step 1] Sum up if enabled:
    global j1
    if sum_auto:
        expr1 = auto_sum(expr)
    else:
        expr1 = [expr]
    # [Step 2] Check the basic information of the expression:
    pre_check, error = 0, []
    j0 = judge0(expr1[0])
    if j0[0] == 1 and j0[1] == 1:
        j1 = judge1(expr1[0])
        if j1[2] == 1:
            pre_check = 1
        else:
            error.append([3, 1])
    else:
        error.append([3, 0])
    # [Step 3] Main Process:
    if pre_check == 0:
        return error
    else:
        if j0[2] == 1:
            return pqr_0(expr1, j0[3])
        else:
            return pqr_1(expr1, j0[3])


def pqr_0(expr, deg0):
    term = pqr_terms(deg0)
    equ_list, pqr_list, term_list, total_list, ineq, expr2 = [], [], [], terms(deg0), 0, 0
    term_count, total_count = term.__len__(), total_list.__len__()
    coeffs = sympy.symbols('v:{}:a'.format(term_count))
    for i in range(0, term_count):
        term_list.append(term[i].subs({p: (a + b + c), q: (a * b + b * c + c * a), r: a * b * c}))
        pqr_list.append(term[i])
        ineq += term_list[i] * coeffs[i]
        expr2 += pqr_list[i] * coeffs[i]
    expr1 = sympy.poly(sympy.simplify(sympy.simplify(ineq) - expr[0]), a, b, c)
    for i in range(0, total_count):
        equ_list.append(expr1.coeff_monomial(total_list[i]))
    ans = solve(equ_list, coeffs)
    expr3 = expr2.subs(ans)
    return expr3


def pqr_1(expr, deg0):
    expr1 = sympy.poly(expr[0], a, b, c)
    poly_dict = expr1.as_dict()
    term_total = list(zip(list(poly_dict.keys()), list(poly_dict.values())))
    total_count = term_total.__len__()
    list0, list1 = [[] for _ in range(0, deg0 + 1)], [0 * a for _ in range(0, deg0 + 1)]
    for i in range(1, deg0 + 1):
        for j in range(0, total_count):
            if sum(term_total[j][0]) == i:
                list0[i].append(
                    (a ** term_total[j][0][0] * b ** term_total[j][0][1] * c ** term_total[j][0][2]) * term_total[j][1])
        count0 = list0[i].__len__()
        for k in range(0, count0):
            list1[i] += list0[i][k]
        list1[i] = sympy.simplify(list1[i])
    for i in range(0, total_count):
        if sum(term_total[i][0]) == 0:
            list1[0] = term_total[i][1]
    expr2 = list1[0]
    for i in range(1, deg0 + 1):
        expr2 += pqr_0([list1[i]], i)
    return expr2


def part_0(expr, who, where, times):
    expr1 = series(expr, who, where, times)
    return expr1


def _core_2_(expr):
    if sum_auto:
        expr0 = judge1(auto_sum(expr)[0])[0]
    else:
        expr0 = judge1(expr)[0]
    expr1 = super_subs(expr0, a, a + s, a + t)
    expr1 = sympy.poly(sympy.simplify(expand(expr1)), a)
    deg0 = expr1.total_degree()
    list0 = []
    for n in range(0, deg0):
        list0.append(expr1.coeff_monomial(a ** (deg0 - n)))
    list0.append(expr1.coeff_monomial(a ** 0))
    len0 = list0.__len__()

    # noinspection PyGlobalUndefined
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
                yag.send(['2913026224@qq.com', '1929842479@qq.com'], '错误报告（版本1.0）',
                         ['错误个数：{0}\n'.format(error),
                          '启动时间：{0}\n'.format(time0.strftime('%Y/%m/%d %H:%M:%S')),
                          '键入内容：{0}\n'.format(expr),
                          '版本信息：{0} based on {1}\n'.format(ver, OS)])
                tkinter.messagebox.showinfo(title='发送成功！',
                                            message='您已成功发送本次错误报告。')
            else:
                tkinter.messagebox.showinfo(title='您已取消！',
                                            message='您已取消发送本次错误报告。')
        else:
            print('OK!')
            tkinter.messagebox.showinfo(title='原不等式成立！',
                                        message='原不等式成立！其中，a, b, c > 0.')

    _core_(list0)


# print(pqr(a ** 2 + a + 1))
# print(super_subs(a ** 3 - a * b * c, a, a + s, a + t))
# _core_2_(a ** 2 - a * b * c)
# print(part_0(a/(a**2 + b**2), who=a, where=1, times=None))

print(square(a ** 10 * (a - b) * (a - c)))
time_1 = time.time()
print(time_1 - time_0)
