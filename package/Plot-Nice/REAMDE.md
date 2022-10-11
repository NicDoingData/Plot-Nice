## Summary
This is a simple little package to quickly make nice, annotated plots of types line, bar, or scatter. The package is based on the matplotlib.pyplot package and essentially provides a simplified interface to use it to make a graph.

The package contains one class, its initialisation function and one further function to show the graph.

All the code is contained within the Plot_Nice.py file. 

This package is the result of a learning exercise. 

##Documentation
class Nice_Plot: A class to hold all the key information required for making the graph:
		x = the values to be plotted on the x-axis (array)
        y = the values to be plotted on the y-axis (array)
        type = type of graph: either "bar", "line", or "scatter" 			(string)
        
function show(self, title = "", xlabel = "", ylabel = ""):
        function to show the graph object with the option of 				adding strings for annotating the graph:
        title = the title to be shown above the graph (string, 				default is none)
        xlabel = the label to be shown on the x axis (string, 				default is none)
        ylabel = the label to be shown on the y axis (string, 				default is none)
    	Output:
        matplotlib graph