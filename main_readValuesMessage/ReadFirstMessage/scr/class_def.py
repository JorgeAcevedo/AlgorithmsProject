# -*- coding: utf-8 -*-

'''
*============================================================================*/
                              CLASS DEFINITION
*============================================================================*/
'''
'''==============================SRR_obj===================================='''
class SRR_obj_FL:
    
    def dynProp_f(self,mssg):
        mssg = mssg[::-1]
        return mssg[0:3][::-1]
    
    def confidence_f(self,mssg):
        mssg = mssg[::-1]
        return mssg[4:6][::-1]
    
    def status_f(self,mssg):
        mssg = mssg[::-1]
        return mssg[6:8]
    
    def classObj_f(self,mssg):
        mssg = mssg[::-1]
        return mssg[8:11][::-1]
    
    def x_f(self,mssg):
        mssg = mssg[::-1]
        MSB = mssg[16:24]
        MSB = MSB[::-1]
        LSB = mssg[24:32]
        LSB = LSB[::-1]
        val = MSB + LSB
       # x_val =(int(x_val,2)/2)*.004
       #Tener en cuenta la division entre enteros
        return val
        
    def y_f(self,mssg):
        mssg = mssg[::-1]
        MSB = mssg[32:40]
        MSB = MSB[::-1]
        LSB = mssg[40:48]
        LSB = LSB[::-1]
        val = MSB + LSB
       # y_val =(int(y_val,2)/2)*.004
        return val
    
    def ID_f(self,mssg):
        mssg = mssg[::-1]
        MSB = mssg[48:56]
        MSB = MSB[::-1]
        LSB = mssg[56:63]
        LSB = LSB[::-1]
        val = MSB + LSB
        return val
    
    def __init__(self):
        self.time_stamp         = 0
        self.CAN_channel        = 0
        self.dynProp            = 0
        self.confidence         = 0
        self.status             = 0
        self.classObj           = 0
        self.x                  = 0
        self.y                  = 0
        self.ID                 = 0
        
class SRR_obj_FR:
    
    def dynProp_f(self,mssg):
        mssg = mssg[::-1]
        return mssg[0:3][::-1]
    
    def confidence_f(self,mssg):
        mssg = mssg[::-1]
        return mssg[4:6][::-1]
    
    def status_f(self,mssg):
        mssg = mssg[::-1]
        return mssg[6:8]
    
    def classObj_f(self,mssg):
        mssg = mssg[::-1]
        return mssg[8:11][::-1]
    
    def x_f(self,mssg):
        mssg = mssg[::-1]
        MSB = mssg[16:24]
        MSB = MSB[::-1]
        LSB = mssg[24:32]
        LSB = LSB[::-1]
        val = MSB + LSB
       # x_val =(int(x_val,2)/2)*.004
       #Tener en cuenta la division entre enteros
        return val
        
    def y_f(self,mssg):
        mssg = mssg[::-1]
        MSB = mssg[32:40]
        MSB = MSB[::-1]
        LSB = mssg[40:48]
        LSB = LSB[::-1]
        val = MSB + LSB
       # y_val =(int(y_val,2)/2)*.004
        return val
    
    def ID_f(self,mssg):
        mssg = mssg[::-1]
        MSB = mssg[48:56]
        MSB = MSB[::-1]
        LSB = mssg[56:63]
        LSB = LSB[::-1]
        val = MSB + LSB
        return val
    
    def __init__(self):
        self.time_stamp         = 0
        self.CAN_channel        = 0
        self.dynProp            = 0
        self.confidence         = 0
        self.status             = 0
        self.classObj           = 0
        self.x                  = 0
        self.y                  = 0
        self.ID                 = 0
        
class SRR_obj_RL:
    
    def dynProp_f(self, mssg):
        mssg=mssg[::-1]
        return mssg[0:3][::-1]
    
    def confidence_f(self,mssg):
        mssg=mssg[::-1]
        return mssg[4:6][::-1]
    
    def status_f(self,mssg):
        mssg=mssg[::-1]
        return mssg[6:8][::-1]
    
    def classObj_f(self,mssg):
        mssg = mssg[::-1]
        return mssg[8:11][::-1]
    
    def x_f(self,mssg):
        mssg=mssg[::-1]
        MSB = mssg[16:24]
        MSB = MSB[::-1]
        LSB = mssg[24:32]
        LSB = LSB[::-1]
        return MSB + LSB
    
    def y_f(self,mssg):
        mssg=mssg[::-1]
        MSB = mssg[32:40]
        MSB = MSB[::-1]
        LSB = mssg[40:48]
        LSB = LSB[::-1]
        return MSB + LSB
    
    def ID_f(self,mssg):
        mssg=mssg[::-1]
        MSB = mssg[48:56]
        MSB = MSB[::-1]
        LSB = mssg[56:64]
        LSB = LSB[::-1]
        return MSB + LSB
    
    def __init__(self):
        self.time_stamp     = 0
        self.CAN_channel    = 0
        self.dynProp        = 0
        self.confidence     = 0
        self.status         = 0
        self.classObj       = 0
        self.x              = 0
        self.y              = 0
        self.ID             = 0
        
