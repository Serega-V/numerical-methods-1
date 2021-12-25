import math

def print_gr(X, Y, color):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter(X, Y, 4, color)
    plt.show()
    plt.close()

def function(x):
    res = math.tan(math.tanh(x)) - math.sinh(math.cos(x / 2)) - 1
    return res

def function_1(x):
    res = 1 / math.cos(math.tanh(x)) ** 2 / math.cosh(x) ** 2 + math.cosh(math.cos(x / 2)) * math.sin(x / 2) / 2
    return res

def function_2(x):
    res = (math.sin(2 * math.tanh(x)) - 2 * math.cosh(x) * math.sinh(x) * math.cos(math.tanh(x)) ** 2) / (math.cos(math.tanh(x)) * math.cosh(x)) ** 4 + 0.25 * (math.cosh(math.cos(x / 2)) * math.cos(x / 2) - math.sinh(math.cos(x / 2)) * math.sin(x / 2) ** 2)
    return res

def option_1(a, b, k):           #метод дихотомии
    error = 10 ** (-1 * k)
    x0 = a
    x1 = b
    N = 0
    while x1 - x0 > 2 * error:
        x2 = (x1 + x0) / 2
        if function(x0) * function(x2) <= 0:
            x1 = x2
        if function(x2) * function(x1) <= 0:
            x0 = x2
        N += 1

    return x2

def limit(a, b):
    res_a = a
    res_b = b
    q = (res_b + res_a) / 2
    check = 0
    if function(res_a) * function(q) <= 0:
        res_b = q
        check = 1
    elif function(res_b) * function(q) <= 0:
        res_a = q
        check = 0
    else:
        print("ERROR_№_0")
    res = [res_a, res_b, check]
    return res

def option_2(a, b, k):            #метод Ньютона
    error = 10 ** (-1 * k)
    N = 0
    err1 = b - a    #текущая погрешность
    err0 = err1    #погрешность предыдущего шага
    while err1 > error:
        if function(a) * function_2(a) >= 0:
            err1 = b - a
            err0 = err1
            x0 = a
            x1 = a
            while err1 <= err0 and x1 >= x0 and err1 > error:
                x0 = x1
                x1 -= function(x1) / function_1(x1)
                N += 1
                err0 = err1
                err1 = abs(0.5 * err1 ** 2 * function_2(x1))
            if err1 > error:
                x1 = x0
        if function(b) * function_2(b) >= 0:
            err1 = b - a
            err0 = err1
            x0 = b
            x1 = b
            while err1 <= err0 and x1 <= x0 and err1 > error:
                x0 = x1
                x1 -= function(x1) / function_1(x1)
                N += 1
                err0 = err1
                err1 = abs(0.5 * err1 ** 2 * function_2((x0 + x1) / 2))
            if err1 > error:
                x1 = x0
        if err1 > error:
            q = limit(a, b)
            a = q[0]
            b = q[1]
            N += 1

    res = ["B, ", "N = ", N, "res = ", round(x1, k)]
    return res

def option_3(a, b, k_n, x_res):            #метод хорд
    error = 10 ** (-1 * k_n)
    res_err = []
    check = -1
    i = 0
    err = min(x_res - a, b - x_res)
    err1 = err
    k = function_2(x_res) / 2 / function_1(x_res)
    while err > error:
        s = 0
        x1 = a - 1
        while function(a) * function_2(a) >= 0 and err > error and a > x1:
            print("while_A")
            if s == 0:
                x1 = a
                a = x1 - function(x1) / function_1(x1)
                check = 0
                s += 1
                err1 = err
                err = abs(0.5 * (x1 - x_res) ** 2 * function_2(a))
                if len(res_err) == i:
                    res_err.append(err)
                else:
                    res_err[i] = err
                i += 1
            else:
                x2 = x1
                x1 = a
                a = x1 - (x1 - x2) * function(x1) / (function(x1) - function(x2))
                check = 0
                err1 = err
                err = abs(k * (x1 - x_res) * (x2 - x_res))
                s += 1
                if len(res_err) == i:
                    res_err.append(err)
                else:
                    res_err[i] = err
                i += 1
        if s > 0 and (function(a) * function_2(a) < 0 or a <= x1):
            print("A_!!!")
            a = x1
            err = err1
            i -= 1
            s = 0
        s = 0
        x1 = b + 1
        while function(b) * function_2(b) >= 0 and err > error and b < x1:
            print("while_B")
            if s == 0:
                x1 = b
                b = x1 - function(x1) / function_1(x1)
                check = 1
                s += 1
                err1 = err
                err = abs(0.5 * (x1 - x_res) ** 2 * function_2(b))
                if len(res_err) == i:
                    res_err.append(err)
                else:
                    res_err[i] = err
                i += 1
            else:
                x2 = x1
                x1 = b
                b = x1 - (x1 - x2) * function(x1) / (function(x1) - function(x2))
                check = 1
                err1 = err
                err = abs(k * (x1 - x_res) * (x2 - x_res))
                s += 1
                if len(res_err) == i:
                    res_err.append(err)
                else:
                    res_err[i] = err
                i += 1
        if s > 0 and (function(b) * function_2(b) < 0 or b >= x1):
            print("B_!!!")
            b = x1
            err = err1
            i -= 1
            s = 0

        if s == 0 and err > error:
            print("LIMIT")
            q = limit(a, b)
            a = q[0]
            b = q[1]
            check = 2
            err = min(x_res - a, b - x_res)
            if len(res_err) == i:
                res_err.append(err)
            else:
                res_err[i] = err
            i += 1
    if check == 0 or (check == 2 and q[2] == 0):
        res = a
    elif check == 1 or (check == 2 and q[2] == 1):
        res = b
    else:
        print("ERROR_№_1")

    X1 = []
    Y1 = []
    j = 3
    while j < i:
        X1.append((j + 1))
        Y1.append(math.log10(res_err[j]))
        if j > 4:
            w = (Y1[j - 3] - Y1[j - 4]) / (Y1[j - 4] - Y1[j - 5])
            print(w)
        j += 1
    print_gr(X1, Y1, "g")



a = 0
b = 10

#print(option_1(a, b, 3))
#print(option_1(a, b, 6))
#print(option_1(a, b, 9))
#print(option_2(a, b, 3))
#print(option_2(a, b, 6))
#print(option_2(a, b, 9))

x_res = option_1(a, b, 15)
option_3(a, b, 13, x_res)