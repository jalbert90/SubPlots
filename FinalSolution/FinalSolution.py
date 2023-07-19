import numpy as np
import matplotlib.pyplot as plt

# Create an array of 50 evenly spaced numbers between 0 and 2pi, inclusive
x = np.linspace(0, 2 * np.pi, 50)

# Create the corresponding function values
y_1 = np.sin(x)
y_2 = np.cos(x)
y_3 = np.tan(x)

# Create a figure with 4 subplots in a 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot the function y-values against their corresponding x-values, label, and color
axes[0, 0].plot(x, y_1, label='sin(x)')
axes[0, 1].plot(x, y_2, color='red', label='cos(x)')
axes[1, 0].plot(x, y_3, color='green', label='tan(x)')

# Delete the subplot in the lower right-hand corner
fig.delaxes(axes[1, 1])

# Create empty lists to store the handles and labels for each of the subplots
handles, labels = [], []

# Iterate through the remaining 3 subplots and extract their handles and labels
for ax in fig.axes:
    h, l = ax.get_legend_handles_labels()
    handles.extend(h)
    labels.extend(l)

# Create a single legend for all 3 of the subplots in the position of the now-deleted fourth subplot
fig.legend(handles=handles, labels=labels, loc='lower right', bbox_to_anchor=(0.8, 0.2), title='Legend')

# Draw the figure
plt.show()
