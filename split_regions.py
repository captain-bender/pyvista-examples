


import pyvista as pv
import pymeshfix
import numpy as np

# Create an STL reader
reader = pv.STLReader('aero.stl')

# Read the mesh
surface = reader.read()

# Repair the mesh using pymeshfix
meshfix = pymeshfix.MeshFix(surface)
meshfix.repair()
repaired_mesh = meshfix.mesh

# Define bounding boxes for each part (adjust these values based on your model)
left_wing_bounds = [-10, 0, -5, 5, -1, 1]
right_wing_bounds = [0, 10, -5, 5, -1, 1]
fuselage_bounds = [-5, 5, -2, 2, -3, 3]

# Function to filter mesh based on bounds
def filter_mesh_by_bounds(mesh, bounds):
    x_min, x_max, y_min, y_max, z_min, z_max = bounds
    mask = (
        (mesh.points[:, 0] >= x_min) & (mesh.points[:, 0] <= x_max) &
        (mesh.points[:, 1] >= y_min) & (mesh.points[:, 1] <= y_max) &
        (mesh.points[:, 2] >= z_min) & (mesh.points[:, 2] <= z_max)
    )
    return mesh.extract_points(mask)

# Filter parts
left_wing = filter_mesh_by_bounds(repaired_mesh, left_wing_bounds)
right_wing = filter_mesh_by_bounds(repaired_mesh, right_wing_bounds)
fuselage = filter_mesh_by_bounds(repaired_mesh, fuselage_bounds)

# Voxelize each part separately with check_surface=False if needed
left_wing_voxels = pv.voxelize(left_wing, density=left_wing.length / 200, check_surface=False)
right_wing_voxels = pv.voxelize(right_wing, density=right_wing.length / 200, check_surface=False)
# fuselage_voxels = pv.voxelize(fuselage, density=fuselage.length / 200, check_surface=False)

# Visualization
p = pv.Plotter()
p.add_mesh(left_wing_voxels, color='green', opacity=0.5)
p.add_mesh(right_wing_voxels, color='blue', opacity=0.5)
# p.add_mesh(fuselage_voxels, color='red', opacity=0.5)
p.show()
