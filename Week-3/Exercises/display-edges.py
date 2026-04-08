import expyriment
# Import the main modules of expyriment
from expyriment import design, control, stimuli

expyriment.control.defaults.initialise_delay = 0 # No countdown
# expyriment.control.defaults.window_mode = True # Not full-screen
expyriment.control.defaults.fast_quit = True # No goodbye message

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Square_Edges")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)
control.start(subject_id=1)

w, h = exp.screen.size # Obtain the screen size
square_size = int(w * 0.05)

positions = [(-w/2+ square_size, h/2-square_size), (-w/2+square_size,-h/2+square_size), (w/2-square_size, -h/2+square_size), (w/2-square_size, h/2-square_size) ]
for pos in positions :

    square = stimuli. Rectangle(size=(square_size, square_size), line_width=1, colour=(255, 0, 0), position=pos)
    square.present(clear=False, update=False)


# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()