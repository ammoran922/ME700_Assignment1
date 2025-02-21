import numpy as np
from pathlib import Path

#Implementation of Newton's method for 1D problems
def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x
        if dfx == 0:
            raise ValueError("Zero derivative encountered, choose a different initial guess.")
        x -= fx / dfx
    raise ValueError("Maximum number of iterations reached without convergence.")

    print("Maximum iterations reached. Root may not have converged.")
    return None

#Implementation of Newton's mthod for higher dimension problems
def newton_multi(F, J, x0, tol=1e-6, max_iter=100):
    x = np.array(x0, dtype=float)
    for i in range(max_iter):
        Fx = np.array(F(x))
        Jx = np.array(J(x))
        if np.linalg.norm(Fx, ord=2) < tol:
            return x
        dx = np.linalg.solve(Jx, -Fx)
        x += dx
    raise ValueError("Maximum number of iterations reached without convergence.")
