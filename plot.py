
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
csv_file = '/home/zhimbot/ros2_ws/src/unmanned_systems_ros2_pkg/unmanned_systems_ros2_pkg/log/Oct_06_15_32.csv'
data = pd.read_csv(csv_file)

# Extract columns
time = data['time'].to_numpy()
x_position = data['x-position'].to_numpy()
y_position = data['y-position'].to_numpy()
velocity = data['velocity'].to_numpy()
angular_velocity = data['angular velocity'].to_numpy()

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Data vs. Time')

# Subplot 1: X Position vs. Time
axs[0, 0].plot(time, x_position)
axs[0, 0].set_title('X Position vs. Time')
axs[0, 0].set_xlabel('Time')
axs[0, 0].set_ylabel('X Position')

# Subplot 2: Y Position vs. Time
axs[0, 1].plot(time, y_position)
axs[0, 1].set_title('Y Position vs. Time')
axs[0, 1].set_xlabel('Time')
axs[0, 1].set_ylabel('Y Position')

# Subplot 3: Velocity vs. Time
axs[1, 0].plot(time, velocity)
axs[1, 0].set_title('Velocity vs. Time')
axs[1, 0].set_xlabel('Time')
axs[1, 0].set_ylabel('Velocity')

# Subplot 4: Angular Velocity vs. Time
axs[1, 1].plot(time, angular_velocity)
axs[1, 1].set_title('Angular Velocity vs. Time')
axs[1, 1].set_xlabel('Time')
axs[1, 1].set_ylabel('Angular Velocity')

# Adjust layout for better visualization
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plots
plt.show()

