import pyvista as pv

# Create a plotter
plotter = pv.Plotter()

# Add your mesh (example using a sphere)
mesh = pv.Sphere()
plotter.add_mesh(mesh, color='blue', opacity=0.5)

# Callback function to print picked point
def point_picked_callback(point):
    print(f"Picked point: {point}")

# Enable point picking with a callback
plotter.enable_point_picking(callback=point_picked_callback, show_message=True)

# Show the plotter
plotter.show()