import copy
import numpy as np





class RandomGame:   ### the strategy you take to beat opponent if you know partial information
                                ### we know the upper bound of EG_max
    def __init__(self,MAOmodel):
        self.myMAOmodel = MAOmodel
        self.K = MAOmodel.K
        self.T =0
        self.eachSum = [0]*self.K
        self.maxiSum = 0
        self.categProb = []
        for i in range(self.K):
            self.categProb.append(1.0/self.K)
        self.acturalGain = 0
    def play(self):
        j = np.random.choice(self.K,1,p=self.categProb)[0]
        #print "j is " + str(j)
        temp = self.myMAOmodel.scheme.getSample()
        curgain = temp[j]
        self.acturalGain = self.acturalGain + curgain
        #print "actural gain is "+str(curgain)
        self.T = self.T+1
        self.myMAOmodel.action(j)
        for i in range(self.K):
            self.eachSum[i] += temp[i]
            if self.eachSum[i] > self.maxiSum:
                self.maxiSum = self.eachSum[i]
        return j,curgain
        

