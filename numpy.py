import numpy as np
import matplotlib.pyplot as plt

# Parameters for the conical circle
r0 = 5  # Mean radius
delta_r = 2  # Amplitude of variation
n = 3  # Frequency of the variation

# Angle values
theta = np.linspace(0, 2 * np.pi, 500)

# Conic radius as a function of theta
r = r0 + delta_r * np.cos(n * theta)

# Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Entropy-like values (as a proxy for particle density)
entropy = r / max(r)  # Normalize entropy between 0 and 1

# Plot the conical circle with entropy values
fig, ax = plt.subplots(figsize=(8, 8))

# Circle with varying radius
scatter = ax.scatter(x, y, c=entropy, cmap='viridis', s=10, label='Entropy Distribution')

# Add color bar for entropy
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Entropy', fontsize=12)

# Add annotations for key regions
ax.text(0, r0 + delta_r + 0.5, "High Entropy Region", color='green', fontsize=10, ha='center')
ax.text(0, -(r0 + delta_r + 0.5), "Low Entropy Region", color='blue', fontsize=10, ha='center')

# Set aspect ratio and labels
ax.set_aspect('equal')
ax.set_title("Conical Circle with Entropy Distribution", fontsize=14)
ax.set_xlabel("X-axis", fontsize=12)
ax.set_ylabel("Y-axis", fontsize=12)
plt.grid(True)
plt.legend()
plt.show()
