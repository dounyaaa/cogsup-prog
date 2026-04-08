from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)
fixation = stimuli.FixCross()
text = stimuli.TextLine('Fixation removed')
t0 = exp.clock.time
fixation.present()
dt = exp.clock.time - t0
print(dt)
#The first time, the computer load everything like the libraries
# --> use the function prior to the important part of the experiment or use a preload function
exp.clock.wait(1000 - dt)
t0 = exp.clock.time
text.present()
dt = exp.clock.time - t0
print(dt)

exp.clock.wait(1000 - dt)

control.end()