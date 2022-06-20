import sys
import random
import numpy as np
import matplotlib.pyplot as plt


def prob_dens1(x_vec):
    y_vec = np.empty(len(x_vec))

    for i in range(len(x_vec)):
        if 0 <= x_vec[i] <= 1:
            y_vec[i] = 2 * x_vec[i]
        else:
            y_vec[i] = 0

    return y_vec


def prob_dens2(x_vec):
    y_vec = np.empty(len(x_vec))

    for i in range(len(x_vec)):
        if -1 < x_vec[i] < 0:
            y_vec[i] = x_vec[i] + 1
        elif 0 <= x_vec[i] < 1:
            y_vec[i] = -1 * x_vec[i] + 1
        else:
            y_vec[i] = 0

    return y_vec


def prob_dens3(x_vec):
    return np.exp(-1 * x_vec)


def prob_dens4(x_vec):
    tmp = -1 * np.abs(x_vec)
    y_vec = 0.5 * np.exp(tmp)

    return y_vec


def prob_dist1(x_vec):
    y_vec = np.empty(len(x_vec))

    for i in range(len(x_vec)):
        if x_vec[i] < 0:
            y_vec[i] = 0
        elif 0 <= x_vec[i] <= 1:
            y_vec[i] = x_vec[i] ** 2
        else:
            y_vec[i] = 1

    return y_vec


def prob_dist2(x_vec):
    y_vec = np.empty(len(x_vec))

    for i in range(len(x_vec)):
        if x_vec[i] <= -1:
            y_vec[i] = 0
        elif -1 < x_vec[i] < 0:
            y_vec[i] = x_vec[i] + x_vec[i] ** 2 / 2 + 0.5
        elif 0 <= x_vec[i] < 1:
            y_vec[i] = x_vec[i] - x_vec[i] ** 2 / 2 + 0.5
        else:
            y_vec[i] = 1

    return y_vec


def prob_dist3(x_vec):
    tmp = np.ones(len(x_vec))
    y_vec = tmp - np.exp(-1 * x_vec)

    return y_vec


def prob_dist4(x_vec):
    y_vec = np.empty(len(x_vec))

    for i in range(len(x_vec)):
        if x_vec[i] < 0:
            y_vec[i] = 0.5 * np.exp(x_vec[i])
        else:
            y_vec[i] = 1 - 0.5 * np.exp(-1 * x_vec[i])

    return y_vec


def prob_dist_inv1(x_vec):
    y_vec = np.empty(len(x_vec))

    for i in range(len(x_vec)):
        if x_vec[i] < 0:
            y_vec[i] = 0
        elif 0 <= x_vec[i] <= 1:
            y_vec[i] = x_vec[i] ** 0.5
        else:
            y_vec[i] = 1

    return y_vec


def prob_dist_inv2(x_vec):
    y_vec = np.empty(len(x_vec))

    for i in range(len(x_vec)):
        if x_vec[i] < 0:
            y_vec[i] = 0
        elif 0 <= x_vec[i] <= 0.5:
            y_vec[i] = (2 * x_vec[i]) ** 0.5 - 1
        elif 0.5 < x_vec[i] <= 1:
            y_vec[i] = 1 - (2 - 2 * x_vec[i]) ** 0.5
        else:
            y_vec[i] = 1

    return y_vec


def prob_dist_inv3(x_vec):
    tmp = np.ones(len(x_vec)) - x_vec
    y_vec = -1 * np.log(tmp)

    return y_vec


def prob_dist_inv4(x_vec):
    y_vec = np.empty(len(x_vec))

    for i in range(len(x_vec)):
        if x_vec[i] < 0.5:
            y_vec[i] = np.log(2 * x_vec[i])
        else:
            y_vec[i] = -1 * np.log(2 - 2 * x_vec[i])

    return y_vec


def rand_from_inverses(n):
    random_uniform_numbers = np.random.uniform(0, 1, n)
    output_numbers1 = prob_dist_inv1(random_uniform_numbers)
    output_numbers2 = prob_dist_inv2(random_uniform_numbers)
    output_numbers3 = prob_dist_inv3(random_uniform_numbers)
    output_numbers4 = prob_dist_inv4(random_uniform_numbers)

    return output_numbers1, output_numbers2, output_numbers3, output_numbers4


