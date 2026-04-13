from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_DOWN, K_UP, K_LEFT, K_RIGHT, C_GREY
import random

""" Global settings """
exp = design.Experiment(name="display_key", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

#Create all needed stimuli

STIM_SIZE = 50
TRIAL_TYPES = ["deterministic", "stochastic"]

circle_left = random.choice([True, False])
#Valeur position pour ce trial

position = "left" if circle_left else "right"
circle_position = (-200, 0) if circle_left else (200, 0)
square_position = (200,0) if circle_left else (-200, 0)
text = stimuli.TextLine("Find the circle. Left or right ?")
text.preload()
circle = stimuli.Circle(radius = STIM_SIZE, colour = C_GREY, position=circle_position)
circle.preload()
square = stimuli.Rectangle(size = (STIM_SIZE, STIM_SIZE), colour=C_GREY, position=square_position)
square.preload()
correct = stimuli.TextLine("CORRECT")
correct.preload()
incorrect =stimuli.TextLine("INCORRECT")
incorrect.preload()
exp.add_data_variable_names(["position", "answer", "rt"])
#Start the experiment
control.start(subject_id=1) 

text.present(clear=True, update = True)
exp.clock.wait(5000)

circle.present(clear = True, update=False)
square.present(clear=False, update=True)

key, rt = exp.keyboard.wait(keys = [K_LEFT, K_RIGHT])
answer = False
if (key == K_LEFT and circle_left) or (key == K_RIGHT and not circle_left):
    correct.present(clear=True, update = True)
    answer=True
else : 
    incorrect.present(clear=True, update=True)
exp.clock.wait(2000)
rt_text = stimuli.TextLine(f"You answered in {rt} ms")
rt_text.present(clear = True, update=True)

exp.data.add([position, answer, rt])
exp.keyboard.wait()

control.end()