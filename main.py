import math

def f (x):
    res = math.pow((math.sin(x / 3)), 3) * math.atan(x)
    return res      # значение исходной функции в точке

def equal (a, b, N):
    i = 1
    h = (b - a) / (N - 1)
    res = []
    res.append(a)

    while i < N - 1:
        res.append(a + h * i)
        i += 1
    res.append(b)
    return res      # массив из N элементов

#   построение массива значений функции в точках интерполяции
def analytical (X, N):
    i = 0
    res = []

    while i < N:
        res.append(f(X[i]))
        i += 1

    return res      # массив из N элементов

#   распределение N узлов Чебышева на отрезке от 0 до 1
def Cheb(a, b, N):
    x = 0.0
    res = []
    i = 1

    while i <= N:
        x = math.cos((2 * i - 1) / 2 / N * math.pi)
        res.append(a + (b - a) * (x + 1) / 2)
        i += 1
    return res      # массив из N элементов

def L_X(X, N):
    res = []
    i = 0
    while i < N - 1:
        res.append((X[i] + X[i + 1]) / 2)
        i += 1
    return res


def L(X, X_res, N):
    res = []
    res_point = 0.0
    Y = analytical(X, N)
    i = 0
    j = 0
    k = 0
    p = 1.0

    while k < N - 1:

        while i < N:

            while j < N:
                if i != j:
                    p *= (X_res[k] - X[j]) / (X[i] - X[j])
                j += 1

            res_point += Y[i] * p
            p = 1.0
            i += 1
            j = 0

        res.append(res_point)
        res_point = 0.0
        k += 1
        i = 0
    return res

def error (X_res, Y_res, N):        # N - количество узлов интерполяции
    res = 0.0
    Y = analytical(X_res, N - 1)
    i = 0

    while i < N - 1:
        res += abs(Y[i] - Y_res[i])
        i += 1
    res /= (N - 1)
    return res


def optimal_N (N_min, N_max):
    res = []
    N_a = [0, 100.1]
    N_b = [0, 100.1]
    r_a = 0.0
    r_b = 0.0
    gr_r_a = []
    gr_r_b = []
    gr_x = []
    i = N_min

    while i <= N_max:
        X_a = equal(a, b, i)
        Y_a = analytical(X_a, i)
        X_res_a = L_X(X_a, i)
        Y_res_a = L(X_a, X_res_a, i)

        X_b = Cheb(a, b, i)
        Y_b = analytical(X_b, i)
        X_res_b = L_X(X_b, i)
        Y_res_b = L(X_b, X_res_b, i)

        r_a = error(X_res_a, Y_res_a, i)
        r_b = error(X_res_b, Y_res_b, i)

        gr_r_a.append(r_a)
        gr_r_b.append(r_b)
        gr_x.append(i)

        if r_a < N_a[1]:
            N_a[0] = i
            N_a[1] = r_a

        if r_b < N_b[1]:
            N_b[0] = i
            N_b[1] = r_b

        i += 20

    #print_gr(gr_x, gr_r_a, "g")
    #print_gr(gr_x, gr_r_b, "b")
    #print_2gr(gr_x, gr_r_a, gr_x, gr_r_b, "g", "b")

    res.append(N_a[0])
    res.append(N_b[0])
    print("optimal a = ", res[0], "; optimal b = ", res[1])
    return res

def print_gr(X, Y, color):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter(X, Y, 3, color)
    plt.show()
    plt.close()

def print_2gr(X1, Y1, X2, Y2, color1, color2):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter(X1, Y1, 3, color1)
    ax.scatter(X2, Y2, 3, color2)
    plt.show()
    plt.close()

def print_3gr(X1, Y1, X2, Y2, X3, Y3, color1, color2, color3):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter(X1, Y1, 10, color1)
    ax.plot(X2, Y2, color2)
    ax.plot(X3, Y3, color3)
    plt.show()
    plt.close()

def print_4gr(X, Y1, Y2, Y3, Y4, color1, color2, color3, color4):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter(X, Y1, 5, color1)
    ax.scatter(X, Y2, 5, color2)
    ax.scatter(X, Y3, 5, color3)
    ax.scatter(X, Y4, 5, color4)
    plt.show()
    plt.close()


def Lebeg (X, X_res, N):
    max_f = [0, 0.0]
    res_point = 0.0
    Y = analytical(X, N)
    i = 0
    j = 0
    k = 0
    p = 1.0

    while k < N - 1:

        while i < N:

            while j < N:
                if i != j:
                    p *= (X_res[k] - X[j]) / (X[i] - X[j])
                j += 1

            res_point += Y[i] * p
            p = 1.0
            i += 1
            j = 0
        if res_point > max_f[1]:
            max_f[0] = k
            max_f[1] = res_point

        res_point = 0.0
        k += 1
        i = 0
    res = max_f[1]
    return res

def qqq (a, b, N_min, N_max):
    i = N_min
    res_n = []
    res_Lebeg = []
    res_ter_a = []
    res_ter_a1 = []
    res_ter_b = []
    q = 0.0

    while i <= N_max:
        X = equal(a, b, i)
        X_res = L_X(X, i)
        q = Lebeg(X, X_res, i)
        res_n.append(i)
        res_Lebeg.append(math.log(q))
        res_ter_a1.append(math.log(1 / 8 / (math.pi ** 0.5) * math.log(i - 1)))
        res_ter_a.append(math.log((2 ** (i - 1)) / 8 / ((i - 1) ** 1.5)))
        res_ter_b.append(math.log(2 ** (i - 2)))
        i += 5

    print_4gr(res_n, res_ter_a1, res_ter_a, res_ter_b, res_Lebeg, "c", "r", "r", "g")

a = 0
b = 10
N = 20

#X_a = equal(a, b, N)
#Y_a = analytical(X_a, N)
#X_res_a = L_X(X_a, N)
#Y_res_a = L(X_a, X_res_a, N)

#X_b = Cheb(a, b, N)
#Y_b = analytical(X_b, N)
#X_res_b = L_X(X_b, N)
#Y_res_b = L(X_b, X_res_b, N)

#print_2gr(X_a, Y_a, X_res_a, Y_res_a, "r", "g")
#print_2gr(X_b, Y_b, X_res_b, Y_res_b, "r", "b")

N_min = 20
N_max = 120
optimal = optimal_N(N_min, N_max)

qqq(a, b, N_min, N_max)
