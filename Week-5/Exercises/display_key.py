from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_DOWN, K_UP, K_LEFT, K_RIGHT, C_GREY
import random

""" Global settings """
exp = design.Experiment(name="display_key", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

# exp.add_data_variable_names(["subject", "position", "accuracy", "rt"])

text = stimuli.TextLine("Find the circle. Left or right ?")
text.present(clear=True, update = True)
exp.clock.wait(2500)

circle = stimuli.Circle(radius = 50, position=(-200, 0))
circle.preload()
square = stimuli.Rectangle(size = (50, 50), position = (200, 0))
square.preload()

circle.present(clear = True, update=False)
square.present(clear=False, update=True)
correct = stimuli.TextLine("CORRECT")
correct.preload
incorrect =stimuli.TextLine("INCORRECT")
incorrect.preload

key, rt = exp.keyboard.wait(keys = [K_LEFT, K_RIGHT])
if key == K_LEFT :
    correct.present(clear = True, update = True)
if key == K_RIGHT : 
    incorrect.present(clear = True, update= True)
exp.clock.wait(2000)
rt = stimuli.TextLine(f"You answered in {rt} ms")
rt.present(clear = True, update=True)
# exp.data.add([])
exp.keyboard.wait()
control.end()