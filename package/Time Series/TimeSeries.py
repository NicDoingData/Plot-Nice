class TimeSeries:
    
    def __init__(self, data):
        self.data = data
        
    def detect_seasonality(self, data, periods = None, sensitivity = 1):
        if periods == None:
            percentage_change_list = ["na"]
            for i in data:
                percentage_change = (data[i+1] - data[i]) / data[i]
                percentage_change_list.append(percentage_change)
                
            season_trend_len_counter = 1
            mean_percentage_change = sum(percentage_change_list)/ len(percentage_change_list)   
            above_mean_perc_change_list = []
            for j in percentage_change_list:
                if percentage_change_list[j] > mean_percentage_change:
                    above_mean_perc_change_list.append[True]
                elif percentage_change_list[j] == mean_percentage_change:
                    above_mean_perc_change_list.append["na"]
                else:
                    above_mean_perc_change_list.append[False]
            
            season_trend_len_list = []
            for k in range(0, len(above_mean_perc_change_list)):
                if above_mean_perc_change_list[k] == above_mean_perc_change_list[k+1]:
                    season_trend_len_counter += 1
                    season_trend_len_list.append(season_trend_len_counter)
                else:
                    season_trend_len_counter = 1
                    season_trend_len_list.append(season_trend_len_counter)
             
           for l in range(0, len(season_trend_len_list)):
                if season_trend_len_list[l] >= season_trend_len_list[l+1]:
                    trend_len = season_trend_len_list[l]
                    acceptable_range = list(range((trend_len - sensitivity):(trend_len + sensitivity)))
                    
                    for m in range(l, len(season_trend_len_list)):
                        if (season_trend_len_list[m] in acceptable_range) and (season_trend_len_list[m] >= season_trend_len_list[m+1]):
                            duration_between_peaks = m - l 
                            o = 1
                            seasonality = []
                            while (m+(duration_between_peaks*o)) <= len(season_trend_len_list):
                                if (season_trend_len_list[m+(duration_between_peaks*o)] in acceptable_range):
                                    o+=1
                                    seasonality.append(True)
                                else:
                                    o+=1
                                    seasonality.append(False)
                    seasonality_list = []
                    if (sum(seasonality)/len(seasonality)) == 1:
                        seasonality_list.append([
                                    
                                    
           
                        
                                    
                                    
                
                