# -*- coding: utf-8 -*-
'''
*============================================================================*/
                                    MACROS
*============================================================================*/
'''
ID_ADAS_matrix = [#SRR_OBJ_FL 0 --> 24
                  '400',
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
                  '410',
                  '411',
                  '412',
                  '413',
                  '414',
                  '415',
                  '416',
                  '417',
                  '418',
                  #SRR_OBJ_FR 25 --> 49
                  '440',
                  '441',
                  '442',
                  '443',
                  '444',
                  '445',
                  '446',
                  '447',
                  '448',
                  '449',
                  '44A',
                  '44B',
                  '44C',
                  '44D',
                  '44E',
                  '44F',
                  '450',
                  '451',
                  '452',
                  '453',
                  '454',
                  '455',
                  '456',
                  '457',
                  '458'
                  ]

ID                         = 2
TIME_STAMP                 = 0
CAN_CHANNEL                = 1

'''
*============================================================================*/
                              CLASS DEFINITION
*============================================================================*/
'''
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
        
class idx_name_class:
    def __init__(self):
        self.name = ''
        self.idx  = 0
    

'''
*============================================================================*/
                              FUNCTION DECLARATION
*============================================================================*/
'''
def init_objects_FL():
    matrix_objects = []
    for count_object in range(25):
        object_FL = SRR_obj_FL()
        matrix_objects.append(object_FL)
    return matrix_objects

def init_objects_FR():
    matrix_objects = []
    for count_object in range(25):
        object_FR = SRR_obj_FR()
        matrix_objects.append(object_FR)
    return matrix_objects

def init_matrix_objects(size,class_type):
    matrix_objects = []
    for count_object in range(size):
        object_type = class_type()
        matrix_objects.append(object_type)
    return matrix_objects
        
def obj_matrix_idx(ID,ADAS_matrix,idx_name_obj):
    idx = ADAS_matrix.index(ID)
    if idx>= 0 and idx<= 24:
        idx_name_obj.idx = idx - 0
        idx_name_obj.name ="SRR_objects_FL"
        
    elif idx>= 25 and idx<= 49:
        idx_name_obj.idx = idx-25
        idx_name_obj.name ="SRR_objects_FR"
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
                                "y","ID"]
            }[name]



'''
*============================================================================*/
                                      MAIN 
*============================================================================*/
'''
#-----------Definition of the memory structures--------------------------------
SRR_objects_FL = init_matrix_objects(25,SRR_obj_FL)
SRR_objects_FR = init_matrix_objects(25,SRR_obj_FR)
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