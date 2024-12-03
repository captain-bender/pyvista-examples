
import pyvista as pv
import numpy as np

# Function to add a z-offset
def add_z_offset(points, z_offset):
    offset_points = points.copy()
    offset_points[:, 2] += z_offset
    return offset_points

# Create an STL reader
reader = pv.STLReader('aero.stl')

# Read the mesh
surface = reader.read()

# Voxelize the surface
voxels = pv.voxelize(surface, density=surface.length / 200)

# Extract the surface of the voxelized mesh
surface_mesh = voxels.extract_surface()

# Get unique (x, y) coordinates and find the max z for each
unique_xy = np.unique(surface_mesh.points[:, :2], axis=0)

# Find maximum z for each unique (x, y)
max_z_points = []
for xy in unique_xy:
    mask = np.all(surface_mesh.points[:, :2] == xy, axis=1)
    max_z = surface_mesh.points[mask][:, 2].max()
    max_z_points.append([xy[0], xy[1], max_z])

max_z_points = np.array(max_z_points)

# Create a grid from these points (attached to the surface)
surface_grid_attached = pv.PolyData(max_z_points)

# Define your desired z-offset
z_offset = 5  # Adjust this value as needed

# Apply the z-offset to move points upwards
offset_max_z_points = add_z_offset(max_z_points, z_offset)

# Create a grid from these points with offset
surface_grid_with_offset = pv.PolyData(offset_max_z_points)

# Visualization
p = pv.Plotter()
p.add_mesh(voxels, color='blue', opacity=0.3)
p.add_mesh(surface_grid_attached, color='yellow', point_size=10)  # Attached grid in yellow
p.add_mesh(surface_grid_with_offset, color='red', point_size=10)  # Offset grid in red
p.show()