class SRR_obj_RR:
    
    def dynProp_f(self, mssg):
        mssg=mssg[::-1]
        return mssg[0:3][::-1]
    
    def confidence_f(self,mssg):
        mssg=mssg[::-1]
        return mssg[4:6][::-1]
    
    def status_f(self,mssg):
        mssg=mssg[::-1]
        return mssg[6:8][::-1]
    
    def classObj_f(self,mssg):
        mssg=mssg[::-1]
        return mssg[8:11][::-1]
    
    def x_f(self,mssg):
        mssg=mssg[::-1]
        MSB = mssg[16:24]
        MSB = MSB[::-1]
        LSB = mssg[24:32]
        LSB = LSB[::-1]
        return MSB + LSB
    
    def y_f(self,mssg):
        mssg=mssg[::-1]
        MSB = mssg[32:40]
        MSB = MSB[::-1]
        LSB = mssg[40:48]
        LSB = LSB[::-1]
        return MSB + LSB
    
    def ID_f(self,mssg):
        mssg=mssg[::-1]
        MSB = mssg[48:56]
        MSB = MSB[::-1]
        LSB = mssg[56:64]
        LSB = LSB[::-1]
        return MSB + LSB
    
    def __init__(self):
        self.time_stamp     = 0
        self.CAN_channel    = 0
        self.dynProp        = 0
        self.confidence     = 0
        self.status         = 0
        self.classObj       = 0
        self.x              = 0
        self.y              = 0
        self.ID             = 0

'''=============================SRR_obj_ext================================='''
class SRR_obj_ext_FL:
    
    def vx_rel_f(self, mssg):
        mssg = mssg[::-1]
        MSB = mssg[0:8]
        MSB = MSB[::-1]
        LSB = mssg[8:16]
        LSB = LSB[::-1]
        return MSB + LSB
    
    def vy_rel_f(self,mssg):
        mssg = mssg[::-1]
        MSB = mssg[16:24]
        MSB = MSB[::-1]
        LSB = mssg[24:32]
        LSB = LSB[::-1]
        return MSB + LSB
    
    def RCS_f(self,mssg):
        mssg = mssg[::-1]
        return mssg[32:40][::-1]
    
    def __init__(self):
        self.time_stamp     = 0
        self.CAN_channel    = 0
        self.vx_rel         = 0
        self.vy_rel         = 0
        self.RCS            = 0

class SRR_obj_ext_FR:
    
    def vx_rel_f(self, mssg):
        mssg = mssg[::-1]
        MSB = mssg[0:8]
        MSB = MSB[::-1]
        LSB = mssg[8:16]
        LSB = LSB[::-1]
        return MSB + LSB
    
    def vy_rel_f(self,mssg):
        mssg = mssg[::-1]
        MSB = mssg[16:24]
        MSB = MSB[::-1]
        LSB = mssg[24:32]
        LSB = LSB[::-1]
        return MSB + LSB
    
    def RCS_f(self,mssg):
        mssg = mssg[::-1]
        return mssg[32:40][::-1]
    
    def __init__(self):
        self.time_stamp     = 0
        self.CAN_channel    = 0
        self.vx_rel         = 0
        self.vy_rel         = 0
        self.RCS            = 0

class SRR_obj_ext_RL:
    
    def vx_rel_f(self, mssg):
        mssg = mssg[::-1]
        MSB = mssg[0:8]
        MSB = MSB[::-1]
        LSB = mssg[8:16]
        LSB = LSB[::-1]
        return MSB + LSB
    
    def vy_rel_f(self,mssg):
        mssg = mssg[::-1]
        MSB = mssg[16:24]
        MSB = MSB[::-1]
        LSB = mssg[24:32]
        LSB = LSB[::-1]
        return MSB + LSB
    
    def RCS_f(self,mssg):
        mssg = mssg[::-1]
        return mssg[32:40][::-1]
    
    def __init__(self):
        self.time_stamp     = 0
        self.CAN_channel    = 0
        self.vx_rel         = 0
        self.vy_rel         = 0
        self.RCS            = 0

class SRR_obj_ext_RR:
    
    def vx_rel_f(self, mssg):
        mssg = mssg[::-1]
        MSB = mssg[0:8]
        MSB = MSB[::-1]
        LSB = mssg[8:16]
        LSB = LSB[::-1]
        return MSB + LSB
    
    def vy_rel_f(self,mssg):
        mssg = mssg[::-1]
        MSB = mssg[16:24]
        MSB = MSB[::-1]
        LSB = mssg[24:32]
        LSB = LSB[::-1]
        return MSB + LSB
    
    def RCS_f(self,mssg):
        mssg = mssg[::-1]
        return mssg[32:40][::-1]
    
    def __init__(self):
        self.time_stamp     = 0
        self.CAN_channel    = 0
        self.vx_rel         = 0
        self.vy_rel         = 0
        self.RCS            = 0