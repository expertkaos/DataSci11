# importing packages
import numpy as np
import matplotlib.pyplot as plt
 
a = [pow(10, i) for i in range(10)]

# create data
x = np.linspace(-2, 2, 100)
 
# making subplots
fig, ax = plt.subplots(3, 3, figsize=(10, 8))

# set data with subplots and plot
ax[0, 0].axhline(y = 0.5, color = 'red', linestyle = '--') 
ax[0, 1].plot(x, x, color='yellow', linewidth=3)
ax[0, 2].plot(x, x**2, color='green', linestyle = 'dotted')
ax[1, 0].plot(x, x**3, color='gray')
ax[1, 1].plot(x, 2**x, color='orange')
ax[1, 2].plot(x, np.log(x), color = 'blue')
ax[2, 0].plot(x, np.log(x)**2, color = 'black')
ax[2, 1].plot(x, np.log(x)*2, color = 'purple')
ax[2, 2].plot(x, np.sin(2 * x), color = 'aqua')

# Set titles for each subplot
titles = ['y = 0.5', 'y = x', 'y = x^2', 'y = x^3', 'y = 2^x', 'y = log(x)', 'y = log(x)^2', 'y = 2 log(x)', 'y = sin(2 * x)']
for i, title in enumerate(titles):
    ax[i // 3, i % 3].set_title(title)

# Customize grid properties
for ax in ax.flat:
    ax.grid(True, linestyle='-', linewidth=0.5)  # Thick grid lines

# Add a main title
font = {'family':'serif','weight':'bold','size':80}
fig.suptitle('Plotting with Matplotlib', fontdict = font)

plt.tight_layout()# Customize the overall layout and prevent overlapping titles

# Show the plot
plt.show()
