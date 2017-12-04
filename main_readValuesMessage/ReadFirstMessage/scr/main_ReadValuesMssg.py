# -*- coding: utf-8 -*-
'''
*============================================================================*/
                                    MACROS
*============================================================================*/
'''
import ID_list 
import class_def

ID_ADAS_matrix = ID_list.matrix

ID                         = 2
TIME_STAMP                 = 0
CAN_CHANNEL                = 1

'''
*============================================================================*/
                              CLASS DEFINITION
*============================================================================*/
'''
class idx_name_class:
    def __init__(self):
        self.name = ''
        self.idx  = 0
    

'''
*============================================================================*/
                              FUNCTION DECLARATION
*============================================================================*/
'''

def init_matrix_objects(size,class_type):
    matrix_objects = []
    for count_object in range(size):
        object_type = class_type()
        matrix_objects.append(object_type)
    return matrix_objects
        
def obj_matrix_idx(ID,ADAS_matrix,idx_name_obj):
    idx = ADAS_matrix.index(ID)
    #SRR_OBJ_FL 0 --> 24
    if idx>= 0 and idx<= 24:
        idx_name_obj.idx = idx - 0
        idx_name_obj.name ="SRR_objects_FL"
        
    #SRR_OBJ_FR 25 --> 49
    elif idx>= 25 and idx<= 49:
        idx_name_obj.idx = idx-25
        idx_name_obj.name ="SRR_objects_FR"
        
    #SRR_OBJ_RL 50--> 74
    elif idx>= 50 and idx<= 74:
        idx_name_obj.idx = idx-50
        idx_name_obj.name ="SRR_objects_RL"
        
    #SRR_OBJ_RR 75 -> 99
    elif idx>= 75 and idx<= 99:
        idx_name_obj.idx = idx-75
        idx_name_obj.name ="SRR_objects_RR"
        
    #SRR_obj_ext_FL
    elif idx>= 100 and idx<= 124:
        idx_name_obj.idx = idx-100
        idx_name_obj.name ="SRR_objects_ext_FL"
    
    #SRR_obj_ext_FR 125 -> 149
    elif idx>= 125 and idx<= 149:
        idx_name_obj.idx = idx-125
        idx_name_obj.name ="SRR_objects_ext_FR"
        
    #SRR_obj_ext_RL 150 -> 174
    elif idx>= 150 and idx<= 174:
        idx_name_obj.idx = idx-150
        idx_name_obj.name ="SRR_objects_ext_RL"
        
    #SRR_obj_ext_RR 175 -> 199
    elif idx>= 175 and idx<= 199:
        idx_name_obj.idx = idx-175
        idx_name_obj.name ="SRR_objects_ext_RR"

    #Add elif here........

    else:
        idx_name_obj.idx = 10101010101
        idx_name_obj.name ="ERROR"
    return;    
    
'''
*============================================================================*/
                              DICTIONARY DECLARATION
*============================================================================*/
'''
def dicc_attr (name):
    return{
            "SRR_objects_FL" : ["time_stamp","CAN_channel","dynProp",
                                "confidence","status","classObj","x",
                                "y","ID"],
            "SRR_objects_FR" : ["time_stamp","CAN_channel","dynProp",
                                "confidence","status","classObj","x",
                                "y","ID"],
            "SRR_objects_RL" : ["time_stamp","CAN_channel","dynProp",
                                "confidence","status","classObj","x",
                                "y","ID"],
            "SRR_objects_RR" : ["time_stamp","CAN_channel","dynProp",
                                "confidence","status","classObj","x",
                                "y","ID"],
            "SRR_objects_ext_FL" : ["time_stamp","CAN_channel","vx_rel",
                                "vy_rel","RCS"],
            "SRR_objects_ext_FR" : ["time_stamp","CAN_channel","vx_rel",
                                "vy_rel","RCS"],                    
            "SRR_objects_ext_RL" : ["time_stamp","CAN_channel","vx_rel",
                                "vy_rel","RCS"] ,
            "SRR_objects_ext_RR" : ["time_stamp","CAN_channel","vx_rel",
                                "vy_rel","RCS"]
            }[name]



'''
*============================================================================*/
                                      MAIN 
*============================================================================*/
'''
#-----------Definition of the memory structures--------------------------------
#SRR_objects
SRR_objects_FL = init_matrix_objects(25,class_def.SRR_obj_FL)
SRR_objects_FR = init_matrix_objects(25,class_def.SRR_obj_FR)
SRR_objects_RL = init_matrix_objects(25,class_def.SRR_obj_RL)
SRR_objects_RR = init_matrix_objects(25,class_def.SRR_obj_RR)

#SRR_objects_ext
SRR_objects_ext_FL = init_matrix_objects(25,class_def.SRR_obj_ext_FL)
SRR_objects_ext_FR = init_matrix_objects(25,class_def.SRR_obj_ext_FR)
SRR_objects_ext_RL = init_matrix_objects(25,class_def.SRR_obj_ext_RL)
SRR_objects_ext_RR = init_matrix_objects(25,class_def.SRR_obj_ext_RR)
#-----------------------------------


idx_name_obj = idx_name_class()


    
f = open("VN1610Dummy.asc", 'r')
for line in f:
    line_analizer = line
    line_divider = line_analizer.split()
    if line_divider[ID] in ID_ADAS_matrix:
        #output_matrix.append(line_analizer)
        #****************************************
        #Getting mssg in binary
        binary_message=[]
        mssg = line_divider[6:]
        mssg = ''.join(mssg)
        for hexadecimal in mssg:
            binary_message.append(bin(int(hexadecimal,16))[2:].zfill(4))
        binary_message = ''.join(binary_message)
        binary_message = binary_message.zfill(64)
        
        #****************************************
        #Getting Time in float
        time_stamp = float(line_divider[TIME_STAMP])
        #****************************************
        #Getting CAN Channel
        CAN_channel =int(line_divider[CAN_CHANNEL])
        #****************************************
        
        obj_matrix_idx(line_divider[ID],ID_ADAS_matrix,idx_name_obj)
        int_counter = 0
        
        for idx_attr in dicc_attr(idx_name_obj.name):
            if int_counter <= 1:
                #filling Time Stamp
                exec(str(idx_name_obj.name) + "[" + str(idx_name_obj.idx) + "]." + str(dicc_attr(idx_name_obj.name)[int_counter]) + "=" + str(dicc_attr(idx_name_obj.name)[int_counter]))
            else:
                exec(str(idx_name_obj.name) + "[" + str(idx_name_obj.idx) + "]." + str(dicc_attr(idx_name_obj.name)[int_counter]) + "=" + str(idx_name_obj.name) + "[" + str(idx_name_obj.idx) + "]." + str(dicc_attr(idx_name_obj.name)[int_counter]) + "_f(binary_message)")
            int_counter = int_counter + 1;
            
#            print(vars(SRR_objects_FL[0]))
         
        
            '''
                 exec(idx_name_obj.name + "[" + idx_name_obj.idx + "]." + 
                     dicc_attr(idx_name_obj)[idx_attr] + "=" + 
                     idx_name_obj.name + "." dicc_attr(idx_name_obj)[idx_attr] +
                     "_f(binary_message)")
                 '''
'''
        object_01_FL=SRR_obj_FL(binary_message,time_stamp,CAN_channel)
'''
'''       
    print(output_matrix)
'''