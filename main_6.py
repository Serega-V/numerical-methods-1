import math

def print_2gr(X, Y1, Y2, color1, color2):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter(X, Y1, 1, color1)
    ax.scatter(X, Y2, 1, color2)
    plt.show()
    plt.close()

def print_3gr(X, Y1, Y2, Y3, color1, color2, color3):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter(X, Y1, 1, color1)
    ax.scatter(X, Y2, 1, color2)
    ax.scatter(X, Y3, 1, color3)
    plt.show()
    plt.close()

def exact(x):
    res = math.sin(x) + math.cos(x)
    return res

def f_p(x):
    res = math.cos(x)
    return res

def f_q(x):
    res = math.sin(x)
    return res

def f_odu(x):
    res = 1 - math.cos(x) - math.sin(x)
    return res

def matrix_O_h(a, b, h, a1, b1, g1, a2, b2, g2):
    M = []
    N = (b - a) // h + 1
    i = 0
    while i < N:
        q = []
        if i == 0:
            q.append(0)
            q.append(a1 - b1 / h)
            q.append(b1 / h)
            q.append(g1)
            M.append(q)
        elif i == N - 1:
            q.append(-1 * b2 / h)
            q.append(a2 + b2 / h)
            q.append(0)
            q.append(g2)
            M.append(q)
        else:
            x = a + h * i
            q.append(1 / h ** 2 - f_p(x) / 2 / h)
            q.append(-2 / h ** 2 + f_q(x))
            q.append(1 / h ** 2 + f_p(x) / 2 / h)
            q.append(f_odu(x))
            M.append(q)
        i += 1
    return M

def matrix_O_2h(a, b, h, a1, b1, g1, a2, b2, g2):
    M = []
    N = (b - a) // h + 1
    i = 0
    while i < N:
        q = []
        if i == 0:
            if b1 != 0:
                q.append(0)
                q.append(-2 + (2 * a1 * h - f_p(a) * a1 * h ** 2) / b1 + f_q(a) * h ** 2)
                q.append(2)
                q.append(f_odu(a) * h ** 2 + (2 * g1 * h - f_p(a) * g1 * h ** 2) / b1)
            else:
                q.append(0)
                q.append(1)
                q.append(0)
                q.append(g1 / a1)
            M.append(q)
        elif i == N - 1:
            x = a + h * i
            if b2 != 0:
                q.append(2)
                q.append(-2 - (2 * a2 * h + f_p(x) * a2 * h ** 2) / b2 + f_q(x) * h ** 2)
                q.append(0)
                q.append(f_odu(x) * h ** 2 - (2 * g2 * h + f_p(x) * g2 * h ** 2) / b2)
            else:
                q.append(0)
                q.append(1)
                q.append(0)
                q.append(g2 / a2)
            M.append(q)
        else:
            x = a + h * i
            q.append(1 / h ** 2 - f_p(x) / 2 / h)
            q.append(-2 / h ** 2 + f_q(x))
            q.append(1 / h ** 2 + f_p(x) / 2 / h)
            q.append(f_odu(x))
            M.append(q)
        i += 1
    return M

def tridiagonal_matrix_algorithm(M):         #метод прогонки для СЛАУ (3 диаг. матр.)
    N = len(M)
    A = []
    B = []
    res = []
    i = 0
    while i < N - 1:
        if i == 0:
            A.append(-1 * M[i][2] / M[i][1])
            B.append(M[i][3] / M[i][1])
        if i > 0:
            A.append(-1 * M[i][2] / (M[i][1] + M[i][0] * A[i - 1]))
            B.append((M[i][3] - M[i][0] * B[i - 1]) / (M[i][1] + M[i][0] * A[i - 1]))
        i += 1
    i = N - 1
    while i >= 0:
        if i == N - 1:
            res.append((M[i][3] - M[i][0] * B[i - 1]) / (M[i][1] + M[i][0] * A[i - 1]))
        else:
            res.append(B[i] + A[i] * res[N - 2 - i])
        i -= 1
    #res - массив с численными решениями от b до a
    return res

def res_X(a, b, h):
    res = []
    N = (b - a) // h + 1
    i = N - 1
    while i >= 0:
        res.append((a + h * i))
        i -= 1
    return res

def err_X(a, b, h):
    res = []
    N = (b - a) // h + 1
    i = N - 1
    while i >= 0:
        res.append((i + 1))
        i -= 1
    return res

def res_exact(X):
    res = []
    N = len(X)
    i = 0
    while i < N:
        res.append(exact(X[i]))
        i += 1
    return res

def error(Y1, Y2):
    N = len(Y1)
    i = 0
    res = []
    while i < N:
        res.append(math.log10(abs(Y1[i] - Y2[i])))
        i += 1
    return res

a = 0
b = 1
h = 0.05
a1 = 1
b1 = -1
g1 = 1
a2 = 1
b2 = 0
g2 = 1.3818

M_h = matrix_O_h(a, b, h, a1, b1, g1, a2, b2, g2)
M_2h = matrix_O_2h(a, b, h, a1, b1, g1, a2, b2, g2)
res_h = tridiagonal_matrix_algorithm(M_h)
res_2h = tridiagonal_matrix_algorithm(M_2h)
X = res_X(a, b, h)
X_err = err_X(a, b, h)
Y = res_exact(X)
error_h = error(Y, res_h)
error_2h = error(Y, res_2h)
print_3gr(X, Y, res_h, res_2h, "r", "b", "g")
#print_2gr(X, error_h, error_2h, "b", "g")
