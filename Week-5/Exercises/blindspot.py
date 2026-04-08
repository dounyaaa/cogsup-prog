# 1. The position and size of the circle must be adjustable (position should be adjusted via keyboard arrows, 
# and size via number keys: 1 = smaller, 2 = larger)
# 2. Add instructions at the beginning of each trial: `stimuli.TextScreen` (which eye to cover, where to fixate,
# how to adjust the circle, what to do when they’re done—press space to move on)
# 3. Modify run_trial so it takes a side as input (left or right) and runs the procedure for the left or 
# right eye of the subject


from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_DOWN, K_UP, K_LEFT, K_RIGHT


""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

""" Experiment """
def run_trial():
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0])
    fixation.preload()

    radius = 75
    circle = make_circle(radius)

    fixation.present(True, False)
    circle.present(False, True)
    key, _ = exp.keyboard.wait(keys = [K_DOWN, K_UP, K_RIGHT, K_LEFT]) 
    match key : 
        case 'K_DOWN' : 
            circle.radius+10
        case _ : 
            pass    
    exp.keyboard.wait()

control.start(subject_id=1)

run_trial()
    
control.end()