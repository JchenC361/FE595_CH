import numpy as np
import matplotlib.pyplot as plt

# Get x values of the sine wave
time = np.arange(0, 2*np.pi, 0.01)

# Amplitude of the sine wave is the value of sin(time)
amplitude_sin = np.sin(time)

# Amplitude of the sine wave is the value of cos(time)
amplitude_cos = np.cos(time)

# Amplitude of the sine wave is the value of cos(time)
amplitude_tan = np.tan(time)

# Limit the range of y axis between -1 to 1.
plt.ylim((-1, 1))

# Plot a sine wave of period and amplitude
plt.plot(time, amplitude_sin, color='b')

# Plot a cosine wave of period and amplitude
plt.plot(time, amplitude_cos, color='r')

# Plot a tangent wave of period and amplitude
plt.plot(time, amplitude_tan, color='y')

# Give the title
plt.title('Sine Wave, Cosine Wave and Tangent Wave.')

# Generate an x axis label
plt.xlabel('Time')

# Generate a y axis label
plt.ylabel('Amplitudes are sin(time), cos(time) and tan(time).')

plt.grid(True)
plt.axhline(y=0, color='k')

# Generate figure before plt.show in order to avoid outputting blank image.
fig = plt.gcf()

# Save the created image in your local directory.
fig.savefig('D:/SinCosTan.png')

# Show the graph
plt.show()
