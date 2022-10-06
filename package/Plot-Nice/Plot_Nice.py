import matplotlib.pyplot as plt
import logging

class Nice_Plot:
    
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        
    def show(self, title):
        if self.type == "bar":
            plt.bar(x = self.x, height = self.y)
            plt.grid(axis = 'y', which = 'both', linstyle = "--")
            plt.title(title)
        elif self.type == "line":
            plt.plot(x = self.x, y = self.y)
            plt.grid(axis = 'y', which = 'both', linstyle = "--")
            plt.title(title)
        elif self.type == "scatter":
            plt.scatter(x = self.x, y = self.y)
            plt.title(title)
        else: 
            logging.error('Please select a valid plot type')
        
        return plt.show()
   
    def annotate_graph (self, xlabel, ylabel, titel):
        self.show(title)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.show()
                                    
           
                        
                                    
                                    
                
                