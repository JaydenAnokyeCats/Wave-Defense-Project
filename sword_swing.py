from utility import load_image, load_images

class Swing_Animation:
    def __init__(self, frame):
        self.frame = frame
        self.frames = []
        self.frames_index = 0
        self.speed = 1
        # self.pos = (0,0)
        
        
    def load_frames(self, frame):
        self.frames.append(load_image('weapons/sword-sprites/sword-swing1.png'))
        self.frames.append(load_image('weapons/sword-sprites/sword-swing2.png'))
        self.frames.append(load_image('weapons/sword-sprites/sword-swing3.png'))
        self.frames.append(load_image('weapons/sword-sprites/sword-swing4.png'))
        pass
        