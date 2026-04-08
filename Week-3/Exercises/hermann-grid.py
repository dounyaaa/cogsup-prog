import expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_BLACK, C_WHITE

expyriment.control.defaults.initialise_delay = 0 # No countdown
expyriment.control.defaults.window_mode = True # Not full-screen
expyriment.control.defaults.fast_quit = True # No goodbye message

exp = design.Experiment(name="Hermann_Grid", background_colour=C_BLACK)

control.initialize(exp)
control.start(subject_id=1)

def hermann_grid(square_size, spacing, rows, cols, square_color, background_color):

    exp.screen.colour=background_color
    dist_centers = square_size + spacing

    for i in range(rows):
        for j in range(cols):

            x = (j - (cols )/2) * dist_centers
            y = (i - (rows)/2) * dist_centers

            square = stimuli.Rectangle(
                size=(square_size, square_size),
                position=(int(x), int(y)),
                colour=square_color
            )
            if i == 0 and j == 0:
                square.present(clear=True, update=False)
            else:
                square.present(clear=False, update=False)

    exp.screen.update()


hermann_grid(
    square_size=80,
    spacing=20,
    rows=2,
    cols=2,
    square_color=C_BLACK,
    background_color=C_WHITE
)

exp.keyboard.wait()
control.end()

#Increasing the spacing or decreasing the number of square reduce the illusion.