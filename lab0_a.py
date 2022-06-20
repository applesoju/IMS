import sys
import random
import numpy as np
import matplotlib.pyplot as plt


K = 5
RANGE = 10

a = np.floor(np.random.random(K) * 5000 + 5000)

if a.size != 0:
    while a[0] == 0:
        a[0] = np.random.randint(0, RANGE)
else:
    a = 0


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def plot_values(random_numbers):
    x = np.linspace(0, len(random_numbers), len(random_numbers))
    colors = np.random.rand(len(random_numbers))
    plt.scatter(x, random_numbers, alpha=0.5, c=colors)
    plt.title('All generated numbers')
    plt.xlabel('Sample number')
    plt.ylabel('Sample value')
    # plt.ylim([0, 1])
    plt.show()


def plot_histogram(random_numbers, vmax):
    r = np.linspace(0, vmax, 11)
    v_count = [0] * 10

    for n in random_numbers:
        if r[0] <= n <= r[1]:
            v_count[0] += 1
        elif r[1] < n <= r[2]:
            v_count[1] += 1
        elif r[2] < n <= r[3]:
            v_count[2] += 1
        elif r[3] < n <= r[4]:
            v_count[3] += 1
        elif r[4] < n <= r[5]:
            v_count[4] += 1
        elif r[5] < n <= r[6]:
            v_count[5] += 1
        elif r[6] < n <= r[7]:
            v_count[6] += 1
        elif r[7] < n <= r[8]:
            v_count[7] += 1
        elif r[8] < n <= r[9]:
            v_count[8] += 1
        else:
            v_count[9] += 1

    plt.bar(np.arange(0.05 * vmax, 1.05 * vmax, step=vmax * 0.1),
            np.array(v_count), width=vmax * 0.1, edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Sample value')
    plt.ylabel('Amount of samples')
    plt.xticks(np.round(np.arange(0, 1.1 * vmax, step=vmax * 0.1), 1),
               np.round(np.arange(0, 1.1 * vmax, step=vmax * 0.1), 1))
    plt.show()


def modulo_rand(x0, c, m, n):
    no_xvec = 0
    x_vec = np.empty(K).transpose()

    if x_vec.size != 0:
        x_vec[0] = x0
    else:
        no_xvec = x0

    output = np.empty(n)

    for i in range(0, n):
        if x_vec.size != 0:
            output[i] = x_vec[0]
            x_next = (a @ x_vec + c) % m
            x_vec = np.roll(x_vec, 1)
            x_vec[0] = x_next

        else:
            output[i] = no_xvec
            x_next = c % m
            no_xvec = x_next

    return output


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('Incorrect number of arguments.')
        exit()

    elif not is_number(sys.argv[1]) or not is_number(sys.argv[2])\
            or not is_number(sys.argv[2]) or not sys.argv[4].isnumeric():
        print('Incorrect arguments.')
        exit()

    print(f'a = {a}')

    x_first = float(sys.argv[1])            # First value for pseudorandom number generator
    const = float(sys.argv[2])              # Constant that is added to the sum of previous numbers in the sequence
    mod = float(sys.argv[3])                # Modulus used to compute the next random number
    iterations = int(sys.argv[4])           # Number of iterations

    # if x_first == 0:
    #     x_first = random.random()

    out = modulo_rand(x_first, const, mod, iterations)

    # Plot all generated numbers
    plot_values(out)

    # Plot a histogram of generated numbers
    # plot_histogram(out, mod)
