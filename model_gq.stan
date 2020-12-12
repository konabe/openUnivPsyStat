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
  X_pred = normal_rng(theta, sigma);
  Var = sigma ^ 2;
  Coeff = sigma / theta;
  DeltaC = (theta - c) / sigma;
}