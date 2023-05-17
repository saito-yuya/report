from utils import *

sns.set()
sns.set_style(style='whitegrid')
def stats(lst):
    avg = sum(lst) / len(lst)
    max_minus_avg = max(lst) - avg
    avg_minus_min = avg - min(lst)
    return avg, max_minus_avg, avg_minus_min

## DP
n_5_time =  [6.38962e-05, 5.88894e-05, 8.39233e-05, 5.31673e-05, 6.79493e-05]
mean_yerr_scope5,max_minus_avg5, avg_minus_min5 = stats(n_5_time)

n_10_time = [9.799e-05, 0.0001220703, 0.0001180172, 9.60827e-05, 0.0001218319]
mean_yerr_scope10,max_minus_avg10, avg_minus_min10 = stats(n_10_time)

n_15_time  = [0.0001318455, 0.0001478195, 0.0001547337, 0.0001380444, 0.0001683235]
mean_yerr_scope15,max_minus_avg15, avg_minus_min15 = stats(n_15_time)

n_20_time  = [0.0001859665,0.0005419254,0.0002191067,0.0001802444,0.0002162457]
mean_yerr_scope20,max_minus_avg20, avg_minus_min20 = stats(n_20_time)

mean_scope = np.array([mean_yerr_scope5,mean_yerr_scope10,mean_yerr_scope15,mean_yerr_scope20])
yerr_scope = np.array([[avg_minus_min5,avg_minus_min10,avg_minus_min15,avg_minus_min20],[max_minus_avg5,max_minus_avg10,max_minus_avg15,max_minus_avg20]])

## Naive
BITn_5_time = [4.19617e-05, 3.69549e-05, 4.62532e-05, 3.60012e-05, 4.81606e-05]
BITmean_yerr_scope5,BITmax_minus_avg5, BITavg_minus_min5 = stats(BITn_5_time)

BITn_10_time = [0.0018258095, 0.0018701553, 0.0019631386, 0.0018320084, 0.0018641949]
BITmean_yerr_scope10,BITmax_minus_avg10, BITavg_minus_min10 = stats(BITn_10_time)

BITn_15_time  = [0.0822768211, 0.0800881386, 0.0799648762, 0.0807192326, 0.0837118626]
BITmean_yerr_scope15,BITmax_minus_avg15, BITavg_minus_min15 = stats(BITn_15_time)

BITn_20_time  = [3.3146628242,3.3347830772,3.268529892,3.2644450665,3.3247628212]
BITmean_yerr_scope20,BITmax_minus_avg20, BITavg_minus_min20 = stats(BITn_20_time)

BITmean_scope = np.array([BITmean_yerr_scope5,BITmean_yerr_scope10,BITmean_yerr_scope15,BITmean_yerr_scope20])
BITyerr_scope = np.array([[BITavg_minus_min5,BITavg_minus_min10,BITavg_minus_min15,BITavg_minus_min20],[BITmax_minus_avg5,BITmax_minus_avg10,BITmax_minus_avg15,BITmax_minus_avg20]])

colors = sns.color_palette("deep")
x = [5,10,15,20]

fig, ax = plt.subplots(figsize=(8,5),tight_layout=True)

# x軸のメモリの設定
ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.plot(x, BITmean_scope, lw=3,marker='o',markersize=5,label='exhaustive',color=colors[8])
ax.errorbar(x, BITmean_scope, yerr=BITyerr_scope, capsize=5, fmt='o', ms=0, mfc='None', mec='k',ecolor=colors[5], elinewidth=2)
ax.plot(x, mean_scope,ls="--", lw=3,marker='o',markersize=5,label='DP',color=colors[3])
ax.errorbar(x, mean_scope, yerr=yerr_scope, capsize=5, fmt='o', ms=0, mfc='None',ecolor=colors[3], elinewidth=2)
# ax.plot(x, [0,0,0,0])

ax.set_xlabel('Number of goods',fontsize=18)
ax.set_ylabel('Exection time[s]',fontsize=18)
ax.set_xlim(0,25,5)

plt.yscale('log')

plt.grid(which='major',color='black',linestyle='-')
# plt.grid(which='minor',color='black',linestyle='-')

ax.set_title('Compare time with DP and exhaustive search',fontsize=18)
plt.legend(loc="upper left",fontsize=15)

 # x軸とy軸のメモリのラベルのフォントサイズを設定
ax.tick_params(axis='x', labelsize=17)
ax.tick_params(axis='y', labelsize=17)
plt.xticks(x)

plt.savefig('exection_time.png',dpi=400)
# plt.savefig('minSk-worst_error.pdf',dpi=400)


plt.show()

