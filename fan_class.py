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
    
    #---------------
    # getter methods
    #---------------

    def get__speed(self):
        return self.__speed
    
    def get__on(self):
        return self.__on

    def get__radius(self):
        return self.__radius
    
    def get__color(self):
        return self.__color
    
    #---------------
    # setter Methods
    #---------------
    def set__speed(self, speed):
        self.__speed = speed
    
    def set__on(self, on):
        self.__on = on
    
    def set__radius(self, radius):
        self.__radius = radius

    def set__color(self, color):
        self.__color = color

fan1 = Fan(speed = Fan.FAST, on = True, radius = 10, color = "yellow")