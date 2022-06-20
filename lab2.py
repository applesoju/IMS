import math
import sys
import random
import numpy as np
import matplotlib.pyplot as plt


def prob_dens1(x_vec):
    y_vec = np.empty(len(x_vec))

    for i in range(len(x_vec)):
        if -1 < x_vec[i] <= 0:
            y_vec[i] = x_vec[i] + 1
        elif 0 < x_vec[i] <= 1:
            y_vec[i] = -x_vec[i] + 1
        else:
            y_vec[i] = 0

    return y_vec


def prob_dist1(x_vec):
    y_vec = np.empty(len(x_vec))

    for i in range(len(x_vec)):
        if x_vec[i] <= -1:
            y_vec[i] = 0
        elif -1 < x_vec[i] <= 0:
            y_vec[i] = 0.5 * x_vec[i] ** 2 + x_vec[i] + 0.5
        elif 0 < x_vec[i] <= 1:
            y_vec[i] = -0.5 * x_vec[i] ** 2 + x_vec[i] + 0.5
        else:
            y_vec[i] = 1

    return y_vec


def plot_gen1(x_vec):
    dens_1 = prob_dens1(x_vec)
    dist_1 = prob_dist1(x_vec)

    plt.plot(x_vec, dens_1, label='f(x)')
    plt.plot(x_vec, dist_1, label='F(x)')
    plt.legend()
    plt.grid()
    plt.show()


def rejection_gen1(q, x_vec):
    dens_1 = prob_dens1(x_vec)
    plt.plot(x_vec, dens_1, label='f(x)')

    out = []
    not_in_count = 0
    i = 0
    while i < q:
        uni_u1 = np.random.uniform(-1, 1, 1)
        uni_u2 = np.random.uniform(0, 1, 1)
        y = 0
        if -1 < uni_u1 <= 0:
            y = uni_u1 + 1
        elif 0 < uni_u1 < 1:
            y = -uni_u1 + 1

        if uni_u2 < y:
            plt.plot(uni_u1, uni_u2, 'g.')
            out.append(uni_u1)
            i += 1
        else:
            plt.plot(uni_u1, uni_u2, 'r.')
            not_in_count += 1

    plt.legend()
    plt.grid()
    plt.show()

    return np.asarray(out), not_in_count


def plot_histogram1(random_numbers):
    v_count = [0] * 20

    for n in random_numbers:
        if -1 < n <= -0.9:
            v_count[0] += 1
        elif -0.9 < n <= -0.8:
            v_count[1] += 1
        elif -0.8 < n <= -0.7:
            v_count[2] += 1
        elif -0.7 < n <= -0.6:
            v_count[3] += 1
        elif -0.6 < n <= -0.5:
            v_count[4] += 1
        elif -0.5 < n <= -0.4:
            v_count[5] += 1
        elif -0.4 < n <= -0.3:
            v_count[6] += 1
        elif -0.3 < n <= -0.2:
            v_count[7] += 1
        elif -0.2 < n <= -0.1:
            v_count[8] += 1
        elif -0.1 < n <= 0:
            v_count[9] += 1
        elif 0 < n <= 0.1:
            v_count[10] += 1
        elif 0.1 < n <= 0.2:
            v_count[11] += 1
        elif 0.2 < n <= 0.3:
            v_count[12] += 1
        elif 0.3 < n <= 0.4:
            v_count[13] += 1
        elif 0.4 < n <= 0.5:
            v_count[14] += 1
        elif 0.5 < n <= 0.6:
            v_count[15] += 1
        elif 0.6 < n <= 0.7:
            v_count[16] += 1
        elif 0.7 < n <= 0.8:
            v_count[17] += 1
        elif 0.8 < n <= 0.9:
            v_count[18] += 1
        else:
            v_count[19] += 1

    plt.bar(np.arange(-0.95, 1.05, step=0.1), np.array(v_count), width=0.1, edgecolor='black')
    plt.title('Histogram')
    plt.xticks(np.round(np.arange(-1, 1.1, step=0.1), 1), np.round(np.arange(-1, 1.1, step=0.1), 1))
    plt.show()


def prob_dens2(x_vec):
    y_vec = np.empty(len(x_vec))

    for i in range(len(x_vec)):
        if 0 < x_vec[i] <= 0.01:
            y_vec[i] = 50
        elif 0.01 < x_vec[i] <= 1:
            y_vec[i] = 50 / 99
        else:
            y_vec[i] = 0

    return y_vec


