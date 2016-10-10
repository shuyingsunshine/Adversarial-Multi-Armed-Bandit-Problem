import numpy as np
import copy


def categoryProbability(ita,gains):
    K = len(gains)
    res = []
    s = 0
    for i in range(K):
        p = np.exp(ita*gains[i])
        s = s+p
        res.append(p)
    for i in range(K):
        res[i] = res[i]*1.0/s
    return res

def hatCategoryProbability(ita,gamma,gains):
    res = categoryProbability(ita,gains)
    for i in range(len(res)):
        res[i] = (1-gamma)*res[i]+gamma*1.0/len(gains)
    return res

class PartialInformationGame:   ### the strategy you take to beat opponent if you know partial information
                                ### we know the upper bound of EG_max
    def __init__(self,ita,gamma, MAOmodel):
        self.myMAOmodel = MAOmodel
        self.K = MAOmodel.K
        self.gamma = gamma
        self.ita = ita
        self.T =0
        self.gains = []
        self.eachSum = [0]*self.K
        self.maxiSum = 0
        for i in range(self.K):
            self.gains.append(0)
        self.categProb = hatCategoryProbability(self.ita,self.gamma,self.gains)
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
        self.gains[j] = self.gains[j] + curgain*1.0/self.categProb[j]
        self.categProb = hatCategoryProbability(self.ita,self.gamma,self.gains)
        for i in range(self.K):
            self.eachSum[i] += temp[i]
            if self.eachSum[i] > self.maxiSum:
                self.maxiSum = self.eachSum[i]
        return j,curgain
        