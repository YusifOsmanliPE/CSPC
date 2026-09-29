import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid


#it is for reading datas from our file
data_freefall = pd.read_csv('freefall.csv')
t = data_freefall['time'].values
y = data_freefall['y'].values

v = np.gradient(y, t)   #derivative 
a = np.gradient(v, t)

mean_a = np.mean(a)
std_a = np.std(a)   #part 3 for showing noise 

print(f"Mean Acceleration: {mean_a:.2f} m/s^2")
print(f"Acceleration Standard Deviation (Noise Level): {std_a:.2f}")



v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# 1. Panel: Position
axs[0].plot(t, y, label="Position (Original)", color='blue')
axs[0].plot(t, y_recovered, label="Position (Recovered)", color='cyan', linestyle='--')
axs[0].set_ylabel("Position (m)")
axs[0].legend()
axs[0].grid(True)

# 2. Panel: Velocity
axs[1].plot(t, v, label="Velocity", color='orange')
axs[1].set_ylabel("Velocity (m/s)")
axs[1].legend()
axs[1].grid(True)

# 3. Panel: Acceleration
axs[2].plot(t, a, label="Acceleration (Noisy)", color='red', alpha=0.6)
axs[2].axhline(-9.81, color='black', linestyle='--', label="Constant Accel (-9.81)")
axs[2].set_ylabel("Acceleration (m/s^2)")
axs[2].set_xlabel("Time (s)")
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.savefig('motion.png') 
plt.show()