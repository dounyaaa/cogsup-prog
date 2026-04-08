import expyriment
from expyriment import design, control, stimuli



# Display a fixation cross inside a blue square of length 50 for half a second then removes the fixation cross and displays only the blue square until a key is pressed
exp = design.Experiment(name="Square")
control.initialize(exp)
fixation = stimuli.FixCross()
square = stimuli.Rectangle(size = (50, 50), colour = (0, 0, 255))
control.start(subject_id=1)
square.present(clear = True, update = False)
fixation.present(clear=False, update = True)
exp.clock.wait(500)
square.present(clear = True, update = True)

exp.keyboard.wait()
control.end()