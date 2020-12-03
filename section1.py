import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('tkagg')  # to avoid Big Sur's bug 

def main():
  df = pd.read_csv('./times.csv', header=None)
  data = np.array(df[0])
  bins = [x for x in range(int(np.floor(min(data))), int(np.ceil(max(data))+1))]
  hist, bin_edges = np.histogram(data, bins=bins)
  [print("{0}s ~ {1}s : {2}".format(bin_edges[i], bin_edges[1], f)) for i, f in enumerate(hist)]
   
  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.set_title("histgram of perception time [sec]")
  ax.hist(data, bins=bins, histtype='barstacked', ec='black')
  plt.show()


if __name__ == "__main__":
    main()