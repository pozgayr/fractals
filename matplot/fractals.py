import numpy as np
import matplotlib.pyplot as plt


n = 2_000_000
seed = 0
bg='#0b0b10'
s = 0.25
cmap = 'plasma'c


def levy_ifs():
    rng = np.random.default_rng(seed)

    a1 = (1 + 1j) / 2.0
    b1 = 0.0 + 0.0j

    a2 = (1 - 1j) / 2.0
    b2 = (1 + 1j) / 2.0

    p1 = 0.5
    z = 0.0 + 0.0j

    pts = np.empty(n, dtype=np.complex128)
    for i in range(n):
        if rng.random() < p1:
            z = a1 * z + b1
        else:
            z = a2 * z + b2
        pts[i] = z

    return pts

def main():
    pts = levy_ifs()
    pts = pts * 1j
    x, y = np.real(pts), np.imag(pts)
    fig, ax = plt.subplots(dpi=160)
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')
    plt.margins(0)

    c = np.linspace(0, 1, len(x))
    ax.scatter(x, y, c=c, s=s, cmap=cmap, linewidths=0, rasterized=True)
    plt.show()


if __name__ == "__main__":
    main()

