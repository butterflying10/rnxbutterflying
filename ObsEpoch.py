# coding=utf-8
class ObsEpoch:
    obs_time=""#观测历元
    prn=""#卫星的prn
    L1=0#L1波段载波相位观测值
    L2=0#L2波段载波相位观测值
    C1=0#L1波段下的C/A码所测伪距
    C2=0#L2波段下的C/A码所测伪距
    P1=0#L1波段下的P码所测伪距
    P2=0#L2波段下的P码所测伪距
    S1=0#L1波段下的SNR
    S2=0#L1波段下的SNR
    D1=0
    D2=0
    L5=0
    C5=0
    D5=0
    S5=0

    #观测值的标识符
    LLI=0
    Rssi=0
    def __init__(self):
        #print("ObsEpoch对象已创建")
        pass
    def getobs_time(self):
        return self.obs_time
    def setobs_time(self,t):
        self.obs_time=t
    def getprn(self):
        return self.prn
    def setprn(self,str):
        self.prn=str
    def getL1(self):
        return self.L1
    def setL1(self,l1):
        self.L1=l1
    def getL2(self):
        return self.L2
    def setL2(self,l2):
        self.L2=l2
    def getC1(self):
        return self.C1
    def setC1(self,c1):
        self.C1=c1
    def getC2(self):
        return self.C2
    def setC2(self,c2):
        self.C2=c2
    def getP1(self):
        return self.P1
    def setP1(self,p1):
        self.P1=p1
    def getP2(self):
        return self.P2
    def setP2(self,p2):
        self.P2=p2
    def getS1(self):
        return self.S1
    def setS1(self,s1):
        self.S1=s1
    def getS2(self):
        return self.S2
    def setS2(self,s2):
        self.S2=s2
    def getD1(self):
        return self.D1
    def setD1(self,d1):
        self.D1=d1
    def getD2(self):
        return self.D2
    def setD2(self,d2):
        self.D2=d2
    def getL5(self):
        return self.L5
    def setL5(self,l5):
        self.L5=l5
    def getC5(self):
        return self.C5
    def setC5(self,c5):
        self.C5=c5
    def getD5(self):
        return self.D5
    def setD5(self,d5):
        self.D5=d5
    def getS5(self):
        return self.S5
    def setS5(self,s5):
        self.S5=s5
    def getLLI(self):
        return self.LLI
    def setLLI(self,lli):
        self.LLI=lli
    def getRssi(self):
        return self.Rssi
    def setRssi(self,rssi):
        self.Rssi=rssi
