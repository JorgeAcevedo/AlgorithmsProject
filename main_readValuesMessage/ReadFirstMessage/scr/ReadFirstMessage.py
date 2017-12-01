# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
#  4578.758101 2  400             Rx   d 8  FD 01 3F FF FF FF FF FF
#import numpy as np
#import pylab
#import matplotlib.pyplot as plt
import SRR_object_FL as SRR_FL
ID                         = 2

'''
*============================================================================*/
                                    MACROS
*============================================================================*/
'''

ID_ADAS_matrix = ['400',
                  '401',
                  '402',
                  '403',
                  '404',
                  '405',
                  '406',
                  '407',
                  '408',
                  '409',
                  '40A',
                  '40B',
                  '40C',
                  '40D',
                  '40E',
                  '40F',
                  '411',
                  '412',
                  '413',
                  '414',
                  '415',
                  '417',
                  '418',]

'''

'''

'''
*============================================================================*/
                             MAIN FUNCTION       
*============================================================================*/
'''
SRR_objects_FL = SRR_FL.init_objects_FL()

def index_SRR_object_FL(ID):
    index = ID_numeric - 0x400
    return index

def object_update(ID,time_stamp,CAN_channel,mssg):
    ID_numeric = int(ID,16)
    if 0x400>=ID_numeric and ID_numeric <=0x458:
        index=index_SRR_object_FL(ID_numeric)
        SRR_objects_FL[index].time_stamp = time_stamp
        SRR_objects_FL[CAN_channel]. = time_stamp
        
        
        
        
        SRR_obj_FL.(mssg)
        
    return; 

output_matrix=[]
f = open("VN1610Dummy.asc", 'r')
for line in f:
    line_analizer = line
    line_divider = line_analizer.split()
    if line_divider[ID] in ID_ADAS_matrix:
        
        
        output_matrix.append(line_analizer)
        #****************************************
        #Getting mssg in binary
        binary_message=[]
        mssg = line_divider[6:]
        mssg = ''.join(mssg)
        for hexadecimal in mssg:
            binary_message.append(bin(int(hexadecimal,16))[2:].zfill(4))
        binary_message=''.join(binary_message)
        
        
        #****************************************
        #Getting Time in float
        time_stamp = float(line_divider[TIME_STAMP])
        #****************************************
        #Getting CAN Channel
        CAN_channel =int(line_divider[CAN_CHANNEL])
        #****************************************
        
        
        
        '''
        object_01_FL=SRR_obj_FL(binary_message,time_stamp,CAN_channel)
        '''
        
    print(output_matrix)
        
    #print((line))
    #Print the length
    #print(len(lineAnalizer))
  
 # mssg ='1111110100000001001111111111111111111111111111111111111111111111'
  

'''
line ='  4578.006538 2  400             Rx   d 8  FD 01 3F FF FF FF FF FF'  
line_analizer = line
line_divider = line_analizer.split()
'''










        
    