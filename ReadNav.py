# coding=utf-8
class GPS_Nav_Data:
    sv_prn=""#卫星号
    time=""#时间
    sv_clock_bias=0#卫星钟的偏差，s
    sv_clock_dirft=0#卫星钟的漂移,s/s
    sv_clock_dirft_rate=0#卫星钟的漂移速度，s/s^2
    IODE=0#数据、星历发布时间
    Crs=0#轨道半径的正弦调和项改正的振幅m
    Delta_n=0#由精密星历计算得到的卫星平均角速度和按给定参数计算所得的平均角速度之差(rad/s)
    M0=0#按参考历元计算的平近点角（rad）
    Cuc=0#纬度幅角的余弦调和项改正的振幅(rad)
    e=0#轨道偏心率
    Cus=0#纬度幅角的正弦调和项改正的振幅(rad)
    sqrt_A=0#轨道长半径的平方根
    TOE=0#星历表参考历元(s)(gps周内的秒数)
    Cic=0#轨道倾角的余弦调和项改正的振幅(rad)
    Cis=0#轨道倾角的正弦调和项改正的振幅(rad)
    Crc=0#轨道半径的正弦调和项改正的振幅m
    Ω=[]#按参考历元TOE计算的升交点赤径  ,OMEGA
    i0=[]#按参考历元TOE计算的轨道倾角
    ω=0#近地点角距
    Ω_DOT=[]#升交点赤经变化率(rad/s)
    I_DOT=[]#轨道倾角变化率(rad/s)
    def get_sv_prn(self):
        return  self.sv_prn
    def get_time(self):
        return  self.time
    def get_sv_clock_bias(self):
        return  self.sv_clock_bias
    def get_sv_clock_dirft(self):
        return self.sv_clock_dirft
    def get_sv_clock_dirft_rate(self):
        return self.sv_clock_dirft_rate
    def get_IODE(self):
        return self.IODE
    def get_Crs(self):
        return self.Crs
    def get_Delta_n(self):
        return self.Delta_n
    def get_M0(self):
        return self.M0
    def get_Cuc(self):
        return self.Cuc
    def get_e(self):
        return self.e
    def get_Cus(self):
        return self.Cus
    def get_sqrt_A(self):
        return self.sqrt_A
    def get_TOE(self):
        return self.TOE
    def get_Cic(self):
        return self.Cic
    def get_Cis(self):
        return self.Cis
    def get_Crc(self):
        return self.Crc
    def get_Ω(self):
        return self.Ω
    def get_i0(self):
        return self.i0
    def get_ω(self):
        return self.ω
    def get_Ω_DOT(self):
        return self.Ω_DOT
    def get_I_DOT(self):
        return self.I_DOT
class GLONASS_Nav_Data:
    sv_prn=""#卫星号
    time=""#时间
    sv_clock_bias=0#卫星钟的偏差，s
    sv_relative_frequency_bias=0#卫星相对频率偏差
    tk=0#电文帧时间
    sv_posX=0#km
    XDOT=0#km/s
    X_acceleration=0#km/s^2
    health=0#0表明卫星正常
    sv_posY=0#km
    YDOT=0#km/s
    Y_acceleration=0#km/s^2
    frequency_num=0#卫星的频率数(1-24)
    sv_posZ=0#km
    ZDOT=0#km/s
    Z_acceleration=0#km/s^2
    age=0#卫星运行年限信息（天）
    def get_sv_prn(self):
        return  self.sv_prn
    def get_time(self):
        return  self.time
    def get_sv_clock_bias(self):
        return  self.sv_clock_bias
    def get_sv_relative_frequency_bias(self):
        return  self.sv_relative_frequency_bias
    def get_tk(self):
        return self.tk
    def get_sv_posX(self):
        return self.sv_posX
    def get_XDOT(self):
        return self.XDOT
    def get_X_acceleration(self):
        return self.X_acceleration
    def get_health(self):
        return self.health
    def get_sv_posY(self):
        return self.sv_posY
    def get_YDOT(self):
        return self.YDOT
    def get_Y_acceleration(self):
        return self.Y_acceleration
    def get_frequency_num(self):
        return self.frequency_num
    def get_sv_posZ(self):
        return self.sv_posZ
    def get_ZDOT(self):
        return self.ZDOT
    def get_Z_acceleration(self):
        return self.Z_acceleration
    def get_age(self):
        return self.age
