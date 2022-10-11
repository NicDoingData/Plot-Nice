import matplotlib.pyplot as plt
import logging

class Nice_Plot:
    """
    A class to hold all the key information required for making the graph"""
    
    def __init__(self, x, y, type):
        """ A function to initialise the class object, containing all the information required to plot the graph:
        x = the values to be plotted on the x-axis (array)
        y = the values to be plotted on the y-axis (array)
        type = type of graph: either "bar", "line", or "scatter" (string)
        """
        
        self.x = x
        self.y = y
        self.type = type
        
    def show(self, title = "", xlabel = "", ylabel = ""):
        """ function to show the graph object with the option of adding strings for annotating the graph:
        title = the title to be shown above the graph (string, default is none)
        xlabel = the label to be shown on the x axis (string, default is none)
        ylabel = the label to be shown on the y axis (string, default is none)
        
        Output:
        matplotlib graph"""
        
        if self.type == "bar":
            plt.bar(x = self.x, height = self.y)
            plt.grid(axis = 'y', which = 'both', linstyle = "--")
            plt.title(title)
        elif self.type == "line":
            plt.plot(self.x, self.y)
            plt.grid(axis = 'y', which = 'both', linstyle = "--")
            plt.title(title)
        elif self.type == "scatter":
            plt.scatter(x = self.x, y = self.y)
            plt.title(title)
        else: 
            logging.error('Please select a valid plot type')
        
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        return plt.show()                  
          
                                  
                                    
                
                