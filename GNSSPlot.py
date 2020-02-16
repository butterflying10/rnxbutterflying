# coding=utf-8
import rnx.ReadObs
import rnx.ReadNav
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class GNSSPlot:
    SNRvalues=list()
    Multipathvalues=list()
    __f1=1.57542e9  #以hz为单位,L1的频率
    __f2=1.22760e9  #以hz为单位,L2的频率
    __clight=299792458.0#光速
    __α=(__f1*__f1)/(__f2*__f2)
    def __init__(self,obsname):
        self.obsname=obsname
        reaadobs=rnx.ReadObs.ReadObs(self.obsname)
        self.__getSNRPlotData(reaadobs)
        self.__getMultipathPlotData(reaadobs)
        pass
    ###########不让外部访问这个方法,所以在前面加上__#################
    def __getMultipathPlotData(self,readobs):
        obsepochs=readobs.get_obsepochs()

        for obsepoch in obsepochs:

            Multipathvalue=MultipathValue()#找多路径效应的数据

            if (obsepoch.getP1()!=None and obsepoch.getL1()!=None and obsepoch.getL2()!=None) or  (obsepoch.getP2()!=None and obsepoch.getL1()!=None and obsepoch.getL2()!=None) or (obsepoch.getP1()!=None and obsepoch.getP2()!=None and obsepoch.getL1()!=None and obsepoch.getL2()!=None):

                strtime=obsepoch.getobs_time()
                hour=int(strtime.split()[3])
                minute=int(strtime.split()[4])
                second=int(strtime.split()[5])

                Multipathvalue.time=hour*60*60+minute*60+second

                Multipathvalue.prn=obsepoch.getprn()

                P1=obsepoch.getP1()
                P2=obsepoch.getP2()
                L1=obsepoch.getL1()
                L2=obsepoch.getL2()
                if P1!=None and P2==None:
                    Multipathvalue.MP1=P1+((1+self.__α)/(1-self.__α))*(self.__clight/self.__f1*L1)-(2/(1-self.__α))*(self.__clight/self.__f2*L2)
                if P2!=None and P1==None:
                    Multipathvalue.MP2=P2+(2*self.__α/(1-self.__α))*(self.__clight/self.__f1*L1)-((1+self.__α)/(1-self.__α))*(self.__clight/self.__f2*L2)
                if P1!=None and P2!=None:
                    Multipathvalue.MP1=P1+((1+self.__α)/(1-self.__α))*(self.__clight/self.__f1*L1)-(2/(1-self.__α))*(self.__clight/self.__f2*L2)
                    Multipathvalue.MP2=P2+(2*self.__α/(1-self.__α))*(self.__clight/self.__f1*L1)-((1+self.__α)/(1-self.__α))*(self.__clight/self.__f2*L2)

                #print(Multipathvalue.getprn(),Multipathvalue.gettime(),Multipathvalue.getMP1(),Multipathvalue.getMP2())
                self.Multipathvalues.append(Multipathvalue)

    def __getSNRPlotData(self,readobs):
        obsepochs=readobs.get_obsepochs()

        for obsepoch in obsepochs:

            SNRvalue=SNRValue()#找SNR的数据

            strtime=obsepoch.getobs_time()
            hour=int(strtime.split()[3])
            minute=int(strtime.split()[4])
            second=int(strtime.split()[5])
            SNRvalue.time=hour*60*60+minute*60+second
            SNRvalue.prn=obsepoch.getprn()
            SNRvalue.SNRL1=obsepoch.getS1()
            SNRvalue.SNRL2=obsepoch.getS2()
            SNRvalue.SNRL5=obsepoch.getS5()
            self.SNRvalues.append(SNRvalue)


    def getSNRPlot(self,obstype,prns):
        try:
            for prn in prns:
                values=[]
                times=[]
                alltimes=[]
                for snrvalue in self.SNRvalues:
                    alltimes.append(snrvalue.time)
                    if snrvalue.prn==prn:
                        times.append(snrvalue.time)
                        if obstype=="L1":
                            values.append(snrvalue.getSNRvalue()[2])
                        if obstype=="L2":
                            values.append(snrvalue.getSNRvalue()[3])
                        if obstype=="L5":
                            values.append(snrvalue.getSNRvalue()[4])
                #############相当重要###############
                alltimes=list(set(alltimes))#去重
                alltimes.sort()#重新排列
                allvalues=len(alltimes)*[None]
                ###################################
                try:
                    for i in range(len(alltimes)):
                        for j in range(len(times)):
                            if alltimes[i]==times[j]:

                                allvalues[i]=values[j]
                except:
                    print("00000/0")
                plt.xlabel(u"time/(s)")
                plt.ylabel(u"SNR-"+obstype+"(dBHz)")

                plt.plot(alltimes,allvalues,'r-', color='blue', alpha=0.8,linestyle='-',linewidth=0.5)
                plt.scatter(alltimes,allvalues,s=1.5,c='blue',marker='x')
                #s=pd.Series(allS1,index=alltimes)
                #s.plot()
                #plt.legend()
            plt.show()
        except:
            print("绘制信噪比图时出现错误")
    def getMultipathPlot(self,obstype,prns):
         try:
            for prn in prns:
                values=[] #存放每个卫星所对应的多路径效应值，没有空值None
                times=[]  #每个卫星多路径效应值不为None的时间
                alltimes=[]  #1-24小时，所有的时间
                for multipathvalue in self.Multipathvalues:
                    alltimes.append(multipathvalue.gettime()) #
                    if multipathvalue.getprn()==prn:
                        times.append(multipathvalue.gettime())  #
                        if obstype=="L1":
                            values.append(multipathvalue.getMP1())
                        if obstype=="L2":
                            values.append(multipathvalue.getMP2())
                        if obstype=="L5":
                            break             #L5载波没有对应的P5
                #############相当重要###############
                
                alltimes=list(set(alltimes))  #去重
                alltimes.sort()               #重新排列
                allvalues=len(alltimes)*[None]#存放每个卫星所对应的多路径效应值，有空值None,1-24时间内有些时间处为空
                ####################################
                try:
                    for i in range(len(alltimes)):
                        for j in range(len(times)):
                            if alltimes[i]==times[j]:
                                allvalues[i]=values[j]

                except:
                    print("此步将一个卫星 1-24时间和仅存在多路径效应的时间  列表叠加，便于画图")   #其实就是有些时间卫星不可见
                ######################################
                plt.xlabel(u"time/(s)")
                plt.ylabel(u"Multipath-"+obstype+"(m)")

                plt.plot(alltimes,allvalues,'r-', color='blue', alpha=0.8,linestyle='-',linewidth=0.5)
                plt.scatter(alltimes,allvalues,s=1.5,c='blue',marker='x')
            plt.show()
         except:
             print("绘制多路径效应图时发生错误")

class SNRValue:
    time=0#以秒为单位
    prn=""
    SNRL1=0#S1
    SNRL2=0#S2
    SNRL5=0#S5
    def getSNRvalue(self):
        return [self.time,self.prn,self.SNRL1,self.SNRL2,self.SNRL5]
class MultipathValue:
    time=0
    prn=""
    MP1=0
    MP2=0
    def gettime(self):
        return self.time
    def getprn(self):
        return self.prn
    def getMP1(self):
        return self.MP1
    def getMP2(self):
        return self.MP2

p=GNSSPlot(r"G:\360MoveData\Users\恒科电脑\Desktop\hj_study\buttfly\data\whc10010.20o")
#p.getMultipathPlot("L1",['G02'])
p.getMultipathPlot("L1",["G01","G02","G03","G05","G06","G07","G08","G09","G10","G11","G12","G13","G14","G15","G16","G17","G18","G19","G20","G21","G22","G23","G24","G25","G26","G27","G28","G29","G30","G31","G32"])