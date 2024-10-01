import time, board, busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt

# Setup I2C and initialize MLX90640
i2c = busio.I2C(board.SCL, board.SDA, frequency=400000)
mlx = adafruit_mlx90640.MLX90640(i2c)
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

# Setup array for storing temperatures (24x32 grid)
frame = np.zeros((24*32,))

# Read the frame
while True:
    try:
        mlx.getFrame(frame)
        break
    except ValueError:
        continue  # retry reading if there's an error

# Convert 1D array to a 2D array (24x32) for visualization
thermal_data = np.reshape(frame, (24, 32))

# Print out average temperature (optional)
print('Average MLX90640 Temperature: {0:2.1f}C ({1:2.1f}F)'.\
      format(np.mean(frame), (((9.0/5.0)*np.mean(frame))+32.0)))

# Plot and save the thermal image
plt.imshow(thermal_data, cmap='inferno')  
plt.colorbar(label="Temperature (°C)")   
plt.title("MLX90640 Thermal Image")     

# Define the path where the image will be saved
save_path = "thermal_image_test.png"

# Save the image
plt.savefig(save_path)


print(f"Thermal image saved to {save_path}")
