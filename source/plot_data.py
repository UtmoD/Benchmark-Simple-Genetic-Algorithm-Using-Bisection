import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker

def plot(data, label, title, plot_eval=False, hold=False):
    X = data[:, 0]
    y = data[:, 1] if not plot_eval else data[:, 2]
    y_err = data[:, 3] if not plot_eval else data[:, 4]

    
    ax.errorbar(X, y, yerr=y_err, label=label, fmt='-o')

    ax.set_xlabel('Problem size (l)')
    ylabel = 'MRPS (mean)' if not plot_eval else 'Average number of fitness function calls'
    ax.set_ylabel(ylabel)  

    ax.set_yscale('log')
    ax.set_xscale('log')

    ax.set_xticks([10 * 2**i for i in range(5)])

    ax.set_xlim(9, 170)
    ax.set_ylim(10, 150000)
    
    # Keep tick from log scale
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_formatter(matplotlib.ticker.NullFormatter())

    plt.legend(loc='upper right')

    ax.set_title(title)
    
    if not hold:
        plt.show()

fig, ax = plt.subplots()
filename = 'sGA-UX-TrapFive.csv'
df = pd.read_csv('../report/{}'.format(filename))
ux_onemax = df.to_numpy()

plot(ux_onemax, 'UX', 'sGA-TrapFive', False, True)

filename = 'sGA-1X-TrapFive.csv'
df = pd.read_csv('../report/{}'.format(filename))
ux_onemax = df.to_numpy()

plot(ux_onemax, '1X', 'sGA-TrapFive', False)

