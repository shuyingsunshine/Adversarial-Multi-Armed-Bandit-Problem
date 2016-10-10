import copy
import numpy as np

def betaParameters(numPlayed,lamda,totalMean): ##herelamda is just some
    ##parameter
    alphas = []
    betas = []
    K = len(numPlayed)
    s = 0
    for i in range(K):
        a = np.exp(-numPlayed[i]*lamda)
        s = s+a
        alphas.append(a)
    for i in range(K):
        b = (s - totalMean*alphas[i])*1.0/totalMean
        betas.append(b)
    return alphas,betas

def meansEachMachine(scheme):
    res = []
    for i in range(scheme.K):
        res.append(scheme.alphas[i]/(scheme.alphas[i]+scheme.betas[i])+scheme.bers[i])
    return res

class betaScheme:
    def __init__(self,K,totalMean = 1):
        self.K = K
        self.T = 0
        self.totalMean = totalMean
        self.numPlayed = []
        for i in range(self.K):
            self.numPlayed.append(0)
        self.alphas,self.betas = betaParameters(self.numPlayed,0,self.totalMean)
        self.bers = []
        for i in range(self.K):
            self.bers.append((i+1)*1.0/2/K)
    def action(self,j):
        self.numPlayed[j] = self.numPlayed[j]+1
        self.T = self.T+1
        self.alphas,self.betas = betaParameters(self.numPlayed,self.K*1.0/self.T,self.totalMean)
    def getSample(self):
        res = []
        for i in range(self.K):
            temp = np.random.beta(self.alphas[i],self.betas[i])
            if np.random.rand() < self.bers[i]:
                temp += 1
            res.append(temp)
        return res
    def jthSample(self,j):
        temp = np.random.beta(self.alphas[j],self.betas[j])
        if np.random.rand() < self.bers[j]:
            temp += 1
        return temp
    def means(self):
        return meansEachMachine(self)

    
class MultiArmOpponent: ### the opponent modifies the probability of win if the number of times playing for some
    ### machine increases, does not depend on number of rounds so far (i.e., self.T)
    def __init__(self,scheme):
        self.scheme = scheme
        self.K = scheme.K
        self.T = 0
    def getSample(self):
        return self.scheme.getSample()
    def jthSample(self,j):
        return self.scheme.jthSample(j)
    def action(self, j):
        self.scheme.action(j)
        self.T = self.T+1
        


