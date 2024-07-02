import numpy as np
import matplotlib.pyplot as plt

def graph(y_derivative):
    fig, axs = plt.subplots(2, 2, figsize=(10, 6))

    axs[0, 0].plot(y_derivative[0], y_derivative[1])
    axs[0, 0].set_title("y(x)")
    axs[0, 0].grid(True)

    axs[0, 1].plot(y_derivative[0], y_derivative[2], y_derivative[0], y_derivative[3], y_derivative[0], y_derivative[4])
    axs[0, 1].set_title("y'(x) and O(h^2)")
    axs[0, 1].grid(True)

    axs[1, 0].plot(y_derivative[0], y_derivative[5])
    axs[1, 0].set_title("y''(x)")
    axs[1, 0].grid(True)

    axs[1, 1].plot(y_derivative[0], y_derivative[6])
    axs[1, 1].set_title("y'''(x)")
    axs[1, 1].grid(True)

    plt.tight_layout()
    plt.show()

    plt.plot(y_derivative[0], y_derivative[2], "-",
             y_derivative[0], y_derivative[3], "--",
             y_derivative[0], y_derivative[4], ".-",
             y_derivative[0], y_derivative[1], "-o")
    plt.grid(True)
    plt.show()

def analytic_function(a, b, N):
    x_y_array = [[], []]
    x = a

    while x < b:
        y = (x**6 + x**3 - 2)/(1-x**3)**(1/2)
        x += N
        x_y_array[0].append(x)
        x_y_array[1].append(y)
    return x_y_array

def compute_derivative_values(a, b, N):
    y_derivative = [[], [], [], [], [], [], []]
    while a < b:
        y = f(a)
        y_derivative[1].append(y)

        y = (f(a + N) - f(a)) / N
        y_derivative[2].append(y)

        y = (f(a) - f(a - N)) / N
        y_derivative[3].append(y)

        y = (f(a + N) - f(a - N)) / (2 * N)
        y_derivative[4].append(y)

        y = (f(a + N) - 2 * f(a) + f(a - N)) / (N ** 2)
        y_derivative[5].append(y)

        y = (f(a + 2 * N) - 2 * f(a + N) + 2 * f(a - N) - f(a - 2 * N)) / (2 * (N ** 3))
        y_derivative[6].append(y)

        y_derivative[0].append(a)
        a += N

    return y_derivative



def f(x):
    try:
        y = (x**6 + x**3 - 2)/(1-x**3)**(1/2) #область определения - x < 1
        if np.iscomplex(y):
            return np.nan  # Если результат комплексный, возвращаем np.nan
        else:
            return y
    except:
        return np.nan  # Если возникает другая ошибка, также возвращаем np.nan

def create_grid(a, b, N):
    return np.linspace(a, b, N)

def compute_function_values(grid):
    return [f(x) for x in grid]

print("Введите a: (a < 0) ")
a = int(input())
print("Введите b: (b < 0)")
b = int(input())
print("Введите значение N: ")
N = int(input())
N_values = [N, 2*N, 4*N]

y_derivative = compute_derivative_values(a, b, N)
graph(y_derivative)

fig, axs = plt.subplots(3, figsize=(8, 12))

for i, N_f in enumerate(N_values):
    grid = create_grid(a, b, N_f)
    function_values = compute_function_values(grid)

    # Рисуем график функции на i-й области рисования
    axs[i].plot(grid, function_values)
    axs[i].set_xlabel('x')
    axs[i].set_ylabel('f(x)')
    axs[i].set_title(f'График функции f(x) для N={N_f}')
    axs[i].grid(True)

plt.tight_layout()  # Улучшает компактность расположения графиков
plt.show()