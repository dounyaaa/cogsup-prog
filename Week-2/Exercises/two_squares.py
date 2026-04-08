import expyriment
from expyriment import design, control, stimuli

exp = design.Experiment(name="Two_Squares")
control.initialize(exp)

square1 = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0), position = (-100, 0))
square2 = stimuli.Rectangle(size = (50, 50), colour = (0, 0, 255), position = (100, 0))
control.start(subject_id=1)
square1.present(clear = True, update = False)
square2.present(clear=False, update = True)

exp.keyboard.wait()
control.end()