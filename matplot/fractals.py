import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [[0.00, 0.00],[0.00, 0.16]],
    [[0.85, 0.04],[-0.04, 0.85]],
    [[0.20,-0.26],[0.23, 0.22]],
    [[-0.15,0.28],[0.26, 0.24]],
], dtype=np.float64)

b = np.array([
    [0.0, 0.0],
    [0.0, 1.6],
    [0.0, 1.6],
    [0.0, 0.44],
], dtype=np.float64)

p = np.array([0.01, 0.85, 0.07, 0.07], dtype=np.float64)

n = 500_000
seed = 0
bg='#0b0b10'
s = 0.25


def ifs_chaos(A, b, p):
    x0=(0.0, 0.0)
    rng = np.random.default_rng(seed)
    
    psum = p.sum()
    p = p / psum
    cum = np.cumsum(p)

    pts = np.empty((n, 2), dtype=np.float64)
    x = np.array(x0, dtype=np.float64)

    for i in range(n):
        k = int(np.searchsorted(cum, rng.random(), side="right"))
        x = A[k] @ x + b[k]
        pts[i] = x
        
    return pts


def main():
    pts = ifs_chaos(A, b, p)
    x, y = pts[:, 0], pts[:, 1]
    fig, ax = plt.subplots(dpi=160)
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')
    plt.margins(0)
    
    solid = (0.2, 0.9, 0.4, 0.7)
    ax.scatter(x, y, s=s, color=solid, linewidths=0, rasterized=True)
    plt.show()


if __name__ == "__main__":
    main()

