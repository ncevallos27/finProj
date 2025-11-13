class Strategy():
    def __init__(self, env, steps=252):
        self.arrStrat = []
        self.count = 0
        self.steps = steps
        self.paths = None
        self.env = env

    def setPaths(self, paths):
        self.paths = paths

    def addTo(self, object):
        self.arrStrat.append(object)
        self.count = len(self.arrStrat)

    def run(self):
        for strat in self.arrStrat:
            strat.run(self.steps, self)

        return self.count
    
    def getFinal(self):
        pass