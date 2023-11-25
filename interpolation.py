import numpy as np
from scipy.interpolate import NearestNDInterpolator

# Define the source and target points
source_points = np.array([
    [60, 150],
    [270, 150],
    [480, 150],
    [62, 360],
    [270, 360],
    [480, 355]
])

target_points = np.array([
    [343, 97],
    [340, 0],
    [342, -100],
    [244, 97],
    [244, 0],
    [244, -100]
])

# Create the NearestNDInterpolator object
interpolator = NearestNDInterpolator(source_points, target_points)

# Define the query points
query_points = np.array([
    [62, 360]
])

# Interpolate the query points
interpolated_values = interpolator(query_points)

print(interpolated_values)
