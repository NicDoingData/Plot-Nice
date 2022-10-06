import numpy as np
import pandas as pd

class Profile:
    
    def __init__(self, name):
        self.name = name
        self.tags = []
        self.budget = none
        self.transactions = []
    
    def read_file (self, file):
        if ".csv" in file:
            self.transactions = pd.read_csv(file)
        elif ".txt" in self.file:
            self.transactions = pd.read_table(file)
        else:
            #throw up error
        
        transaction_list = []
        for i in range(i, len(self.transactions):
                       str("transaction_"+i) = Transaction(profile = self.transaction[i,0], value = self.transaction[i,1], date = self.transaction[i,2], tag = self.transaction[i,3])
                       transaction_list.append(transaction)
         
                       
         return self.transactions = transaction_list
         
                       
                       
         
    
    def set_budget(self, budget):
        self.budget = budget
        
   def compare_spend_budget(self, month):
                       
    
        
class Transaction:
    
    def __init__(self, profile, value, tag = None, date):
        self.value = value
        self.tag = tag
        self.date = date
        self.profile = profile
        
"""class Data:
    
     def __init__(self, file):
        #self.filetype = filetype
        self.file = file
        self.data = []
       
    def read_file (self):
        if ".csv" in self.file:
            self.data = pd.read_csv(self.file)
        elif ".txt" in self.file:
            self.data = pd.read_table(self.file)
        else:
            #throw up error
         
         
        
    