def plot_gen1(x_vec):
    dens_1 = prob_dens1(x_vec)
    dist_1 = prob_dist1(x_vec)
    inv_dist1 = prob_dist_inv1(x_vec)

    plt.plot(x_vec, dens_1, label='f(x)')
    plt.plot(x_vec, dist_1, label='F(x)')
    plt.plot(x_vec, inv_dist1, label='F-1(y)')
    plt.legend()
    plt.grid()
    plt.show()


def plot_gen2(x_vec, xv_inv):
    dens_2 = prob_dens2(x_vec)
    dist_2 = prob_dist2(x_vec)
    inv_dist2 = prob_dist_inv2(xv_inv)

    plt.plot(x_vec, dens_2, label='f(x)')
    plt.plot(x_vec, dist_2, label='F(x)')
    plt.plot(xv_inv, inv_dist2, label='F-1(y)')
    plt.legend()
    plt.grid()
    plt.show()


def plot_gen3(x_vec, xv_inv):
    dens_3 = prob_dens3(x_vec)
    dist_3 = prob_dist3(x_vec)
    inv_dist3 = prob_dist_inv3(xv_inv)

    plt.plot(x_vec, dens_3, label='f(x)')
    plt.plot(x_vec, dist_3, label='F(x)')
    plt.plot(xv_inv, inv_dist3, label='F-1(y)')
    plt.legend()
    plt.grid()
    plt.show()


def plot_gen4(x_vec, xv_inv):
    dens_4 = prob_dens4(x_vec)
    dist_4 = prob_dist4(x_vec)
    inv_dist4 = prob_dist_inv4(xv_inv)

    plt.plot(x_vec, dens_4, label='f(x)')
    plt.plot(x_vec, dist_4, label='F(x)')
    plt.plot(xv_inv, inv_dist4, label='F-1(y)')
    plt.grid()
    plt.legend()
    plt.show()


def plot_histogram1(random_numbers):
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
    plt.xlabel('Values')
    plt.ylabel('Number of samples')
    plt.xticks(np.round(np.arange(0, 1.1, step=0.1), 1), np.round(np.arange(0, 1.1, step=0.1), 1))
    plt.show()


def plot_histogram2(random_numbers):
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
    plt.xlabel('Values')
    plt.ylabel('Number of samples')
    plt.xticks(np.round(np.arange(-1, 1.1, step=0.1), 1), np.round(np.arange(-1, 1.1, step=0.1), 1))
    plt.show()