def prob_dist2(x_vec):
    y_vec = np.empty(len(x_vec))

    for i in range(len(x_vec)):
        if x_vec[i] <= 0:
            y_vec[i] = 0
        elif 0 < x_vec[i] <= 0.01:
            y_vec[i] = 50 * x_vec[i]
        elif 0.01 < x_vec[i] <= 1:
            y_vec[i] = 50 / 99 * x_vec[i] + 0.5
        else:
            y_vec[i] = 1

    return y_vec


def plot_gen2(x_vec):
    dens_2 = prob_dens2(x_vec)
    dist_2 = prob_dist2(x_vec)

    plt.plot(x_vec, dens_2)
    plt.title('f(x)')
    plt.grid()
    plt.show()

    plt.plot(x_vec, dist_2)
    plt.title('F(x)')
    plt.grid()
    plt.show()


def rejection_gen2(q, x_vec):
    # dens_2 = prob_dens2(x_vec)
    # plt.plot(x_vec, dens_2, label='f(x)')

    out = []
    not_in_count = 0
    i = 0
    while i < q:
        uni_u1 = np.random.uniform(0, 1, 1)
        uni_u2 = np.random.uniform(0, 50, 1)
        y = 0

        if 0 < uni_u1 <= 0.01:
            y = 50
        elif 0.01 < uni_u1 <= 1:
            y = 50 / 99

        if uni_u2 < y:
            # plt.plot(uni_u1, uni_u2, 'g.')
            out.append(uni_u1)
            i += 1
        else:
            # plt.plot(uni_u1, uni_u2, 'r.')
            not_in_count += 1

    plt.legend()
    plt.grid()
    plt.show()

    return np.asarray(out), not_in_count


def plot_histogram2(random_numbers):
    v_count = [0] * 10

    for n in random_numbers:
        if 0 < n <= 0.1:
            v_count[0] += 1
        elif 0.1 < n <= 0.2:
            v_count[1] += 1
        elif 0.2 < n <= 0.3:
            v_count[2] += 1
        elif 0.3 < n <= 0.4:
            v_count[3] += 1
        elif 0.4 < n <= 0.5:
            v_count[4] += 1
        elif 0.5 < n <= 0.6:
            v_count[5] += 1
        elif 0.6 < n <= 0.7:
            v_count[6] += 1
        elif 0.7 < n <= 0.8:
            v_count[7] += 1
        elif 0.8 < n <= 0.9:
            v_count[8] += 1
        else:
            v_count[9] += 1

    plt.bar(np.arange(0.05, 1.05, step=0.1), np.array(v_count), width=0.1, edgecolor='black')
    plt.title('Histogram')
    plt.xticks(np.round(np.arange(0, 1.1, step=0.1), 1), np.round(np.arange(0, 1.1, step=0.1), 1))
    plt.show()


def prob_dens3(x_vec):
    y_vec = np.empty(len(x_vec))
    r = np.sqrt(2 / np.pi)

    for i in range(len(x_vec)):
        if x_vec[i] < -np.sqrt(r):
            y_vec[i] = 0
        elif -r <= x_vec[i] <= r:
            y_vec[i] = np.sqrt(r ** 2 - x_vec[i] ** 2)
        else:
            y_vec[i] = 0

    return y_vec


def plot_gen3(x_vec):
    dens_3 = prob_dens3(x_vec)

    plt.plot(x_vec, dens_3)
    plt.title('f(x)')
    plt.ylim([-1, 2])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid()
    plt.show()


def rejection_gen3(q, x_vec):
    dens_3 = prob_dens3(x_vec)
    plt.plot(x_vec, dens_3, label='f(x)')

    out = []
    not_in_count = 0
    i = 0
    r = np.sqrt(2 / np.pi)
    while i < q:
        uni_u1 = np.random.uniform(-r, r, 1)
        uni_u2 = np.random.uniform(0, r, 1)
        y = np.sqrt(r ** 2 - uni_u1 ** 2)

        if uni_u2 < y:
            plt.plot(uni_u1, uni_u2, 'g.')
            out.append(uni_u1)
            i += 1
        else:
            plt.plot(uni_u1, uni_u2, 'r.')
            not_in_count += 1

    plt.legend()
    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

    return np.asarray(out), not_in_count


