'''
ZansatVIII_Protoparser

Made by the ZansatVIII team. 
'''

import os
#Semi-Global, Push. 
push = ""
APP = ['Temper','Press','Height','Humid','Head','Drive','HeightC','Fallflag']
#line class, will be usefull in later data handling, already integrated.  
class Line():
    #How the class will be printed 
    def __str__(self):
        return str(self.LARR)+str(self.Validity)
    #Checks for validity Extracts all variables from LARR
    def App(self):
        if len(self.LARR) == 8:
            self.Temper = self.LARR[0]
            self.Press = self.LARR[1]
            self.Height = self.LARR[2]
            self.Humid = self.LARR[3]
            self.Head = self.LARR[4]
            self.Drive = self.LARR[5]
            self.HeightC = self.LARR[6]
            self.Fallflag = self.LARR[7] == 1
            self.LARR[7] = self.Fallflag
            return True
        else:
            print("False Line found")
            return False
    #Constructor of a line 
    def __init__(self, linestr,ind = 0):
        self.Time = ind
        self.LARR = []
        self.Validity = False 
        prev = 0 
        #parses all into floats
        for pointr in range(0, len(linestr)):
            if linestr[pointr] == ';' :
                self.LARR.append(float(linestr[prev:pointr]))
                prev = pointr + 1
        #Parses the last variable that gets skipped by the previous  
        self.LARR.append(linestr[prev:])
        self.Validity =  self.App()
    
#When run standalone
if __name__ == "__main__" : 
    import numpy as np
    import matplotlib.pyplot as plt
    #import serial from here 
    import serial as ser 
    
    #overwritten as this is the only function working 
    if str(input("from file? 'Y'/'Anything' \n")) == "Y":
        #Open a file Also overwritten
        inp = open("%s.txt" %(input("\nChoose path or filename from the place the program is run\n ")), 'r')
        #create a temp file
        if os.path.exists('./_temp.txt'):
             os.remove("./_temp.txt")
        temp = open("./_temp.txt",'w')
        #Reads out the lines from input
        push = inp.readlines()
        linelist = []
        
        #Line parsing 
        for l in push:
           linelist.append(Line(l[:-len(os.linesep)]))
           temp.write(str(linelist[-1]) + os.linesep)
        listlen = len(linelist) - 1
        
        #Axes creation 
        fig, axs = plt.subplots(6,1, sharex = True)
        (axt,axp,axh,axm,axo,axd) = axs
        plt.ion()
        

        
        #initializes plot variable and time lists
        vars = [[linelist[3].LARR[0]],[linelist[3].LARR[1]],[linelist[3].LARR[2]],[linelist[3].LARR[3]],[linelist[3].LARR[4]],[linelist[3].LARR[5]]]
        times = [0.0]
        
        
        #Initial show
        plt.show()
        plt.pause(1)
        
        #Variable extraction
        for i in range(3,listlen):
            #If valid loads the vars from the lines LARR
            if linelist[i].Validity:
                for u in range(0,6):
                    vars[u].append(linelist[i].LARR[u])
                #Time ticks on 
                times.append(i)
            #Drawing the graph 
            if i % 5 == 0:
                for a in range(0,6):
                    axs[a].cla()
                    axs[a].plot(times,vars[a])
                    axs[a].set_title(APP[a])
            plt.draw()
            plt.pause(0.00001)
        
        #Work Finished
        print("Finished")
        while True:
             plt.pause(1)
        
