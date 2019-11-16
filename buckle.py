import numpy as np
import math
import matplotlib.pyplot as plt

class BucklingBundle():
    def __init__(self,force=1765000,E=250000000000,
                 diameter_range=[10,40],k=1,
                 granularity=1):

        self.force = force
        self.E = E
        self.k = k
        self.granularity = granularity
        self.diameter_range = np.arange(diameter_range[0],diameter_range[1],self.granularity)

        self._inertiaMoment()
        self._lengths()

    def _inertiaMoment(self):
        self.inertia_moment = (math.pi * (self.diameter_range/2000)**4)/4

    def _lengths(self):
        self.lengths = ((((math.pi**2) * self.E * self.inertia_moment) / (self.force * self.k) )**(1/2) * 1000)

    def generatePlot(self,figname='buckling',title= 'Buckling lenght vs diameter',
                     yaxis='Maximum length',xaxis='Diameter'):
        fig = plt.figure()

        plt.plot(self.diameter_range,self.lengths)
        plt.grid()

        plt.title(title)
        plt.ylabel(yaxis)
        plt.xlabel(xaxis)

        fig.savefig(figname)


B=BucklingBundle()
B.generatePlot()