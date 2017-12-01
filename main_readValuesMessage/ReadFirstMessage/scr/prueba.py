# -*- coding: utf-8 -*-
ID                         = 2
TIME_STAMP                 = 0
CAN_CHANNEL                = 1
INIT_MSSG='0000000000000000000000000000000000000000000000000000000000000000'
INIT_CAN_CHANNEL           = 0
INIT_TIME_STAMP            = 0000.0000


class SRR_obj_FL:
    
    def dynPropf(self, mssg):
        mssg = mssg[::-1]
        return mssg[0:3][::-1]
    
    def confidencef(self,mssg):
        mssg = mssg[::-1]
        return mssg[4:6][::-1]
    
    def statusf(self,mssg):
        mssg = mssg[::-1]
        return mssg[6:8]
    
    def classObjf(self,mssg):
        mssg = mssg[::-1]
        return mssg[8:11][::-1]
    
    def xf(self,mssg):
        mssg = mssg[::-1]
        MSB = mssg[16:24]
        MSB = MSB[::-1]
        LSB = mssg[24:32]
        LSB = LSB[::-1]
        x_val = MSB + LSB
       # x_val =(int(x_val,2)/2)*.004
       #Tener en cuenta la division entre enteros
        return x_val
        
    def yf(self,mssg):
        mssg = mssg[::-1]
        MSB = mssg[32:40]
        MSB = MSB[::-1]
        LSB = mssg[40:48]
        LSB = LSB[::-1]
        y_val = MSB + LSB
       # y_val =(int(y_val,2)/2)*.004
        return y_val
    
    def IDf(self,mssg):
        mssg = mssg[::-1]
        MSB = mssg[48:56]
        MSB = MSB[::-1]
        LSB = mssg[56:63]
        LSB = LSB[::-1]
        ID_val = MSB + LSB
        return ID_val
    
    def __init__(self):
        self.time_stamp         = INIT_TIME_STAMP
        self.CAN_channel        = INIT_CAN_CHANNEL
        self.mssg               = INIT_MSSG
        self.dynProp            = 0
        self.confidence         = 0
        self.status             = 0
        self.classObj           = 0
        self.x                  = 0
        self.y                  = 0
        self.ID                 = 0
        
def modificax():
    object_FL.x='1111111'
    return;

object_FL = SRR_obj_FL()
modificax()