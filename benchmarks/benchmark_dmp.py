import numpy as np
from dmp import DMP
import timeit


n_dims = 10
start_y = np.zeros(n_dims)
goal_y = np.ones(n_dims)
dt = 0.001
int_dt = 0.0001

dmp = DMP(n_dims=n_dims, execution_time=1.0, dt=dt, n_weights_per_dim=6, int_dt=int_dt)
dmp.configure(start_y=start_y, goal_y=goal_y)
dmp.forcing_term.weights = 1000 * np.random.randn(*dmp.forcing_term.weights.shape)

times = timeit.repeat(dmp.open_loop, repeat=10, number=1)
print("Mean: %.5f; Std. dev.: %.5f" % (np.mean(times), np.std(times)))
# Pure python
# Mean: 0.58188; Std. dev.: 0.00225