def plot_histogram3(random_numbers):
    v_count = [0] * 20

    for n in random_numbers:
        if -1 < n <= -0.9:
            v_count[0] += 1
        elif -0.9 < n <= -0.8:
            v_count[1] += 1
        elif -0.8 < n <= -0.7:
            v_count[2] += 1
        elif -0.7 < n <= -0.6:
            v_count[3] += 1
        elif -0.6 < n <= -0.5:
            v_count[4] += 1
        elif -0.5 < n <= -0.4:
            v_count[5] += 1
        elif -0.4 < n <= -0.3:
            v_count[6] += 1
        elif -0.3 < n <= -0.2:
            v_count[7] += 1
        elif -0.2 < n <= -0.1:
            v_count[8] += 1
        elif -0.1 < n <= 0:
            v_count[9] += 1
        elif 0 < n <= 0.1:
            v_count[10] += 1
        elif 0.1 < n <= 0.2:
            v_count[11] += 1
        elif 0.2 < n <= 0.3:
            v_count[12] += 1
        elif 0.3 < n <= 0.4:
            v_count[13] += 1
        elif 0.4 < n <= 0.5:
            v_count[14] += 1
        elif 0.5 < n <= 0.6:
            v_count[15] += 1
        elif 0.6 < n <= 0.7:
            v_count[16] += 1
        elif 0.7 < n <= 0.8:
            v_count[17] += 1
        elif 0.8 < n <= 0.9:
            v_count[18] += 1
        else:
            v_count[19] += 1

    plt.bar(np.arange(-0.95, 1.05, step=0.1), np.array(v_count), width=0.1, edgecolor='black')
    plt.title('Histogram')
    plt.xticks(np.round(np.arange(-1, 1.1, step=0.1), 1), np.round(np.arange(-1, 1.1, step=0.1), 1))
    plt.show()


def prob_dens4(x_vec):
    y_vec = np.empty(len(x_vec))

    for i in range(len(x_vec)):
        y_vec[i] = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * (x_vec[i] ** 2))

    return y_vec


def plot_gen4(x_vec):
    dens_4 = prob_dens4(x_vec)

    plt.plot(x_vec, dens_4)
    plt.title('f(x)')
    plt.grid()
    plt.show()


def rejection_gen4(q, x_vec):
    dens_4 = prob_dens4(x_vec)
    plt.plot(x_vec, dens_4, label='f(x)')

    out = []
    not_in_count = 0
    i = 0

    while i < q:
        uni_u1 = np.random.uniform(-5, 5, 1)
        uni_u2 = np.random.uniform(0, 1, 1)
        y = prob_dens4([uni_u1])[0]

        if uni_u2 <= y:
            plt.plot(uni_u1, uni_u2, 'g.')
            out.append(uni_u1)
            i += 1
        else:
            plt.plot(uni_u1, uni_u2, 'r.')
            not_in_count += 1

    plt.legend()
    plt.grid()
    plt.show()

    return np.asarray(out), not_in_count


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Incorrect number of arguments.')
        exit()
    elif not sys.argv[1].isnumeric():
        print('Incorrect arguments.')
        exit()
    quantity = int(sys.argv[1])            # Number of generated numbers

    x_1 = np.linspace(-1.5, 1.5, 3000)
    x_2 = np.linspace(0, 1, 1000)
    x_3 = np.linspace(-1.5, 1.5, 3000)
    x_4 = np.linspace(-5, 5, 10000)

    # plot_gen1(x_1)
    # numbers, outside_cout = rejection_gen1(quantity, np.linspace(-1, 1, 1000))
    # print(f'Number of rejected numbers = {outside_cout}')
    # plot_histogram1(numbers)

    # plot_gen2(x_2)
    # numbers, outside_cout = rejection_gen2(quantity, np.linspace(0, 1, 1000))
    # print(f'Number of rejected numbers = {outside_cout}')
    # plot_histogram2(numbers)

    # plot_gen3(x_3)
    # numbers, outside_cout = rejection_gen3(quantity, np.linspace(-np.sqrt(2 / np.pi), np.sqrt(2 / np.pi), 1000))
    # print(f'Number of rejected numbers = {outside_cout}')
    # plot_histogram3(numbers)

    plot_gen4(x_4)
    numbers, outside_cout = rejection_gen4(quantity, x_4)
    print(f'Number of rejected numbers = {outside_cout}')
