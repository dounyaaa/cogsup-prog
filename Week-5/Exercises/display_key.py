from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_DOWN, K_UP, K_LEFT, K_RIGHT


""" Global settings """
exp = design.Experiment(name="display_key", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

control.start(subject_id=1)

text = stimuli.TextLine("Find the circle. Left or right ?")
text.present(clear=True, update = True)
exp.clock.wait(5000)

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

key, _ = exp.keyboard.wait(keys = [K_LEFT, K_RIGHT])


if key == K_LEFT : 
    correct.present()
if key == K_RIGHT : 
    incorrect.present()


exp.keyboard.wait()
control.end()