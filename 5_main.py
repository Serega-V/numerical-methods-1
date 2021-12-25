import math

def print_gr(X, Y, color):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter(X, Y, 4, color)
    plt.show()
    plt.close()

def print_2gr(X, Y1, Y2, color1, color2):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter(X, Y1, 4, color1)
    ax.scatter(X, Y2, 4, color2)
    plt.show()
    plt.close()

def print_22gr(X1, Y1, X2, Y2, color1, color2):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter(X1, Y1, 4, color1)
    ax.scatter(X2, Y2, 4, color2)
    plt.show()
    plt.close()

def print_3gr(X1, Y1, X2, Y2, Y3, color1, color2, color3):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter(X1, Y1, 4, color1)
    ax.scatter(X2, Y2, 4, color2)
    ax.scatter(X2, Y3, 4, color3)
    plt.show()
    plt.close()

def result (x):
    res = math.sin(x) + math.cos(x)
    return res

def f (x, u0_0, u1_0):
    res = -1 * math.cos(x) * (u1_0 + 1) - math.sin(x) * (u0_0 + 1) + 1
    return res

def function1 (h, a, b, u0_0, u1_0):    #метод Эйлера (1-ый порядок)
    res = [u0_0]
    X = [a]
    n = 0
    correct = [u0_0]
    error = [0]
    u1_1 = 0
    while X[n] < b:
        u1_1 = u1_0 + h * f(X[n], res[n], u1_0)
        res.append(res[n] + h * u1_0)
        u1_0 = u1_1
        n += 1
        X.append(a + h * n)
        correct.append(result(X[n]))
        error.append(abs(res[n] - correct[n]))
    print_gr(X, error, "r")

def function_2(h, a, b, u0_0, u1_0):    #метод Рунге - Кутта 4 порядка
    for_3 = [u0_0, u1_0]
    res_h = [u0_0]
    res_2h = [u0_0]
    X_h = [a]
    X_2h = [a]
    u1_0_2h = u1_0
    i = 0
    correct_h = [u0_0]
    error_h = []
    err_X = []
    error_2h = [0]
    error_R = [0]
    while X_h[i] < b:
        q1 = f(X_h[i], res_h[i], u1_0)
        k1 = u1_0
        q2 = f(X_h[i] + h / 2, res_h[i] + h / 2 * k1, u1_0 + h / 2 * q1)
        k2 = u1_0 + h / 2 * q1
        q3 = f(X_h[i] + h / 2, res_h[i] + h / 2 * k2, u1_0 + h / 2 * q2)
        k3 = u1_0 + h / 2 * q2
        q4 = f(X_h[i] + h, res_h[i] + h * k3, u1_0 + h * q3)
        k4 = u1_0 + h * q3
        res_h.append(res_h[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
        u1_0 += h / 6 * (q1 + 2 * q2 + 2 * q3 + q4)
        if i <= 2:
            for_3.append(res_h[i + 1])
            for_3.append(u1_0)
        X_h.append(a + (i + 1) * h)
        correct_h.append(result(X_h[i + 1]))
        if i > 0:
            error_h.append(math.log10((abs(correct_h[i + 1] - res_h[i + 1]))))
            err_X.append(a + h * (i + 1))


        if i % 2 == 0:
            q1 = f(X_h[i], res_2h[i // 2], u1_0_2h)
            k1 = u1_0_2h
            q2 = f(X_h[i] + h / 2, res_2h[i // 2] + h / 2 * k1, u1_0_2h + h / 2 * q1)
            k2 = u1_0_2h + h / 2 * q1
            q3 = f(X_h[i] + h / 2, res_2h[i // 2] + h / 2 * k2, u1_0_2h + h / 2 * q2)
            k3 = u1_0_2h + h / 2 * q2
            q4 = f(X_h[i] + h, res_2h[i // 2] + h * k3, u1_0_2h + h * q3)
            k4 = u1_0_2h + h * q3
            res_2h.append(res_2h[i // 2] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
            u1_0_2h += 2 * h / 6 * (q1 + 2 * q2 + 2 * q3 + q4)
            error_2h.append((abs(correct_h[i] - res_2h[i // 2])))
            error_R.append(abs(res_h[i] - res_2h[i // 2]) / 15)
            X_2h.append(a + i * h)

        i += 1

    #print_3gr(X_h, error_h, X_2h, error_2h, error_R, "g", "b", "r")
    #print_22gr(X_2h, error_R, X_h, error_h, "r", "g")
    print_gr(err_X, error_h, "r")
    return for_3

def F2(x0, y0, x1, y1):
    res = (y0 - y1) / (x0 - x1)
    return res

def F3(x0, y0, x1, y1, x2, y2):
    res = 1 / (x0 - x2) * ((y0 - y1) / (x0 - x1) - (y1 - y2) / (x1 - x2))
    return res

def shift (for_3, u0_1, u1_1):
    for_3[0] = for_3[2]
    for_3[1] = for_3[3]
    for_3[2] = for_3[4]
    for_3[3] = for_3[5]
    for_3[4] = u0_1
    for_3[5] = u1_1
    return for_3

def function_3(h, a, b, for_3):    #метод Адамса 3-го порядка
    x = a + h * 2
    i = 2
    res = [for_3[0], for_3[2], for_3[4]]
    correct = [for_3[0], result(a + h), result(a + 2 * h)]
    error = []
    err_X = []
    X = [a, a + h, a + 2 * h]
    while x < b:
        f_m1 = f(x, for_3[4], for_3[5])
        f_m2 = f(x - h, for_3[2], for_3[3])
        f_m3 = f(x - 2 * h, for_3[0], for_3[1])
        u1_1 = for_3[5] + h * f_m1 + h ** 2 / 2 * F2(x, f_m1, x - h, f_m2) + 5 / 6 * h ** 3 * F3(x, f_m1, x - h, f_m2, x - 2 * h, f_m3)
        u0_1 = for_3[4] + h * for_3[5] + h ** 2 / 2 * F2(x, for_3[5], x - h, for_3[3]) + 5 * h ** 3 / 6 * F3(x, for_3[5], x - h, for_3[3], x - 2 * h, for_3[1])
        res.append(u0_1)
        shift(for_3, u0_1, u1_1)
        x += h
        i += 1
        X.append(x)
        correct.append(result(x))
        if i > 2:
            error.append(math.log10((abs(res[i] - correct[i]))))
            err_X.append(x)
    print_gr(err_X, error, "r")

a = 0
b = 1
h = 0.05
u0_0 = 1
u1_0 = 1

#function1(h, a, b, u0_0, u1_0)
for_3 = function_2(h, a, b, u0_0, u1_0)
function_3(h, a, b, for_3)