class ReadNav:
    Nav_data_list=[]#导航文件信息存放列表
    sv_system=""
    def __init__(self,name):
        self.filename=name
        self.readnavfile()
    def readnavfile(self):
        with open(self.filename,'r+',encoding="utf-8") as f :
            ############头文件#####################
            strline=f.readline().rstrip('\n')
            while strline!="":
                if strline[60:]=="RINEX VERSION / TYPE":
                    if "GPS" in strline[0:40]:
                        self.sv_system="G"
                    if "GLONASS" in strline[0:40]:
                        self.sv_system="R"
                    strline=f.readline().rstrip('\n')
                elif strline[60:]=="END OF HEADER":
                    break
                else:
                    strline=f.readline().rstrip('\n')
            ##############导航数据文件################
            strline=f.readline().rstrip('\n')
            nav_data=None
            while strline!="":
                if strline[0:2].strip()!="":#判断是否是以卫星号开头,是
                    if self.sv_system=="G":
                        nav_data=GPS_Nav_Data()
                        sv_digtal=strline[0:2].strip()
                        if len(sv_digtal)==1:
                            nav_data.sv_prn=self.sv_system+"0"+sv_digtal
                        if len(sv_digtal)==2:
                            nav_data.sv_prn=self.sv_system+sv_digtal
                        #获取年月日时分秒
                        year=eval(strline[3:5])
                        mouth=eval(strline[6:8])
                        day=eval(strline[9:11])
                        hour=eval(strline[12:14])
                        minute=eval(strline[15:17])
                        second=eval(strline[18:20])
                        #将时间的书写格式调整规范
                        strtime="20"+str(year)+" "+str(mouth)+" "+str(day)+" "+str(hour)+" "+str(minute)+" "+str(second)
                        nav_data.time=strtime
                        #############gps导航文件数据#################
                        nav_data.sv_clock_bias=eval(strline[22:41].replace('D','e'))
                        nav_data.sv_clock_dirft=eval(strline[41:60].replace('D','e'))
                        nav_data.sv_clock_dirft_rate=eval(strline[60:].replace('D','e'))
                        strline=f.readline().rstrip('\n')#读下一行,1
                        nav_data.IODE=eval(strline[3:22].replace('D','e'))
                        nav_data.Crs=eval(strline[22:41].replace('D','e'))
                        nav_data.Delta_n=eval(strline[41:60].replace('D','e'))
                        nav_data.M0=eval(strline[60:].replace('D','e'))
                        strline=f.readline().rstrip('\n')#读下一行,2
                        nav_data.Cuc=eval(strline[3:22].replace('D','e'))
                        nav_data.e=eval(strline[22:41].replace('D','e'))
                        nav_data.Cus=eval(strline[41:60].replace('D','e'))
                        nav_data.sqrt_A=eval(strline[60:].replace('D','e'))
                        strline=f.readline().rstrip('\n')#读下一行,3
                        nav_data.TOE=eval(strline[3:22].replace('D','e'))
                        nav_data.Cic=eval(strline[22:41].replace('D','e'))
                        nav_data.Ω=eval(strline[41:60].replace('D','e'))
                        nav_data.Cis=eval(strline[60:].replace('D','e'))
                        strline=f.readline().rstrip('\n')#读下一行,4
                        nav_data.i0=eval(strline[3:22].replace('D','e'))
                        nav_data.Crc=eval(strline[22:41].replace('D','e'))
                        nav_data.ω=eval(strline[41:60].replace('D','e'))
                        nav_data.Ω_DOT=eval(strline[60:].replace('D','e'))
                        strline=f.readline().rstrip('\n')#读下一行,5
                        nav_data.I_DOT=eval(strline[3:22].replace('D','e'))
                        strline=f.readline().rstrip('\n')#读下一行,6
                    if self.sv_system=="R":
                        nav_data=GLONASS_Nav_Data()
                        sv_digtal=strline[0:2].strip()
                        if len(sv_digtal)==1:
                            nav_data.sv_prn=self.sv_system+"0"+sv_digtal
                        if len(sv_digtal)==2:
                            nav_data.sv_prn=self.sv_system+sv_digtal
                        #获取年月日时分秒
                        year=eval(strline[3:5])
                        mouth=eval(strline[6:8])
                        day=eval(strline[9:11])
                        hour=eval(strline[12:14])
                        minute=eval(strline[15:17])
                        second=eval(strline[18:20])
                        #将时间的书写格式调整规范
                        strtime="20"+str(year)+" "+str(mouth)+" "+str(day)+" "+str(hour)+" "+str(minute)+" "+str(second)
                        nav_data.time=strtime
                        #################glonass导航文件数据###############
                        nav_data.sv_clock_bias=eval(strline[22:41].replace('D','e'))
                        nav_data.sv_relative_frequency_bias=eval(strline[41:60].replace('D','e'))
                        nav_data.tk=eval(strline[60:].replace('D','e'))
                        strline=f.readline().strip('\n')#读下一行，1
                        nav_data.sv_posX=eval(strline[3:22].replace('D','e'))
                        nav_data.XDOT=eval(strline[22:41].replace('D','e'))
                        nav_data.X_acceleration=eval(strline[41:60].replace('D','e'))
                        nav_data.health=eval(strline[60:].replace('D','e'))
                        strline=f.readline().strip('\n')#读下一行，2
                        nav_data.sv_posY=eval(strline[3:22].replace('D','e'))
                        nav_data.YDOT=eval(strline[22:41].replace('D','e'))
                        nav_data.Y_acceleration=eval(strline[41:60].replace('D','e'))
                        nav_data.frequency_num=eval(strline[60:].replace('D','e'))
                        strline=f.readline().strip('\n')#读下一行，3
                        nav_data.sv_posZ=eval(strline[3:22].replace('D','e'))
                        nav_data.ZDOT=eval(strline[22:41].replace('D','e'))
                        nav_data.Z_acceleration=eval(strline[41:60].replace('D','e'))
                        nav_data.age=eval(strline[60:].replace('D','e'))
                    print(nav_data.get_time(),nav_data.get_sv_prn(),nav_data.get_sv_clock_bias(),nav_data.get_age())
                    self.Nav_data_list.append(nav_data)
                    strline=f.readline().rstrip('\n')
                else:#否
                    strline=f.readline().rstrip('\n')
p=ReadNav("abmf0010.19g")
print()
