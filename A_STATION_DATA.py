# coding=utf-8
class A_Station_Data:
    #观测间隔
    interval=0
    #测站近似坐标
    X_Pos=0
    Y_Pos=0
    Z_Pos=0
    #观测值类型
    isL1=False
    isL2=False
    isC1=False
    isC2=False
    isP1=False
    isP2=False
    isS1=False
    isS2=False
    #构造函数,好像不需要构造函数
    #def __init__(self,x_pos,y_pos,z_pos,isl1,isl2,isc1,isc2,isp1,isp2,iss1,iss2):
    #    self
    def __init__(self):
        print("A_STATION_DATA对象已创建")
    def getX_Pos(self):
        return self.X_Pos
    def getY_Pos(self):
        return self.Y_Pos
    def getZ_Pos(self):
        return self.Z_Pos
    def setX_Pos(self,x_pos):
        self.X_Pos=x_pos
    def setY_Pos(self,y_pos):
        self.Y_Pos=y_pos
    def setZ_Pos(self,z_pos):
        self.Z_Pos=z_pos
    def is_L1(self):
        return self.isL1
    def setL1(self,l1):
        self.isL1=l1
    def is_L2(self):
        return self.isL2
    def setL2(self,l2):
        self.isL2=l2
    def is_C1(self):
        return self.isC1
    def setC1(self,c1):
        self.isC1=c1
    def is_C2(self):
        return self.isC2
    def setC2(self,c2):
        self.isC2=c2
    def is_P1(self):
        return self.isP1
    def setP1(self,p1):
        self.isP1=p1
    def is_P2(self):
        return self.isP2
    def setP2(self,p2):
        self.isP2=p2
    def is_S1(self):
        return self.isS1
    def setS1(self,s1):
        self.isS1=s1
    def is_S2(self):
        return self.isS2
    def setS2(self,s2):
        self.isS2=s2
    def get_interval(self):
        return self.interval
    def set_interval(self,n):
        self.interval=n
