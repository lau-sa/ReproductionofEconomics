#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:30:01 2020

@author: laura, sarah
"""

import os
if (os.getcwd()[-6:] == "python") | (os.getcwd()[-9:] == "notebooks"):
    os.chdir("..")
print(os.getcwd())
import sys; sys.path.insert(0, 'python')


from Agent_EASY import Agent
import matplotlib.pyplot as plt


class Academic_Institutions: 
    """
    Governs academic power and produces network value 
    
    The class in which academic power and thus the network value is produced and assigned to each paradigm
    
    Attributes
    ----------
    academic_power: dict
        a value of academic power is assigned to each paradigm
    
    networkvalue : dict
        a networkvalue is assigned to each paradigm, correlates with academic power of a paradigm
        
    agents : list
        the list of agents in the Academic_Institutions, in the beginning empty
    
    Methods
    --------
    add_agent
        add agents to the agents list within one academic institution
    
    update_academic_power
        calculates and assigns a value of academic power to each paradigm according to the 
        share of economists associated with this paradigm. 
        For example:the more economists have mainstream as current paradigm, 
        the higher is the academic power of this paradigm.
        
    update_network_value
        is a square function of academic power. assigns each paradigm a (new) networkvalue
        
    """
    def __init__(self, academic_power_Mainstream, academic_power_Heterodoxy): 
            self.academic_power = {
                    "Mainstream" : academic_power_Mainstream, 
                    "Heterodoxy" : academic_power_Heterodoxy}
            self.networkvalue = {
                    "Mainstream" : 0.00, 
                    "Heterodoxy" : 0.00}
            self.agents = []
            self.update_network_value()
          
    def add_agent(self, agent):
        self.agents.append(agent)
    
    def update_academic_power(self):
        """Calculates new academic power (share of agents adhering to certain paradigm).
        
        """
        counter = 0
        
        for a in self.agents: 
            if a.current_paradigm == "Mainstream": 
                    counter +=1
        share = counter/len(self.agents) 
        self.academic_power["Mainstream"] = share
        self.academic_power["Heterodoxy"] = 1 - share
        
    def update_network_value(self):
        """
        Networkvalue of paradigm gets calculated, new network value gets calculated 
        """
        for k in self.academic_power:
            self.networkvalue[k] = self.academic_power[k]**4


class Model: 
    """
    Within the Model economists choose a paradigm to work with, for this they orientate on intrinsic_value and network_value 
    of the past period - from that arises a certain distribution of Mainstream and Heterodoxy and hence the possibility to 
    calculate a new network_value
    
        Attributes
    ----------
    institution: int
        The insitution (e.g. a specific university) contains the different paradigms, more specifically their academic power values.
        
    powerDistribution: list
        shows the power of each paradigm, here it indicates the academic power of the Mainstream 
        
    Methods
    --------
    
    timestep
        Economists are added and choose one paradigm according to their individual utility and the network value given to the paradigm by the modeler,
        this changes the academic power, the networkvalue of each paradigm and thus the powerDistribution
        so the (new) agents are grouped according to their chosen paradigm- in each timestep
    
    run
        Runs the model, i.e. all Economists choose their paradigm sequentially.
        
    """
    
    def __init__(self, academic_power_Mainstream, academic_power_Heterodoxy):
        self.institution = Academic_Institutions(academic_power_Mainstream, academic_power_Heterodoxy)
        self.powerDistribution = []
           
        
    def timestep(self):
        for i in range(10): #number of agents
            Agent(self.institution) #10 agents are added as soon as timestep is called up
        self.institution.update_academic_power()
        self.institution.update_network_value()
        #print(self.institution.academic_power)
        self.powerDistribution.append(self.institution.academic_power["Mainstream"])
           

    def run(self, timesteps): 
        for t in range(timesteps): 
           # print(t)
            self.timestep()

institutions = []
for i in range(100): #number of the runs of the model /correlates with the number of lines in the output graphic 
    University_Vienna = Model(0.9, 0.1) #first value is the academic power of the mainstream, the latter is the academic power of the Heterodoxy
    University_Vienna.run(10) #number of timesteps 
    institutions.append(University_Vienna)

for inst in institutions:
    plt.plot(inst.powerDistribution)
plt.ylabel('Dist Mainstream')
plt.savefig("test.png", dpi = 800)
plt.show()

