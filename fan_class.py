class Fan:

    #three constants named SLOW, MEDIUM and FAST.
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    
    #constructor
    def __init__(self, speed=SLOW, on=False, radius=5, color="blue"):
        self.speed = speed
        self.on = on
        self.radius = radius
        self.color = color