import expyriment
from expyriment import design, control, stimuli

expyriment.control.defaults.initialise_delay = 0 # No countdown
#expyriment.control.defaults.window_mode = True # Not full-screen
expyriment.control.defaults.fast_quit = True # No goodbye message

exp = design.Experiment(name="Two_Squares")
control.initialize(exp)

def launching_function(temp_gap=False, spatial_gap=False, speed=False):

    square_red = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0), position = (-400, 0))
    square_green = stimuli.Rectangle(size = (50, 50), colour = (0, 255, 0), position = (0, 0))

    square_red.present(clear = True, update = False)
    square_green.present(clear=False, update = True)

    temp_value = 115 if temp_gap else 0
    spatial_value = 200 if spatial_gap else 0
    speed_value = 3 if speed else 1
    for x in range(-400, -51-temp_value, 5): #move the red square to the left by 5 pixels, every 1ms until it reaches position of the green square
        square_red.position =(x, 0)
        square_red.present(clear = True, update = False)
        square_green.present(clear=False, update = True)
        exp.clock.wait(10*speed_value)
    exp.clock.wait(10)
    for x in range(50, 350, 5): #Move the green square to the right on the same distance and same speed as before
        square_green.position =(x, 0)
        square_red.present(clear = True, update = False)
        square_green.present(clear=False, update = True)
        exp.clock.wait(10)

control.start(subject_id=1)
launching_function()
launching_function(temp_gap=True)
launching_function(spatial_gap=True)
launching_function(speed=True)
control.end()