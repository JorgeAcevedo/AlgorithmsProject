# -*- coding: utf-8 -*-

class F_vision_object_track:
    
    '''
*****************************************************************
                        functions of the class
*****************************************************************
    '''

    def objDirTrk_f(self,mssg):
        value = mssg
        return value
    
    def FVisionWidthTrk_f(self,mssg):
        return mssg+1
    
    def FVisionMeasStatTrk_f(self,mssg):
        return mssg+2
    
    
    '''
*****************************************************************
                init atrributes of the class
*****************************************************************
    '''
    def __init__ (self):
        self.objDirTrk = 0
        self.FVisionWidthTrk = 0
        self.FVisionMeasStatTrk = 0
        '''
        Fill with the others
        '''
        
#Function
var = 0

track = F_vision_object_track()