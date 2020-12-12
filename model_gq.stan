data {
  int<lower=0> N;
  vector[N] X;
  real c; // 基準点
}
parameters {
  real theta;
  real<lower=0> sigma;
}
model {
  X ~ normal(theta, sigma);
}
generated quantities {
  real X_pred;
  real Var; // 分散
  real Coeff; // 変動係数
  real DeltaC; // 効果量
  real QFPer; // 第一四分位点
  real ObsSec; // 区間での観測確率 (30 ~ 31で整数部が30となる確率)
  real RatioC; // 比の確率
  X_pred = normal_rng(theta, sigma);
  Var = sigma ^ 2;
  Coeff = sigma / theta;
  DeltaC = (theta - c) / sigma;
  QFPer = theta -0.675 * sigma; // F(-0.675|0, 1) = 0.25
  ObsSec = normal_cdf(31, theta, sigma) - normal_cdf(30, theta, sigma);
  RatioC = X_pred / c;
}