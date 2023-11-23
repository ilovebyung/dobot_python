import numpy as np
from scipy.interpolate import interp2d

# Define source and target points
source_points = np.array([[60, 150], [270, 150], [480, 150], [62, 360], [270, 360], [480, 355]])
target_points = np.array([[343, 97], [340, 0], [342, -100], [244, 97], [244, 0], [244, -100]])

# Extract x and y coordinates from source and target points
x_source, y_source = source_points[:, 0], source_points[:, 1]
x_target, y_target = target_points[:, 0], target_points[:, 1]

# Create the interpolation function
x_f = interp2d(x_source, y_source, x_target, kind='linear')
y_f = interp2d(x_source, y_source, y_target, kind='linear')

# Define the mapping function using the interpolation functions
def map_points(x, y):
    return x_f(x, y)[0], y_f(x, y)[0]

# Test the mapping function with some example points
test_point = [150, 150]
mapped_point = map_points(*test_point)

print(f"Original point: {test_point}")
print(f"Mapped point: {mapped_point}")
