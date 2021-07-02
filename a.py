import numpy as np
from matplotlib import pyplot as plt


def linear_search(data, n, key):
    count = 0
    axis = np.arange(0, 101, 1)

    # ここからグラフ描画
    # フォントの種類とサイズを設定する。
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.family'] = 'Times New Roman'

    # 目盛を内側にする。
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    # グラフの上下左右に目盛線を付ける。
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.yaxis.set_ticks_position('both')
    ax1.xaxis.set_ticks_position('both')

    # 軸のラベルを設定する。
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_xticks(np.arange(0, 101, 10))
    ax1.set_xlim(0, 101)
    ax1.set_ylim(0, 140)

    # データプロットの準備。
    ax1.bar(axis, data, label='data')
    ax1.bar(key, data[key], label='answer', color='red')
    ax1.bar(0, 0, label='searched')
    plt.text(10, 120, 'count=' + str(count), fontsize=20)

    # グラフを表示する。
    fig.tight_layout()
    fig.legend()
    plt.savefig('fig_' + str("{:05}".format(count)) + '.png')
    plt.close()

    for i in range(n):
        count += 1
        # ここからグラフ描画
        # フォントの種類とサイズを設定する。
        plt.rcParams['font.size'] = 14
        plt.rcParams['font.family'] = 'Times New Roman'

        # 目盛を内側にする。
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'

        # グラフの上下左右に目盛線を付ける。
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.yaxis.set_ticks_position('both')
        ax1.xaxis.set_ticks_position('both')

        # 軸のラベルを設定する。
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        ax1.set_xticks(np.arange(0, 101, 10))
        ax1.set_xlim(0, 101)
        ax1.set_ylim(0, 140)

        # データプロットの準備。
        ax1.bar(axis, data, label='data')
        ax1.bar(key, data[key], label='answer', color='red')
        ax1.bar(i, data[i], label='searched')
        plt.text(10, 120, 'count=' + str(count), fontsize=20)

        # グラフを表示する。
        fig.tight_layout()
        fig.legend()
        plt.savefig('fig_' + str("{:05}".format(count)) + '.png')
        plt.close()
        if data[i] == key:
            return i

    return np.nan


y = np.arange(0, 101, 1)
print(y)

index = linear_search(y, len(y), key=65)
print(index)
