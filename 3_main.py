import math

def print_4gr(X, Y1, Y2, Y3, Y4, color1, color2, color3, color4):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter(X, Y1, 4, color1)
    ax.scatter(X, Y2, 4, color2)
    ax.scatter(X, Y3, 4, color3)
    ax.scatter(X, Y4, 4, color4)
    plt.show()
    plt.close()

def analytical_point(x):
    res = math.sin(x) + x
    return res

def analytical (X, N):
    res = []
    i = 0

    while i < N:
        res.append(math.sin(X[i]) + X[i])
        i += 1
    return  res

def analytical_res (a, b):
    res = math.cos(a) - math.cos(b) + (b ** 2 - a ** 2) / 2
    return res

def res_1h (h, N, Y):
    res = 0.0
    i = 0

    while i < N - 1:
        res += Y[i] * h
        i += 1
    return res

def res_2h (h, N, Y):
    res = 0.0
    i = 0

    while i < N - 1:
        res += (Y[i] + Y[i + 1]) / 2 * h
        i += 1
    return res

def res_3h (a, h, N):           #метод Гаусса
    res = 0.0
    i = 0

    while i < N - 1:
        w1 = (2 * a + (2 * i + 1) * h) / 2 - h / 2 / 3 ** 0.5
        w2 = (2 * a + (2 * i + 1) * h) / 2 + h / 2 / 3 ** 0.5
        res += h / 2 * (analytical_point(w1) + analytical_point(w2))
        i += 1
    return res

def res_4h (h, N, Y):
    res = 0.0
    i = 0

    while i < N:
        if i == 0 or i == N - 1:
            res += Y[i]
        elif i % 2 == 1:
            res += 4 * Y[i]
        elif i % 2 == 0:
            res += 2 * Y[i]
        else:
            print("ERROR")
        i += 1
    res *= h / 3
    return res

def X_res (a, b, N):
    res = []
    i = 0
    h = (b - a) / (N - 1)

    while i < N:
        res.append(a + i * h)
        i += 1
    return res

def K (X, Y, N):
    i = 0
    res = 0.0
    xy = 0.0
    x = 0.0
    y = 0.0
    x2 = 0.0

    while i < N:
        xy += X[i] * Y[i]
        x += X[i]
        y += Y[i]
        x2 += X[i] ** 2
        i += 1

    res = (N * xy - x * y) / (N * x2 - x ** 2)
    return res

def error (a, b, N_min, N_max):
    i = N_min
    error1 = []
    error2 = []
    error3 = []
    error4 = []
    error_h = []
    n = 0

    while i <= N_max:
        h = (b - a) / (i - 1)
        X = X_res(a, b, i)
        Y = analytical(X, i)

        res1 = res_1h(h, i, Y)
        res2 = res_2h(h, i, Y)
        res3 = res_3h(a, h, i)
        res4 = res_4h(h, i, Y)

        res = analytical_res(a, b)

        error1.append(math.log(abs(res1 - res)))
        error2.append(math.log(abs(res2 - res)))
        error3.append(math.log(abs(res3 - res)))
        error4.append(math.log(abs(res4 - res)))
        error_h.append(math.log(h))
        i += 2                                          #формула Симсона верна только для равномерной сетки с четным числом узлов
        n += 1

    print_4gr(error_h, error1, error2, error3, error4, "c", "b", "r", "g")
    k1 = K(error_h, error1, n)
    k2 = K(error_h, error2, n)
    k3 = K(error_h, error3, n)
    k4 = K(error_h, error4, n)
    print("k1 = ", k1, "; k2 = ", k2, "; k3 = ", k3, "; k4 = ", k4)



a = 0
b = 2
N_min = 101                 #нечетное!!!
N_max = 1001                #нечетное!!!
error(a, b, N_min, N_max)