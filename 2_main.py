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

def analytical (X, N):
    res = []
    i = 0
    q = 0.0
    while i < N:
        q = (math.sin(X[i])) ** 2
        res.append(q)
        i += 1
    return res

def analytical_in_point (x):
    res = math.sin(x) ** 2
    return res

def analytical_1 (X, N):
    res = []
    i = 0
    q = 0.0

    while i < N:
        q = 2 * math.cos(X[i]) * math.sin(X[i])
        res.append(q)
        i += 1
    return res

def analytical_2 (X, N):
    res = []
    i = 0
    q = 0.0

    while i < N:
        q = 2 * (math.cos(X[i]) ** 2 - math.sin(X[i]) ** 2)
        res.append(q)
        i += 1
    return res

def res_1_h1 (h, Y, N):
    i = 0
    res = []
    q = 0.0
    while i < N - 1:
        q = (Y[i + 1] - Y[i]) / h
        res.append(q)
        i += 1
    q = (Y[i] - Y[i - 1]) / h
    res.append(q)
    return res

def res_1_h2 (h, Y, N):
    i = 1
    res = []
    q = 0.0

    q = (-3 * Y[0] + 4 * Y[1] - Y[2]) / 2 / h
    res.append(q)

    while i < N - 1:
        q = (Y[i + 1] - Y[i - 1]) / 2 / h
        res.append(q)
        i += 1
    q = (3 * Y[i] - 4 * Y[i - 1] + Y[i - 2]) / 2 / h
    res.append(q)
    return res

def res_2_h2 (h, Y, N):
    i = 1
    res = []
    q = 0.0
    q = (2 * Y[0] - 5 * Y[1] + 4 * Y[2] - Y[3]) / h ** 2
    res.append(q)

    while i < N - 1:
        q = (Y[i + 1] - 2 * Y[i] + Y[i - 1]) / h ** 2
        res.append(q)
        i += 1

    q = (2 * Y[i] - 5 * Y[i - 1] + 4 * Y[i - 2] - Y[i - 3]) / h ** 2
    res.append(q)
    return res

def res_2_h4 (X, h, Y, N):
    res = []
    i = 2
    q = 0.0
    p1 = 0.0
    p2 = 0.0

    p1 = analytical_in_point(X[0] - 2 * h)
    p2 = analytical_in_point(X[0] - h)
    q = (-1 * p1 + 16 * p2 - 30 * Y[0] + 16 * Y[1] - Y[2]) / 12 / h ** 2
    res.append(q)

    q = (-1 * p2 + 16 * Y[0] - 30 * Y[1] + 16 * Y[2] - Y[3]) / 12 / h ** 2
    res.append(q)

    while i < N - 2:
        q = (-1 * Y[i - 2] + 16 * Y[i - 1] - 30 * Y[i] + 16 * Y[i + 1] - Y[i + 2]) / 12 / h ** 2
        res.append(q)
        i += 1

    p1 = analytical_in_point(X[i + 1] + 2 * h)
    p2 = analytical_in_point(X[i + 1] + h)
    q = (-1 * p2 + 16 * Y[i + 1] - 30 * Y[i] + 16 * Y[i - 1] - Y[i - 2]) / 12 / h ** 2
    res.append(q)

    q = (-1 * p1 + 16 * p2 - 30 * Y[i + 1] + 16 * Y[i] - Y[i - 1]) / 12 / h ** 2
    res.append(q)
    return res

def error (Y, Y_res, N):
    i = 0
    res = 0.0

    while i < N:
        res += abs(Y[i] - Y_res[i])
        i += 1
    res /= N
    return res

def X_res (a, h, N):
    res = []
    i = 0

    while i < N:
        res.append(a + i * h)
        i += 1
    return res

def work_1_h1 (a, h, N):
    X = X_res(a, h, N)
    Y = analytical(X, N)
    Y_res = res_1_h1(h, Y, N)
    #Y_analytical = analytical_1(X, N)
    #print_2gr(X, Y_analytical, X, Y_res, "r", "g")
    return Y_res

def work_1_h2 (a, h, N):
    X = X_res(a, h, N)
    Y = analytical(X, N)
    Y_res = res_1_h2(h, Y, N)
    #Y_analytical = analytical_1(X, N)
    #print_2gr(X, Y_analytical, X, Y_res, "r", "g")
    return Y_res

def work_2_h2 (a, h, N):
    X = X_res(a, h, N)
    Y = analytical(X, N)
    Y_res = res_2_h2(h, Y, N)
    #Y_analytical = analytical_2(X, N)
    #print_2gr(X, Y_analytical, X, Y_res, "r", "g")
    return Y_res

def work_2_h4 (a, h, N):
    X = X_res(a, h, N)
    Y = analytical(X, N)
    Y_res = res_2_h4(X, h, Y, N)
    #Y_analytical = analytical_2(X, N)
    #print_2gr(X, Y_analytical, X, Y_res, "r", "g")
    return Y_res

def error (Y, Y_res, N):
    res = 0.0
    i = 0

    while i < N:
        r = abs(Y[i] - Y_res[i])
        if r >= res:
            res = r
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

def main_error (a, b, N_min, N_max):
    i = N_min
    error_1_1h = []
    error_1_2h = []
    error_2_2h = []
    error_2_4h = []
    mas_h = []

    while i <= N_max:
        h = (b - a) / (i - 1)
        X = X_res(a, h, i)
        Y = analytical(X, i)
        Y1 = analytical_1(X, i)
        Y2 = analytical_2(X, i)

        res11h = res_1_h1(h, Y, i)
        res12h = res_1_h2(h, Y, i)
        res22h = res_2_h2(h, Y, i)
        res24h = res_2_h4(X, h, Y, i)

        error_1_1h.append(math.log(error(Y1, res11h, i)))
        error_1_2h.append(math.log(error(Y1, res12h, i)))
        error_2_2h.append(math.log(error(Y2, res22h, i)))
        error_2_4h.append(math.log(error(Y2, res24h, i)))
        mas_h.append(math.log(h))

        i += 1

    print_4gr(mas_h, error_1_1h, error_1_2h, error_2_2h, error_2_4h, "g", "r", "b", "c")

    main_N = N_max - N_min + 1
    k11 = K(mas_h, error_1_1h, main_N)
    k12 = K(mas_h, error_1_2h, main_N)
    k22 = K(mas_h, error_2_2h, main_N)
    k24 = K(mas_h, error_2_4h, main_N)

    print("k11 = ", k11, "; k12 = ", k12, "; k22 = ", k22, "; k24 = ", k24)


a = -1.5
b = 1.5

main_error(a, b, 20, 100)
