import pyvista as pv
import numpy as np

# Create an STL reader
reader = pv.STLReader('aero.stl')

# Read the mesh
surface = reader.read()

# Voxelize the surface
voxels = pv.voxelize(surface, density=surface.length / 200)

# Callback function to print picked point
def point_picked_callback(point):
    print(f"Picked point: {point}")

# Create a plotter with two subplots
plotter = pv.Plotter(shape=(1, 2))

# Visualization for the first subplot
plotter.subplot(0, 0)
plotter.add_mesh(voxels, color='blue', opacity=0.3)
plotter.add_text("View 1")
plotter.enable_point_picking(callback=point_picked_callback, show_message=True)

# Visualization for the second subplot
plotter.subplot(0, 1)
plotter.add_mesh(voxels, color='blue', opacity=0.3)
plotter.add_text("View 2")

# Set a different camera position for the second view
plotter.camera_position = [(0, 0, 27), (-3, 0, 0), (0, 1, 0)]

# Show the plotter with both views
plotter.show()
