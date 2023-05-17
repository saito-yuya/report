from utils import *
from report.bit_search import subset_bit
from knapsack_dp import subset_dp
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='hyper parameter',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--seed',type = int, default=0,
                        help='# of goods')
    parser.add_argument('--N', type = int, default=5,
                        help='# of goods')
    parser.add_argument('--W', type = int, default=30,
                        help='weight capasity')
    # parser.add_argument('--w_list', type = list,default=[9, 6, 4, 3 ,5 ,6],
    #                     help='each goods weight')
    # parser.add_argument('--v_list', type = list,default=[15, 10, 16, 4, 12, 25],
    #                     help='each goods value')
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    N = args.N
    W = args.W
    seed = args.seed

    DP_time = []
    BIT_time = []
    check_value = []
    
    for i in range(5):
        set_seed(i)
        w_list = generate_random_ints(N)

        res,s_time = subset_dp(N,W,w_list)
        DP_time.append(s_time)
        check_value.append(res)
        print(f"DP_seed={seed}",(res,s_time))

        res,s_time = subset_bit(N,W,w_list)
        BIT_time.append(s_time)
        check_value.append(res)
        print(f"BIT_seed={seed}",(res,s_time))

    # print(f"DP_time",DP_time)
    # print(f"BIT_time",BIT_time)
    print("finish")



