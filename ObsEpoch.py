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
    #观测值的标识符
    LLI=0
    Rssi=0
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
    def getLLI(self):
        return self.LLI
    def setLLI(self,lli):
        self.LLI=lli
    def getRssi(self):
        return self.Rssi
    def setRssi(self,rssi):
        self.Rssi=rssi
