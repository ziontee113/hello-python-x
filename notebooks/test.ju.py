# %%%[md]

## Hello Jupyter Notebook from Neovim

- Edit Jupyter Notebook in Neovim via [jupynium.nvim](https://github.com/kiyoon/jupynium.nvim)
- Environment inside `poetry shell`
- Dark mode using `jupyterthemes`

# %%

import numpy as np
import matplotlib.pyplot as plt

# %%

print("hello world")

# %%

x = np.linspace(-10, 10, 1000)
y = np.sin(x**2)

plt.plot(x, y)
