from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")

control.set_develop_mode()
control.initialize(exp)

def draw(stims):
    for i, stim in enumerate(stims):
        #clear if it's the first stimuli, update if it is the last
        clear = True if i==0 else False
        update = True if i == (len(stims)-1) else False
        stim.present(clear=(clear), update=(update))

fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5)

control.start(subject_id=1)

draw([fixation, square])

# fixation.present(clear=True, update=False)
# exp.clock.wait(500)

# square.present(clear=False, update=True)

exp.keyboard.wait()

control.end()