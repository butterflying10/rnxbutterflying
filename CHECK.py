# coding=utf-8
import rnx.ReadObs as ReadObs
class Check_sum:
    markername=""#点号
    rctype=""#接收机类型
    antype=""#天线类型
    sv_nums=0#统计总共出现的卫星数
    sv_list=[]#观测文件中出现的卫星列表
    sv_G=[]
    sv_R=[]
    sv_E=[]
    sv_C=[]
    interval=0#时间间隔
    first_time=""#观测开始时间
    end_time=""#观测结束时间
    sv_type_nums=list()#卫星prn——观测值类型——观测值出现次数---列表
    obsepochs_num=0#一共有多少个观测历元,实际观测历元数
    obsepochs_num_theo=2880#理论观测历元数
    #fullobsepochs_num=0#完整的观测历元
    data_utilization=0#数据利用率
    #导航文件的输入
    navfileG=""#gps导航文件
    navfileR=""#glonass导航文件

    def __init__(self,name):
        self.filename=name
        readobs=ReadObs.ReadObs(self.filename)
        self.chk(readobs)
        self.getSVGREC()
        self.output()


    def set_navfile(self,name1,name2):
        self.navfileG=name1
        self.navfileR=name2
    def get_sv_nums(self):
        return self.sv_nums
    def get_interval(self):
        return self.interval
    def get_first_time(self):
        return self.first_time
    def get_end_time(self):
        return self.end_time
    def get_sv_type_nums(self):
        return self.sv_type_nums
    def get_sv_list(self):
        return self.sv_list
    def get_markername(self):
        return self.markername
    def get_rctype(self):
        return self.rctype
    def get_antype(self):
        return self.antype
    def get_obsepochnum(self):
        return self.obsepochs_num
    
    def chk(self,readobs):
        sv_list=[]#卫星列表
        times=[]
        station_data=readobs.get_station_data()
        obsepochs=readobs.get_obsepochs()

        try:
            self.markername=station_data.get_markername()
            self.antype=station_data.get_antype()
            self.rctype=station_data.get_rctype()
            ##########获取卫星总数##############
            ###获取观测历元个数###############
            for i in range(len(obsepochs)):
                obsepoch=obsepochs[i]
                sv_list.append(obsepoch.getprn())
                times.append(obsepoch.getobs_time())
                #########获取开始时间和结束时间##########
                if i==0:
                    self.first_time=obsepoch.getobs_time()
                if i==len(obsepochs)-1:
                    self.end_time=obsepoch.getobs_time()
                ########################################
            times=list(set(times))#把观测时间去重，不就是有多少个观测历元嘛
            #times.sort()
            #print(len(times))
            self.obsepochs_num=len(times)
            sv_list=list(set(sv_list))
            sv_list.sort()
            self.data_utilization=self.obsepochs_num/self.obsepochs_num_theo
            self.sv_list=sv_list
            self.sv_nums=len(sv_list)
            self.interval=readobs.get_station_data().get_interval()
        except:
            print("获取卫星总数、历元个数、观测历元数出现问题")

        try:
            for j in range(len(sv_list)):
                sv_type_num=SV_Type_num()
                L1_num=0
                L2_num=0
                L5_num=0
                C1_num=0
                C2_num=0
                C5_num=0
                P1_num=0
                P2_num=0
                S1_num=0
                S2_num=0
                S5_num=0
                D1_num=0
                D2_num=0
                D5_num=0
                #print(sv_list[j])
                sv_type_num.sv_prn=sv_list[j]
                for jj in range(len(obsepochs)):
                    obsepoch=obsepochs[jj]
                    sv_prn=obsepoch.getprn()
                    if sv_prn==sv_list[j]:
                        if obsepoch.getL1()!=None:
                            L1_num=L1_num+1
                        if obsepoch.getL2()!=None:
                            L2_num=L2_num+1
                        if obsepoch.getL5()!=None:
                            L5_num=L5_num+1
                        if obsepoch.getC1()!=None:
                            C1_num=C1_num+1
                        if obsepoch.getC2()!=None:
                            C2_num=C2_num+1
                        if obsepoch.getC5()!=None:
                            C5_num=C5_num+1
                        if obsepoch.getP1()!=None:
                            P1_num=P1_num+1
                        if obsepoch.getP2()!=None:
                            P2_num=P2_num+1
                        if obsepoch.getS1()!=None:
                            S1_num=S1_num+1
                        if obsepoch.getS2()!=None:
                            S2_num=S2_num+1
                        if obsepoch.getS5()!=None:
                            S5_num=S5_num+1
                        if obsepoch.getD1()!=None:
                            D1_num=D1_num+1
                        if obsepoch.getD2()!=None:
                            D2_num=D2_num+1
                        if obsepoch.getD5()!=None:
                            D5_num=D5_num+1
                sv_type_num.L1_num=L1_num
                sv_type_num.L2_num=L2_num
                sv_type_num.L5_num=L5_num
                sv_type_num.C1_num=C1_num
                sv_type_num.C2_num=C2_num
                sv_type_num.C5_num=C5_num
                sv_type_num.P1_num=P1_num
                sv_type_num.P2_num=P2_num
                sv_type_num.S1_num=S1_num
                sv_type_num.S2_num=S2_num
                sv_type_num.S5_num=S5_num
                sv_type_num.D1_num=D1_num
                sv_type_num.D2_num=D2_num
                sv_type_num.D5_num=D5_num
                self.sv_type_nums.append(sv_type_num)
                #print(L1_num,L2_num,L5_num,C1_num,C2_num,C5_num,P1_num,P2_num,S1_num,S2_num,S5_num,D1_num,D2_num,D5_num)
        except:
            print("检测出现异常")
    ###########获取各系统卫星号##########
    def getSVGREC(self):
        svG=[]
        svR=[]
        svE=[]
        svC=[]
        try:
            for sv in self.sv_list:
                if sv[0:1]=="G":
                    svG.append(sv)
                if sv[0:1]=="R":
                    svR.append(sv)
                if sv[0:1]=="E":
                    svE.append(sv)
                if sv[0:1]=="B":
                    svC.append(sv)
            #进行排序
            svG.sort()
            svR.sort()
            svE.sort()
            svC.sort()
        except:
            print("获取各系统卫星号出现异常")
        self.sv_G=svG
        self.sv_R=svR
        self.sv_E=svE
        self.sv_C=svC
    def getdata_utilization(self):
        return self.data_utilization
    def output(self):
        print("###########基本信息#############")
        print("测站点名称:"+self.get_markername())
        print("接收机类型:"+self.get_rctype())
        print("天线类型:"+self.get_antype())
        print("观测开始时间:"+self.get_first_time())
        print("观测结束时间:"+self.get_end_time())
        print("观测时间间隔:"+str(self.get_interval()))
        print("观测历元总数:"+str(self.get_obsepochnum()))
        print("理论观测历元数:"+str(self.obsepochs_num_theo))
        print("数据完整率:"+str(self.getdata_utilization()))
        ###########卫星prn——观测值类型——观测值出现次数#########
        print("###########卫星号——观测值类型——观测值出现次数#########")
        print("卫星号  L1  L2  L5  C1  C2  C5  P1  P2  S1  S2  S5  D1  D2  D5")
        l=self.get_sv_type_nums()
        for sv_type_num in l :
            print(sv_type_num.get_sv_prn(),end="  ")
            print(sv_type_num.get_L1_num(),end="  ")
            print(sv_type_num.get_L2_num(),end="  ")
            print(sv_type_num.get_L5_num(),end="  ")
            print(sv_type_num.get_C1_num(),end="  ")
            print(sv_type_num.get_C2_num(),end="  ")
            print(sv_type_num.get_C5_num(),end="  ")
            print(sv_type_num.get_P1_num(),end="  ")
            print(sv_type_num.get_P2_num(),end="  ")
            print(sv_type_num.get_S1_num(),end="  ")
            print(sv_type_num.get_S2_num(),end="  ")
            print(sv_type_num.get_S5_num(),end="  ")
            print(sv_type_num.get_D1_num(),end="  ")
            print(sv_type_num.get_D2_num(),end="  ")
            print(sv_type_num.get_D5_num(),end="  ")
            print("\n")
        ###############各系统卫星号#################
        print("卫星总数:"+str(self.get_sv_nums()))
        print("#############各系统卫星号##############")

        print("GPS:",end=" ")#输出不换行
        for g in self.sv_G:
            print(g,end=" ")
        print('\n')
        print("GALILEO:",end=" ")#输出不换行
        for g in self.sv_E:
            print(g,end=" ")
        print('\n')
        print("GLONASS:",end=" ")#输出不换行
        for g in self.sv_R:
            print(g,end=" ")
        print('\n')
        print("BeiDou:",end=" ")#输出不换行
        for g in self.sv_C:
            print(g,end=" ")
        print('\n')

