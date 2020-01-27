# coding=utf-8
import rnx.ReadObs as ReadObs
import rnx.ObsEpoch as ObsEpoch
class Check_sum:
    sv_nums=0#统计总共出现的卫星数
    interval=0#时间间隔
    first_time=""#观测开始时间
    end_time=""#观测结束时间
    sv_type_nums=[]#卫星prn——观测值类型——观测值出现次数---列表
    def __init__(self,name):
        self.filename=name
        self.chk()
    def get_sv_nums(self):
        return self.sv_nums
    #def set_sv_nums(self,n):
        #self.sv_nums=n
    def get_interval(self):
        return self.interval
    #def set_interval(self,n):
        #self.interval=n
    def get_first_time(self):
        return self.first_time
    #def set_first_time(self,n):
        #self.first_time=n
    def get_end_time(self):
        return self.end_time
    #def set_end_time(self,n):
        #self.end_time=n
    def chk(self):
        ##########获取卫星总数##############
        sv_list=[]#卫星列表
        readobs=ReadObs.ReadObs(self.filename)
        obsepochs=readobs.get_obsepochs()
        for i in range(len(obsepochs)):
            obsepoch=obsepochs[i]
            sv_list.append(obsepoch.getprn())
            if i==0:
                self.first_time=obsepoch.getobs_time()
            if i==len(obsepochs)-1:
                self.end_time=obsepoch.getobs_time()

        sv_list=list(set(sv_list))
        self.sv_nums=len(sv_list)
        self.interval=readobs.get_station_data().get_interval()
        for j in range(len(sv_list)):
            sv_type_num=SV_Type_num()
            L1_num=0
            L2_num=0
            C1_num=0
            C2_num=0
            P1_num=0
            P2_num=0
            S1_num=0
            S2_num=0
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
                    if obsepoch.getC1()!=None:
                        C1_num=C1_num+1
                    if obsepoch.getC2()!=None:
                        C2_num=C2_num+1
                    if obsepoch.getP1()!=None:
                        P1_num=P1_num+1
                    if obsepoch.getP2()!=None:
                        P2_num=P2_num+1
                    if obsepoch.getS1()!=None:
                        S1_num=S1_num+1
                    if obsepoch.getS2()!=None:
                        S2_num=S2_num+1
            sv_type_num.L1_num=L1_num
            sv_type_num.L2_num=L2_num
            sv_type_num.C1_num=C1_num
            sv_type_num.C2_num=C2_num
            sv_type_num.P1_num=P1_num
            sv_type_num.P2_num=P2_num
            sv_type_num.S1_num=S1_num
            sv_type_num.S2_num=S2_num
            self.sv_type_nums.append(sv_type_num)
            #print(L1_num,L2_num,C1_num,C2_num,P1_num,P2_num,S1_num,S2_num)


class SV_Type_num:#卫星prn——观测值类型——观测值出现次数
    sv_prn=""
    L1_num=0
    L2_num=0
    C1_num=0
    C2_num=0
    P1_num=0
    P2_num=0
    S1_num=0
    S2_num=0
    def get_sv_prn(self):
        return self.sv_prn
    def get_L1_num(self):
        return self.L1_num
    def get_L2_num(self):
        return self.L2_num
    def get_C1_num(self):
        return self.C1_num
    def get_C2_num(self):
        return self.C2_num
    def get_P1_num(self):
        return self.P1_num
    def get_P2_num(self):
        return self.P2_num
    def get_S1_num(self):
        return self.S1_num
    def get_S2_num(self):
        return self.S2_num











p=Check_sum("abmf0010.19o")
print(p.sv_nums)
print(p.get_interval())
print(p.first_time)
print(p.end_time)

print("vvvv")
