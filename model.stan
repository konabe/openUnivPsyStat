data {
  int<lower=0> N;
  vector[N] X;
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
  X_pred = normal_rng(theta, sigma);
}