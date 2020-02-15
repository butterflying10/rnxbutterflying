# coding=utf-8
import rnx.A_STATION_DATA as A_STATION_DATA
import rnx.ObsEpoch as ObsEpoch
import math
class ReadObs:
    station_data=A_STATION_DATA.A_Station_Data()
    obsepochs=list()
    def __init__(self,name):
        self.filename=name
        self.readobsfile()
    def readobsfile(self):
        ############读取头文件数据##########
        obstype_list=()
        with open(self.filename,'r+',encoding="utf-8") as f :
            strline=f.readline().rstrip('\n')
            while strline!="":
                try:
                    if strline[60:]=="APPROX POSITION XYZ":#测站近似坐标
                        strpos=strline[0:60].split()
                        self.station_data.setX_Pos(eval(strpos[0]))
                        self.station_data.setY_Pos(eval(strpos[1]))
                        self.station_data.setZ_Pos(eval(strpos[2]))
                        strline=f.readline().rstrip('\n')
                    elif strline[60:]=="INTERVAL":#观测值类型
                        strinterval=strline[0:60].strip()
                        self.station_data.interval=eval(strinterval)
                        strline=f.readline().rstrip('\n')
                    elif strline[60:]=="MARKER NAME":#点号
                        strmarker=strline[0:60].strip()
                        self.station_data.markername=strmarker
                        strline=f.readline().rstrip('\n')
                    elif strline[60:]=="REC # / TYPE / VERS":#接收机类型
                        strrec=strline[0:20].strip()+"-"+strline[20:40].strip()
                        self.station_data.rctype=strrec
                        strline=f.readline().rstrip('\n')
                    elif strline[60:]=="ANT # / TYPE":#天线
                        strant=strline[20:40].strip()
                        self.station_data.antype=strant
                        strline=f.readline().rstrip('\n')
                    elif strline[60:]=="# / TYPES OF OBSERV":#观测值类型
                        strtype=strline[0:60].split()
                        typenumber=eval(strtype[0])
                        for t in range(math.ceil(typenumber/9)-1):
                            strline=f.readline()
                            strtype_add=strline[0:60].split()
                            for type_add in strtype_add:
                                strtype.append(type_add)
                        obstype_list=strtype[1:]
                        for i in range(1,len(strtype)):
                            if strtype[i]=="L1":
                                self.station_data.setL1(True)
                            if strtype[i]=="L2":
                                self.station_data.setL2(True)
                            if strtype[i]=="L5":
                                self.station_data.setL5(True)
                            if strtype[i]=="C1":
                                self.station_data.setC1(True)
                            if strtype[i]=="C2":
                                self.station_data.setC2(True)
                            if strtype[i]=="C5":
                                self.station_data.setC5(True)
                            if strtype[i]=="P1":
                                self.station_data.setP1(True)
                            if strtype[i]=="P2":
                                self.station_data.setP2(True)
                            if strtype[i]=="S1":
                                self.station_data.setS1(True)
                            if strtype[i]=="S2":
                                self.station_data.setS2(True)
                            if strtype[i]=="S5":
                                self.station_data.setS5(True)
                            if strtype[i]=="D1":
                                self.station_data.setD1(True)
                            if strtype[i]=="D2":
                                self.station_data.setD2(True)
                            if strtype[i]=="D5":
                                self.station_data.setD5(True)
                        strline=f.readline().rstrip('\n')
                    elif strline[60:]=="END OF HEADER":#头文件结束标识符
                        break
                    else:
                        strline=f.readline().rstrip('\n')
                except:
                    print(strline+"此处出现异常")
                    strline=f.readline().rstrip('\n')
                    #print("异常")

        ############读取观测历元数据################
            strline=f.readline().rstrip('\n')#去掉右侧的换行符
            while strline!="":
                try:
                    if 'G' in strline or 'R' in strline or 'E' in strline :#判断是否在某一观测历元的开头
                        #获取年月日时分秒
                        year=eval(strline[1:3])
                        mouth=eval(strline[4:6])
                        day=eval(strline[7:9])
                        hour=eval(strline[10:12])
                        minute=eval(strline[13:15])
                        second=eval(strline[16:18])
                        #将时间的书写格式调整规范
                        strtime="20"+str(year)+" "+str(mouth)+" "+str(day)+" "+str(hour)+" "+str(minute)+" "+str(second)
                        #print(strtime)
                        #该历元下的卫星数
                        sv_sum=eval(strline[30:32])
                        #print(sv_sum)
                        sv_prn_str=strline[32:]
                        #超过12颗卫星那么继续下一行读取
                        if sv_sum>12:
                            strline=f.readline().rstrip('\n')
                            str_sv_prn_add=strline.strip()
                            sv_prn_str=sv_prn_str+str_sv_prn_add
                        if sv_sum>24:
                            strline=f.readline().rstrip('\n')
                            str_sv_prn_add=strline.strip()
                            sv_prn_str=sv_prn_str+str_sv_prn_add
                        if sv_sum>36:#我觉得36已经很多了，在一个时间点接收机能接收到的卫星
                            strline=f.readline().rstrip('\n')
                            str_sv_prn_add=strline.strip()
                            sv_prn_str=sv_prn_str+str_sv_prn_add
                        if sv_sum>48:#我觉得48已经很多了，在一个时间点接收机能接收到的卫星
                            strline=f.readline().rstrip('\n')
                            str_sv_prn_add=strline.strip()
                            sv_prn_str=sv_prn_str+str_sv_prn_add
                        ################获取此历元下的观测值数据###############
                        for n in range(sv_sum):
                            obsepoch=ObsEpoch.ObsEpoch()#单历元单卫星数据存放
                            obsepoch.setobs_time(strtime)
                            sv_prn=sv_prn_str[n*3:n*3+3]
                            obsepoch.setprn(sv_prn)
                            obstype_num=len(obstype_list)#观测值类型个数
                            str_epoch=""
                            for m in range(math.ceil(obstype_num/5)):#向上取整，即8/5=2
                                ssline=f.readline().rstrip('\n')
                                if len(ssline)<80:
                                    ssline=ssline+" "*(80-len(ssline))#每一行都把它变成80个字符
                                str_epoch=str_epoch+ssline
                            for mm in range(obstype_num):
                                str_value=str_epoch[mm*16:mm*16+14]
                                if str_value=="              ":
                                    value=None
                                else:
                                    value=eval(str_epoch[mm*16:mm*16+14])#获取观测值
                                typename=obstype_list[mm]
                                if typename=="L1":
                                    obsepoch.setL1(value)
                                if typename=="L2":
                                    obsepoch.setL2(value)
                                if typename=="L5":
                                    obsepoch.setL5(value)
                                if typename=="C1":
                                    obsepoch.setC1(value)
                                if typename=="C2":
                                    obsepoch.setC2(value)
                                if typename=="C5":
                                    obsepoch.setC5(value)
                                if typename=="P1":
                                    obsepoch.setP1(value)
                                if typename=="P2":
                                    obsepoch.setP2(value)
                                if typename=="S1":
                                    obsepoch.setS1(value)
                                if typename=="S2":
                                    obsepoch.setS2(value)
                                if typename=="S5":
                                    obsepoch.setS5(value)
                                if typename=="D1":
                                    obsepoch.setD1(value)
                                if typename=="D2":
                                    obsepoch.setD2(value)
                                if typename=="D5":
                                    obsepoch.setD5(value)
                            self.obsepochs.append(obsepoch)
                        strline=f.readline().rstrip('\n')
                    else:
                        strline=f.readline().rstrip('\n')
                except:
                    print(strline+"此处出现异常")
                    strline=f.readline().rstrip('\n')#出现异常跳过这行就行了
    def get_station_data(self):
        return self.station_data
    def get_obsepochs(self):
        return self.obsepochs
'''c=ReadObs("abmf0010.19o")
print(c.get_station_data().get_rctype())
pp=c.get_obsepochs()
print(len(pp))
print("cccc")'''













