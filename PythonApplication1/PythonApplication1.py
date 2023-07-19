import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 50)

y_1 = np.sin(x)
y_2 = np.cos(x)
y_3 = np.tan(x)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

line_1 = axes[0, 0].plot(x, y_1, label='sin(x)')
line_2 = axes[0, 1].plot(x, y_2, color='red', label='cos(x)')
line_3 = axes[1, 0].plot(x, y_3, color='green', label='tan(x)')

fig.delaxes(axes[1, 1])
handles, labels = [], []

for ax in fig.axes:
    h, l = ax.get_legend_handles_labels()
    handles.extend(h)
    labels.extend(l)

fig.legend(handles=handles, labels=labels, loc='lower right', bbox_to_anchor=(0.8, 0.2), title='Legend')
plt.tight_layout()
plt.show()