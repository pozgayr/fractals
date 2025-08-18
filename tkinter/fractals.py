import tkinter as tk
import numpy as np
import time

A = np.array([
    [[0.5, -0.5],
     [0.5,  0.5]],    

    [[ 0.5,  0.5],
     [-0.5,  0.5]],  
], dtype=np.float64)

b = np.array([
    [0.0, 0.0],      
    [0.5, 0.5],      
], dtype=np.float64)

p = np.array([0.5, 0.5], dtype=np.float64)

XMIN, XMAX = 0.0, 1.0
YMIN, YMAX = 0.0, 0.5

n = 50_000
seed = 0
SIZE = 800

root = tk.Tk()
canvas = tk.Canvas(root, width=SIZE, height=SIZE, bg="#0b0b10")
canvas.pack()


def ifs_chaos(A, b, p):
    x0=(0.0, 0.0)
    
    rng = np.random.default_rng(seed)

    w, h = XMAX - XMIN, YMAX - YMIN
    s = 0.48 * SIZE / max(w, h)            
    cx, cy = (XMIN + XMAX) / 2, (YMIN + YMAX) / 2

    def to_screen(x, y):
        X = (x - cx) * s + SIZE/2
        Y = -(y - cy) * s + SIZE/2      
        return X, Y
    
    psum = p.sum()
    p = p / psum
    cum = np.cumsum(p)
    
    x = np.array(x0, dtype=np.float64)
    colors = ["#ff5555", "#55ff55", "#5599ff", "#ffff55"]


    for i in range(n):
        k = int(np.searchsorted(cum, rng.random(), side="right"))
        x = A[k] @ x + b[k]
        X, Y = to_screen(x[0], x[1])
        r = 0
        g = int(255 * (i / n))
        bcol = 255
        color = f"#{r:02x}{g:02x}{bcol:02x}"
        canvas.create_rectangle(X, Y, X+1, Y+1, outline="", fill=color)
        canvas.update()
    print("finished")

if __name__ == "__main__":
    ifs_chaos(A, b, p)
    root.mainloop()
