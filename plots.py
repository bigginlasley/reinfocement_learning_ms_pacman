import matplotlib.pyplot as plt
import numpy as np
import statistics

def get_summary_statistics(dataset):
    
    mean =       np.round(statistics.mean(dataset), 2)
    median =     np.round(statistics.median(dataset), 2)
    min_value =  np.round(min(dataset), 2)
    max_value =  np.round(max(dataset), 2)

    print('Min: %s' % min_value)
    print('Mean: %s' % mean)
    print('Max: %s' % max_value)
    print('Median: %s' % median)

 
pdd7   = [143.000,143.000,143.000,143.000,143.000,143.000, 143.000, 143.000, 122.000,137.000,143.000, 143.000, 143.000, 144.000,143.000, 143.000, 143.000, 143.000, 143.000, 143.000, 143.000, 143.000, 143.000, 84.000,143.000, 143.000, 129.000,140.000,143.000, 143.000, 147.000, 143.000, 143.000, 143.000, 143.000, 143.000, 143.000, 143.000, 143.000, 143.000, 143.000, 143.000, 136.000,143.000, 143.000, 143.000, 134.000,143.000, 143.000, 143.000]
pdd6   = [138.000,138.000,138.000,138.000,138.000,138.000,138.000,138.000,143.000,137.000,138.000,147.000,138.000,146.000,138.000,138.000,138.000,138.000,138.000,138.000,138.000,138.000,138.000,141.000,138.000,138.000,137.000,141.000,138.000,138.000,144.000,138.000,138.000,138.000,138.000,138.000,138.000,138.000,138.000,138.000,138.000,138.000,146.000,138.000,138.000,138.000,146.000,138.000,138.000,138.000]
pdd1   = [50.000,50.000,50.000,50.000,50.000,50.000,50.000,50.000,60.000,49.000,50.000,47.000,68.000,76.000,50.000,50.000,50.000,50.000,50.000,50.000,50.000,50.000,50.000,50.000,50.000,50.000,47.000,51.000,50.000,50.000,44.000,50.000,50.000,50.000,50.000,50.000,50.000,50.000,50.000,50.000,50.000,50.000,47.000,50.000,50.000,50.000,46.000,50.000,50.000,50.000]
nstep7 = [146.000,140.000,142.000,143.000,143.000,126.000,118.000,132.000,138.000,142.000,149.000,133.000,140.000,115.000,143.000,143.000,133.000,147.000,147.000,136.000,135.000,142.000,79.000, 147.000,141.000,118.000,140.000,151.000,134.000,131.000,150.000,142.000,128.000,138.000,133.000,144.000,137.000,147.000,136.000,143.000,147.000,144.000,138.000,145.000,143.000,146.000,128.000,149.000,137.000,141.000]
nstep6 = [143.000,139.000,142.000,131.000,133.000,143.000,144.000,143.000,145.000,105.000,134.000,144.000,141.000,130.000,116.000,144.000,148.000,140.000,146.000,123.000,135.000,143.000,143.000,145.000,136.000,123.000,144.000,136.000,108.000,143.000,144.000,133.000,141.000,117.000,135.000,143.000,139.000,145.000,142.000,118.000,141.000,137.000,141.000,144.000,130.000,137.000,144.000,141.000,139.000,143.000]
nstep1 = [106.000, 88.000, 99.000, 89.000, 75.000, 114.000, 83.000, 86.000, 103.000, 92.000, 103.000, 90.000, 86.000, 80.000, 105.000, 99.000, 89.000, 101.000, 99.000, 96.000, 100.000, 100.000, 114.000, 93.000, 81.000, 84.000, 93.000, 105.000, 97.000, 58.000, 89.000, 112.000, 69.000, 99.000, 107.000, 118.000, 82.000, 101.000, 83.000, 98.000, 100.000, 89.000, 98.000, 108.000, 102.000, 103.000, 69.000, 83.000, 80.000, 113.000]

medianprops = dict(linewidth=3)
plt.ylabel("Reward (Items Consumed)")
plt.ylim([40, 160])
plt.xlabel("Agent")
plt.grid(True, which='major', axis='y')
plt.title("PDD vs Noisy N Step PDD Reward at 1 Million Steps")
plt.boxplot([pdd1, nstep1], labels=["PDD", "Noisy N Step PDD"], widths=.6, patch_artist = True, medianprops=medianprops, showmeans=True)
plt.show()

plt.ylabel("Reward (Items Consumed)")
plt.ylim([40, 160])
plt.xlabel("Agent")
plt.grid(True, which='major', axis='y')
plt.title("PDD vs Noisy N Step PDD Reward at 6.5 Million Steps")
plt.boxplot([pdd6, nstep6], labels=["PDD", "Noisy N Step PDD"], widths=.6, patch_artist = True, medianprops=medianprops, showmeans=True)
plt.show()

plt.ylabel("Reward (Items Consumed)")
plt.ylim([40, 160])
plt.xlabel("Agent")
plt.grid(True, which='major', axis='y')
plt.title("PDD vs Noisy N Step PDD Reward at 7 Million Steps")
plt.boxplot([pdd7, nstep7], labels=["PDD", "Noisy N Step PDD"], widths=.6, patch_artist = True, medianprops=medianprops, showmeans=True)
plt.show()
#######################################################

plt.ylabel("Reward (Items Consumed)")
plt.ylim([40, 160])
plt.title("PDD Comparisons at Different Steps")
plt.xlabel("PDD Agent")
plt.grid(True, which='major', axis='y')
plt.boxplot([pdd1, pdd6, pdd7], labels=["1 Million Steps", "6.5 Million Steps", "7 Million Steps"], widths=.6, patch_artist = True, medianprops=medianprops, showmeans=True)
plt.show()

plt.ylabel("Reward (Items Consumed)")
plt.ylim([40, 160])
plt.title("Noisy N Step PDD Comparisons at Different Steps")
plt.xlabel("Noisy N Step PDD Agent")
plt.grid(True, which='major', axis='y')
plt.boxplot([nstep1, nstep6, nstep7], labels=["1 Million Steps", "6.5 Million Steps", "7 Million Steps"], widths=.6, patch_artist = True, medianprops=medianprops, showmeans=True)
plt.show()

#####################
# pdd7 summary statistics
# Min: 84.0
# Mean: 140.72
# Max: 147.0
# Median: 143.0

# pdd6 summary statistics
# Min: 137.0
# Mean: 138.96
# Max: 147.0
# Median: 138.0

# pdd1 summary statistics
# Min: 44.0
# Mean: 50.7
# Max: 76.0
# Median: 50.0

# n7 summary statistics
# Min: 79.0
# Mean: 137.8
# Max: 151.0
# Median: 141.0

# n6 summary statistics
# Min: 105.0
# Mean: 136.88
# Max: 148.0
# Median: 141.0

# n1 summary statistics
# Min: 58.0
# Mean: 94.22
# Max: 118.0
# Median: 97.5

print('\n\npdd7 summary statistics')
get_summary_statistics(pdd7)

print('\n\npdd6 summary statistics')
get_summary_statistics(pdd6)

print('\n\npdd1 summary statistics')
get_summary_statistics(pdd1)

print('\n\nn7 summary statistics')
get_summary_statistics(nstep7)

print('\n\nn6 summary statistics')
get_summary_statistics(nstep6)

print('\n\nn1 summary statistics')
get_summary_statistics(nstep1)