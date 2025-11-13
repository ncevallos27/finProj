import math

class Binomial():
    """
    Class that models that bionomial tree world
    """
    def __init__(self, steps, start, u, d, r, timeStep):
        """
        constructor that takes in standard variables 
        """
        self.steps = steps
        self.start = start
        self.u = u
        self.d = d
        self.r = r
        self.timeStep = timeStep
        self.upProb = self.calculateProb()
        self.currentTime = 0
        # TODO: implement dividend schedule

    def calculateProb(self):
        """
        calculates risk nuetral probabilites for going up
        """
        return float((math.exp(self.r*self.timeStep) - self.d)/(self.u-self.d))
    
    def __str__(self):
        return f"Current time: {self.currentTime*self.timeStep}\n Total Time: {self.timeStep*self.steps}"
    
    def getStep(self, step):
        """
        gets the prices at the current step, outputs an array of values starting for smallest to greatest
        """
        return [self.start*math.pow(self.u, i)*math.pow(self.d, step-i) for i in range(0, step+1)]