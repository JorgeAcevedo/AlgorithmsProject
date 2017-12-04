# -*- coding: utf-8 -*-

def dicc_attr (name):
    return{
            "SRR_objects_FL" : ["time_stamp","CAN_channel","dynProp",
                                "confidence","status","classObj","x"
                                "y","ID"],
            "SRR_objects_FR" : ["time_stamp","CAN_channel","dynProp",
                                "confidence","status","classObj","x"
                                "y","ID"]
            }[name]
    
