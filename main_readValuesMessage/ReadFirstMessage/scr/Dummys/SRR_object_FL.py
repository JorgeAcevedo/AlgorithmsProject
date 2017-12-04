# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:32:28 2017

@author: UIDN8311
"""
'''
*============================================================================*/
                                    MACROS
*============================================================================*/
'''
ID                         = 2
TIME_STAMP                 = 0
CAN_CHANNEL                = 1
INIT_MSSG='0000000000000000000000000000000000000000000000000000000000000000'
INIT_CAN_CHANNEL           = 0
INIT_TIME_STAMP            = 0000.0000
'''
*============================================================================*/
                             MAIN FUNCTION       
*============================================================================*/
'''
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:32:28 2017

@author: UIDN8311
"""


'''
*============================================================================*/
                              CLASS DEFINITION   
*============================================================================*/
'''
class SRR_obj_FL:
    
    def dynPropf(mssg):
        mssg = mssg[::-1]
        return mssg[0:3][::-1]
    
    def confidencef(mssg):
        mssg = mssg[::-1]
        return mssg[4:6][::-1]
    
    def statusf(mssg):
        mssg = mssg[::-1]
        return mssg[6:8]
    
    def classObjf(mssg):
        mssg = mssg[::-1]
        return mssg[8:11][::-1]
    
    def xf(mssg):
        mssg = mssg[::-1]
        MSB = mssg[16:24]
        MSB = MSB[::-1]
        LSB = mssg[24:32]
        LSB = LSB[::-1]
        x_val = MSB + LSB
       # x_val =(int(x_val,2)/2)*.004
       #Tener en cuenta la division entre enteros
        return x_val
        
    def yf(mssg):
        mssg = mssg[::-1]
        MSB = mssg[32:40]
        MSB = MSB[::-1]
        LSB = mssg[40:48]
        LSB = LSB[::-1]
        y_val = MSB + LSB
       # y_val =(int(y_val,2)/2)*.004
        return y_val
    
    def IDf(mssg):
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
        

def init_objects_FL():
    matrix_objects = []
    for count_object in range(25):
        object_FL = SRR_obj_FL()
        matrix_objects.append(object_FL)
    return matrix_objects

def object_ident(ID):
    ID_numeric = int(ID,16)
    if 0x400>=ID_numeric and ID_numeric <=0x458:
        classType = 'SRR_object_FL'
    return classType

def matrix_object_selector(object_ident):
    return{
            'SRR_object_FL':SRR_FL_objects
            }[object_ident]
    '''

    return {
            '400':SRR_FL_objects
            }.get(ID,'error')
    '''


    
    
    #****************************************
    #Getting Time in float
    time_stamp = float(line_divider[TIME_STAMP])
    #****************************************
    #Getting CAN Channel
    CAN_channel =int(line_divider[CAN_CHANNEL])
    #****************************************
    

  
    
    

