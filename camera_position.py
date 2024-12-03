
import pyvista as pv
import vtk

# Create a plotter
plotter = pv.Plotter()

# Add your mesh (example using a sphere)
mesh = pv.Sphere()
plotter.add_mesh(mesh, color='blue', opacity=0.5)

# Function to update camera position text
def update_camera_position():
    pos = plotter.camera_position
    text = f"Camera Position:\nPos: {pos[0]}\nFocal Point: {pos[1]}\nView Up: {pos[2]}"
    plotter.add_text(text, position='upper_left', name='camera_position_text')

# Initial camera position text
update_camera_position()

# Callback for when the camera moves
def on_camera_move(*args):
    plotter.remove_actor('camera_position_text')
    update_camera_position()

# Add an observer for camera movement
plotter.iren.add_observer(vtk.vtkCommand.EndInteractionEvent, on_camera_move)

# Show the plotter
plotter.show()
