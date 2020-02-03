'''
Documentation, License etc.

@package ZansatVIII_Protoparser
'''

import numpy as np 
from numpy import genfromtxt
import os
#Semi-Global, Push. 
push = ""
APP = ['Temper','Press','Height','Head','Drive','HeightC','Fallflag']

class Line():
    LARR = []
    Temper = 0.0
    Humid = 0.0
    Press = 0.0
    Height = 0.0
    Head = 0.0
    Drive = 0.0
    HeightC = 0.0
    Fallflag = False
    Validity = False 
    def App(self):
        if len(self.LARR) == len(APP):
            self.Temper = self.LARR[0]
            self.Press = self.LARR[1]
            self.Height = self.LARR[2]
            self.Humid = self.LARR[3]
            self.Head = self.LARR[4]
            self.Drive = self.LARR[5]
            self.HeightC = self.LARR[6]
            self.Fallflag = self.LARR[7] == 1
            return True
        else:
            print("False Line found")
            return False
    def __init__(self, linestr):
        prev = 0 
        pointr = 0 
        #parses all into floats
        for pointr in range(0, len(linestr)):
            if linestr[pointr] == '\\':
                break 
            elif linestr[pointr] == ';' :
                self.LARR.append(float(linestr[prev:pointr]))
                prev = pointr + 1
       
        self.Validity =  self.App()
    
            
       
    
            


#When run standalone
if __name__ == "__main__" : 
    #import matplotlib as ma 
    #import pyserial as ps 
    if input("from file? Y/N \n") == 'Y':
        inp = open("zansattest_2.txt", 'r')
        push = inp.readlines()
        linelist = []
        for l in range(0,len(push)):
            linelist.append(Line(push[l]))
        print(linelist)

    
    
