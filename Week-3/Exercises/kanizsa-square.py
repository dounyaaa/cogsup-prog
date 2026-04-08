import expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY

expyriment.control.defaults.initialise_delay = 0 # No countdown
# expyriment.control.defaults.window_mode = True # Not full-screen
expyriment.control.defaults.fast_quit = True # No goodbye message

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Square_Edges", background_colour=C_GREY)

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

w, h = exp.screen.size # Obtain the screen size
s = int(w * 0.25)

# k_square = stimuli.Rectangle(size=(s, s), position=(0, 0))
# k_square.present(clear=True, update=True)

positions = [
    (-s/2, -s/2),
    (s/2, -s/2),
    (-s/2, +s/2),
    (s/2, s/2)
]
i=0

control.start(subject_id=1)
exp.screen.clear()
for pos in positions:
    i=i+1
    if i in [1, 2]:
        colour = (255, 255, 255)
    else : 
        colour = (0, 0, 0)
    circle = stimuli.Circle(radius=int(s/4), colour=colour, position=pos)
    circle.present(clear=False, update=False)
square = stimuli.Rectangle(size=(s,s), colour=C_GREY)
square.present(clear=False, update=False)

exp.screen.update()

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()