def plot_histogram3(random_numbers):
    v_count = [0] * 20

    for n in random_numbers:
        if 0 < n <= 0.5:
            v_count[0] += 1
        elif 0.5 < n <= 1:
            v_count[1] += 1
        elif 1 < n <= 1.5:
            v_count[2] += 1
        elif 1.5 < n <= 2:
            v_count[3] += 1
        elif 2 < n <= 2.5:
            v_count[4] += 1
        elif 2.5 < n <= 3:
            v_count[5] += 1
        elif 3 < n <= 3.5:
            v_count[6] += 1
        elif 3.5 < n <= 4:
            v_count[7] += 1
        elif 4 < n <= 4.5:
            v_count[8] += 1
        elif 4.5 < n <= 5:
            v_count[9] += 1
        elif 5 < n <= 5.5:
            v_count[10] += 1
        elif 5.5 < n <= 6:
            v_count[11] += 1
        elif 6 < n <= 6.5:
            v_count[12] += 1
        elif 6.5 < n <= 7:
            v_count[13] += 1
        elif 7 < n <= 7.5:
            v_count[14] += 1
        elif 7.5 < n <= 8:
            v_count[15] += 1
        elif 8 < n <= 8.5:
            v_count[16] += 1
        elif 8.5 < n <= 9:
            v_count[17] += 1
        elif 9 < n <= 9.5:
            v_count[18] += 1
        else:
            v_count[19] += 1

    plt.bar(np.arange(0.25, 10.25, step=0.5), np.array(v_count), width=0.5, edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Values')
    plt.ylabel('Number of samples')
    plt.xticks(np.round(np.arange(0, 10.5, step=0.5), 1), np.round(np.arange(0, 10.5, step=0.5), 1))
    plt.show()


def plot_histogram4(random_numbers):
    v_count = [0] * 41

    for n in random_numbers:
        if n < -5:
            v_count[0] += 1
        elif -5 < n < -4.75:
            v_count[1] += 1
        elif -4.75 < n < -4.5:
            v_count[2] += 1
        elif -4.5 < n < -4.25:
            v_count[3] += 1
        elif -4.25 < n < -4:
            v_count[4] += 1
        elif -4 < n < -3.75:
            v_count[5] += 1
        elif -3.75 < n < -3.5:
            v_count[6] += 1
        elif -3.5 < n < -3.25:
            v_count[7] += 1
        elif -3.25 < n < -3:
            v_count[8] += 1
        elif -3 < n < -2.75:
            v_count[9] += 1
        elif -2.75 < n < -2.5:
            v_count[10] += 1
        elif -2.5 < n < -2.25:
            v_count[11] += 1
        elif -2.25 < n < -2:
            v_count[12] += 1
        elif -2 < n < -1.75:
            v_count[13] += 1
        elif -1.75 < n < -1.5:
            v_count[14] += 1
        elif -1.5 < n < -1.25:
            v_count[15] += 1
        elif -1.25 < n < -1:
            v_count[16] += 1
        elif -1 < n < -0.75:
            v_count[17] += 1
        elif -0.75 < n < -0.5:
            v_count[18] += 1
        elif -0.5 < n < -0.25:
            v_count[19] += 1
        elif -0.25 < n < 0:
            v_count[20] += 1
        elif 0 < n < 0.25:
            v_count[21] += 1
        elif 0.25 < n < 0.5:
            v_count[22] += 1
        elif 0.5 < n < 0.75:
            v_count[23] += 1
        elif 0.75 < n < 1:
            v_count[24] += 1
        elif 1 < n < 1.25:
            v_count[25] += 1
        elif 1.25 < n < 1.5:
            v_count[26] += 1
        elif 1.5 < n < 1.75:
            v_count[27] += 1
        elif 1.75 < n < 2:
            v_count[28] += 1
        elif 2 < n < 2.25:
            v_count[29] += 1
        elif 2.25 < n < 2.5:
            v_count[30] += 1
        elif 2.5 < n < 2.75:
            v_count[31] += 1
        elif 2.75 < n < 3:
            v_count[32] += 1
        elif 3 < n < 3.25:
            v_count[33] += 1
        elif 3.25 < n < 3.5:
            v_count[34] += 1
        elif 3.5 < n < 3.75:
            v_count[35] += 1
        elif 3.75 < n < 4:
            v_count[36] += 1
        elif 4 < n < 4.25:
            v_count[37] += 1
        elif 4.25 < n < 4.5:
            v_count[38] += 1
        elif 4.5 < n < 4.75:
            v_count[39] += 1
        else:
            v_count[40] += 1

    plt.bar(np.arange(-4.875, 5.126, step=0.25), np.array(v_count), width=0.25, edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Values')
    plt.ylabel('Number of samples')
    plt.xticks(np.round(np.arange(-5, 5.25, step=0.5), 5), np.round(np.arange(-5, 5.25, step=0.5), 5))
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Incorrect number of arguments.')
        exit()
    elif not sys.argv[1].isnumeric():
        print('Incorrect arguments.')
        exit()
    quantity = int(sys.argv[1])            # Number of generated numbers

    x_1 = np.linspace(-0.5, 1.5, 2000)

    x_2 = np.linspace(-1, 1, 1000)
    x_2_inv = np.linspace(0, 1, 1000)

    x_3 = np.linspace(-2, 8, 1000)
    x_3_inv = np.linspace(-2, 0.9999, 1000)

    x_4 = np.linspace(-1, 1, 2000)
    x_4_inv = np.linspace(0.183, 0.816, 1000)

    rng_output1, rng_output2, rng_output3, rng_output4 = rand_from_inverses(quantity)

    # Plot a generator and a histogram of numbers from the first generator
    # plot_gen1(x_1)
    # plot_histogram1(rng_output1)

    # Plot a generator and a histogram of numbers from the second generator
    # plot_gen2(x_2, x_2_inv)
    # plot_histogram2(rng_output2)

    # Plot a generator and a histogram of numbers from the third generator
    # plot_gen3(x_3, x_3_inv)
    # plot_histogram3(rng_output3)

    # Plot a generator and a histogram of numbers from the fourth generator
    plot_gen4(x_4, x_4_inv)
    plot_histogram4(rng_output4)
