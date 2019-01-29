import numpy as np
import matplotlib.pyplot as plt

# Get x values of the sine wave
time = np.arange(0, 10, 0.1)

# Amplitude of the sine wave is the value of sin(time)
amplitude_sin = np.sin(time)

# Amplitude of the sine wave is the value of cos(time)
amplitude_cos = np.cos(time)

# Plot a sine wave of period and amplitude
plt.plot(time, amplitude_sin, color='b')

# Plot a cosine wave of period and amplitude
plt.plot(time, amplitude_cos, color='g')

# Give the title
plt.title('Sine Wave and Cosine Wave')

# Generate an x axis label
plt.xlabel('Time')

# Generate a y axis label
plt.ylabel('Amplitudes are sin(time) and cos(time).')

plt.grid(True)
plt.axhline(y=0, color='k')

# Show the graph
plt.show()
