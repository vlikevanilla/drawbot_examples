TOTAL_FRAMES = 360
OVAL_WIDTH = 50
OVAL_HEIGHT = 50

def new_canvas():
    # for each loop create a new path
    newPage(500, 500)
    # set a random fill color
    fill(0, 0, 0)
    # draw a rect with the size of the page
    rect(0, 0, width(), height())


def color_oval(x_pos, y_pos, color):
    fill(color, color, color)
    oval(x_pos, y_pos, OVAL_WIDTH, OVAL_HEIGHT)

def draw_column(col_x_pos, col_y_pos, column_length):
    # setup the named range
    x_range = range(col_x_pos, col_x_pos+column_length)
    # start color of gray (0.5)
    start_color = 0.1
    # end color of white (1.0)
    end_color = 1.0
    # figure out how much to increment the fill color by determining how many time we
    # will be iterating in the for loop using the LENgth of the range
    color_increment = (end_color - start_color) / len(x_range)

    # move the oval from starting x_pos incrementing by each element in the range
    for x_pos in x_range:
        start_color += color_increment
        color_oval(x_pos, col_y_pos, start_color)

for frame_id in range(TOTAL_FRAMES):
    new_canvas()
    frameDuration(1/30)
    
    x_start = 225
    y_start = 225
    column_length = 150
    rotate1 = -1 * frame_id * 2
    rotate(rotate1, center=(250,250))
    draw_column(x_start, y_start, column_length)

    with savedState():
        column2_length = 90
        rotation2 = -1 * frame_id
        rotate(rotation2, center=(250,250))
        draw_column(x_start, y_start, column2_length)
        
    with savedState():
        column3_length = 120
        rotation3 = -1 * frame_id * 3
        rotate(rotation3, center=(250,250))
        draw_column(x_start, y_start, column3_length)

    
saveImage("~/tmp/drawbot/rotating_columns.gif")
