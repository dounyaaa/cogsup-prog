import expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY

expyriment.control.defaults.initialise_delay = 0 # No countdown
# expyriment.control.defaults.window_mode = True # Not full-screen
expyriment.control.defaults.fast_quit = True # No goodbye message

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Square_Edges", background_colour=C_GREY)
control.initialize(exp)

def kanizsa_rectangle(aspect_ratio=3, rect_scale=2, circle_scale=12):

    w, _ = exp.screen.size # Obtain the screen size
    width = w // rect_scale
    height = width // aspect_ratio

    
    positions = [
        (-width//2, -height//2),
        (width//2, -height//2),
        (-width//2, height//2),
        (width//2, height//2)
    ]

    radius = int(min(width, height) /circle_scale)
    i=0
    exp.screen.clear()
    for pos in positions:
        i=i+1
        if i in [1, 2]:
            colour = (255, 255, 255)
        else : 
            colour = (0, 0, 0)
        circle = stimuli.Circle(radius=radius, colour=colour, position=pos)
        circle.present(clear=False, update=False)
        rectangle = stimuli.Rectangle(size=(width,height), colour=C_GREY)
        rectangle.present(clear=False, update=False)
    exp.screen.update()

control.start(subject_id=1)
kanizsa_rectangle(circle_scale=4)
exp.keyboard.wait()
# End the current session and quit expyriment
control.end()