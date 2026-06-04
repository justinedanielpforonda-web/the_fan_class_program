class Fan:

    #three constants named SLOW, MEDIUM and FAST.
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    
    #constructor
    def __init__(self, speed=SLOW, on=False, radius=5, color="blue"):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
    
    #getter
    def get__speed(self):
        return self.__speed
    
    #setter
    def set__speed(self, speed):
        self.__speed = speed