#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:08:05 2020

@author: laura, sarah
"""

import numpy as np

class Agent: 
    """A single economist
    
    Chooses a paradigm, depending on own preferences and academic power expressed in network value.
    
    Attributes
    ---------- 
        
    individual_utility : dict
        assigns each paradigm  (Mainstream and Heterodoxy) a certain utility, calculated from the networkvalue and intrinsic utility 
        
    current_paradigm : int
        the paradigm chosen by the agent. `None` in the beginning, then "Mainstream" or "Heterodoxy"
        
    intrinsic_value: dict
        assigns randomly generated values as intrinsic values to a paradigm for each economist
    
   
    Methods
    --------        
    
    calculate_utility
        calculates the individual utility for each Economist as a sum = intrinsic_value + networkvalue.
        
    choose_paradigm
        Chooses a paradigm based on own preferences (intrinsic_value) and the paradigm's network value
        
    """
    
    Profession = "Economist"
    
    def __init__(self, institution):
        self.institution = institution
        self.individual_utility = {
                "Mainstream" : 0, 
                "Heterodoxy" : 0}
        self.current_paradigm = None
        self.intrinsic_value = { 
                "Mainstream" : np.random.uniform(0,1),
                "Heterodoxy" : np.random.uniform(0,1)}
        institution.add_agent(self)
        self.calculate_utility()
        self.choose_paradigm()

    def calculate_utility(self):
        #utility of agents is calculated by adding for each paradigm the intrinsic value and the network value
        for k in self.intrinsic_value: 
            self.individual_utility[k] = (self.intrinsic_value[k]) + (self.institution.networkvalue[k])
            
    def choose_paradigm(self):
        #each agents chooses the paradigm with maximum utility 
        maximal_utility = max(self.individual_utility, key=self.individual_utility.get) 
        self.current_paradigm = maximal_utility
        #print(self.current_paradigm)

