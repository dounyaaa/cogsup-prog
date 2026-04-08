from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)

def draw(stims):
    for i, stim in enumerate(stims):
        #clear if it's the first stimuli, update if it is the last
        clear = True if i==0 else False
        update = True if i == (len(stims)-1) else False
        stim.present(clear=(clear), update=(update))

def load(stims):
    for stim in stims :
        stim.preload()

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")
# load([fixation, text])
# fixation.present()
draw([fixation])

exp.clock.wait(1000)

t0 = exp.clock.time
text.present()
dt = exp.clock.time - t0
print(dt)
t1 = exp.clock.time

fix_duration = (t1 - t0)/1000

exp.clock.wait(1000)

units = "second" if fix_duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.clock.wait(2000)

control.end()