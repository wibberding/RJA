"""
Example "Arcade" library code.

This example shows the drawing primitives and how they are used.
It does not assume the programmer knows how to define functions or classes
yet.

API documentation for the draw commands can be found here:
http://arcade.academy/quick_index.html#id1

A video explaining this example can be found here:
https://vimeo.com/167158158

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.drawing_primitives
"""

# Import the Arcade library. If this fails, then try following the instructions
# for how to install arcade:
# http://arcade.academy/installation.html
import arcade
import os


###### My Functions ######
def hello():
	print('hello')

def draw_bird(x, y):
    """
    Draw a bird using a couple arcs.
    """
    arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(x + 40, y, 20, 20, arcade.color.BLACK, 90, 180)


def draw_pine_tree(x, y):
    """
    This function draws a pine tree at the specified location.
    """
    # Draw the triangle on top of the trunk
    arcade.draw_triangle_filled(x + 40, y,
                                x, y - 100,
                                x + 80, y - 100,
                                arcade.color.DARK_GREEN)

    # Draw the trunk
    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                      arcade.color.DARK_BROWN)


# Set the working directory (where we expect to find files) to the same
# directory this .py file is in. You can leave this out of your own
# code, but it is needed to easily run the examples using "python -m"
# as mentioned at the top of this program.
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(600, 600, "Drawing Primitives Example")

# Set the background color to white
# For a list of named colors see
# http://arcade.academy/arcade.color.html
# Colors can also be specified in (red, green, blue) format and
# (red, green, blue, alpha) format.
arcade.set_background_color(arcade.color.AERO_BLUE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# Green grass
arcade.draw_rectangle_filled(300, 150, 600, 300, (0,255,0))

#Draw mountains
point_list = ((0, 300),
              (100, 450),
              (180, 300),
              (250, 420),
              (390, 300),
              (450, 450),
              (520, 350),
              (600, 300))
arcade.draw_polygon_filled(point_list, arcade.color.SPANISH_VIOLET)

# Draw a cloud
arcade.draw_circle_filled(420, 525, 25, arcade.color.WHITE)
arcade.draw_circle_filled(480, 515, 25, arcade.color.WHITE)
arcade.draw_circle_filled(450, 525, 25, arcade.color.WHITE)

# Finish the render.
# Nothing will be drawn without this.
# Must happen after all draw commands
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
