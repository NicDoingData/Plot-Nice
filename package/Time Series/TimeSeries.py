class TimeSeries:
    
    def __init__(self, data):
        self.data = data
        
    def detect_seasonality(self, data, periods = None, method):
        if periods == None:
            seasonality_index = [na]
            for i in data:
                