class SV_Type_num:#卫星prn——观测值类型——观测值出现次数
    sv_prn=""
    L1_num=0
    L2_num=0
    L5_num=0
    C1_num=0
    C2_num=0
    C5_num=0
    P1_num=0
    P2_num=0
    S1_num=0
    S2_num=0
    S5_num=0
    D1_num=0
    D2_num=0
    D5_num=0
    def get_sv_prn(self):
        return self.sv_prn
    def set_sv_prn(self,n):
        self.sv_prn=n
    def get_L1_num(self):
        return self.L1_num
    def get_L2_num(self):
        return self.L2_num
    def get_L5_num(self):
        return self.L5_num
    def get_C1_num(self):
        return self.C1_num
    def get_C2_num(self):
        return self.C2_num
    def get_C5_num(self):
        return self.C5_num
    def get_P1_num(self):
        return self.P1_num
    def get_P2_num(self):
        return self.P2_num
    def get_S1_num(self):
        return self.S1_num
    def get_S2_num(self):
        return self.S2_num
    def get_S5_num(self):
        return self.S5_num
    def get_D1_num(self):
        return self.D1_num
    def get_D2_num(self):
        return self.D2_num
    def get_D5_num(self):
        return self.D5_num











p=Check_sum("abmf0010.19o")









