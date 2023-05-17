import math
import numpy as np
import random
import time
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def set_seed(seed=0):
    # random
    random.seed(seed)
    # numpy
    np.random.seed(seed)

    return True

# Generate random ints_list
def generate_random_ints(n):
    return [random.randint(0, 50) for _ in range(n)]

# example
# x = [1,2,3,4,5,6,7,8,9,10]
# y = [2,4,6,8,5,6,5,8,2,1]
# graph_show(x,y."temp")
def graph_show(x_list,y_list,path):
    ## input:x_list,y_list,save_figure_path
    sns.set()
    sns.set_style(style='whitegrid')
    col = sns.color_palette("deep")
    colors = [col[3],col[8],col[6],col[2],col[0]]
    fig, ax1 = plt.subplots(figsize=(8,5),tight_layout=True)
    # 軸のラベルを設定する。
    ax1.set_xlabel('x_label', fontsize = 18)
    ax1.set_ylabel('y_label' ,fontsize = 18)
    # x軸とy軸のメモリのラベルのフォントサイズを設定
    ax1.tick_params(axis='x', labelsize=17)
    ax1.tick_params(axis='y', labelsize=17)
    #データ点のプロット結果
    plt.plot(x_list,y_list, lw =3, label = f"label : {x_list}", color=colors[0])
    plt.plot(x_list,y_list, lw =3, label = f"label : {y_list}", color=colors[1])
    ax1.legend(loc = "upper left", fontsize = 15)
    plt.savefig(path,dpi=400)
    return True
# def average_bar()

