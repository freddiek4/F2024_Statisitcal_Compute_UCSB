import jax.numpy as np
from jax import random
from neural_tangents import stax
from jax.scipy.linalg import solve

key = random.PRNGKey(42)
x_train = random.normal(key, (100, 5))
y_train = random.normal(key, (100, 1))

init_fn, apply_fn, kernel_fn = stax.serial(
    stax.Dense(512),
    stax.Relu(),
    stax.Dense(1)
)

ntk = kernel_fn(x_train, x_train, 'ntk')
weights_optimal = solve(ntk + 1e-5 * np.eye(ntk.shape[0]), y_train, sym_pos=True)

x_test = random.normal(key, (20, 5))
ntk_test_train = kernel_fn(x_test, x_train, 'ntk')
y_pred = ntk_test_train @ weights_optimal

x_test_2 = random.normal(key, (10, 5))
ntk_test_train_2 = kernel_fn(x_test_2, x_train, 'ntk')
y_pred_2 = ntk_test_train_2 @ weights_optimal

print(y_pred)
print(y_pred_2)
