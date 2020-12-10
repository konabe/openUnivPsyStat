import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('tkagg')  # to avoid Big Sur's bug 

# 1_1 度数分布表、ヒストグラム
def problem_1_1(data):
  bins = [x for x in range(int(np.floor(min(data))), int(np.ceil(max(data))+1))]
  hist, bin_edges = np.histogram(data, bins=bins)
  print("度数分布")
  [print("{0}s ~ {1}s : {2}".format(bin_edges[i], bin_edges[i+1], f)) for i, f in enumerate(hist)]
  i_t = np.argmax(hist)
  print("最頻値 => {0}s ~ {1}s".format(bin_edges[i_t], bin_edges[i_t+1]))

  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.set_title("histgram of perception time [sec]")
  ax.hist(data, bins=bins, histtype='barstacked', ec='black')

# 1_2 要約統計量（平均・分散・標準偏差・最頻値・中央値・四分位）
def problem_1_2(data):
  def print_solution(label, value):
    print("{0}: {1}".format(label, np.round(value, decimals=2)))
  print_solution("平均", np.mean(data))
  print_solution("分散", np.var(data))
  print_solution("標準偏差", np.std(data))
  print_solution("中央値", np.median(data))
  print_solution("第一四分位数", np.percentile(data, 25))
  print_solution("第三四分位数", np.percentile(data, 75))

# 1_3 生成分布は正規分布を仮定し、その母数に標本平均と標本分散を用いた場合の95%の予測区間
def problem_1_3(data):
  mu = np.mean(data)
  sigma = np.std(data)
  print("95%予測区間: {0} ~ {1}".format(mu - 1.96*sigma, mu + 1.96*sigma))

def main():
  df = pd.read_csv('./times.csv', header=None)
  data = np.array(df[0])
  print(data)

  problem_1_1(data)
  problem_1_2(data)
  problem_1_3(data)

  plt.show()

if __name__ == "__main__":
    main()