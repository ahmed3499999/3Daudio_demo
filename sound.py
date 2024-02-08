import synthizer

ctx = ''
generator = ''
source = ''

def init():
    global ctx, generator, source
    synthizer.initialize()
    ctx = synthizer.Context()
    ctx.default_panner_strategy.value = synthizer.PannerStrategy.HRTF

    generator = synthizer.BufferGenerator(ctx)

    source = synthizer.Source3D(ctx)
    source.add_generator(generator)
    source.pause()
    print("Initialized synthizer")
    

def load_sound(filename):
    generator.buffer.value = synthizer.Buffer.from_file(filename)
    
def play():
    source.play()

def pause():
    source.pause()

def updateSourcePos(x, y):
    source.position.value = (x/25, -y/25, 0)
    print(x,y)

def deinit():
    synthizer.shutdown()